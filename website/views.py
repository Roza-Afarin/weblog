from django.shortcuts import render

# Create your views here.
def home_index(request):
    return render(request,'website/index.html')

def about_index(request):
    return render(request,'website/about.html')

def contact_index(request):
    return render(request,'website/contact.html')