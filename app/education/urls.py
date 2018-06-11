from django.urls import path

from education import views

urlpatterns = [
    path('', views.index, name='index'),
    path('school/', views.school_list, name='school-list'),
    path('school/<int:pk>/', views.school_detail, name='school-detail'),
    path('student/', views.student_list, name='student-list'),
    path('student/<int:pk>/', views.student_detail, name='student-detail'),
]