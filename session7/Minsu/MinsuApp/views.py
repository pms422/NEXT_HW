from django.shortcuts import render

# Create your views here.
def Minsu(request):
    #로직
    return render(request, 'Minsu.html')

def project(request):
    #로직
    return render(request, 'project.html')