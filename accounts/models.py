from django.db import models
from django.conf import settings
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user    = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    photo   = models.ImageField(upload_to='profile_pics/',default='default/person.png')
    dob     = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.user.username

    def save(self,*args,**kwargs):
        super(Profile,self).save(*args,**kwargs)
        img = Image.open(self.photo.path)
        if img.width>300 or img.height:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.photo.path)
