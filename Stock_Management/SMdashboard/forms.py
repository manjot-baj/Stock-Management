import os
from django import forms


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
