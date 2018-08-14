from django.db import models

# Create your models here.

class airplanes(models.Model):
    name = models.CharField(max_length=120)
    weight = models.IntegerField()
    passengers = models.CharField(max_length=120)
    picture = models.ImageField(null=True)
    other_info = models.CharField(max_length=120)

    def __str__(self):
        return self.name