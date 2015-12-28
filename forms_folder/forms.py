from django import forms

from django.db import models



class TeacherForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    office_details = forms.CharField(max_length=30)
    phone_number = forms.CharField(max_length=12)
    email_add = forms.EmailField()


class StudentForm(forms.Form):
    first_name_s = forms.CharField(max_length=30)
    last_name_s = forms.CharField(max_length=30)
    email_add_s = forms.EmailField()
    def __unicode__(self):
        return self.first_name_s #I wrote just to check my codes

class CourseForm(forms.Form):
    course_name = forms.CharField(max_length=30)
    course_code = forms.CharField(max_length=30)
    classroom = forms.CharField(max_length=30)
    times = forms.CharField(max_length=30)
    c_teacher = forms.CharField(max_length=30)
    c_students = forms.CharField(max_length=30)
