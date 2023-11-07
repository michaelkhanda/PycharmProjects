from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')


def shop(request):
    return None


def about(request):
    return None


def contact(request):
    return None


def faq(request):
    return None