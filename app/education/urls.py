from django.urls import path

from education import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schools/', views.school_list, name='school-list'),
    path('schools/<int:pk>/', views.school_detail, name='school-detail'),
    path('students/', views.student_list, name='student-list'),
    path('students/<int:pk>/', views.student_detail, name='student-detail'),
]