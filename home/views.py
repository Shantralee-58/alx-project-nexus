from django.shortcuts import render

def home_page_view(request):
    """
    Renders the main homepage template.
    """
    return render(request, 'home/home.html')
