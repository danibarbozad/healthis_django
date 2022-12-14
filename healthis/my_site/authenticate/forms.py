from itertools import count
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
	email = forms.EmailField(label="E-mail", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail'}))
	first_name = forms.CharField(label="Nome", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Insira aqui seu nome'}))
	last_name = forms.CharField(label="Sobrenome", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Insira aqui seu sobrenome'}))
	date_of_birth = forms.DateField(label="Data de Nascimento", widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control', 'placeholder':'01/01/2022'}))
	phonenumber = forms.CharField(label="Telefone principal", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'(51) 99999-9999'}))
	landline_phonenumber = forms.CharField(label="Telefone residencial", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'(51) 99999-9999'}))
	zipcode = forms.CharField(label="CEP", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'9999-999'}))
	address = forms.CharField(label="Endereço", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Rua Silva Só, 1234'}))
	complement = forms.CharField(label="Complemento", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Número apto, bloco, ponto de referência'}))
	neighborhood = forms.CharField(label="Bairro", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do bairro'}))
	city = forms.CharField(label="Cidade", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Santa Cruz do Sul'}))
	state = forms.CharField(label="Estado", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'RS'}))

	class Meta:
		model = Patient
		fields = "__all__"



from .models import Vacines



class EditProfileForm(UserChangeForm):
	
	password = forms.CharField(label="", widget=forms.TextInput(attrs={'type':'hidden'}))
	class Meta:
		model = User
		#excludes private information from User
		fields = ('username', 'first_name', 'last_name', 'email','password',)
class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}), )
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Primeiro nome'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Último nome'}))
	
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Usuário'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requerido 150 caracteres ou menos. Apenas letras, dígitos e @/./+/-/_.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Sua senha não pode ser muito parecida com suas outras informações pessoais.</li><li>Sua senha deve conter pelo menos 8 caracteres.</li><li>Sua senha não pode ser uma senha comumente usada.</li><li>Sua senha não pode ser totalmente numérica.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirme sua senha'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Digite a mesma senha de antes, para verificação.</small></span>'

class UpdateVacines(forms.ModelForm):
    class Meta:
        model=Vacines
        fields="__all__"
