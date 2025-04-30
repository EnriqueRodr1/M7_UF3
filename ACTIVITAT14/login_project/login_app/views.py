from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Usuari

def login_view(request):  # 👈 nombre exacto requerido
    error = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                usuari = Usuari.objects.get(email=email, password=password)
                return render(request, "inicio.html", {"user": usuari})
            except Usuari.DoesNotExist:
                error = "Credencials incorrectes"
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form, "error": error})




def pagina_inici(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login_session')
    user = Usuari.objects.get(id=user_id)
    return render(request, 'inicio.html', {'user': user})

def logout_view(request):
    request.session.flush()
    return redirect('login_session')

def login_session_view(request):
    error = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                usuari = Usuari.objects.get(email=email, password=password)
                request.session['user_id'] = usuari.id
                return redirect("pagina_inici")
            except Usuari.DoesNotExist:
                error = "Credencials incorrectes"
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form, "error": error})

