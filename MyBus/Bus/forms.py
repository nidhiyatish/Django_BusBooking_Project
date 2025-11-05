from django.forms import ModelForm
from .models import BusImage

# ModelForm -> helps create form object for a given model


class BusImageForm(ModelForm):
    class Meta:
        model = BusImage
        fields = ['image', 'category']

