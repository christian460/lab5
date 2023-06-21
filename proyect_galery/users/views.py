from django.shortcuts import redirect, render
from .forms import cutomUser
from django.contrib.auth import authenticate, login

# Create your views here.
def registro(request):
    data = {
        'form': cutomUser()
    }
    if request.method == 'POST':
        formulario=cutomUser(data=request.POST) 
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password"])
            login(request, user)
            return redirect(to="home")
        data["form"] = formulario
    return render(request,'registro.html', data)
