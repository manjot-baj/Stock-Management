from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from SM.company_data import Client, Vendor
import xlrd
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.db.models import (Case, CharField, Count, DateTimeField,
                              ExpressionWrapper, F, FloatField, Func, Max, Min,
                              Prefetch, Q, Sum, Value, When, Subquery)
from SM import enquiry, dayBook


class Dashboard(View):
    dashboard_template = 'SMdashboard/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.dashboard_template)

    def post(self, request, *args, **kwargs):
        return render(request, self.dashboard_template)


class ClientView(View):
    from .forms import ClientForm
    dashboard_template = 'SMdashboard/dashboard.html'
    data_template = 'SMdashboard/client-table.html'
    form_template = 'SMdashboard/clientform.html'
    form = ClientForm
    model = Client

    def get_data(self):
        data = self.model.objects.all().values('pk', 'name', 'contact_Name', 'TIN', 'email', 'phone',
                                               'billing_address', 'billing_zip', 'billing_city',
                                               'billing_state', 'billing_country',
                                               'shipping_address', 'shipping_zip', 'shipping_city',
                                               'shipping_state', 'shipping_country', 'details',
                                               'GSTIN', 'PAN', 'balance').order_by("-pk")
        return list(data)

    def get(self, request, *args, **kwargs):
        if 'client_form' in kwargs:
            return render(request, self.form_template, {'form': self.form})
        data = self.get_data()
        print(data)
        return render(request, self.data_template, {'data': data})

    def post(self, request, *args, **kwargs):
        form = self.ClientForm(request.POST, request.FILES)
        if form.is_valid():
            input_excel = request.FILES['input_excel']
            book = xlrd.open_workbook(file_contents=input_excel.read())
            sheet = book.sheet_by_index(0)
            # data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
            client_name = []
            contact_name = []
            client_tin = []
            email = []
            phone = []
            billing_address = []
            billing_zip = []
            billing_city = []
            billing_state = []
            billing_country = []
            shipping_address = []
            shipping_zip = []
            shipping_city = []
            shipping_state = []
            shipping_country = []
            private_details = []
            gstin = []
            pan = []
            balance = []

            for i in range(sheet.nrows):
                client_name.append(sheet.cell_value(i, 0))
                contact_name.append(sheet.cell_value(i, 1))
                client_tin.append(sheet.cell_value(i, 2))
                email.append(sheet.cell_value(i, 3))
                phone.append(sheet.cell_value(i, 4))
                billing_address.append(sheet.cell_value(i, 5))
                billing_zip.append(sheet.cell_value(i, 6))
                billing_city.append(sheet.cell_value(i, 7))
                billing_state.append(sheet.cell_value(i, 8))
                billing_country.append(sheet.cell_value(i, 9))
                shipping_address.append(sheet.cell_value(i, 10))
                shipping_zip.append(sheet.cell_value(i, 11))
                shipping_city.append(sheet.cell_value(i, 12))
                shipping_state.append(sheet.cell_value(i, 13))
                shipping_country.append(sheet.cell_value(i, 14))
                private_details.append(sheet.cell_value(i, 15))
                gstin.append(sheet.cell_value(i, 16))
                pan.append(sheet.cell_value(i, 17))
                balance.append(sheet.cell_value(i, 18))

            client_name.pop(0)
            contact_name.pop(0)
            client_tin.pop(0)
            email.pop(0)
            phone.pop(0)
            billing_address.pop(0)
            billing_zip.pop(0)
            billing_city.pop(0)
            billing_state.pop(0)
            billing_country.pop(0)
            shipping_address.pop(0)
            shipping_zip.pop(0)
            shipping_city.pop(0)
            shipping_state.pop(0)
            shipping_country.pop(0)
            private_details.pop(0)
            gstin.pop(0)
            pan.pop(0)
            balance.pop(0)

            for i in range(len(client_name)):
                self.model.objects.get_or_create(name=client_name[i], contact_Name=contact_name[i],
                                                 TIN=client_tin[i], email=email[i], phone=phone[i],
                                                 billing_address=billing_address[i], billing_zip=billing_zip[i],
                                                 billing_city=billing_city[i], billing_state=billing_state[i],
                                                 billing_country=billing_country[i],
                                                 shipping_address=shipping_address[i],
                                                 shipping_zip=shipping_zip[i], shipping_city=shipping_city[i],
                                                 shipping_state=shipping_state[i], shipping_country=shipping_country[i],
                                                 details=private_details[i], GSTIN=gstin[i], PAN=pan[i],
                                                 balance=balance[i])
            return redirect(to='client_data')
        return redirect(to='new_client')


