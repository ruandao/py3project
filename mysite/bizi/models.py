from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

class Img(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length = 200)
    model_pic = models.ImageField(upload_to='pic_folder/')
    pub_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title
