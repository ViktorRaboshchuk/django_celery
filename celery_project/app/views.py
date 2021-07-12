from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from app.forms import ContactForm
from app.models import Contact
from app.service import send
from .tasks import send_spam_email


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'app/contact.html'

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)