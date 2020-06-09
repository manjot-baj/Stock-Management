from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('', views.Dashboard.as_view(), name="dashboard"),
                  path('login/', views.Dashboard.as_view(), {'login': ''}, name="login"),
                  path('logout/', views.Dashboard.as_view(), {'logout': ''}, name="logout"),
                  path('client_data/', views.ClientView.as_view(), name="client_data"),
                  path('new_client/', views.ClientView.as_view(), {'client_form': ''}, name="new_client"),
                  path('new_client_add/', views.ClientAdd.as_view(), {'client_form_fill': ''}, name="new_client_add"),
                  path('viewclient/<int:object_id>', views.ClientView.as_view(), name="viewclient"),
                  path('client_edit_form/<int:object_id>', views.ClientEdit.as_view(), {'client_edit_form': ''},
                       name="client_edit_form"),
                  path('vendor_data/', views.VendorView.as_view(), name="vendor_data"),
                  path('new_vendor/', views.VendorView.as_view(), {'vendor_form': ''}, name="new_vendor"),
                  path('new_vendor_add/', views.VendorAdd.as_view(), {'vendor_form_fill': ''}, name="new_vendor_add"),
                  path('viewvendor/<int:object_id>', views.VendorView.as_view(), name="viewvendor"),
                  path('enquiry_form/', views.Enquiry.as_view(), {'enquiry_form': ''}, name="enquiry_form"),
                  path('enquiry/', views.Enquiry.as_view(), name="enquiry"),
                  path('viewEnquiry/<int:object_id>', views.Enquiry.as_view(), name="view_enquiry"),
                  path('enquiry_edit_form/<int:object_id>/', views.EnquiryEdit.as_view(), {'enquiry_edit_form': ''},
                       name="enquiry_edit_form"),
                  path('enquiry_reply_form/<int:object_id>', views.EnquiryReply.as_view(), {'enquiry_reply_form': ''},
                       name="enquiry_reply_form"),
                  path('filterEnquiry/', views.Enquiry.as_view(), {'filterDate': ''},
                       name="filter_enquiry_date"),
                  # path('viewReply/<int:object_id>', views.EnquiryReply.as_view(), {'viewReply': ''},
                  #      name="viewReply"),
                  path('daybook/', views.DayBookView.as_view(), name="daybook"),
                  path('daybook_form/', views.DayBookView.as_view(), {'daybook_form': ''}, name="daybook_form"),
                  path('daybook_edit_form/<int:object_id>', views.DayBookEdit.as_view(), {'daybook_edit_form': ''},
                       name="daybook_edit_form"),
                  path('filterDayBookDate/', views.DayBookView.as_view(), {'filterDate': ''},
                       name="filter_day_book_date"),
                  path('viewdaybook/<int:object_id>', views.DayBookView.as_view(), name="view_daybook"),
                  path('employee/', views.Employee.as_view(), name="employee"),
                  path('employee_form/', views.Employee.as_view(), {'employee_form': ''}, name="employee_form"),
                  path('viewEmployee/<int:object_id>', views.Employee.as_view(), name="view_employee"),
                  path('employee_edit_form/<int:object_id>', views.EmployeeEdit.as_view(), {'employee_edit_form': ''},
                       name="employee_edit_form"),
                  path('filterEmployee/', views.Employee.as_view(), {'filterDate': ''},
                       name="filter_employee_date"),
                  path('service/', views.Service.as_view(), name="service"),
                  path('service_form/', views.Service.as_view(), {'service_form': ''}, name="service_form"),
                  path('viewservice/<int:object_id>', views.Service.as_view(), name="viewservice"),
                  path('viewserviceinvoice/<int:service_id>', views.Service.as_view(), name="viewserviceinvoice"),
                  path('service_edit_form/<int:object_id>/', views.ServiceEdit.as_view(), {'service_edit_form': ''},
                       name="service_edit_form"),
                  path('service_reply_form/<int:object_id>', views.ServiceReply.as_view(), {'service_reply_form': ''},
                       name="service_reply_form"),
                  path('filterServiceDate/', views.Service.as_view(), {'filterDate': ''},
                       name="filter_service_date"),
                  # path('product_data/', views.ProductView.as_view(), name="product_data"),
                  # path('viewProduct/<int:object_id>', views.ProductView.as_view(), name="view_product"),
                  # path('new_product/', views.ProductView.as_view(), {'product_form': ''}, name="new_product"),
                  path('amc_data/', views.AMC_View.as_view(), name="amc_data"),
                  path('amc_view/<int:object_id>', views.AMC_View.as_view(), name="amc_view"),
                  path('amc/<int:object_id>', views.AMC_View.as_view(), {'amc_form': ''}, name="amc"),

                  path('quotation_order_maker/', views.QuotationView.as_view(),
                       {'quotation_order_maker': '', 'quotation_order_lines': ''},
                       name="quotation_order_maker"),
                  path('quotation_order_table/', views.QuotationView.as_view(), name="quotation_order_table"),

                  path('quotation_product_detail/', views.QuotationView.as_view(), {'quotation_product_detail': ''},
                       name="quotation_product_detail"),

                  path('view_quotation_order/<int:object_id>', views.QuotationView.as_view(),
                       name="view_quotation_order"),
                  path('filter_quotation_date/', views.QuotationView.as_view(), {'filterDate': ''},
                       name="filter_quotation_date"),
                  path('quotation_without_gst/', views.QuotationView.as_view(), {'quotation_without_gst': ''},
                       name="quotation_without_gst"),


                  path('invoice_maker/', views.InvoiceView.as_view(), {'invoice_maker': '', 'invoice_lines': ''},
                       name="invoice_maker"),
                  path('invoice_table/', views.InvoiceView.as_view(), name="invoice_table"),
                  path('view_invoice_order/<int:object_id>', views.InvoiceView.as_view(),
                       name="view_invoice_order"),
                  path('product_detail/', views.InvoiceView.as_view(), {'product_detail': ''},
                       name="product_detail"),

                  path('client_billing_state_detail/', views.InvoiceView.as_view(), {'client_billing_state_detail': ''},
                       name="client_billing_state_detail"),

                  path('invoice_without_gst/', views.InvoiceView.as_view(), {'invoice_without_gst': ''},
                       name="invoice_without_gst"),

                  path('filter_invoice_date/', views.InvoiceView.as_view(), {'filterDate': ''},
                       name="filter_invoice_date"),


                  path('billOfSupply_table/', views.BillOfSupplyView.as_view(), name="billOfSupply_table"),
                  path('billOfSupply_maker/', views.BillOfSupplyView.as_view(), {'billOfSupply_maker': '', 'billOfSupply_lines': ''},
                       name="billOfSupply_maker"),
                  path('billOfSupply_without_gst/', views.BillOfSupplyView.as_view(), {'billOfSupply_without_gst': ''},
                       name="billOfSupply_without_gst"),
                  path('filter_billOfSupply_date/', views.BillOfSupplyView.as_view(), {'filterDate': ''},
                       name="filter_billOfSupply_date"),
                  path('view_billOfSupply_order/<int:object_id>', views.BillOfSupplyView.as_view(),
                       name="view_billOfSupply_order"),



              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
