from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .forms import PatientForm, SignUpForm, EditProfileForm, UpdateVacines 
from .models import Patient, Vacines
import logging
# Create your views here.
def home(request): 
	return render(request, 'authenticate/home.html', {})

def login_user (request):
	if request.method == 'POST': #if someone fills out form , Post it 
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:# if user exist
			login(request, user)
			messages.success(request,('Você está logado'))
			return redirect('home') #routes to 'home' on successful login  
		else:
			messages.success(request,('Error no login'))
			return redirect('login') #re routes to login page upon unsucessful login
	else: 
		return render(request, 'authenticate/login.html', {})

@login_required	
def logout_user(request):
	logout(request)
	messages.success(request,('Você acabou de deslogar'))
	return redirect('home')

def register_user(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ('Você está registrado'))
			return redirect('home')
	else: 
		form = SignUpForm() 

	context = {'form': form}
	return render(request, 'authenticate/register.html', context)

@login_required	
def edit_profile(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, instance= request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('Você editou seu perfil'))
			return redirect('home')
	else: 		#passes in user information 
		form = EditProfileForm(instance= request.user) 

	context = {'form': form}
	return render(request, 'authenticate/edit_profile.html', context)
	#return render(request, 'authenticate/edit_profile.html',{})


@login_required	
def change_password(request):
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST, user= request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('Você editou sua senha'))
			return redirect('home')
	else: 		#passes in user information 
		form = PasswordChangeForm(user= request.user) 

	context = {'form': form}
	return render(request, 'authenticate/change_password.html', context)


@login_required
def datapatient(request): 
	form = PatientForm()
	try:
		form = PatientForm(instance = Patient.objects.first())
	except Patient.DoesNotExist:
		form = PatientForm()

	if request.method == "GET":
		context = {
			'form': form
		}
		return render(request, 'authenticate/datapatient.html', context=context)	
	else:
		form = PatientForm(request.POST, instance = Patient.objects.first())
		if form.is_valid():
			form.save()
			messages.success(request, "Dados salvos com sucesso!")
		else:
			messages.error(request, form.errors)
		context = {
			'form': form
		}
		return render(request, 'authenticate/datapatient.html', context=context)

def history(request): 
	return render(request, 'authenticate/history.html', {})

def history_vacines(request):
	return render(request, 'authenticate/history_vacines.html', {})


@login_required	
def vacines(request):
	if request.method == 'POST':
		# fazer validações ainda
		date = request.POST['date']
		vacine = request.POST['vacine']
		dose = request.POST['dose']
		batch = request.POST['batch']
		vaccinator = request.POST['vaccinator']
		healthcenter = request.POST['healthcenter']
		vacinesPost = Vacines(
			date=date, 
			vacine=vacine,
			dose=dose,
			batch=batch,
			vaccinator=vaccinator,
			healthcenter=healthcenter,
			)
		vacinesPost.save()
		messages.success(request, ('Salvo com sucesso.'))
	vacinesGet = Vacines.objects.all()
	context = {
        'vacines': vacinesGet
    }
	return render(request, 'authenticate/vacines.html',  context)

@login_required	
def vacinesEdit(request, id):
	vacineEdit = Vacines.objects.get(id = id)
	form = UpdateVacines()
	if request.method == 'POST':
		form = UpdateVacines(request.POST, instance=vacineEdit)
		if form.is_valid():
			form.save(commit=True)
			messages.success(request, ('Salvo com sucesso.'))
			return redirect("/vacines")
		else:
			messages.error(request, ('Erro na edição.'))
			return redirect("/vacines")
	context = {
        'vacine': vacineEdit
    }
	return render(request, 'authenticate/vacines_edit.html',  context)
@login_required	
def vacinesDelete(request, id):
	vacineEdit = Vacines.objects.get(id = id)
	vacineEdit.delete()
	messages.success(request, ('Deletado com sucesso.'))
	return redirect("/vacines")


@login_required	
def datapatient(request): 
	return render(request, 'authenticate/datapatient.html', {})	

def data_health(request): 
	return render(request, 'authenticate/data_health.html', {})



