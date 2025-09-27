from django.shortcuts import render

def about_us_view(request):
    """
    Renders the About Us page template.
    """
    return render(request, 'about/about_us.html')

def contact_us_view(request):
    """
    Renders the Contact Us page template (templates/about/contact_us.html).

    NOTE: In a real application, this function would also handle form submission
    (POST request) to process and send the message, but here it just renders
    the static page.
    """
    return render(request, 'about/contact_us.html')

