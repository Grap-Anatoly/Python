from django.shortcuts import render, redirect
from django.core import mail
from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import *

from myapp.models import Dreamreal

def hello(request):
   # render allows to pass params to the html frow view directly
   # render(request/response, 'html', {'paramName in html : param in view'})
   today = datetime.now().date()
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "hello.html", {"today": today, "days_of_week": daysOfWeek})

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