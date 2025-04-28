from django.shortcuts import render


def home(request):
    return render(request,'college/home.html')