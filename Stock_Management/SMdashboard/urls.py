from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('', views.Dashboard.as_view(), name="dashboard"),
                  path('client_data/', views.ClientView.as_view(), name="client_data"),
                  path('new_client/', views.ClientView.as_view(), {'client_form': ''}, name="new_client"),
                  path('viewclient/<int:object_id>', views.ClientView.as_view(), name="viewclient"),
                  path('vendor_data/', views.VendorView.as_view(), name="vendor_data"),
                  path('new_vendor/', views.VendorView.as_view(), {'vendor_form': ''}, name="new_vendor"),
                  path('viewvendor/<int:object_id>', views.VendorView.as_view(), name="viewvendor"),
                  path('enquiry_form/', views.Enquiry.as_view(), {'enquiry_form': ''}, name="enquiry_form"),
                  path('enquiry/', views.Enquiry.as_view(), name="enquiry"),
                  path('daybook/', views.DayBookView.as_view(), name="daybook"),
                  path('daybook_form/', views.DayBookView.as_view(), {'daybook_form': ''}, name="daybook_form"),
                  path('employee/', views.Employee.as_view(), name="employee"),
                  path('employee_form/', views.Employee.as_view(), {'employee_form': ''}, name="employee_form"),
                  path('service/', views.Service.as_view(), name="service"),
                  path('service_form/', views.Service.as_view(), {'service_form': ''}, name="service_form"),
                  path('product_data/', views.ProductView.as_view(), name="product_data"),
                  path('new_product/', views.ProductView.as_view(), {'product_form': ''}, name="new_product"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
