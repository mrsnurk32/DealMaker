from django.db import models
import time
class Deal(models.Model):
    first_name = models.CharField(max_length = 120)
    last_name = models.CharField(max_length = 120)
    price = models.IntegerField()
    date = models.DateField(
        default = (time.strftime("%Y-%m-%d"))
    )
    time_str = models.TimeField()
    time_end = models.TimeField()
    def __str__(self):
        return self.first_name
