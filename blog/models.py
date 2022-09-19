from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
from django.utils.timezone import now

User = get_user_model()


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return f'{self.name[:50]}'

    def get_absolute_url(self):
        return reverse('post_list', args=[self.slug])

    def get_qty_of_each_category(self):
        return self.post.all().count()


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return f'{self.name[:50]}'


class Post(models.Model):
    author = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    text = models.TextField()
    image = models.ImageField(upload_to='articles/%Y/%m/%d/')
    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag, related_name='post')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Post: {self.title[:50]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.category.slug, self.slug])


class Recipe(models.Model):
    name = models.CharField(max_length=150)
    serves = models.CharField(max_length=100)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = RichTextField()
    directions = RichTextField()
    post = models.ForeignKey(
        Post,
        related_name='recipe',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Recipe: {self.name[:50]}'


class Comment(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField(max_length=500)
    post = models.ForeignKey(
        Post,
        related_name='comment',
        on_delete=models.CASCADE,
    )
    create_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return f'Comment: {self.name[:50]}'
