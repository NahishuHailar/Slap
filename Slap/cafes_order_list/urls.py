from django.urls import path
from .views import StudentOrder, HomePage, MentorPage, MentorAddClass, MentorAddStudent


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('student', StudentOrder.as_view(), name='student_order'),
    path('mentor', MentorPage.as_view(), name='mentor_page'),
    path('mentor/addclass', MentorAddClass.as_view(), name='mentor_add_class'),
    path('mentor/addstudent', MentorAddStudent.as_view(), name='mentor_add_student'),

]
