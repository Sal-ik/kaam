from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    current_stock = models.IntegerField()
    reorder_point = models.IntegerField()
    reorder_quantity = models.IntegerField()

    def use_stock(self, quantity):
        messages = []
        if self.current_stock >= quantity:
            self.current_stock -= quantity
            messages.append(('success', f"Used {quantity} units of {self.name}. Remaining stock: {self.current_stock}"))
            self.save()
            if self.current_stock <= self.reorder_point:
                reorder_msg = self.reorder_stock()
                messages.append(('success', reorder_msg))
        else:
            messages.append(('error', f"Not enough stock of {self.name}. Available: {self.current_stock}"))
        return messages

    def reorder_stock(self):
        previous_stock = self.current_stock
        self.current_stock += self.reorder_quantity
        self.save()
        return f"Reordered {self.reorder_quantity} units of {self.name}. Stock increased from {previous_stock} to {self.current_stock}."

    def __str__(self):
        return f"{self.name} (Stock: {self.current_stock})"