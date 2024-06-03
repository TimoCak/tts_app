from django.db import models

# Create your models here.
from django.db import models

class SingleSpeaker(models.Model):
    model = models.TextField,
    emotion = models.TextField,
    speed = models.DecimalField
    text = models.TextField
