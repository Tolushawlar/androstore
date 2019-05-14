from django.db import models
from django.urls import reverse


# for the cateogory of the products in the store
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True ,db_index=True, help_text='Unique value for product page URL, created from name.')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
  

# for the products in each of the product cateogories
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, help_text='Unique value for product page URL, created from name.')
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    search = models.CharField(max_length=50, null=True)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField()    

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ProductDetails", kwargs={"id": self.id})
    

# for the signup of the newsletter 
class SignUp(models.Model):
    email = models.EmailField(max_length=254)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
