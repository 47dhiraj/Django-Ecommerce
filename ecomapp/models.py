from django.db import models

from django.contrib.auth.models import User                                     

# Create your models here.

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)                 # One to One realtionship cha vanna khojeko ho, i.e A user has one Admin & A admin is associated with one User
    full_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="admins")
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)                 # models.OneToOneField() vannale one to one relationship cha vanna khojeko (i.e A User has one Customer & A Customer is assosciated with one User)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)           
    joined_on = models.DateTimeField(auto_now_add=True)                         

    def __str__(self):
        return self.full_name                                                   



class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title                                                       



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)            # models.ForeignKey() vannale Many To One relationship vanne bujincha django ma (i.e here, A Category has many products & Many Products is associated with One Category)   # on_delete=models.CASCADE vannale whenever we delete category, the automatically delete all the products assosicated with the category
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="products")
    marked_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    description = models.TextField()
    warranty = models.CharField(max_length=300, null=True, blank=True)          
    return_policy = models.CharField(max_length=300, null=True, blank=True)     
    view_count = models.PositiveIntegerField(default=0)                         

    def __str__(self):
        return self.title                                                       


class ProductImage(models.Model):                                               
    product = models.ForeignKey(Product, on_delete=models.CASCADE)              # yo ProdcutImage vanni model ko Product vanni model sanga foreign key batw relation set gareko
    image = models.ImageField(upload_to="products/images/")                     

    def __str__(self):
        return self.product.title



class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)    # models.ForeignKey() vannale, A customer can have many carts & A cart is associated with only one Customer
    total = models.PositiveIntegerField(default=0)                                              
    created_at = models.DateTimeField(auto_now_add=True)                                        

    def __str__(self):
        return "Cart: " + str(self.id)                                                          # Cart model ko each instance or object lai cart id le recognize garauna ko lagi


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Cart: " + str(self.cart.id) + " CartProduct: " + str(self.id)





ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

METHOD = (
    ("Cash On Delivery", "Cash On Delivery"),
    ("Khalti", "Khalti"),
    ("Esewa", "Esewa"),
)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    ordered_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    subtotal = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)           
    created_at = models.DateTimeField(auto_now_add=True)

    payment_method = models.CharField(max_length=20, choices=METHOD, default="Cash On Delivery")
    payment_completed = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return "Order: " + str(self.id)










