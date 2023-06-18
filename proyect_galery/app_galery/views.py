from django.shortcuts import render
from .forms import ProductoForm

# Create your views here.

def form_add_productos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            # hacer algo después de guardar los datos del usuario
    else:
        form = ProductoForm()
    return render(request, 'add-producto.html', {'form': form})

"""

class AdmProductos(View):
    def get(self, request):
        productos = Producto.objects.all()
        return render(request, "app_galery/templates/adm-productos.html", {
            "productos": productos
        })

class SaveProducto(View):
    def get(self, request):
        form = ProductoForm()
        return render(request, "app_galery/templates/add-producto.html", {
            "form": form
        })

    def post(self, request):
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adm-productos'))
            
"""