from django.shortcuts import render
from datetime import date
import datetime
from datetime import timedelta
from datetime import date
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Farmdata, Scheduledata, Farmerdata
import datetime

from datetime import datetime
from datetime import timedelta


def index(request):

    farmerdata = Farmerdata.objects.all()
    crops = Farmdata.objects.all()
    schedules = Scheduledata.objects.all()
    template = loader.get_template('leancrop/index.html')
    context = {"farmerdat":farmerdata,}
    # HttpResponse(template.render(contoext, request))
    html = '<h1>Farmers<h1>' \
           'click on farmers name to get fertilizer price'
    for farmer in farmerdata:
        html += '<br>'+ "<a href="+str(farmer.id)+ ">"+str(farmer)+"</a>"
        # HttpResponse(template.render(context, request))
    html += '<h1>Crops<h1>' \
           'click on crops name to get farmers'

    for crop in crops:
        html += '<br>'+ "<a href=farmers/"+str(crop.id)+ ">"+str(crop)+"</a>"

    html += "<br><br><a href='schedules/'>click here to check schedules of today</a>"
    return HttpResponse(html)



def fertilisers(request, id):
    # fertlst = Farmerdata.objects.get(id=id).sd.all()
    try:
        fertlst = Farmdata.objects.get(id=id).fm.all()
    except:
        fertlst = []

    price1 = 80
    price2 = 40
    price3 = 55
    default_price = 60
    html = ''
    for fert in fertlst:
        quant = Farmerdata.objects.get(id=id).sd.get(fertiliser=fert).quantity
        if fert == "ammonium sulfate":
            cost = quant * price1
        elif fert == "urea":
            cost = quant * price2
        elif fert == "DAP":
            cost = quant * price3
        else:
            cost = quant * default_price
        html += "<h2>fertilizer price<h2>""<strong>"+str(fert)+"</strong>""<p>"+str(cost)+"</p>"

    return HttpResponse(html)

def  schedules(request, id):

    sowing_date = Farmdata.objects.get(id=id).sowing_date

    today = date.today()

    days_to = abs(sowing_date - today)
    days_to = int(str(days_to).split('day')[0])
    fertilisers = Farmerdata.objects.get(id=id).sd.filter(days_after=days_to)

    html = ''
    for fert in fertilisers:
        html += '<br>' + fert

    return HttpResponse(html)


def farmers(request, id):

    if len(Farmdata.objects.all().filter(id = id))> 0:

        farmer = str(Farmerdata.objects.all().filter(id = id)[0])
        # html = '<h1>Farmers<h1>' \
        #        'click on farmers name to get fertilizer price'
        # # for farmer in farmerdata:
        #     html += '<br>' + "<a href=" + str(farmer.id) + ">" + str(farmer) + "</a>"
    else:
        farmer = "none"

    return HttpResponse(farmer)

# def crop(request):
#     farm = Farmdata.objects.all()
#     crops = farm.filter(sowing_date=datetime.date.today())
#     ids = farm.values_list("id", flat=True).filter(sowing_date=datetime.date.today())
#     farmers = Farmerdata.objects.all()
#     farmers.filter(id__in=set(ids))
#     html = ''
#
#     for crop, farmer in zip(crops, farmers):
#         html += '<br>' + str(farmer) + " " + str(crop)
#
#     return  HttpResponse("<h1></h1>")