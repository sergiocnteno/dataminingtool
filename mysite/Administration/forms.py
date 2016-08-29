from django import forms


class PostForms(forms.Form):
    nombreProyecto = forms.CharField(max_length = 50, label=("Nombre del Proyecto :"))

class tipoAtribute(forms.Form):
    nombreAtribute = forms.CharField(max_length = 25)
    CHOICES = (
        ('Categorico', 'Categorico'),
        ('Numerico', 'Numerico'))
    tipoAtributo = forms.MultipleChoiceField(choices = CHOICES, widget=forms.SelectMultiple())

class data_Form(forms.Form):
    data = forms.CharField()
    csvArchive = forms.FileField(label='Selecciona un archivo para subir tus datos')
