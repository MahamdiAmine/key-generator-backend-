from django.db import models
from datetime import date

from django.urls import reverse


class Key(models.Model):
    name = models.CharField(max_length=25)
    key = models.CharField(max_length=50, unique=True)
    creation_date = models.DateField(default=date.today)
    life_duration = models.IntegerField(blank=True, default=365)
    remark = models.CharField(max_length=500, blank=True)

    @property
    def is_expired(self):
        return (date.today() - self.creation_date).days >= self.life_duration

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('key:key-detail', args=[str(self.id)])
