import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import MarketStore, MarketProduct, MarketOrder


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['marketstore_count'] = MarketStore.objects.count()
    ctx['marketstore_active'] = MarketStore.objects.filter(status='active').count()
    ctx['marketstore_pending'] = MarketStore.objects.filter(status='pending').count()
    ctx['marketstore_suspended'] = MarketStore.objects.filter(status='suspended').count()
    ctx['marketstore_total_rating'] = MarketStore.objects.aggregate(t=Sum('rating'))['t'] or 0
    ctx['marketproduct_count'] = MarketProduct.objects.count()
    ctx['marketproduct_active'] = MarketProduct.objects.filter(status='active').count()
    ctx['marketproduct_out_of_stock'] = MarketProduct.objects.filter(status='out_of_stock').count()
    ctx['marketproduct_pending_review'] = MarketProduct.objects.filter(status='pending_review').count()
    ctx['marketproduct_total_price'] = MarketProduct.objects.aggregate(t=Sum('price'))['t'] or 0
    ctx['marketorder_count'] = MarketOrder.objects.count()
    ctx['marketorder_pending'] = MarketOrder.objects.filter(status='pending').count()
    ctx['marketorder_confirmed'] = MarketOrder.objects.filter(status='confirmed').count()
    ctx['marketorder_shipped'] = MarketOrder.objects.filter(status='shipped').count()
    ctx['marketorder_total_total'] = MarketOrder.objects.aggregate(t=Sum('total'))['t'] or 0
    ctx['recent'] = MarketStore.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def marketstore_list(request):
    qs = MarketStore.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'marketstore_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def marketstore_create(request):
    if request.method == 'POST':
        obj = MarketStore()
        obj.name = request.POST.get('name', '')
        obj.owner_name = request.POST.get('owner_name', '')
        obj.email = request.POST.get('email', '')
        obj.category = request.POST.get('category', '')
        obj.products_count = request.POST.get('products_count') or 0
        obj.rating = request.POST.get('rating') or 0
        obj.commission_rate = request.POST.get('commission_rate') or 0
        obj.status = request.POST.get('status', '')
        obj.joined_date = request.POST.get('joined_date') or None
        obj.save()
        return redirect('/marketstores/')
    return render(request, 'marketstore_form.html', {'editing': False})


@login_required
def marketstore_edit(request, pk):
    obj = get_object_or_404(MarketStore, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.owner_name = request.POST.get('owner_name', '')
        obj.email = request.POST.get('email', '')
        obj.category = request.POST.get('category', '')
        obj.products_count = request.POST.get('products_count') or 0
        obj.rating = request.POST.get('rating') or 0
        obj.commission_rate = request.POST.get('commission_rate') or 0
        obj.status = request.POST.get('status', '')
        obj.joined_date = request.POST.get('joined_date') or None
        obj.save()
        return redirect('/marketstores/')
    return render(request, 'marketstore_form.html', {'record': obj, 'editing': True})


@login_required
def marketstore_delete(request, pk):
    obj = get_object_or_404(MarketStore, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/marketstores/')


@login_required
def marketproduct_list(request):
    qs = MarketProduct.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'marketproduct_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def marketproduct_create(request):
    if request.method == 'POST':
        obj = MarketProduct()
        obj.name = request.POST.get('name', '')
        obj.store_name = request.POST.get('store_name', '')
        obj.price = request.POST.get('price') or 0
        obj.compare_price = request.POST.get('compare_price') or 0
        obj.stock = request.POST.get('stock') or 0
        obj.category = request.POST.get('category', '')
        obj.status = request.POST.get('status', '')
        obj.rating = request.POST.get('rating') or 0
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/marketproducts/')
    return render(request, 'marketproduct_form.html', {'editing': False})


@login_required
def marketproduct_edit(request, pk):
    obj = get_object_or_404(MarketProduct, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.store_name = request.POST.get('store_name', '')
        obj.price = request.POST.get('price') or 0
        obj.compare_price = request.POST.get('compare_price') or 0
        obj.stock = request.POST.get('stock') or 0
        obj.category = request.POST.get('category', '')
        obj.status = request.POST.get('status', '')
        obj.rating = request.POST.get('rating') or 0
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/marketproducts/')
    return render(request, 'marketproduct_form.html', {'record': obj, 'editing': True})


@login_required
def marketproduct_delete(request, pk):
    obj = get_object_or_404(MarketProduct, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/marketproducts/')


@login_required
def marketorder_list(request):
    qs = MarketOrder.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(order_number__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'marketorder_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def marketorder_create(request):
    if request.method == 'POST':
        obj = MarketOrder()
        obj.order_number = request.POST.get('order_number', '')
        obj.buyer_name = request.POST.get('buyer_name', '')
        obj.store_name = request.POST.get('store_name', '')
        obj.total = request.POST.get('total') or 0
        obj.status = request.POST.get('status', '')
        obj.order_date = request.POST.get('order_date') or None
        obj.payment = request.POST.get('payment', '')
        obj.save()
        return redirect('/marketorders/')
    return render(request, 'marketorder_form.html', {'editing': False})


@login_required
def marketorder_edit(request, pk):
    obj = get_object_or_404(MarketOrder, pk=pk)
    if request.method == 'POST':
        obj.order_number = request.POST.get('order_number', '')
        obj.buyer_name = request.POST.get('buyer_name', '')
        obj.store_name = request.POST.get('store_name', '')
        obj.total = request.POST.get('total') or 0
        obj.status = request.POST.get('status', '')
        obj.order_date = request.POST.get('order_date') or None
        obj.payment = request.POST.get('payment', '')
        obj.save()
        return redirect('/marketorders/')
    return render(request, 'marketorder_form.html', {'record': obj, 'editing': True})


@login_required
def marketorder_delete(request, pk):
    obj = get_object_or_404(MarketOrder, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/marketorders/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['marketstore_count'] = MarketStore.objects.count()
    data['marketproduct_count'] = MarketProduct.objects.count()
    data['marketorder_count'] = MarketOrder.objects.count()
    return JsonResponse(data)
