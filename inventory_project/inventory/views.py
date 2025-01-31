from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import InventoryItem
from .forms import InventoryItemForm

class InventoryListView(ListView):
    model = InventoryItem
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'items'

class InventoryCreateView(CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory:inventory_list')

class InventoryUpdateView(UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory:inventory_list')

class InventoryDeleteView(DeleteView):
    model = InventoryItem
    template_name = 'inventory/inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory:inventory_list')

def use_stock(request, pk):
    if request.method == 'POST':
        item = get_object_or_404(InventoryItem, pk=pk)
        quantity = request.POST.get('quantity')
        
        if not quantity:
            messages.error(request, "Please enter a quantity.")
            return redirect('inventory:inventory_list')
        
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            messages.error(request, "Invalid quantity. Please enter a positive integer.")
            return redirect('inventory:inventory_list')
        
        messages_list = item.use_stock(quantity)
        for level, msg in messages_list:
            if level == 'success':
                messages.success(request, msg)
            elif level == 'error':
                messages.error(request, msg)
        
        return redirect('inventory:inventory_list')
    
    return redirect('inventory:inventory_list')