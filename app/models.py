from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    name= models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number= models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Image(models.Model):
    image=models.ImageField(upload_to='products/')

class Products(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    images = models.ManyToManyField(Image, related_name='products')
    selling_price = models.DecimalField(max_digits=10, default="0.00", decimal_places=2, null=True, blank=True)
    discount_price = models.DecimalField(max_digits=10,default="0.00", decimal_places=2, null=True, blank=True)
    available = models.BooleanField(default=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.title

    def discount(self):
        if self.selling_price > 0 and self.discount_price > 0:
            discounted = ((self.selling_price - self.discount_price) / self.selling_price) * 100
            return round(discounted, 2)
        return 0
    

class Rating(models.Model):
    product = models.ForeignKey(Products, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(default=1)  # 1 to 5 star rating
    review = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.title} - {self.stars} Stars'
    


class OrderItem(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    weight = models.PositiveIntegerField(default=1, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    price = models.PositiveIntegerField(default=1, null=True, blank=True)
    odered_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.product

class DeliveryAddress(models.Model):
    order = models.ForeignKey(OrderItem, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address1 = models.TextField(null=True, blank=True)
    address2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    date_time= models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.order
    
