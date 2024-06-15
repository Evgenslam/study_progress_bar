from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

from ..base_model import BaseModel

# TODO: refactor models, including M2M
# TODO: refactor slug as SELFEDU 
# TODO: put CustomUser to users?

class CustomUser(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=255, unique=False, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name), allow_unicode=True)
        super().save(*args, **kwargs) 

    def __str__(self):
        return self.name


class Textbook(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    textbook = models.ForeignKey(Textbook, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserTextbook(BaseModel):
    user = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    textbook = models.ForeignKey("Textbook", on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.textbook} for {self.user}"


class UserLesson(BaseModel):
    user = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    lesson = models.ForeignKey("Lesson", on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.lesson} for {self.user}"
