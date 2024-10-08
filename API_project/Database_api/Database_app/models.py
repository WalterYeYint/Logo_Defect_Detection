from django.db import models
from django.utils import timezone
import datetime

class Detections(models.Model):
    serial_no = models.IntegerField(primary_key = True, blank=False)
    # time = models.DateTimeField(default = timezone.now)
    time = models.CharField(default = timezone.now, max_length=30)
    image = models.ImageField(upload_to='images/')
    result_image = models.ImageField(upload_to='result_images/', default = "None")
    result = models.CharField(max_length = 50, default='not assigned', blank=True)
    # name = models.CharField(max_length = 50, default='NULL', blank=True)

    # def __str__(self):
    #     return self.serial_no
    
