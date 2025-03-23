from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def admin_check(request):
    return render(request, 'Check_Application.html')