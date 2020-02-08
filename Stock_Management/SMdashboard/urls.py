from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                path('', views.Dashboard.as_view(), name="dashboard"),
                path('enquiry', views.Enquiry.as_view(), name="enquiry"),
                path('enquirySubmitted/', views.Success.as_view(), name="enquirySubmitted"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
