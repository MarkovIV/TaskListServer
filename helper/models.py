from django.db import models

# Create your models here.

class Helper(models.Model):
    task = models.CharField(max_length=500, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, blank=True)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return self.task
