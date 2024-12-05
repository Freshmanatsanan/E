from django.shortcuts import render,get_object_or_404, redirect
from .models import Course
# Create your views here.

def C(request):
    if 'course_id' in request.GET:
        course_id = request.GET['course_id']
        courses = Course.objects.filter(course_id__icontains=course_id)
    else:
        courses = []
    return render(request, 'E.html', {'courses':courses})

def E(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    if request.method == "POST":
        course.delete()
        return redirect('C')
    return redirect('C')




