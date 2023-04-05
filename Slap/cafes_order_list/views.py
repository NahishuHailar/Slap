from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import StudentOrderForm, CreateStudentForm, MentorOrderForm, CreateStudentsClass
from .utils import DataMixin


"""Общее формирование контекста страниц представлено классом Datamixin"""
class HomePage(DataMixin, TemplateView):
    template_name = 'cafes_order_list/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        c_def['title'] = 'Главная'
        return dict(list(context.items()) + list(c_def.items()))


class StudentOrder(DataMixin, CreateView):
    form_class = StudentOrderForm
    template_name = 'cafes_order_list/student_order.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Заказ')

        return dict(list(context.items()) + list(c_def.items()))


class MentorPage(DataMixin, CreateView):
    form_class = MentorOrderForm
    template_name = 'cafes_order_list/mentor_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Mentor')

        return dict(list(context.items()) + list(c_def.items()))


class MentorAddClass(DataMixin, CreateView):
    form_class = CreateStudentsClass
    template_name = 'cafes_order_list/mentor_add_class.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='AddClass')

        return dict(list(context.items()) + list(c_def.items()))


class MentorAddStudent(DataMixin, CreateView):
    form_class = CreateStudentForm
    template_name = 'cafes_order_list/mentor_add_student.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='AddClass')

        return dict(list(context.items()) + list(c_def.items()))
