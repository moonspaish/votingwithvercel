from django.db import models


class Vote(models.Model):
    name = models.CharField(max_length=100)
    choice = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' - ' + self.choice
