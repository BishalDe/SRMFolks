from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'homePage.html')

def eventsPage(request):
    return render(request, 'eventsPage.html')