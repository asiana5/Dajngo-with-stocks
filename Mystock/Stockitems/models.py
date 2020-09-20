from django.db import models

# Create your models here.
class Stockinfo(models.Model):
    stock_name = models.CharField(max_length=30)
    stock_no = models.CharField(max_length=10)
    stock_keypoint = models.CharField(max_length=100,null=True)
    stock_lastprice = models.IntegerField(null=True)
    stock_yesterdayprice = models.CharField(max_length=10,null=True)
    stock_startprice = models.CharField(max_length=10,null=True)
    stock_gab = models.FloatField(null=True)
    stock_gabwon = models.IntegerField(null=True)
    stock_memo = models.TextField(null=True)
    create_date = models.DateTimeField(null=True)

class Stock_list(models.Model):
    corpName = models.CharField(max_length=200)
    corpCode = models.CharField(max_length=10)
    corpCategory = models.CharField(max_length=200, blank=True)