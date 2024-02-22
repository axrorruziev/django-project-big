from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


# Create your views here.
def index2(request):
    return render(request, 'main/site.html')


def index3(request):
    return render(request, 'main/buy.html')

def index4(request):
    return render(request, 'main/laptop.html')