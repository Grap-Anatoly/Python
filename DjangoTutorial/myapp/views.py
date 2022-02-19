from django.shortcuts import render, redirect
from django.core import mail
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import RequestContext
from datetime import *

from myapp.models import Dreamreal
from myapp.forms import LoginForm
from myapp.forms import ProfileForm
from myapp.models import Profile


def saveProfile(request):
    saved = False

    if request.method == "POST":
        # Get the posted form
        MyProfileForm = ProfileForm(request.POST, request.FILES)

        if MyProfileForm.is_valid():
            profile = Profile()
            profile.name = MyProfileForm.cleaned_data["name"]
            profile.picture = MyProfileForm.cleaned_data["picture"]
            profile.save()
            saved = True
    else:
        MyProfileForm = ProfileForm()

def hello(request):
   # render allows to pass params to the html frow view directly
   # render(request/response, 'html', {'paramName in html : param in view'})
   today = datetime.now().date()
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "hello.html", {"today": today, "days_of_week": daysOfWeek})

def login(request):
    username = "not logged in"

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
    else:
        MyLoginForm = LoginForm()

    response = render(request, 'loggedin.html', {"username": username},context_instance=RequestContext(request))

    response.set_cookie('last_connection', datetime.datetime.now())
    response.set_cookie('username', datetime.datetime.now())


def formView(request):
    if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
        username = request.COOKIES['username']

        last_connection = request.COOKIES['last_connection']
        last_connection_time = datetime.datetime.strptime(last_connection[:-7],
                                                          "%Y-%m-%d %H:%M:%S")

        if (datetime.datetime.now() - last_connection_time).seconds < 10:
            return render(request, 'loggedin.html', {"username": username})
        else:
            return render(request, 'login.html', {})

    else:
        return render(request, 'login.html', {})

def redirectPage(request):
   return redirect("https://www.djangoproject.com")

def viewArticle(request, articleName, articleId):
   text = "Displaying %s Number : %s" % (articleName,articleId)
   return HttpResponse(text)

def crudops(request):
   # Creating an entry

   dreamreal = Dreamreal(
      website="www.polo.com", mail="sorex@polo.com",
      name="sorex", phonenumber="002376970"
   )

   dreamreal.save()

   # Read ALL entries
   objects = Dreamreal.objects.all()
   res = 'Printing all Dreamreal entries in the DB : <br>'

   for elt in objects:
      res += elt.name + "<br>"

   # Read a specific entry:
   sorex = Dreamreal.objects.get(name="sorex")
   res += 'Printing One entry <br>'
   res += sorex.name

   # Delete an entry
   res += '<br> Deleting an entry <br>'
   sorex.delete()

   # Update
   dreamreal = Dreamreal(
      website="www.polo.com", mail="sorex@polo.com",
      name="sorex", phonenumber="002376970"
   )

   dreamreal.save()
   res += 'Updating entry<br>'

   dreamreal = Dreamreal.objects.get(name='sorex')
   dreamreal.name = 'thierry'
   dreamreal.save()

   return HttpResponse(res)


def datamanipulation(request):

   res = ''

   # Filtering data:
   qs = Dreamreal.objects.filter(name="paul")
   res += "Found : %s results<br>" % len(qs)

   # Ordering results
   qs = Dreamreal.objects.order_by("name")

   for elt in qs:
      res += elt.name + '<br>'

   return HttpResponse(res)

def sendSimpleEmail(request, emailto):
   res = mail.send_mail("hello paul", "comment tu vas?", "paul@polo.com", [emailto])
   return HttpResponse('%s' % res)

class StaticView(TemplateView):
   template_name = "static.html"