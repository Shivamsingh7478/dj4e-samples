from django.db import models

class Breed(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Cat(models.Model):
    nickname = models.CharField(max_length=200)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length=300)

    def __str__(self):
        return self.nickname