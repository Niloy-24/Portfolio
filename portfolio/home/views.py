from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("/")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("/about")
    return render(request, 'about.html')

def projects(request):
    # return HttpResponse("/projects")
    return render(request, 'projects.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        # print(name, email, phone, desc )
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("Thank You")

    # return HttpResponse("/contact") 
    return render(request, 'contact.html')