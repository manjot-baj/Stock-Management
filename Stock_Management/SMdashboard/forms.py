from django import forms
from SM import enquiry
# from ckeditor_uploader.widgets import CKEditorUploadingWidget

class EnqueryFom(forms.ModelForm):
    class Meta:
        model = enquiry.EnquiryForm
        fields = ['first_name', 'last_name', 'customer_type', 'address', 'handled_by', 'enquiry_type', 'product_name',
                  'description', 'startPrice', 'endPrice', 'mobile_no', 'whatsapp_no', 'contact_no', 'email_id',
                  ]
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

            # 'description': forms.CharField(widget=CKEditorUploadingWidget()),
            
        }