from django.db import models


class Analysis(models.Model):
    """
    Defines an Analysis that can be showed on the website.
    """
    title = models.CharField(max_length=100)
    text = models.TextField()
    link = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)

    def __str__(self):
        return self.title
