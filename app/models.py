from django.db import models


class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["nombre"] = "Nombre de curso debe tener a lo menos 5 caracteres"
        if len(postData['description']) < 15:
            errors["description"] = "Descripción de curso debe tener a lo menos 15 caracteres"
        if self.filter(name=postData['name']).exists():
            errors['name2'] = "Ya existe el Curso"
        return errors


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __str__(self):
        return f'{self.name} {self.description}'


# class Description(models.Model):
#     description = models.TextField()
#     course = models.OneToOneField(
#         Course, on_delete=models.CASCADE, null=False, blank=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
