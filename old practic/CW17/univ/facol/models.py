from django.db import models

class Facolty(models.Model):
    name = models.CharField(max_length=72)
    def __str__(self):
        return self.name


class Prof(models.Model):
    name = models.CharField(max_length=72)
    Facolty= models.ForeignKey(Facolty, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=72)
    Prof= models.ForeignKey(Prof, on_delete=models.CASCADE)
    Facolty=models.ForeignKey(Facolty, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Student(models.Model):
    Facolty=models.ForeignKey(Facolty, on_delete=models.CASCADE)
    name = models.CharField(max_length=72)
    Lesson = models.ManyToManyField('Lesson')











# Create your models here.
