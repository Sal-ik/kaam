class InventoryItem:
    def __init__(self, name, initial_stock, reorder_point, reorder_quantity):
        self.name = name
        self.current_stock = initial_stock
        self.reorder_point = reorder_point
        self.reorder_quantity = reorder_quantity

    def use_stock(self, quantity):
        if self.current_stock >= quantity:
            self.current_stock -= quantity
            print(f"Used {quantity} units of {self.name}. Remaining stock: {self.current_stock}")
        else:
            print(f"Not enough stock of {self.name}. Available: {self.current_stock}")

        # Check if reorder is needed
        if self.current_stock <= self.reorder_point:
            self.reorder_stock()

    def reorder_stock(self):
        self.current_stock += self.reorder_quantity
        print(f"Reordered {self.reorder_quantity} units of {self.name}. New stock: {self.current_stock}")

    def __str__(self):
        return f"Inventory Item: {self.name}, Stock: {self.current_stock}, Reorder Point: {self.reorder_point}, Reorder Quantity: {self.reorder_quantity}"


# Simulation of the inventory system
if __name__ == "__main__":
    # Create an inventory item
    item = InventoryItem(name="Widget A", initial_stock=100, reorder_point=20, reorder_quantity=50)

    print("Initial Inventory:")
    print(item)

    # Simulate usage and reordering
    usage_pattern = [30, 40, 25, 15, 10]  # Units used in each time period
    for i, usage in enumerate(usage_pattern, start=1):
        print(f"\nTime Period {i}:")
        item.use_stock(usage)
        print(item)