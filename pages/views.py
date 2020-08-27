from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from listings.models import Listing
from contacts.models import Contact
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage

def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

	context = {
		'listings': listings		
	}
	return render(request, 'pages/index.html', context)


def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']		
		contact = Contact(name = name, email = email, phone = phone, message = message)		
		contact.save()
		# messages.success(request, 'Your request has been submitted')


		# # send email:
		# send_mail(
		# 	'Quiry Email',
		# 	'Mr./Mrs. ['+name+'] from ['+email+']. Phone no. ['+phone+']. ['+message+'].',
		# 	'abdur15-741@diu.edu.bd',
		# 	['arnirob741@gmail.com'],
		# 	fail_silently = False
		# )

		return redirect('contact')
		
	return render(request, 'pages/contact.html')

	

def about(request):
	return render(request, 'pages/about.html')
