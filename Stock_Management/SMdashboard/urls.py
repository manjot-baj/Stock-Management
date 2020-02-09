from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                path('', views.Dashboard.as_view(), name="dashboard"),
                path('client_data/', views.ClientView.as_view(), name="client_data"),
                path('new_client/', views.ClientView.as_view(), {'client_form': ''}, name="new_client")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
