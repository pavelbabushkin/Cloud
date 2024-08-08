from django.shortcuts import render

def authorize(request):
    return render(request, "Index.html")

def reg(request):
    return render(request, "Regist.html")

'''
def postuser(request):
    if Newuser.objects.filter(email=request.POST.get("auth_email", "Undefined")).exists():
        render(request, "Profile.html")
    else:
        User = Newuser(email=request.POST.get("auth_email", "Undefined"),
                       password=request.POST.get("auth_pass", "Undefined"))
    return User.save()
'''


# Create your views here.
