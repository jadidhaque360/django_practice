from django.db import models

# Create your models here.

class cricketerfulldetails(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    department=models.CharField(max_length=50)
    class Meta:
        verbose_name="cricketerfulldetails"
        verbose_name_plural="cricketerfulldetailss"
    def __str__(self):
        return (self.name)