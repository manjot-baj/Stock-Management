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
from SM import enquiry, employee_data, service, dayBook, invoice


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
    detailed_view = 'SMdashboard/view-client.html'
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
        elif 'object_id' in kwargs:
            from .reports import ClientReport
            data = ClientReport().get_data(request, client_id=kwargs.get('object_id'))
            return render(request, self.detailed_view, data)
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


class ProductView(View):
    from .forms import ProductForm
    dashboard_template = 'SMdashboard/dashboard.html'
    data_template = 'SMdashboard/product-table.html'
    form_template = 'SMdashboard/productform.html'
    detailed_template_view = 'SMdashboard/product.html'
    form = ProductForm
    model = invoice.Product

    def get_data(self):
        data = self.model.objects.all().values('pk', 'name', 'unit_price', 'u_o_m', 'quantity', 'description',
                                               'product_type',
                                               'purchase_rate', 'purchase_rate_currency', 'h_s_n_or_s_a_c', 's_k_u',
                                               'tax', 'c_e_s_s_percent', 'c_e_s_s'
                                               ).order_by("-pk")
        return list(data)

    def get(self, request, *args, **kwargs):
        if 'product_form' in kwargs:
            return render(request, self.form_template, {'form': self.form})
        elif 'object_id' in kwargs:
            from .reports import ProductReport
            data = ProductReport().get_data(request, product_id=kwargs.get('object_id'))
            template = self.detailed_template_view
            return render(request, template, data)

        data = self.get_data()
        print(data)
        return render(request, self.data_template, {'data': data})

    def post(self, request, *args, **kwargs):
        form = self.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            input_excel = request.FILES['input_excel']
            book = xlrd.open_workbook(file_contents=input_excel.read())
            sheet = book.sheet_by_index(0)
            # data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
            product_name = []
            unit_price = []
            uom = []
            quantity = []
            description = []
            type = []
            purchase_rate = []
            purchase_rate_currency = []
            h_s_n_or_s_a_c = []
            s_k_u = []
            tax = []
            c_e_s_s_percent = []
            c_e_s_s = []

            for i in range(sheet.nrows):
                product_name.append(sheet.cell_value(i, 0))
                unit_price.append(sheet.cell_value(i, 1))
                uom.append(sheet.cell_value(i, 2))
                quantity.append(sheet.cell_value(i, 3))
                description.append(sheet.cell_value(i, 4))
                type.append(sheet.cell_value(i, 5))
                purchase_rate.append(sheet.cell_value(i, 6))
                purchase_rate_currency.append(sheet.cell_value(i, 7))
                h_s_n_or_s_a_c.append(sheet.cell_value(i, 8))
                s_k_u.append(sheet.cell_value(i, 9))
                tax.append(sheet.cell_value(i, 10))
                c_e_s_s_percent.append(sheet.cell_value(i, 11))
                c_e_s_s.append(sheet.cell_value(i, 12))

            product_name.pop(0)
            unit_price.pop(0)
            uom.pop(0)
            quantity.pop(0)
            description.pop(0)
            type.pop(0)
            purchase_rate.pop(0)
            purchase_rate_currency.pop(0)
            h_s_n_or_s_a_c.pop(0)
            s_k_u.pop(0)
            tax.pop(0)
            c_e_s_s_percent.pop(0)
            c_e_s_s.pop(0)

            for i in range(len(product_name)):
                self.model.objects.get_or_create(name=product_name[i], unit_price=unit_price[i],
                                                 u_o_m=uom[i], quantity=quantity[i], description=description[i],
                                                 product_type=type[i], purchase_rate=purchase_rate[i],
                                                 purchase_rate_currency=purchase_rate_currency[i],
                                                 h_s_n_or_s_a_c=h_s_n_or_s_a_c[i],
                                                 s_k_u=s_k_u[i],
                                                 tax=tax[i],
                                                 c_e_s_s_percent=c_e_s_s_percent[i], c_e_s_s=c_e_s_s[i])

            return redirect(to='product_data')
        return redirect(to='new_product')


class VendorView(View):
    from .forms import VendorForm
    dashboard_template = 'SMdashboard/dashboard.html'
    data_template = 'SMdashboard/vendor-table.html'
    form_template = 'SMdashboard/vendorform.html'
    detailed_view = 'SMdashboard/view-vendor.html'
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
        elif 'object_id' in kwargs:
            from .reports import VendorReport
            data = VendorReport().get_data(request, vendor_id=kwargs.get('object_id'))
            return render(request, self.detailed_view, data)
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
    from .forms import EnquiryForm
    form = EnquiryForm
    # dashboard_template = 'SMdashboard/dashboard.html'
    enquiryForm_template = 'SMdashboard/enquiry_form.html'
    enquiryForm_table = 'SMdashboard/table-enquiry.html'
    detailed_template_view = 'SMdashboard/enquiry.html'

    model = enquiry.Enquiry

    # enquiry_tableTemplate = 'dashboard/table-enquiry.html'

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
        elif 'object_id' in kwargs:
            from .reports import EnquiryReport
            data = EnquiryReport().get_data(request, enquiry_id=kwargs.get('object_id'))
            template = self.detailed_template_view
            return render(request, template, data)
        data = self.get_data()
        print(data)
        return render(request, self.enquiryForm_table, {'data': data})

    def post(self, request, *args, **kwargs):
        form = self.EnquiryForm(request.POST)
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


