from django.db import models
from django.conf import settings

class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blogs/')
    blog_name = models.CharField(max_length=255)
    blog_content = models.TextField()
    publish_date = models.DateField(auto_now_add=True)
