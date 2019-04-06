from django.db import models

class Name(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
    last_name = models.CharField(max_length=264, unique=True)
    email = models.EmailField(max_length=24, unique=True)
    def __str__(self):
        return self.top_name
