from django.db import models


class Settings(models.Model):
    site_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='settings/')
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    description = models.TextField(max_length=300)
    facebook_link = models.URLField(max_length=200)
    twitter_link = models.URLField(max_length=200)
    instagram_link = models.URLField(max_length=200)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name_plural = "Settings"
