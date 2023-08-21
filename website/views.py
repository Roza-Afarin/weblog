from django.shortcuts import render
from django.contrib import messages
from website.forms import ContactForm

# Create your views here.
def home_index(request):
    return render(request,'website/index.html')

def about_index(request):
    return render(request,'website/about.html')

def contact_index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.SUCCESS, "your ticket submitted successfully")
        else:
            messages.add_message(request, messages.ERROR, "your ticket didn't submitted")
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})