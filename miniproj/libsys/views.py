from django.shortcuts import get_object_or_404, render
from libsys.models import Member, SignupForm, Book, Borrow
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
import datetime
#from libsys import forms


def index(request):
	if request.POST.get('submit'):
		phone = request.POST.get('phonenum')
		passwd = request.POST.get('password')
		q = Member.objects.get(phone = phone)
		if q.password == passwd:
			return HttpResponseRedirect('/libsys/userhome')
		else:
			return HttpResponse("Incorrect phone number or password!")
	else:
		template = loader.get_template('libsys/index.html')
    	context = RequestContext(request)
    	return HttpResponse(template.render(context))

def signup(request):
	form = 	SignupForm
	if request.POST:
		form = SignupForm(request.POST)
		form.save()
		p = form.cleaned_data
		return HttpResponseRedirect('/libsys/success')
	else:
		return render(request, 'libsys/signupform.html', {'form': form})

def signupsuccess(request):
	template = loader.get_template('libsys/signupsuccess.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

def dashboard(request):
	template = loader.get_template('libsys/dashboard.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

def bookborrow(request):
	if request.POST.get('submit'):
		bookid = request.POST.get('bookie')
		memid = request.POST.get('mid')
		bk = Book.objects.get(bid = bookid)
		memberr = Member.objects.get(mid = memid)
		bk.noofcopies = bk.noofcopies - 1
		i = datetime.datetime.now()
		issuedate = '2014-11-04'
		duedate = '2014-11-18'
		borrowed = Borrow(bookid=bk, memid=memberr, issuedate=issuedate, duedate=duedate)
		if bk.noofcopies>=0:
			bk.save()
			borrowed.save()
			return HttpResponse("Book borrowal success!")
		else:
			return HttpResponse("No copies of this book are available!")
	else:
		template = loader.get_template('libsys/bookborrowal.html')
		context = RequestContext(request)
		return HttpResponse(template.render(context))

def viewbooks(request):
	book_list = Book.objects.all()
	template = loader.get_template('libsys/booklist.html')
	context = RequestContext(request, {
		'book_list' : book_list,
		})
	return HttpResponse(template.render(context))

def viewstatus(request):
	borrow_list = Borrow.objects.all()
	template = loader.get_template('libsys/viewstatus.html')
	context = RequestContext(request, {
		'borrow_list' : borrow_list,
		})
	return HttpResponse(template.render(context))


# Create your views here.
