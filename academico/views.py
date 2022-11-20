from django.shortcuts import render
from django.db.models import Q
from academico.models import curso
#from .models import curso
#from django.http import HttpResponse
# Create your views here.

#def listarEstudiantes(request):
    #curso = curso.objects.all()
    #return render(request,'index.html', {"curso":curso})
 

def home(request):
    cursos = curso.objects.all()
    data = {'curso':cursos}
    return render(request,'index.html', data)
  


#def home(request):
 #   consulta = request.GET.get("buscar")
  #  cursos = curso.objects.filter()
   # if consulta:
    #    cursos = curso.objects.filter(
     #       Q(Nombre__icontains = consulta) |
      #      Q(cedula__icontains = consulta)
       # ).distinct

    #return render(request,'index.html', { 'cursos':cursos })    