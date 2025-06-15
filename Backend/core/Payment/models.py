from django.db import models

class KhaltiTransaction(models.Model):
    pidx = models.CharField(max_length=100, unique=True)
    purchase_order_id = models.CharField(max_length=100)
    purchase_order_name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    status = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.purchase_order_id} - {self.status}"