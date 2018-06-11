from django.shortcuts import render


def index(request):
    return render(request, 'education/index.html')

def school_list(request):
    return render(request, 'education/school_list.html')

def school_detail(request):
    return render(request, 'education/school_detail.html')

def student_list(request):
    return render(request, 'education/student_list.html')

def student_detail(request):
    return render(request, 'education/student_detail.html')