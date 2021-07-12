from django.urls import path

from app.views import ContactView

urlpatterns = [
    path('', ContactView.as_view(), name="contact")
]