from django.shortcuts import render

def crud_view(request):
    return render(request, 'crud_app/crud.html')
