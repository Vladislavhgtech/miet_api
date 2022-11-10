from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Iot(models.Model):
    title=models.CharField(max_length=255)
    gps_x=models.CharField(max_length=255)
    gps_y=models.CharField(max_length=255)
    param_value=models.CharField(max_length=255)
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, verbose_name='Устройство', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
