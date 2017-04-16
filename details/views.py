from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from details.models import Details
from .models import Details
from login.models import Login

# Create your views here.

class DetailsList(ListView):
    template_name = "details/index.html"
    model = Details

class DetailsId(ListView):
    template_name = "details/detailsID.html"
    model = Details

#    return render(request,'details/index.html')

#def detailsId(request, album_id):
#    return HttpResponse("<h2>Details for Album id : " + str(album_id) + "</h2>")
    #return render(request,album_id,'details/detailsID.html')