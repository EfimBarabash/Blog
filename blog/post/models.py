from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'
        ordering = ('-created_date',)
