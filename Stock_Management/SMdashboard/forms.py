import os
from django import forms
from SM import enquiry, dayBook


class ClientForm(forms.Form):
    input_excel = forms.FileField(required=True, label=u"Upload the Excel file to import to the system.")

    def clean_input_excel(self):
        input_excel = self.cleaned_data['input_excel']
        print(input_excel.name)
        IMPORT_FILE_TYPES = ['.xls', ]
        FILE_NAME = ['Clients', ]
        extension = os.path.splitext(input_excel.name)[1]
        extension2 = os.path.splitext(input_excel.name)[0]
        print(extension2)
        if not (extension in IMPORT_FILE_TYPES) or not (extension2 in FILE_NAME):
            raise forms.ValidationError(
                u'%s is not a valid excel file or the correct file for import.'
                u' Please make sure your input file is a correct excel file' % extension)
        else:
            return input_excel


class VendorForm(forms.Form):
    input_excel = forms.FileField(required=True, label=u"Upload the Excel file to import to the system.")

    def clean_input_excel(self):
        input_excel = self.cleaned_data['input_excel']
        print(input_excel.name)
        IMPORT_FILE_TYPES = ['.xls', ]
        FILE_NAME = ['Vendors', ]
        extension = os.path.splitext(input_excel.name)[1]
        extension2 = os.path.splitext(input_excel.name)[0]
        print(extension2)
        if not (extension in IMPORT_FILE_TYPES) or not (extension2 in FILE_NAME):
            raise forms.ValidationError(
                u'%s is not a valid excel file or the correct file for import.'
                u' Please make sure your input file is a correct excel file' % extension)
        else:
            return input_excel


class EnqueryForm(forms.ModelForm):
    class Meta:
        model = enquiry.Enquiry
        fields = ['first_name', 'last_name', 'customer_type', 'address', 'handled_by', 'enquiry_type', 'product_name',
                  'description', 'startPrice', 'endPrice', 'mobile_no', 'whatsapp_no', 'contact_no', 'email_id']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_type': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 3, 'cols': 58, 'class': 'form-control'}),
            'handled_by': forms.Select(attrs={'class': 'form-control'}),
            'enquiry_type': forms.Select(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 58, 'class': 'form-control'}),
            'startPrice': forms.TextInput(attrs={'class': 'form-control'}),
            'endPrice': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp_no': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email_id': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DayBookForm(forms.ModelForm):
    class Meta:
        model = dayBook.DayBook
        fields = ['number', 'date', 'customer_type', 'name', 'customer_name', 'employee_name', 'vendor_name',
                  'description', 'status', 'amount']
        widgets = {
            'number': forms.HiddenInput(attrs={'class': 'form-control-sm'}),
            'date': forms.HiddenInput(attrs={'class': 'form-control-sm'}),
            'customer_type': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'customer_name': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'employee_name': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'vendor_name': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 58, 'class': 'form-control-sm'}),
            'status': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'amount': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }
