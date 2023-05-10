from django.forms import ModelForm
from .models import Profile

class Profile_form(ModelForm):
    class Meta:
        model = Profile
        fields = [
           'Imagen', 'nombre', 'apellido' , 'fecha_nacimiento' , 'edad' , 'celular' , 'cc_passport', 'pais' , 'ciudad' , 'domicilio'   
        ]