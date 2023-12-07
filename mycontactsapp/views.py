from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from .models import Contact


def index(request):
    # Display contacts
    contacts = Contact.objects.all().order_by(
        "first_name", "last_name"
    )  # Fetch contacts and order them alphabetically
    contact_list = ""
    for contact in contacts:
        contact_list += f"{contact.first_name} {contact.last_name}<br>"
    # Make stylistic modifications
    styled_list = f"<div style='text-align: center; font-family: Arial, sans-serif;'>{contact_list}</div>"
    # Center the list and set the font family to Arial or sans-serif
    return HttpResponse("All Contacts:<br>" + styled_list)
    # Return the updated contact list
