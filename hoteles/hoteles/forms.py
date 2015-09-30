from django import forms

from hoteles.models import Ciudad,DatosHotel

class CiudadForm(forms.ModelForm):

    class Meta:
        model = Ciudad
        fields = ('nombre',)

class HotelForm(forms.ModelForm):

    class Meta:
        model = DatosHotel
        fields = ('nombre','telefono','direccion','colonia','ciudad')

class HotelForm(forms.ModelFormUser):

    class Meta2:
        model = DatosHotelUser
        fields = ('nombre','telefono','direccion','colonia','ciudad', user)