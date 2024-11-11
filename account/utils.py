from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.http import HttpResponse

def send_email_to_client(request):
    subject = "Django Ayush"
    message = "Om Sai Ram"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["a20042580@gmail.com"]

    try:
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")
def send_email_with_attached_file(subject,message,recipient_list,file_path):
    mail= EmailMessage(subject=subject,body=message, from_email = settings.EMAIL_HOST_USER,to=recipient_list) 
    mail.attach_file(file_path)
    mail.send()       

