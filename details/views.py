from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from details.models import Details
from .models import Details
from rest_framework.response import Response
#from login.models import Login

# Create your views here.

class DetailsList(ListView):
    template_name = "details/index.html"
    model = Details

class DetailsId(ListView):
    template_name = "details/detailsID.html"
    model = Details
    def get_context_data(self, **kwargs):
	id = self.request.GET.get('album_id',None)
	if id is not None:
	    return Response({"detail":"Proper value required"}, status = status.HTTP_400_BAD_REQUEST)
	else:
	    #do your work over here
#    return render(request,'details/index.html')

#def detailsId(request, album_id):
#    return HttpResponse("<h2>Details for Album id : " + str(album_id) + "</h2>")
    #return render(request,album_id,'details/detailsID.html')

class BrowseList(ListView):
    template_name = "details/browse.html"

def login(request):
    return render(request,'details/login.html')

def home(request):
    return render(request,'details/home.html')

#def browse(request):
#    return render(request,'details/browse.html')
