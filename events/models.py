from __future__ import unicode_literals
 
from django.db import models
from django.core.exceptions import ValidationError 
from django.urls import reverse

class MyModel(models.Model):
    attribute = models.CharField(max_length=100)

    def __str__(self):
        return self.attribute

    def get_absolute_url(self):
        return reverse('url-name', kwargs={'pk':self.pk})

class Tutor(models.Model):
    tutorname=models.TextField()

class Grade(models.Model):
    grade=models.TextField()

class Student(models.Model):
    studentname=models.TextField()

class Subject(models.Model):
    subjectname=models.TextField()
 
class Event(models.Model):
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
    class Subjects(models.TextChoices):
        ENG = '1', "ENGLISH"
        BM = '2', "BAHASA MELAYU"
        MAT = '3', "MATH"
        SCI = '4', "SCIENCE"
    
    class Grades(models.TextChoices):
        Grade_1 = '1', "Year 1"
        Grade_2 = '2', "Year 2"
        Grade_3 = '3', "Year 3"
        Grade_4 = '4', "Year 4"
        Grade_5 = '5', "Year 5"
        Grade_6 = '6', "Year 6"
        Grade_7 = '7', "Form 1"
        Grade_8 = '8', "Form 2"
        Grade_9 = '9', "Form 3"
        Grade_10 = '10', "Form 4"
        Grade_11 = '11', "Form 5"
    
    subject=models.TextField(choices=Subjects.choices,default=1)
    grade=models.TextField(choices=Grades.choices,default=1)
    
    
 
    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True
 
        return overlap
 
    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))
 
    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')
 
'''
        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))
'''






