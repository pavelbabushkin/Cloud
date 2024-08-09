from django.shortcuts import render

def authorize(request):
    return render(request, "Index.html")

def reg(request):
    return render(request, "Regist.html")


# Create your views here.
