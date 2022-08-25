from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='users/%Y/%m/%d/')
    about = models.TextField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
