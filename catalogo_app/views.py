from django.shortcuts import render

def catalogo_view(request):
    return render(request, 'catalogo_app/catalogo.html')
