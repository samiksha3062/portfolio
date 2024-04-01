from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("This is my homepage (/)")
    context = {'name':'Samiksha','course':'Django'}
    return render(request,'home.html',context)

def about(request):
    # return HttpResponse("This is my about page (/about)")
    return render(request,'about.html')

def projects(request):
    # return HttpResponse("This is my project page (/projects)")
    return render(request,'projects.html')

def concat(request):
    # return HttpResponse("This is my concat page (/concat)")
    return render(request,'concat.html')




