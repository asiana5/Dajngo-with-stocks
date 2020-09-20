from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('itemadd/', views.itemadd, name='Itemadd'),
    path('itemadd/itemcreate/', views.itemcreate, name="Itemcreate"),
    path('Itempricerefresh/', views.itempricerefresh, name="Itempricerefresh"),
    path('itemdetail/<int:stock_id>/', views.itemdetail, name="Itemdetail"),
    path('search/', views.search, name='search'),
    path('itemdetail/modify/modify_submit/', views.modify_submit, name='modifysubmit'),
    path('itemdetail/modify/<int:stock_id>/', views.modify, name='modify'),
]