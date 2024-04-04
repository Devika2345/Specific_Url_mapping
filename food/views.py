from django.shortcuts import render

# Create your views here.
def biriyani(request):
    return render(request,'biriyani.html')
    
def pizza(request):
    return render(request,'pizza.html')