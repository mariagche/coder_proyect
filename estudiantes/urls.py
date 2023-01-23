from django.urls import path


from estudiantes.views import (
 
    listar_estudiantes, listar_profesor, listar_cursos,
    crear_curso, buscar_cursos,
    crear_profesor, buscar_profesor,
    crear_estudiante, buscar_estudiante,
)


urlpatterns = [
    path('alumnos/', listar_estudiantes, name="listar_alumnos"),
    path('profesores/', listar_profesor, name="listar_profesores"),
    path('cursos/', listar_cursos, name="listar_cursos"),
    path('crear-estudiante/', crear_estudiante, name="crear_estudiante"),
    path('crear-profesor/', crear_profesor, name="crear_profesor"),
    path('crear-curso/', crear_curso, name="crear_curso"),
    path('buscar-estudiante/', buscar_estudiante, name="buscar_estudiante"),
    path('buscar-profesor/', buscar_profesor, name="buscar_profesor"),
    path('buscar-cursos/', buscar_cursos, name="buscar_cursos"),
]
    
    
    
