from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe 
from PIL import Image as Im
from taggit.managers import TaggableManager



class Image(models.Model):

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', name = 'image')
    tags = TaggableManager()

    def __str__(self):
        """
        String for representing the Image object.
        """
        return self.title
    
    def get_absolute_url(self):
        """
        Returns the url to image instance.
        """
        return reverse('image-detail', args=[str(self.id)])
    







