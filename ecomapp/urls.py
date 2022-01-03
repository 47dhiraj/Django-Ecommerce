from django.urls import path
from .views import *                            


app_name = "ecomapp"

urlpatterns = [

    # Client side pages url
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact-us/", ContactView.as_view(), name="contact"),
    path("all-products/", AllProductsView.as_view(), name="allproducts"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="productdetail"),        
    
    
    # cart related url
    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    path("my-cart/", MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),


    # checkout url 
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    

    # Customer Registration
    path("register/",CustomerRegistrationView.as_view(), name="customerregistration"),
    # Customer Logout
    path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
    # Customer Login
    path("login/", CustomerLoginView.as_view(), name="customerlogin"),



    # Customer Profile
    path("profile/", CustomerProfileView.as_view(), name="customerprofile"),

    # Customer Order Detail View
    path("profile/order-<int:pk>/", CustomerOrderDetailView.as_view(),name="customerorderdetail"),

    # search product url
    path("search/", SearchView.as_view(), name="search"), 



    # Admin Login Pages
    path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),

    # Admin Home
    path("admin-home/", AdminHomeView.as_view(), name="adminhome"),

    # Admin Order Detail
    path("admin-order/<int:pk>/", AdminOrderDetailView.as_view(),name="adminorderdetail"),

    # Admin order list url

    path("admin-all-orders/", AdminOrderListView.as_view(), name="adminorderlist"),
    # Admin Status Change url
    path("admin-order-<int:pk>-change/",AdminOrderStatuChangeView.as_view(), name="adminorderstatuschange"),

    # URL for Admin Product list View 
    path("admin-product/list/", AdminProductListView.as_view(), name="adminproductlist"),
    # URL for adding new product by Admin
    path("admin-product/add/", AdminProductCreateView.as_view(), name="adminproductcreate"),


    # URL for Khalti Payment Inegration
    # yo chai khalti lai request garney url
    path("khalti-request/", KhaltiRequestView.as_view(), name="khaltirequest"),
    #khalti le verify garne url
    path("khalti-verify/", KhaltiVerifyView.as_view(), name="khaltiverify"),


    # URL For Esewa payment Integration
    # Yo chai esewa lai request garney url  ==> 1st url
    path("esewa-request/", EsewaRequestView.as_view(), name="esewarequest"),
    # Yo chai url for esewa payement verification   ==> 2nd URL 
    path("esewa-verify/", EsewaVerifyView.as_view(), name="esewaverify"),

    

]
