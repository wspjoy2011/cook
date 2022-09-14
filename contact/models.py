from django.db import models
from ckeditor.fields import RichTextField


class Contact(models.Model):
    """Feedback model class"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    facebook = models.URLField()
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'


class ContactLink(models.Model):
    """Contact model class"""
    icon = models.FileField(upload_to='users_icons/%Y/%m/%d/')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class About(models.Model):
    """About model class"""
    text = RichTextField()
    mini_text = RichTextField()

    def __str__(self):
        return f'About {self.text[:50]}'


class ImageAbout(models.Model):
    """Image about class model"""
    image = models.ImageField(upload_to='about_images/')
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name='image_about')
    alt = models.CharField(max_length=100)

    def __str__(self):
        return self.alt


class Social(models.Model):
    """Social networks about class model"""
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.name
