from .models import MainSection, Section, Thread, Post
from .forms import PostForm, ThreadForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from user_profile.models import UserProfile


def home(request):
    ctx = {
        'main_sections': MainSection.objects.all()
    }

    return render(request, 'index.html', ctx)


def section_page(request, section_id):
    try:
        section_obj = Section.objects.get(id=section_id)
    except ObjectDoesNotExist:
        raise Http404('Section does not exists')

    ctx = {
        'section': section_obj,
        'threads': Thread.objects.filter(section=section_obj)
    }

    return render(request, 'sections.html', ctx)


def thread_page(request, thread_id):
    if request.method == 'POST':
        post_id = request.POST.get('edit_post_id')

        if post_id:
            post_instance = Post.objects.get(id=post_id)
            if post_instance.user.user != request.user:
                raise Http404('Post does not exist')

            form = PostForm(request.POST, instance=post_instance)
        else:
            form = PostForm(request.POST)

        if form.is_valid():
            post_instance = form.save(commit=False)
            post_instance.thread = Thread.objects.get(id=thread_id)
            post_instance.user = UserProfile.objects.get(user=request.user)
            post_instance.save()
            return HttpResponseRedirect(reverse('thread_page', kwargs={'thread_id': thread_id}))
            # return render(request, 'threads.html', ctx)
    else:
        form = PostForm()

    try:
        thread_obj = Thread.objects.get(id=thread_id)
    except ObjectDoesNotExist:
        raise Http404('Section does not exists')
    # TODO: This should probably be replaced with a proper hits counter.
    thread_obj.views = thread_obj.views + 1
    thread_obj.save()
    # remove the first post since that will be treated differently in the template
    posts = Post.objects.filter(thread=thread_obj).exclude(id=thread_obj.get_first_post.id)
    ctx = {
        'thread': thread_obj,
        'posts': posts,
        'postform': form,
    }
    return render(request, 'threads.html', ctx)


# TODO: Add proper login url here
@login_required(login_url='/')
def thread_create(request, section_id):
    if request.method == 'POST':
        form_thread = ThreadForm(request.POST)
        form_post = PostForm(request.POST)
        if form_thread.is_valid() and form_post.is_valid():
            thread_instance = form_thread.save(commit=False)
            thread_instance.section = Section.objects.get(id=section_id)
            thread_instance.owner = UserProfile.objects.get(user=request.user)
            thread_instance.save()

            post_instance = form_post.save(commit=False)
            post_instance.thread = thread_instance
            post_instance.user = UserProfile.objects.get(user=request.user)
            post_instance.save()

            return HttpResponseRedirect(reverse('thread_page', kwargs={'thread_id': thread_instance.id}))

    else:
        form_thread = ThreadForm()
        form_post = PostForm()

    ctx = {
        'form_post': form_post,
        'form_thread': form_thread
    }
    return render(request, 'thread_create.html', ctx)


def get_post(request, post_id):
    return HttpResponse(Post.objects.get(id=post_id).comment)
