from django.shortcuts import render

def library_view(requesrt):
    return render(requesrt, "library.html")