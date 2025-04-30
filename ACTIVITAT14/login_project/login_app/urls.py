from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login_session/', views.login_session_view, name='login_session'),
    path('inicio/', views.pagina_inici, name='pagina_inici'),
    path('logout/', views.logout_view, name='logout'),
]
