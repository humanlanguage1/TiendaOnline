from django import forms   

class ClienteForm(forms.Form):
    doc_ide= forms.CharField(label='DNI', max_length=20,required=True)
    nombres = forms.CharField(max_length=200,required=True)
    apellidos = forms.CharField(max_length=200,required=True)
    email = forms.EmailField(required=True)
    direccion = forms.CharField(widget= forms.Textarea,required=False)
    telefono = forms.CharField(max_length=20,required=False)
    usuario = forms.CharField(max_length=20,required=True)
    clave = forms.CharField(widget= forms.PasswordInput)