from django.db import models



class Teachers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    office_details = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    email_add = models.EmailField()


class Students(models.Model):
    first_name_s = models.CharField(max_length=30)
    last_name_s = models.CharField(max_length=30)
    email_add_s = models.EmailField()
    def __unicode__(self):
        return self.first_name_s #I wrote just to check my codes

class Courses(models.Model):
    course_name = models.CharField(max_length=30)
    course_code = models.CharField(max_length=30)
    classroom = models.CharField(max_length=30)
    times = models.CharField(max_length=30)
    c_teacher = models.ForeignKey(Teachers)
    c_students = models.ManyToManyField(Students)