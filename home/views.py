from django.shortcuts import render

def index(request):
    """ a view to render the index page """
    return render(request, 'index.html')
