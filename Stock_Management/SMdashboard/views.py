from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from SM.company_data import Client
import xlrd


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
