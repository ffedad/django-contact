from django.shortcuts import render

def contact_view(request):
    return render(request, 'contactapp/home.html')
