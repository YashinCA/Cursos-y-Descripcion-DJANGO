from django import forms
from django.template import RequestContext
from django.urls import reverse
from django.shortcuts import render, HttpResponse, redirect
from .models import Course
from django.contrib import messages


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'description']

        labels = {
            'name': 'Nombre: ',
            'description': 'Descripción: ',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


def index(request):
    if request.method == 'GET':
        context = {
            'cursos': Course.objects.all(),
            'formModel': CourseForm(),

        }
        return render(request, 'app/index.html', context)

    if request.method == 'POST':
        error = Course.objects.basic_validator(request.POST)
        if len(error) > 0:
            form = CourseForm(request.POST)
            for valor in error.values():
                messages.error(request, valor)
            context = {
                'formModel': form,
                'cursos': Course.objects.all(),

            }
            return render(request, 'app/index.html', context)
        else:
            form = CourseForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Curso creado correctamente')
                return redirect(reverse('cursos:index'))


def delete_curso(request, id):
    # para reutilizar el contexto usuario en get y post, lo dejamos afuera
    curso = Course.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'curso': curso,
        }
        return render(request, 'app/delete.html', contexto)

    if request.method == 'POST':
        curso.delete()

        return redirect(reverse('cursos:index'))

    # if request.method == 'POST':
    #     error = Course.objects.basic_validator(request.POST)
    #     if len(error) == 0:
    #         form = CourseForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             messages.success(request, 'Curso creado correctamente')
    #             return redirect(reverse('cursos:index'))
    #     else:
    #         form = CourseForm(request.POST)
    #         for valor in error.values():
    #             messages.error(request, valor)
    #         return render(request, 'app/index.html', {'formModel': form})


# def add_cursos_forms(request):
#     if request.method == 'GET':

#         return render(request, 'usuarios/formulario_form.html', {'formModel': CourseForm()})