class Employee(View):
    from .forms import EmployeeForm
    form = EmployeeForm

    model = employee_data.Employee

    detailed_template_view = 'SMdashboard/employee.html'

    # dashboard_template = 'SMdashboard/dashboard.html'
    employeeForm_template = 'SMdashboard/employee_form.html'
    employeeForm_table = 'SMdashboard/table-employee.html'

    def get_data(self):
        data = self.model.objects.all().values(
            'photo', 'name', 'address', 'city', 'state', 'pin_code', 'country', 'mobile_no', 'email_id',
            'qualification', 'type', 'job_profile', 'job_description', 'pk',
        ).annotate(
            date=ExpressionWrapper(Func(F('join_date'), Value("DD/MM/YYYY"), function='TO_CHAR'),
                                   output_field=CharField()),
        ).order_by("-date")
        return list(data)

    def get(self, request, *args, **kwargs):
        if 'employee_form' in kwargs:
            return render(request, self.employeeForm_template, {'employee': self.form()})

        elif 'object_id' in kwargs:
            from .reports import EmployeeReport
            data = EmployeeReport().get_data(request, employee_id=kwargs.get('object_id'))
            template = self.detailed_template_view
            return render(request, template, data)

        data = self.get_data()
        print(data)
        return render(request, self.employeeForm_table, {'data': data})

    def post(self, request, *args, **kwargs):
        form = self.EmployeeForm(request.POST, request.FILES, )
        print(form.is_valid)
        print(form)
        if form.is_valid():
            photo = form.cleaned_data.get('photo')
            join_date = form.cleaned_data.get('join_date')
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')
            city = form.cleaned_data.get('city')
            state = form.cleaned_data.get('state')
            pin_code = form.cleaned_data.get('pin_code')
            country = form.cleaned_data.get('country')
            mobile_no = form.cleaned_data.get('mobile_no')
            email_id = form.cleaned_data.get('email_id')
            qualification = form.cleaned_data.get('qualification')
            type = form.cleaned_data.get('type')
            job_profile = form.cleaned_data.get('job_profile')
            job_description = form.cleaned_data.get('job_description')

            employee_data.Employee.objects.create(
                photo=photo, join_date=join_date, name=name, address=address, city=city, state=state, pin_code=pin_code,
                country=country, mobile_no=mobile_no, email_id=email_id, qualification=qualification, type=type,
                job_profile=job_profile, job_description=job_description,
            )
            return redirect(to="employee")
        return redirect(to="employee_form")


class Service(View):
    from .forms import ServiceForm
    form = ServiceForm
    model = service.Service

    serviceForm_template = 'SMdashboard/service_form.html'
    serviceForm_table = 'SMdashboard/table-service.html'

    def get_data(self):
        data = self.model.objects.all().values(
            'service_number', 'description', 'photo', 'status', 'pk'
        ).annotate(
            service_client=F('client__name'),
            service=F('service_type__name'),
            service_date=ExpressionWrapper(Func(F('date'), Value("DD/MM/YYYY"), function='TO_CHAR'),
                                           output_field=CharField()),
        ).order_by("-service_date")
        return list(data)

    def get(self, request, *args, **kwargs):
        if 'service_form' in kwargs:
            return render(request, self.serviceForm_template, {'service': self.form()})
        data = self.get_data()
        print(data)
        return render(request, self.serviceForm_table, {'data': data})

    def post(self, request, *args, **kwargs):
        form = self.ServiceForm(request.POST, request.FILES, )
        print(form.is_valid())
        if form.is_valid():
            service_number = form.cleaned_data.get('service_number')
            date = form.cleaned_data.get('date')
            client = form.cleaned_data.get('client')
            service_type = form.cleaned_data.get('service_type')
            description = form.cleaned_data.get('service_type')
            photo = form.cleaned_data.get('photo')
            status = form.cleaned_data.get('status')
            service.Service.objects.create(
                service_number=service_number, date=date, client=client, service_type=service_type,
                description=description, photo=photo, status=status
            )
            return redirect(to="service")
        return redirect(to="service_form")
