from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

def about_us_view(request):
    """
    Renders the About Us page template (templates/about/about_us.html).
    """
    return render(request, 'about/about_us.html')

def contact_us_view(request):
    """
    Handles the Contact Us page, displaying the form on GET and processing 
    the email submission on POST.
    """
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        from_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Simple validation
        if not all([name, from_email, subject, message]):
            messages.error(request, 'Please fill out all fields in the contact form.')
            return render(request, 'about/contact_us.html')
        
        # 1. Define the email recipient (from settings.py)
        recipient_list = [settings.CONTACT_FORM_RECIPIENT]
        
        # 2. Construct the email body
        email_subject = f"Contact Form: {subject}"
        email_body = (
            f"Message from: {name}\n"
            f"Reply-to Email: {from_email}\n\n"
            f"Message:\n{message}"
        )
        
        try:
            # 3. Send the email using configured backend (console/SMTP)
            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL, # Sender address
                recipient_list,               # Recipient address (support@sustainify.com)
                fail_silently=False,
            )
            # Success message and redirect
            messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
            return redirect('about:contact_us') 

        except Exception as e:
            # Error message
            print(f"Error sending email: {e}")
            messages.error(request, 'There was an error sending your message. Please try again later.')
            
    # For GET requests, render the page
    return render(request, 'about/contact_us.html')
