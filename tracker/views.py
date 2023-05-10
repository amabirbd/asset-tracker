# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Asset, Employee
from .forms import AssetForm
from django.http import HttpResponse
import datetime

def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'asset_list.html', {'assets': assets})

def asset_add(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            return redirect('asset_list')
    else:
        form = AssetForm()
    return render(request, 'asset_add.html', {'form': form})

def asset_assign(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    if request.method == 'POST':
        asset.assigned_to_id = request.POST['assigned_to']
        asset.save()
        return redirect('asset_list')
    return render(request, 'asset_assign.html', {'asset': asset})

def asset_return(request, asset_id):
    print("req: ", request)
    asset = get_object_or_404(Asset, id=asset_id)
    asset.returned_date = datetime.date.today()
    print(asset, asset.returned_date)
    
    asset.save()
    return redirect('asset_list')

def dashboard(request):
    total_assets = Asset.objects.count()
    assigned_assets = Asset.objects.exclude(assigned_to=None).count()
    employees = Employee.objects.all()
    return render(request, 'dashboard.html', {'total_assets': total_assets,
                                               'assigned_assets': assigned_assets,
                                               'employees': employees})