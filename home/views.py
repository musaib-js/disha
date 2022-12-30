from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Email, Video, Service
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from .models import College, Courses

def home(request):
    service = Service.objects.all()
    context = {'service':service}
    return render(request, 'index.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['number']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Check For the erronous input
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(subject)<4 or len(message)<20:
            messages.error(request, "Please fill the form correctly")

        # Save the Data to the database
        else:
        
             newcontact = Contact(name = name, phone = phone, email = email, subject = subject, message = message)
             newcontact.save()

             #Send the Data Via Email
             fromemail = 'disharightcareers5@gmail.com'
             subject = "New Query"
             message = "Name: " + name + '\n' + "Phone: " + phone + '\n' + "Email: " +  email + '\n' + "Concern: " + subject + '\n' + "Details: " + message

             send_mail(subject, message, fromemail, ['disharightcareers5@gmail.com'])
             messages.success(request, "Your Details Have Been Submittted Successfully. We'll Get Back To You Soon")
            

    return render(request, 'index.html')

def email(request):
    if request.method == "POST":
        email = request.POST['email']

        # Save the Data to the Database
        newmail = Email(email = email)
        newmail.save()
        print(newmail)
    return render(request, "index.html")

def service(request, slugtwo):
    service = Service.objects.filter(slugtwo = slugtwo).first()
    context = {'service': service}
    return render(request, "servicepage.html", context)
    
def colleges(request):
    colleges = College.objects.all()
    context  = {'colleges': colleges}
    return render(request, 'colleges.html', context)
