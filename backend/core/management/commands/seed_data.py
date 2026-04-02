from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import MarketStore, MarketProduct, MarketOrder
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusMarketplace with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusmarketplace.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if MarketStore.objects.count() == 0:
            for i in range(10):
                MarketStore.objects.create(
                    name=f"Sample MarketStore {i+1}",
                    owner_name=f"Sample MarketStore {i+1}",
                    email=f"demo{i+1}@example.com",
                    category=f"Sample {i+1}",
                    products_count=random.randint(1, 100),
                    rating=round(random.uniform(1000, 50000), 2),
                    commission_rate=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["active", "pending", "suspended"]),
                    joined_date=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 MarketStore records created'))

        if MarketProduct.objects.count() == 0:
            for i in range(10):
                MarketProduct.objects.create(
                    name=f"Sample MarketProduct {i+1}",
                    store_name=f"Sample MarketProduct {i+1}",
                    price=round(random.uniform(1000, 50000), 2),
                    compare_price=round(random.uniform(1000, 50000), 2),
                    stock=random.randint(1, 100),
                    category=f"Sample {i+1}",
                    status=random.choice(["active", "out_of_stock", "pending_review"]),
                    rating=round(random.uniform(1000, 50000), 2),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 MarketProduct records created'))

        if MarketOrder.objects.count() == 0:
            for i in range(10):
                MarketOrder.objects.create(
                    order_number=f"Sample {i+1}",
                    buyer_name=f"Sample MarketOrder {i+1}",
                    store_name=f"Sample MarketOrder {i+1}",
                    total=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["pending", "confirmed", "shipped", "delivered", "returned", "cancelled"]),
                    order_date=date.today() - timedelta(days=random.randint(0, 90)),
                    payment=random.choice(["paid", "cod"]),
                )
            self.stdout.write(self.style.SUCCESS('10 MarketOrder records created'))
