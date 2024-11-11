from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.utils import send_email_to_client,send_email_with_attached_file
from django.conf import settings
def send_email(request):
    subject = "Django Ayush"
    message = "Om Sai Ram"
    recipient_list = ["a20042580@gmail.com"]
    file_path = r"C:\Users\Ayush Kumar\sai\home\main.xlsx"

    send_email_with_attached_file(subject,message,recipient_list,file_path)  
    return redirect('/')  

def home(request):
    people = [
        {'name': 'Ayush Kumar', 'age': 26},
        {'name': 'Ashish Kumar', 'age': 16},
    ]
    return render(request, "index.html", context={'people': people})

def contaxt(request):
    return render(request, "contaxt.html")

def about(request):
    return render(request, "about.html")
