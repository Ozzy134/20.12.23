from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Companies'


class Products(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'

class Course(models.Model):
    name = models.CharField(max_length=20)

class Students(models.Model):
    name = models.CharField(max_length=50)
    course = models.ManyToManyField('Course')