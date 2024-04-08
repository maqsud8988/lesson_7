from django.shortcuts import render
from django.views import View
from .models import Student

class StudentListView(View):
    def get(self, request):
        student = Student.objects.all=()
        return render(request, "student.html", {"talabalar": student})

class LandingView(View):
    def get(self, request):
        return render(request, "index.html")