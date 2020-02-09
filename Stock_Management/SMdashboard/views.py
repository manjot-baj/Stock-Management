import json
from django.http import JsonResponse, HttpResponse
from django.db.models.functions import Concat

from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.db.models import (Case, CharField, Count, DateTimeField,
                              ExpressionWrapper, F, FloatField, Func, Max, Min,
                              Prefetch, Q, Sum, Value, When, Subquery)
from SM import enquiry


class Dashboard(View):
    dashboard_template = 'SMdashboard/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.dashboard_template)

    def post(self, request, *args, **kwargs):
        return render(request, self.dashboard_template)


class Enquiry(View):
    from .forms import EnqueryForm
    form = EnqueryForm
    dashboard_template = 'SMdashboard/dashboard.html'
    enquiryForm_template = 'SMdashboard/enquiry_form.html'
    enquiryForm_table = 'SMdashboard/table-enquiry.html'

    model = enquiry.Enquiry
    enquiry_tableTemplate = 'dashboard/table-enquiry.html'

    def get_data(self):

        # data = self.model.objects.all().values(
        #     'first_name', 'last_name', 'customer_type', 'address', 'handled_by', 'enquiry_type', 'enquiry_date'
        # )

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
        form = self.EnqueryFom(request.POST)
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

            return redirect(to='enquirySubmitted')
        return redirect(to='SMdashboard: dashboard')


class Success(View):
    dashboard_template = 'SMdashboard/success.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.dashboard_template)
