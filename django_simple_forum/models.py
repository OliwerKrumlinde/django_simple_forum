from django.db import models
from .user_profile.models import UserProfile
from ckeditor.fields import RichTextField

APPROVAL_CHOICES = (
    (u'1', u'Pending'),
    (u'2', u'No'),
    (u'3', u'Yes'),
    (u'4', u'Mixed'),
)


class MainSection(models.Model):
    name = models.CharField(verbose_name='Section headers', blank=False, null=False, max_length=64)

    @property
    def get_sections(self):
        return Section.objects.filter(over_all_section=self)


class Section(models.Model):
    over_all_section = models.ForeignKey(MainSection, blank=False, null=False)
    title = models.CharField(verbose_name='Section name', blank=False, null=False, max_length=64)
    comment = models.CharField(verbose_name='Section comment', blank=False, null=False, max_length=64)

    @property
    def get_total_views(self):
        total_views = 0
        for thread in Thread.objects.filter(section=self):
            total_views = total_views + thread.views

        return total_views

    @property
    def get_total_threads(self):
        return Thread.objects.filter(section=self).count()

    @property
    def get_total_posts(self):
        return Post.objects.filter(thread=Thread.objects.filter(section=self)).count()

    @property
    def get_latest_post_activity(self):
        return Post.objects.filter(thread=Thread.objects.filter(section=self)).order_by('created_date')[0]


class Thread(models.Model):
    section = models.ForeignKey(Section, blank=False, null=False)
    name = models.CharField(verbose_name='Thread name', blank=False, null=False, max_length=64)
    views = models.BigIntegerField(verbose_name='Amount of views', default=0)
    disabled = models.BooleanField(verbose_name='Disabled', default=False)
    created_date = models.DateTimeField(verbose_name='Creation date', auto_now_add=True)
    owner = models.ForeignKey(UserProfile, blank=False, null=False)
    # TODO: Add tags field

    @property
    def get_latest_post_activity(self):
        return Post.objects.filter(thread=self).order_by('created_date')[0]

    @property
    def get_first_post(self):
        return Post.objects.filter(thread=self).order_by('created_date')[0]


class Post(models.Model):
    thread = models.ForeignKey(Thread, blank=False, null=False)
    user = models.ForeignKey(UserProfile, verbose_name='User', blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    comment = RichTextField(verbose_name="Comment", blank=False, null=False)
    attached_file = models.FileField(
        verbose_name="Attached file",
        blank=True,
        null=True,
        upload_to='uploads/'
    )
    up_votes = models.IntegerField(verbose_name='Upvotes', default=0)


