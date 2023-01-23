from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from estudiantes.models import Estudiante, Profesor, Curso
from estudiantes.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario



def inicio(request):
    return render(
        request=request,
        template_name='estudiantes/inicio.html',
    )


def listar_estudiantes(request):
    ## Aqui iria la validacion del permiso lectura estudiantes
    contexto = {
        'estudiantes': Estudiante.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_estudiantes.html',
        context=contexto,
    )


def listar_profesor(request):
    contexto = {
        'profesor': Profesor.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_profesor.html',
        context=contexto,
    )


def listar_cursos(request):
    contexto = {
        'cursos': Curso.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_cursos.html',
        context=contexto,
    )


#def crear_curso_version_1(request):
    """No la estamos usando"""
    if request.method == "POST":
        data = request.POST      #creo el curso
        curso = Curso(nombre=data['nombre'], comision=data['comision'])
        curso.save()
        url_exitosa = reverse('listar_cursos')
        return redirect(url_exitosa)
    else:  # GET                 #si no consulto si existe
        return render(
            request=request,
            template_name='estudiantes/formulario_curso_a_mano.html',
        )


def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso(nombre=data['Nombre'], comision=data['Comision'])
            curso.save()
            url_exitosa = reverse('listar_cursos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = CursoFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_curso.html',
        context={'formulario': formulario},
    )


def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        cursos = Curso.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(comision__exact=data['busqueda'])
        )
        contexto = {
            'curso': cursos
        }
        return render(
            request=request,
            template_name='estudiantes/lista_cursos.html',
            context=contexto,
        )

def crear_profesor(request):               #creo ala db de profes
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            profesor = Profesor(nombre=data['Nombre'], apellido=data['Apellido'],comision=data['Comision'],tema=data['Tema'], Fecha_nacimiento=data['fecha_nacimiento'], profesion=data['profesion'], bio=data['bio'], curso=data['curso'], dni=data['dni'], email=data['email'])
            profesor.save()         #guardo en el dicc la info
            url_exitosa = reverse('listar_profesor')    #reverse crea una url sobre el path
            return redirect(url_exitosa) #variable que vuelve a listar_profesor
    else:  # GET
        formulario = ProfesorFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_profesor.html',
        context={'formulario': formulario},
    )


def buscar_profesor(request):          # busco a los profes
    if request.method == "POST":
        data = request.POST
        profesor = Profesor.objects.filter(
            Q(apellido__contains=data['busqueda']) | Q(comision__exact=data['busqueda'])
        )
        contexto = {
            'profesor': profesor       #busco profesor por el campo profesor
        }
        return render(
            request=request,
            template_name='estudiantes/lista_profesor.html',
            context=contexto,
        )
        
def crear_estudiante(request):         #creo estudiante
    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            estudiante = Estudiante(Nombre=data['Nombre'], Apellido=data['Apellido'], DNI=data['DNI'])  #email=data['email'], Fecha_de_nacimiento=data['fecha_nacimiento']
            estudiante.save()
            url_exitosa = reverse('listas_estudiantes')
            return redirect(url_exitosa)
    else:  # GET
        formulario = EstudianteFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_estudiante.html',
        context={'formulario': formulario},
    )


def buscar_estudiante(request):   #buscamos el estudiante
    if request.method == "POST":
        data = request.POST
        estudiante = Estudiante.objects.filter(
            Q(Apellido__exact=data['busqueda']) | Q(Nombre__contains=data['busqueda']) | Q(DNI__exact=data['busqueda']) | Q(email__contains=data['busqueda']) | Q(Fecha_nacimiento__contains=data['busqueda'])
        )
        contexto = {
            'estudiantes': estudiante
        }
        return render(
            request=request,
            template_name='estudiantes/lista_estudiantes.html',
            context=contexto,
        )