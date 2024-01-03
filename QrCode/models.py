from django.db import models


class ImageGenerator(models.Model):
    imag = models.ImageField(upload_to='media')


class DecodeImage(models.Model):
    imag = models.ImageField(upload_to='media')
