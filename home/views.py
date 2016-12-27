from django.shortcuts import render
import logging

logger = logging.getLogger('django')


def home(request):
    message = 'This is a Python Generated Message'
    logger.info(message)
    return render(request, 'home.html', {'message': message})


def python(request):
    return render(request, 'python.html')


def django(request):
    return render(request, 'django.html')
