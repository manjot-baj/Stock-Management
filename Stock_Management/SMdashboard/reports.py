from django.db.models import CharField, ExpressionWrapper, F, Func, Prefetch, Q
from django.db.models import Value as V
from django.db.models.functions import Cast, Concat
from django.shortcuts import redirect
from SM import employee_data, enquiry, invoice


class EmployeeReport:

    def get_data(self, request, employee_id=None):
        data = {}
        record = employee_data.Employee.objects.filter(pk=employee_id).annotate(
            employee_photo=F('photo'),
            employee_name=F('name'),
            employee_address=F('address'),
            employee_city=F('city'),
            employee_state=F('state'),
            employee_pin_code=F('pin_code'),
            employee_country=F('country'),
            employee_mobile_no=F('mobile_no'),
            employee_email_id=F('email_id'),
            employee_qualification=F('qualification'),
            employee_type=F('type'),
            employee_job_profile=F('job_profile'),
            employee_job_description=F('job_description'),
            employee_date=ExpressionWrapper(Func(F('join_date'), V("DD/MM/YYYY"), function='TO_CHAR'),
                                            output_field=CharField()),
        )
        print(record)

        for each in record:
            data.update({
                'pk': each.pk,
                'employee_photo': each.employee_photo,
                'employee_name': each.employee_name,
                'employee_address': each.employee_address,
                'employee_city': each.employee_city,
                'employee_state': each.employee_state,
                'employee_pin_code': each.employee_pin_code,
                'employee_country': each.employee_country,
                'employee_mobile_no': each.employee_mobile_no,
                'employee_email_id': each.employee_email_id,
                'employee_qualification': each.employee_qualification,
                'employee_type': each.employee_type,
                'employee_job_profile': each.employee_job_profile,
                'employee_job_description': each.employee_job_description,
                'employee_date': each.employee_date,

            })
            print(data)
        return data

class EnquiryReport:

    def get_data(self, request, enquiry_id=None):
        data = {}
        record = enquiry.Enquiry.objects.filter(pk=enquiry_id).annotate(
            enquiry_first_name=F('first_name'),
            enquiry_last_name=F('last_name'),
            enquiry_customer_type=F('customer_type__name'),
            enquiry_address=F('address'),
            enquiry_handled_by=F('handled_by__name'),
            enq_type=F('enquiry_type__name'),
            enquiry_product_name=F('product_name'),
            enquiry_description=F('description'),
            enquiry_startPrice=F('startPrice'),
            enquiry_endPrice=F('endPrice'),
            enquiry_mobile_no=F('mobile_no'),
            enquiry_whatsapp_no=F('whatsapp_no'),
            enquiry_contact_no=F('contact_no'),
            enquiry_email_id=F('contact_no'),

            date=ExpressionWrapper(Func(F('enquiry_date'), V("DD/MM/YYYY"), function='TO_CHAR'),
                                            output_field=CharField()),
        )
        print(record)

        for each in record:
            data.update({
                'pk': each.pk,
                'enquiry_first_name': each.enquiry_first_name,
                'enquiry_last_name': each.enquiry_last_name,
                'enquiry_customer_type': each.enquiry_customer_type,
                'enquiry_address': each.enquiry_address,
                'enquiry_handled_by': each.enquiry_handled_by,
                'enq_type': each.enq_type,
                'enquiry_product_name': each.enquiry_product_name,
                'enquiry_description': each.enquiry_description,
                'enquiry_startPrice': each.enquiry_startPrice,
                'enquiry_endPrice': each.enquiry_endPrice,
                'enquiry_mobile_no': each.enquiry_mobile_no,
                'enquiry_whatsapp_no': each.enquiry_whatsapp_no,
                'enquiry_contact_no': each.enquiry_contact_no,
                'enquiry_email_id': each.enquiry_email_id,

            })
            print(data)
        return data


class ProductReport:

    def get_data(self, request, product_id=None):
        data = {}
        record = invoice.Product.objects.filter(pk=product_id).annotate(
            product_name=F('name'),
            product_unit_price=F('unit_price'),
            product_u_o_m=F('u_o_m'),
            product_quantity=F('quantity'),
            product_description=F('description'),
            product_product_type=F('product_type'),
            product_purchase_rate=F('purchase_rate'),
            product_purchase_rate_currency=F('purchase_rate_currency'),
            product_h_s_n_or_s_a_c=F('h_s_n_or_s_a_c'),
            product_s_k_u=F('s_k_u'),
            product_tax=F('tax'),
            product_c_e_s_s_percent=F('c_e_s_s_percent'),
            product_c_e_s_s=F('c_e_s_s'),
            #
            # date=ExpressionWrapper(Func(F('enquiry_date'), V("DD/MM/YYYY"), function='TO_CHAR'),
            #                                 output_field=CharField()),
        )
        print(record)

        for each in record:
            data.update({
                'pk': each.pk,
                'product_name': each.product_name,
                'product_unit_price': each.product_unit_price,
                'product_u_o_m': each.product_u_o_m,
                'product_quantity': each.product_quantity,
                'product_description': each.product_description,
                'product_product_type': each.product_product_type,
                'product_purchase_rate': each.product_purchase_rate,
                'product_purchase_rate_currency': each.product_purchase_rate_currency,
                'product_h_s_n_or_s_a_c': each.product_h_s_n_or_s_a_c,
                'product_s_k_u': each.product_s_k_u,
                'product_tax': each.product_tax,
                'product_c_e_s_s_percent': each.product_c_e_s_s_percent,
                'product_c_e_s_s': each.product_c_e_s_s,

            })
            print(data)
        return data
