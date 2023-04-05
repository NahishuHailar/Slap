from django.db import models


class Student(models.Model):
    surname = models.CharField('surname', max_length=30)
    name = models.CharField('name', max_length=30)
    student_class = models.ForeignKey('StudentClass', on_delete=models.CASCADE)


class StudentClass(models.Model):
    """Grouping students by class"""
    class_title = models.CharField('class_title', max_length=30)
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    mentor = models.ForeignKey('Mentor', on_delete=models.CASCADE)


class School(models.Model):
    title = models.CharField('school_title', max_length=40)


class Mentor(models.Model):
    """Every student class has a mentor"""
    surname = models.CharField('surname', max_length=30)
    name = models.CharField('name', max_length=30)
    school = models.ForeignKey('School', on_delete=models.CASCADE)


class StudentOrder(models.Model):
    """Student's orders for every school day"""
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    breakfast = models.BooleanField('breakfast', default=False)
    dinner = models.BooleanField('dinner', default=False)
    nothing = models.BooleanField('without food', default=True)
    order_time = models.DateTimeField(auto_now=True)
    auto_order = models.BooleanField('auto ordering', default=False)


class MentorOrder(models.Model):
    breakfast_amount = models.IntegerField(default=0)
    dinner_amount = models.IntegerField(default=0)
    order_time = models.DateTimeField(auto_now=True)



class Bartender(models.Model):
    """Restaurant worker"""
    surname = models.CharField('surname', max_length=30)
    name = models.CharField('name', max_length=30)
    school = models.ForeignKey('School', on_delete=models.CASCADE)



