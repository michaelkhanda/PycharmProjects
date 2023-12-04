from django.shortcuts import render

from main_app.users import people


# Create your views here.
def home_page(request):
    name = "Jerry Springer"
    age = 18
    users = people

    data = {
        "name": name,
        'age': age,
        'users': users
    }
    return render(request, 'index.html', context=data)
