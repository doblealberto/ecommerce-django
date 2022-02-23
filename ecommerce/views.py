from django.shortcuts import render

def templateshooting(request):
    return render(request, 'store.html')
