from django.shortcuts import render
from .models import DollarCourse


def main(request):
    return render(request, 'index.html')
