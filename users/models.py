from django.db import models

# Create your models here.

class Command(models.Model):
    name = models.CharField(max_length=250)
    scientific_name = models.CharField(max_length=250)

    def __str__(self):
        return self.common_name