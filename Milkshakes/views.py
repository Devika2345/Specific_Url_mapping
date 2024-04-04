from django.shortcuts import render

# Create your views here.
def oreoshake(request):
    return render(request,'oreoshake.html')
def kitkatshake(request):
    return render(request,'kitkatshake.html')
    
