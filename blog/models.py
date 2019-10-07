from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager,self).get_queryset().filter(status=True)

class Post(models.Model):
    title       = models.CharField(max_length=255)
    slug        = models.SlugField(max_length=255,unique_for_date='created')
    body        = models.TextField()
    image       = models.ImageField(upload_to='post_pics/',default='default/post_pic.jpg')
    author      = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    publish     = models.DateTimeField(default=timezone.now)
    status      = models.BooleanField(default=True)

    user_likes  = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='post_liked',blank=True)

    objects     = models.Manager()
    published   = PublishManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk,'slug':self.slug})
