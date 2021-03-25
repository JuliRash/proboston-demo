from django.db import models


class UserInformation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    ico = models.CharField(max_length=8)

    def __str__(self):
        return self.name
