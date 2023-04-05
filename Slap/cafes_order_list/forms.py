from django import forms
from .models import StudentOrder, Student, MentorOrder, StudentClass


class StudentOrderForm(forms.ModelForm):
    class Meta:
        model = StudentOrder
        fields = '__all__'


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class MentorOrderForm(forms.ModelForm):
    class Meta:
        model = MentorOrder
        fields = '__all__'


class CreateStudentsClass(forms.ModelForm):
    class Meta:
        model = StudentClass
        fields = '__all__'
