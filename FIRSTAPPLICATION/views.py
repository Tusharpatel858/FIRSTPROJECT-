from django.shortcuts import render


# Create your views here.
def index(request):
    """The home page for FIRSTAPPLICATION"""
    return render(request,'FIRSTAPPLICATION/Index.html')

def img(request):
    return render(request ,'FIRSTAPPLICATION/static_image.html')