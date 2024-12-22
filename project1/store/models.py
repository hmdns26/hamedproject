from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=500,blank=True)
    top_product=models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')
class Discount(models.Model):
    discount=models.FloatField()
    description=models.CharField(max_length=500)

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.PROTECT,related_name='products')
    name = models.CharField( max_length=255)
    slug = models.SlugField()
    description=models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory =models.IntegerField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    discount =models.ManyToManyField(Discount,blank=True)

class Customer(models.Model):
    first_name = models.CharField( max_length=255)
    last_name = models.CharField( max_length=255)
    last_name = models.CharField( max_length=255)
    email = models.EmailField()
    birth_date =models.DateField(null=True,blank=True)

class Address(models.Model):
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
    province = models.CharField( max_length=255)
    city = models.CharField( max_length=255)
    street = models.CharField( max_length=255)   

class Order(models.Model):
    ORDER_STATUS_PAID='p'
    ORDER_STATUS_UNPAID='u'
    ORDER_STATUS_CANCELD='c'
    ORDER_STATUS=[
        (ORDER_STATUS_PAID,'PAID'),
        (ORDER_STATUS_UNPAID,'UNPAID'),
        ( ORDER_STATUS_CANCELD,'CANCEL')
    ]
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT,related_name='order')
    datetime_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1,choices=ORDER_STATUS,default=ORDER_STATUS_UNPAID)


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT,related_name='items')
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT,related_name='order_items')
    quantity = models.PositiveSmallIntegerField()
    price=models.DecimalField(max_digits=6,decimal_places=2)  
    class Meta:
        unique_together=[['order' ,'product']]

class Comment(models.Model):
    COMENT_STATUS_WATING='w'
    COMENT_STATUS_APPROVED='a'
    COMENT_STATUS_NOT_APPROVED='na'
    COMENT_STATUS=[
        (COMENT_STATUS_WATING,'WAITING'),
        (COMENT_STATUS_APPROVED,'APPROVED'),
        ( COMENT_STATUS_NOT_APPROVED,'NOT APPROVED')
    ]
    product= models.ForeignKey(Product ,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=255)
    body=models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2,choices=COMENT_STATUS,default=COMENT_STATUS_WATING)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Customer,on_delete=models.PROTECT,related_name='cart_items')
    quantity = models.PositiveSmallIntegerField()
    class Meta:
        nique_together=[['cart' ,'product']]