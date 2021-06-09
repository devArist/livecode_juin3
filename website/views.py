from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')