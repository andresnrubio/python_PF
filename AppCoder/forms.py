from django import forms


class formularioCurso(forms.Form):
    curso = forms.CharField(max_length=50)
    comision = forms.IntegerField()


class formularioEstudiante(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()


class formularioProfesor(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)


class formularioEntregable(forms.Form):
    nombre = forms.CharField(max_length=50)
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField()
