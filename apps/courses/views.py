# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse

from .models import Course

def index(request):
    context = {"courses": []}
    courses = Course.objects.all()
    for course in courses:
        context['courses'].append({
            "id": course.id,
            "name": course.name,
            "description": course.description,
            "date_added": course.created_at.strftime('%B %e %Y %l:%M%p')
        })
    return render(request, 'courses/index.html', context)

def add(request):
    if request.method == 'POST':

        # FORM VALIDATION
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('courses:index'))

        # ADD TO DATABASE
        Course.objects.create(name=request.POST['name'], description=request.POST['description'])

        return redirect(reverse('courses:index'))
    else:
        return redirect(reverse('courses:index'))

def destroy(request, id):
    course = Course.objects.get(id=id)
    context = {
        "id": course.id,
        "name": course.name,
        "description": course.description
    }
    return render(request, 'courses/destroy.html', context)

def destroy_really(request, id):
    if request.method == "POST":
        Course.objects.get(id = id).delete()
        return redirect(reverse('courses:index'))
    else:
        return redirect(reverse('courses:index'))