class VendorView(View):
    from .forms import VendorForm
    dashboard_template = 'SMdashboard/dashboard.html'
    data_template = 'SMdashboard/vendor-table.html'
    form_template = 'SMdashboard/vendorform.html'
    form = VendorForm
    model = Vendor

    def get_data(self):
        data = self.model.objects.all().values('pk', 'name', 'contact_Name', 'TIN', 'email', 'phone',
                                               'billing_address', 'billing_zip', 'billing_city',
                                               'billing_state', 'billing_country',
                                               'shipping_address', 'shipping_zip', 'shipping_city',
                                               'shipping_state', 'shipping_country', 'details',
                                               'GSTIN').order_by("-pk")
        return list(data)

    def get(self, request, *args, **kwargs):
        if 'vendor_form' in kwargs:
            return render(request, self.form_template, {'form': self.form})
        data = self.get_data()
        print(data)
        return render(request, self.data_template, {'data': data})

    def post(self, request, *args, **kwargs):
        form = self.VendorForm(request.POST, request.FILES)
        if form.is_valid():
            input_excel = request.FILES['input_excel']
            book = xlrd.open_workbook(file_contents=input_excel.read())
            sheet = book.sheet_by_index(0)
            # data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
            vendor_name = []
            contact_name = []
            vendor_tin = []
            email = []
            phone = []
            billing_address = []
            billing_zip = []
            billing_city = []
            billing_state = []
            billing_country = []
            shipping_address = []
            shipping_zip = []
            shipping_city = []
            shipping_state = []
            shipping_country = []
            private_details = []
            gstin = []

            for i in range(sheet.nrows):
                vendor_name.append(sheet.cell_value(i, 0))
                contact_name.append(sheet.cell_value(i, 1))
                vendor_tin.append(sheet.cell_value(i, 2))
                email.append(sheet.cell_value(i, 3))
                phone.append(sheet.cell_value(i, 4))
                billing_address.append(sheet.cell_value(i, 5))
                billing_zip.append(sheet.cell_value(i, 6))
                billing_city.append(sheet.cell_value(i, 7))
                billing_state.append(sheet.cell_value(i, 8))
                billing_country.append(sheet.cell_value(i, 9))
                shipping_address.append(sheet.cell_value(i, 10))
                shipping_zip.append(sheet.cell_value(i, 11))
                shipping_city.append(sheet.cell_value(i, 12))
                shipping_state.append(sheet.cell_value(i, 13))
                shipping_country.append(sheet.cell_value(i, 14))
                private_details.append(sheet.cell_value(i, 15))
                gstin.append(sheet.cell_value(i, 16))

            vendor_name.pop(0)
            contact_name.pop(0)
            vendor_tin.pop(0)
            email.pop(0)
            phone.pop(0)
            billing_address.pop(0)
            billing_zip.pop(0)
            billing_city.pop(0)
            billing_state.pop(0)
            billing_country.pop(0)
            shipping_address.pop(0)
            shipping_zip.pop(0)
            shipping_city.pop(0)
            shipping_state.pop(0)
            shipping_country.pop(0)
            private_details.pop(0)
            gstin.pop(0)

            for i in range(len(vendor_name)):
                self.model.objects.get_or_create(name=vendor_name[i], contact_Name=contact_name[i],
                                                 TIN=vendor_tin[i], email=email[i], phone=phone[i],
                                                 billing_address=billing_address[i], billing_zip=billing_zip[i],
                                                 billing_city=billing_city[i], billing_state=billing_state[i],
                                                 billing_country=billing_country[i],
                                                 shipping_address=shipping_address[i],
                                                 shipping_zip=shipping_zip[i], shipping_city=shipping_city[i],
                                                 shipping_state=shipping_state[i], shipping_country=shipping_country[i],
                                                 details=private_details[i], GSTIN=gstin[i])
            return redirect(to='vendor_data')
        return redirect(to='new_vendor')


