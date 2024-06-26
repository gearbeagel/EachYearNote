from django.db import models
from django.utils.text import slugify


# Create your models here.
class YearlyCards(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    contents = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Photo(models.Model):
    card = models.ForeignKey(YearlyCards, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255, blank=True)
