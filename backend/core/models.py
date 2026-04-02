from django.db import models

class MarketStore(models.Model):
    name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    category = models.CharField(max_length=255, blank=True, default="")
    products_count = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    commission_rate = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("pending", "Pending"), ("suspended", "Suspended")], default="active")
    joined_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class MarketProduct(models.Model):
    name = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255, blank=True, default="")
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    compare_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("out_of_stock", "Out of Stock"), ("pending_review", "Pending Review")], default="active")
    rating = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class MarketOrder(models.Model):
    order_number = models.CharField(max_length=255)
    buyer_name = models.CharField(max_length=255, blank=True, default="")
    store_name = models.CharField(max_length=255, blank=True, default="")
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("shipped", "Shipped"), ("delivered", "Delivered"), ("returned", "Returned"), ("cancelled", "Cancelled")], default="pending")
    order_date = models.DateField(null=True, blank=True)
    payment = models.CharField(max_length=50, choices=[("paid", "Paid"), ("cod", "COD")], default="paid")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.order_number
