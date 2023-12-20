from django.shortcuts import render
from .models import Products, Company, Students, Course
from django.http import HttpResponse

def index(request):
    # company = Company.objects.get(name='Alabuga')
    # products = company.products_set.create(name='Телек', price='25000')
    tom = Students.objects.create(name='Tom')
    student = tom.course.create(name='Algebra')
    
    return render(request, 'index.html', context={'student': student})
