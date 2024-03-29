from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "valid_ver":
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin,forms.ModelForm):

    class Meta:
        model=Product
        fields=('name','description','price','category',)

    def clean_name(self):
        cleaned_data=self.cleaned_data['name']

        if cleaned_data.lower() in ['казино','криптовалюта','крипта','биржа',
                            'дешево','бесплатно','обман','полиция','радар']:
            raise forms.ValidationError('Введен заперщенный продукт')
        return cleaned_data

class VersionForm(StyleFormMixin,forms.ModelForm):

    class Meta:
        model=Version
        fields ='__all__'
