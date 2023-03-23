import os
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from . import forms
from .models import Contact
from .utils import generate_qr_code

# Create your views here.
def index(request):
    return render(request, 'contact/index.html')


def create_contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            profile_pic = form.cleaned_data['profile_pic']

            new_contact = Contact.objects.create(name=name, phone_number=phone_number, profile_pic=profile_pic)

            qr = generate_qr_code(request, new_contact.id)
            qr_filename = f"{new_contact.id}.png"
            qr_path = os.path.join(settings.MEDIA_ROOT, 'qr_codes', qr_filename)

            qr.save(qr_path)

            new_contact.qr_code = os.path.join('qr_codes', qr_filename)
            new_contact.save()

            print(new_contact)

            return HttpResponseRedirect(reverse('view_contact', args=[new_contact.id]))
        else:
            print(form.errors)

    return render(request, 'contact/create_contact.html', {
        'form': forms.ContactForm
    })


def view_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    return render(request, "contact/view_contact.html", {
        'contact': contact
    })
