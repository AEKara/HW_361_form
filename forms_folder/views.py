from django.shortcuts import render
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from forms_folder.forms import *
from forms_folder.models import *
# Create your views here.

def addteacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            a = Teachers(first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        office_details = form.cleaned_data["office_details"],
                        phone_number = form.cleaned_data["phone_number"],
                        email_add=form.cleaned_data["email_add"])
            a.save()
            return HttpResponseRedirect('/all-teachers/')
    else:
        form = TeacherForm()
    return render_to_response('form_teacher.html', {'form': form}, RequestContext(request))

def all_teacher(request):
    return render_to_response('all_teacher.html', {'teacher_list': Teachers.objects.all()})


def addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            a = Students(first_name_s=form.cleaned_data["first_name_s"],
                        last_name_s=form.cleaned_data["last_name_s"],
                        email_add_s=form.cleaned_data["email_add_s"])

            a.save()
            return HttpResponseRedirect('/all-students/')
    else:
        form = StudentForm()
    return render_to_response('form_student.html', {'form': form}, RequestContext(request))

def all_student(request):
    return render_to_response('all_student.html', {'student_list': Students.objects.all()})


def addcourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            a = Courses(course_name=form.cleaned_data["course_name"],
                        course_code=form.cleaned_data["course_code"],
                        classroom=form.cleaned_data["classroom"],
                        times=form.cleaned_data["times"],
                        c_teacher=form.cleaned_data["c_teacher"],
                        c_students=form.cleaned_data["c_students"])

            a.save()
            return HttpResponseRedirect('/all-courses/')
    else:
        form = CourseForm()
    return render_to_response('form_course.html', {'form': form}, RequestContext(request))

def all_courses(request):
    return render_to_response('all_course.html', {'course_list': Courses.objects.all()})
