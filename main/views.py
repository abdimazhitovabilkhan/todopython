from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage (request):
    return HttpResponse("Абильхан Молодец!")


def test (request):
    return render (request, "test.html")
def second (request):
    return HttpResponse("Hello Bishkek")
def third (request):
    return HttpResponse("This is page3")

