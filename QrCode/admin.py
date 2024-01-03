from django.contrib import admin
from QrCode.models import ImageGenerator, DecodeImage
# Register your models here.


@admin.register(ImageGenerator)
class ImageGeneratorAdmin(admin.ModelAdmin):
    list_display = ('id', 'imag')


@admin.register(DecodeImage)
class DecodeImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'imag')