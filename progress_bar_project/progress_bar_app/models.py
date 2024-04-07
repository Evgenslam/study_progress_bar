from django.db import models


class Textbook(models.Model):
    name = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    textbook = models.ForeignKey(Textbook, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
