from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    thumbnail = models.ImageField(upload_to='categories/photos/%Y/%m/%d/')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Course(models.Model):
    category = models.ForeignKey(
        Category, related_name='courses', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    thumbnail = models.ImageField(upload_to='courses/thumbnails/')
    sub_title = models.CharField(max_length=200)
    video_intro_url = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={
            'slug': self.slug
        })


class Section(models.Model):
    course = models.ForeignKey(
        Course, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    description = models.TextField(blank=True, null=True)
    position = models.IntegerField()

    def __str__(self):
        return self.title


class Video(models.Model):
    section = models.ForeignKey(
        Section, related_name='videos', on_delete=models.CASCADE)
    video_url = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='lessons/photos/%Y/%m/%d/')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    description = models.TextField(blank=True, null=True)
    position = models.IntegerField()

    def __str__(self):
        return self.title


def pre_save_item(sender, instance, *args, **kwargs):
    if not instance.slug:
        if sender != Course:
            instance.slug = slugify(instance.title)
        else:
            instance.slug = slugify(instance.name)


pre_save.connect(pre_save_item, sender=Category)
pre_save.connect(pre_save_item, sender=Course)
pre_save.connect(pre_save_item, sender=Section)
pre_save.connect(pre_save_item, sender=Video)
