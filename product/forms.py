from django import forms
from product.models import BillingDetails


class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingDetails
        exclude = ('user', )
    

    def __init__(self, *args, **kwargs):
        super(BillingForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            self.fields[field_name].widget.attrs['required'] = True