class Enquiry(View):
    from .forms import EnqueryForm
    form = EnqueryForm
    dashboard_template = 'SMdashboard/dashboard.html'
    enquiryForm_template = 'SMdashboard/enquiry_form.html'
    enquiryForm_table = 'SMdashboard/table-enquiry.html'

    model = enquiry.Enquiry
    enquiry_tableTemplate = 'dashboard/table-enquiry.html'

    def get_data(self):

        data = self.model.objects.all().values(
            'first_name', 'last_name', 'product_name', 'description', 'startPrice', 'endPrice', 'mobile_no',
            'email_id', 'address', 'contact_no', 'whatsapp_no', 'pk',

        ).annotate(
            customer=F('customer_type__name'),
            handled=F('handled_by__name'),
            enquiry=F('enquiry_type__name'),
            date=ExpressionWrapper(Func(F('enquiry_date'), Value("DD/MM/YYYY"), function='TO_CHAR'),
                                   output_field=CharField()),
        ).order_by("-date")
        return list(data)

    def get(self, request, *args, **kwargs):
        if 'enquiry_form' in kwargs:
            return render(request, self.enquiryForm_template, {'enquiry': self.form()})
        data = self.get_data()
        print(data)
        return render(request, self.enquiryForm_table, {'data': data})  # json.dumps(data)

    def post(self, request, *args, **kwargs):
        form = self.EnqueryForm(request.POST)
        print(form.is_valid())
        print(form)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            customer_type = form.cleaned_data.get('customer_type')
            address = form.cleaned_data.get('address')
            handled_by = form.cleaned_data.get('handled_by')
            enquiry_type = form.cleaned_data.get('enquiry_type')
            product_name = form.cleaned_data.get('product_name')
            description = form.cleaned_data.get('description')
            startPrice = form.cleaned_data.get('startPrice')
            endPrice = form.cleaned_data.get('endPrice')
            mobile_no = form.cleaned_data.get('mobile_no')
            whatsapp_no = form.cleaned_data.get('whatsapp_no')
            contact_no = form.cleaned_data.get('contact_no')
            email_id = form.cleaned_data.get('email_id')
            enquiry.Enquiry.objects.create(
                first_name=first_name, last_name=last_name, customer_type=customer_type, address=address,
                handled_by=handled_by,
                enquiry_type=enquiry_type, product_name=product_name, description=description, startPrice=startPrice,
                endPrice=endPrice, mobile_no=mobile_no, whatsapp_no=whatsapp_no, contact_no=contact_no,
                email_id=email_id
            )
            return redirect(to='enquiry')
        return redirect(to='enquiry_form')


class DayBookView(View):
    from .forms import DayBookForm
    form = DayBookForm
    dashboard_template = 'SMdashboard/dashboard.html'
    form_template = 'SMdashboard/daybookform.html'
    data_template = 'SMdashboard/daybook-table.html'
    model = dayBook.DayBook

    def get_data(self):

        data = self.model.objects.all().values('pk', 'number', 'customer_type',
                                               'description', 'status').annotate(
            dayBook_name=Coalesce('name', Value("-")),
            customer=Coalesce('customer_name__name', Value("-")),
            employee=Coalesce('employee_name__name', Value("-")),
            vendor=Coalesce('vendor_name__name', Value("-")),
            dayBook_date=ExpressionWrapper(Func(F('date'), Value("DD/MM/YYYY"), function='TO_CHAR'),
                                           output_field=CharField()),
            dayBook_amount=ExpressionWrapper(
                F('amount'), output_field=FloatField())
        ).order_by("-dayBook_date")

        return list(data)

    def get(self, request, *args, **kwargs):
        if 'daybook_form' in kwargs:
            return render(request, self.form_template, {'daybook': self.form()})
        data = self.get_data()
        print(data)
        return render(request, self.data_template, {'data': data})

    def post(self, request, *args, **kwargs):
        form = self.DayBookForm(request.POST)
        print(form.is_valid())
        print(form)
        if form.is_valid():
            number = form.cleaned_data.get('number')
            date = form.cleaned_data.get('date')
            customer_type = form.cleaned_data.get('customer_type')
            name = form.cleaned_data.get('name')
            customer_name = form.cleaned_data.get('customer_name')
            employee_name = form.cleaned_data.get('employee_name')
            vendor_name = form.cleaned_data.get('vendor_name')
            description = form.cleaned_data.get('description')
            status = form.cleaned_data.get('status')
            amount = form.cleaned_data.get('amount')
            self.model.objects.create(
                number=number, date=date, customer_type=customer_type, name=name,
                customer_name=customer_name, employee_name=employee_name, vendor_name=vendor_name,
                description=description, status=status, amount=amount)
            return redirect(to='daybook')
        return redirect(to='daybook_form')
