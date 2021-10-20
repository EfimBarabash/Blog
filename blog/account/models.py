from django.db import models
from django.contrib.auth.models import User


def user_directory_path_profile(instance, filename):
    return f'{instance.user.username}/profile/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    about_me = models.TextField(blank=True)
    photo = models.ImageField(upload_to=user_directory_path_profile, blank=True,)
    birthday = models.DateField(blank=True, null=True)
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False)

    def __str__(self):
        return f'Profile for user {self.user.username}'

