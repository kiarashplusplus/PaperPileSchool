#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.generic.edit import CreateView
import datetime
from .models import Gradeable, Student, Teacher
from .forms import GradeableForm


def home(request):
    return render(request, 'home.html')


@login_required(login_url='/accounts/login/')
def student_create_gradeable(request):
    try:
        student = Student.objects.get(id=request.user.id)
    except ObjectDoesNotExist:
        return HttpResponseNotAllowed('Student with this id is not found.')

    if request.method == 'POST':
        form = GradeableForm(request.POST, request.FILES)
        if form.is_valid():
            if str(request.user.id) != form.data['student']:
                return JsonResponse(data={'status': 'Fail',
                                    'errors': 'Submit only on behalf of authorized student.'})
            form.save()
            return JsonResponse(data={'status': 'Success', 'errors': ''})
        else:
            return JsonResponse(data={'status': 'Fail', 'errors': form.errors})
    else:

        form = GradeableForm()
        return render(request, 'upload.html', {'form': form})


@login_required(login_url='/accounts/login/')
def student_get_grades(request):
    try:
        student = Student.objects.get(id=request.user.id)
        grades = Gradeable.objects.filter(student=student.id)
        grades_list = [(g.name, g.grade) for g in grades]
        return JsonResponse(data={'status': 'Success', 'errors': '',
                            'grades': grades_list})
    except ObjectDoesNotExist:
        return HttpResponseNotAllowed('Student with this id is not found.' )

    return JsonResponse(data={'status': 'Fail', 'errors': ''})


@login_required(login_url='/accounts/login/')
def teacher_get_gradeables(request):
    try:
        teacher = Teacher.objects.get(id=request.user.id)
        gradeable = Gradeable.objects.filter(grade='ungraded')
        g_list = [(g.gradeable_id, g.name, g.submission_datetime,
                  g.student) for g in gradeable]
        return JsonResponse(data={'status': 'Success', 'errors': '',
                            'grades': g_list})
    except ObjectDoesNotExist:
        return HttpResponseNotAllowed('Teacher with this id is not found.')

    return JsonResponse(data={'status': 'Fail', 'errors': ''})


@require_POST
def teacher_post_grade(request):
    try:
        data = json.loads(request.body)
        if data['gid'] and data['final_grade'] in ['A', 'B', 'C', 'D', 'F', 'incomplete']:
            gradeable = Gradeable.objects.get(id=data['gid'])
            gradeable.grade = data['final_grade'] 
            gradeable.teacher_notes = data.get('comments', "")
            gradeable.save()
    except Exception as e:
        return HttpResponseNotAllowed('Bad format.')
    return JsonResponse({'status': "Success"})