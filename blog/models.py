from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    temporary_field = models.CharField(max_length=100, null=True, blank=True)  # Temporary field

    def __str__(self):
        return self.title


