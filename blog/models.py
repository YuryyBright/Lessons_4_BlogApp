from django.db import models
from django.urls import reverse
# Create your models here

class Post(models.Model):
    title = models.CharField(max_length=255,)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    required_css_class = "form-control"
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_post', args=[str(self.id)])