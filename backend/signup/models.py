from django.db import models

class Subscriber(models.Model):
    user_email = models.CharField(max_length=254)
    user_location = models.CharField(max_length=30)
    registered_on = models.DateTimeField('registered on')
    def __str__(self):
        return self.user_email + " from " + self.user_location