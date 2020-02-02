from django.urls import path
from .views import *

urlpatterns = [
    path('EnquiryForm/', EnquiryForm, name='EnquiryForm'),
]