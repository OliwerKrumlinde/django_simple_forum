"""django_simple_forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django_simple_forum import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^section/(?P<section_id>\w+)', views.section_page, name='section_page'),
    url(r'^threads/(?P<thread_id>\w+)', views.thread_page, name='thread_page'),
    url(r'^thread/new/(?P<section_id>\w+)', views.thread_create, name='thread_create'),
    url(r'^post/(?P<post_id>\w+)', views.get_post, name='get_post'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)