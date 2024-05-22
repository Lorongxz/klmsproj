from django.shortcuts import render

# Create your views here.

def index_gender(requests):
    return render(requests, 'gender/index.html')