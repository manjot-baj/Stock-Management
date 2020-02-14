from django.db.models import CharField, ExpressionWrapper, F, Func, Prefetch, Q
from django.db.models import Value as V
from django.db.models.functions import Cast, Concat
from django.shortcuts import redirect
from SM.company_data import Client, Vendor


class ClientReport:

    def get_data(self, request, client_id=None):
        data = {}
        record = Client.objects.filter(pk=client_id).annotate(
            client_name=F('name'), client_contact_Name=F('contact_Name'), client_TIN=F('TIN'),
            client_email=F('email'), client_phone=F('phone'), client_billing_address=F('billing_address'),
            client_billing_zip=F('billing_zip'), client_billing_city=F('billing_city'),
            client_billing_state=F('billing_state'), client_billing_country=F('billing_country'),
            client_shipping_address=F('shipping_address'), client_shipping_zip=F('shipping_zip'),
            client_shipping_city=F('shipping_city'), client_shipping_state=F('shipping_state'),
            client_shipping_country=F('shipping_country'), client_details=F('details'),
            client_GSTIN=F('GSTIN'), client_PAN=F('PAN'), client_balance=F('balance')
        )
        print(record)

        for each in record:
            data.update({
                'pk': each.pk,
                'client_name': each.client_name,
                'client_contact_Name': each.client_contact_Name,
                'client_TIN': each.client_TIN,
                'client_email': each.client_email,
                'client_phone': each.client_phone,
                'client_billing_address': each.client_billing_address,
                'client_billing_zip': each.client_billing_zip,
                'client_billing_city': each.client_billing_city,
                'client_billing_state': each.client_billing_state,
                'client_billing_country': each.client_billing_country,
                'client_shipping_address': each.client_shipping_address,
                'client_shipping_zip': each.client_shipping_zip,
                'client_shipping_city': each.client_shipping_city,
                'client_shipping_state': each.client_shipping_state,
                'client_shipping_country': each.client_shipping_country,
                'client_details': each.client_details,
                'client_GSTIN': each.client_GSTIN,
                'client_PAN': each.client_PAN,
                'client_balance': each.client_balance
            })
            print(data)
        return data


class VendorReport:

    def get_data(self, request, vendor_id=None):
        data = {}
        record = Vendor.objects.filter(pk=vendor_id).annotate(
            vendor_name=F('name'), vendor_contact_Name=F('contact_Name'), vendor_TIN=F('TIN'),
            vendor_email=F('email'), vendor_phone=F('phone'), vendor_billing_address=F('billing_address'),
            vendor_billing_zip=F('billing_zip'), vendor_billing_city=F('billing_city'),
            vendor_billing_state=F('billing_state'), vendor_billing_country=F('billing_country'),
            vendor_shipping_address=F('shipping_address'), vendor_shipping_zip=F('shipping_zip'),
            vendor_shipping_city=F('shipping_city'), vendor_shipping_state=F('shipping_state'),
            vendor_shipping_country=F('shipping_country'), vendor_details=F('details'),
            vendor_GSTIN=F('GSTIN'))
        print(record)

        for each in record:
            data.update({
                'pk': each.pk,
                'vendor_name': each.vendor_name,
                'vendor_contact_Name': each.vendor_contact_Name,
                'vendor_TIN': each.vendor_TIN,
                'vendor_email': each.vendor_email,
                'vendor_phone': each.vendor_phone,
                'vendor_billing_address': each.vendor_billing_address,
                'vendor_billing_zip': each.vendor_billing_zip,
                'vendor_billing_city': each.vendor_billing_city,
                'vendor_billing_state': each.vendor_billing_state,
                'vendor_billing_country': each.vendor_billing_country,
                'vendor_shipping_address': each.vendor_shipping_address,
                'vendor_shipping_zip': each.vendor_shipping_zip,
                'vendor_shipping_city': each.vendor_shipping_city,
                'vendor_shipping_state': each.vendor_shipping_state,
                'vendor_shipping_country': each.vendor_shipping_country,
                'vendor_details': each.vendor_details,
                'vendor_GSTIN': each.vendor_GSTIN,
            })
            print(data)
        return data
