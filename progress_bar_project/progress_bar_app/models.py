from django.db import models


class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name


class Textbook(models.Model):
    name = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    textbook = models.ForeignKey(Textbook, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserTextbook(models.Model):
    user = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    textbook = models.ForeignKey("Textbook", on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.textbook} for {self.user}"


class UserLesson(models.Model):
    user = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    lesson = models.ForeignKey("Lesson", on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.lesson} for {self.user}"

