from django.db import models

def upload_to(instance, filename):
    return f'images/{filename}'


class Image(models.Model):
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)