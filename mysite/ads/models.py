from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator

class Ad(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    text = models.TextField()
    tags = models.TextField(blank=True, help_text='Enter tags separated by commas')
    picture = models.BinaryField(null=True, blank=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # ✅ FIX HERE
    comments = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='ads.Comment',
        related_name='comments_owned'
    )


    # Favorites
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL,
        through='Fav', related_name='favorite_ads')

    def __str__(self):
        return self.title

class Auto(models.Model):
    nickname = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)

    def __str__(self):
        return self.nickname

class Comment(models.Model):
    text = models.TextField(validators=[MinLengthValidator(3)])
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:11] + ' ...' if len(self.text) > 15 else self.text

class Fav(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # https://docs.djangoproject.com/en/4.2/ref/models/options/#unique-together
    class Meta:
        unique_together = ('ad', 'user')

    def __str__(self):
        return '%s likes %s'%(self.user.username, self.ad.title[:10])

