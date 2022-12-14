from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    # path('accounts/profile/', views.home, name ="home"),
    path('datapatient/', views.datapatient, name ="datapatient"),
    path('data_health/', views.data_health, name ="data_health"),
    path('login/', views.login_user, name ='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('history/', views.history, name='history'),
    path('history_vacines/', views.history_vacines, name='history_vacines'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('vacines/', views.vacines, name ="vacines"),
    path('vacines/<int:id>', views.vacinesEdit, name ="vacines_edit"),
    path('vacines/delete/<int:id>', views.vacinesDelete, name ="vacines_delete"),
    path('data_health/', views.data_health, name='data_health'),
]

 