from django import forms
from .models import Order, Customer, Product
from django.contrib.auth.models import User


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["ordered_by", "shipping_address", "mobile", "email", "payment_method"]



class CustomerRegistrationForm(forms.ModelForm):
    
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())


    class Meta:
        model = Customer                   
        fields = ["username", "password", "email", "full_name", "address"]


    def clean_username(self):              
        uname = self.cleaned_data.get("username")
        
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "Customer with this username already exists.")

        return uname




class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())



class ProductForm(forms.ModelForm):
    # Creating Custom Field ==> i.e Product model mai navako field banayer form ma display garna cha vani yesari garna sakincha.. yaha more_images vanni field Product model ma chaina
    more_images = forms.FileField(required=False, widget=forms.FileInput(attrs={            # yo field chai FileField ho
        "class": "form-control",            # bootstrap ko form contraol class lagako
        "multiple": True                    # multiple: True ko help garesi form batw multiple image halna sakincha
    }))

    class Meta:            
        model = Product     

       
        fields = ["title", "slug", "category", "image", "marked_price", "selling_price", "description", "warranty", "return_policy"]

        # widgets  ko kaam vaneko form ko field lai styling dine ho... alli chittikai parera display garna help garcha.... # Note: widget ko type chai dictionary huna parcha
        widgets = {
            "title": forms.TextInput(attrs={                        
                "class": "form-control",                         
                "placeholder": "Enter the product title here..."    
            }),
            "slug": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the unique slug here..."
            }),
            "category": forms.Select(attrs={                       
                "class": "form-control"
            }),
            "image": forms.ClearableFileInput(attrs={               
                "class": "form-control"
            }),
            "marked_price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Marked price of the product..."
            }),
            "selling_price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Selling price of the product..."
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Description of the product...",
                "rows": 5
            }),
            "warranty": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the product warranty here..."
            }),
            "return_policy": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the product return policy here..."
            }),

        }




