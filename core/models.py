from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from core.managers import EmployerManager, PositionManager


class Position(models.Model):
    category_choices = (
        ('specialist', 'Специалист'),
        ('employee', 'Служащий'),
        ('worker', 'Рабочий'),
    )

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=category_choices)

    objects_pos = PositionManager()  # объявляем свой менеджер позиций

    def __str__(self):
        return self.name


class Employer(models.Model):
    gender_choices = (
        ('male', 'Мужской'),
        ('female', 'Женский'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=gender_choices)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    position = models.ForeignKey("Position", on_delete=models.PROTECT, null=True, blank=True)

    objects_emp = EmployerManager()  # объявляем свой менеджер сотрудников

    def __str__(self):
        return self.first_name
