from django.db import models


class ImageModel(models.Model):
    img = models.ImageField(upload_to='img/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
