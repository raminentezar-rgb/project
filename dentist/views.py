from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail

def dental(request):
    return render(request,'dentist/dental.html')
def about(request):
    return render(request,'dentist/about.html')
def blog(request):
    return render(request,'dentist/blog.html')
def doctors(request):
    return render(request,'dentist/doctors.html')
def services(request):
    return render(request,'dentist/services.html')
def blog_single(request):
    return render(request,'dentist/blog-single.html')



def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message']
        # send Email
        send_mail(
            message_subject, # subject email
            message_name,
            message,
            message_email, # from  email
            
            ['ramin.ent33@gmail.com','raminentezarprogrammer@gmail.com'] # to email
            
        )
        return HttpResponse("ایمیل با موفقیت ارسال شد!")
        
    else:
        return render(request,'dentist/contact.html',{})
