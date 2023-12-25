from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bank(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title