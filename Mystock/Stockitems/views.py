from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Stockinfo, Stock_list
from bs4 import BeautifulSoup
import urllib.request
from django.db.models import Q

# Create your views here.
def index(request):
    stockinfo_list = Stockinfo.objects.order_by('-create_date')

    context = {'stockinfo_list': stockinfo_list}
    return render(request, 'Stockitems/Mystockitems.html', context)


def search(request):
    stockinfo_list = Stockinfo.objects.all().order_by('-id')
    q = request.GET.get('q', "")
    if q:
        stockinfo_list = stockinfo_list.filter(
            Q(stock_name__icontains=q) |
            Q(stock_memo__icontains=q)
            )
        return render(request, 'Stockitems/Mystockitems.html', {'stockinfo_list': stockinfo_list, 'q': q})
    else:
        return render(request, 'Stockitems/Mystockitems.html',{'stockinfo_list': stockinfo_list})

def itemadd(request):
    itemtotal_list = Stock_list.objects.all()
    context = {'itemtotal_list': itemtotal_list}
    return render(request, 'Stockitems/Itemadd.html',context)

def itemcreate(request):
    no = request.POST['create_code']
    name = request.POST['create_name']
    keypoint = request.POST['create_keypoint']
    memo = request.POST['create_memo']
    startprice = request.POST['create_startprice']
    data = Stockinfo(
        stock_no = no,
        stock_name = name,
        stock_keypoint = keypoint,
        stock_memo = memo,
        stock_startprice = startprice,
        create_date = timezone.now(),
    )
    data.save()
    return redirect('index')

def itempricerefresh(request):
    stockinfo_update = Stockinfo.objects.all()
    for key in stockinfo_update:

        stock_no = key.stock_no

        fullurl = "http://asp1.krx.co.kr/servlet/krx.asp.XMLSiseEng?code={}".format(stock_no)
        # req = urllib.request.Request(fullurl, headers={'User-Agent': 'Mozilla/5.0'})
        # result = urllib.request.urlopen(req).read()
        req = urllib.request.Request(fullurl, headers={'User-Agent': 'Mozilla/5.0'})
        result = urllib.request.urlopen(req).read()
        xmlsoup = BeautifulSoup(result, "lxml-xml")

        price = []
        for stock in xmlsoup.find_all("DailyStock"):
            nowPrice = stock['day_EndPrice']
            price.append(nowPrice)

        data = Stockinfo.objects.get(stock_no = stock_no)

        update_price = int(price[0].replace(',', ''))
        yesterday_price = int(price[1].replace(',',''))
        data.stock_gabwon = update_price - yesterday_price
        data.stock_gab = round((update_price / yesterday_price-1)*100 ,2)
        data.stock_lastprice = update_price
        data.stock_yesterdayprice = yesterday_price
        data.save()
    return redirect('index')

def itemdetail(request, stock_id):
    stock_detail = Stockinfo.objects.get(id=stock_id)
    context = {'stockinfo': stock_detail}
    return render(request, 'Stockitems/itemdetail.html', context)

def modify(request,stock_id):
    stock_modify = Stockinfo.objects.get(id=stock_id)
    context = {'stockinfo': stock_modify}
    return render(request, 'Stockitems/Itemmodify.html', context)

def modify_submit(request):
    find_id = request.POST['update_id']
    update_name = request.POST['update_name']
    update_keypoint = request.POST['update_keypoint']
    update_no = request.POST['update_no']
    update_memo = request.POST['update_memo']
    update_startprice = request.POST['update_startprice']
    before_stockinfo = Stockinfo.objects.get(id=find_id)
    before_stockinfo.stock_name = update_name
    before_stockinfo.stock_keypoint = update_keypoint
    before_stockinfo.stock_no = update_no
    before_stockinfo.stock_memo = update_memo
    before_stockinfo.stock_startprice = update_startprice
    before_stockinfo.save()
    return HttpResponseRedirect(reverse('Itemdetail', kwargs={'stock_id':find_id}))