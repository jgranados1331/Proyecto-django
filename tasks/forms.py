from django.forms import ModelForm
from .models import Profile

class Profile(ModelForm):
    class Meta:
        model = Profile
        fields = [
           'Imagen', 'nombre', 'apellido' , 'fecha_nacimiento' , 'edad' , 'celular' , 'cc_passport', 'pais' , 'ciudad' , 'domicilio'   
        ]