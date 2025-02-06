from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("<h1>Returned By HttpResponse</h1>")


def render_html(request):
    return render(request, 'index.html')
