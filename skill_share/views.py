# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from skill_share.models import *
from skill_share.forms import *
from django.shortcuts import render,redirect
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def profile(request):
    template = "profile.html"
    context = {
	'student_list': Student.objects.all,
    }
    return render(request, template, context)

def login(request):
    template = "login.html"
    return render(request, template)

def create_profile(request):
    p_skills = Skill.objects.all()
    form = createAccountForm(request.POST or None)
    form2 = createSkillForm(request.POST or None)
    template = "create_profile.html"
    context  = {
    "form":form,
    "form2":form2,
    }
    if form2.is_valid():
        obj = form.save(commit=False)
        print(obj)
        obj.save()
        return redirect('create_profile')

    if form.is_valid():
        obj = form.save(commit=False)
        print(obj)

        obj.save()
        form.save_m2m()

        return redirect('profile')
    return render(request,template,context)

def create_skill(request):
    p_skills = Skill.objects.all()
    form = createSkillForm(request.POST or None)
    template = "create_skill.html"
    context  = {
    "form":form,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        print(obj)
        obj.save()
        return redirect('create_profile')
    return render(request,template,context)
