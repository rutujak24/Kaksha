from django.db import models
from django.utils import timezone

class Subscriber(models.Model):
    email = models.EmailField(unique=False)
    subscribed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.email}"



