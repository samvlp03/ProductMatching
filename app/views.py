from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Product, ScannedProduct1
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .forms import PartForm
import os
from barcode.writer import ImageWriter
from barcode.codex import Code128

@csrf_exempt
def match_product(request):
    if request.method == 'POST':
        
        serial_no = request.POST.get('serial_no')
        part_no = request.POST.get('part_no')

        # Assuming model_no is a prefix in the serial_no
        model_no = serial_no[:4]

        product_exists = Product.objects.filter(serial_no=serial_no, part_no=part_no).exists() #change table name and field name
        already_scanned = ScannedProduct1.objects.filter(serial_no=serial_no, part_no=part_no).exists()

        scanned_products = ScannedProduct1.objects.all().values('model_no','serial_no', 'part_no')

        if already_scanned:
            return JsonResponse({'status': 'already_scanned', 'scanned_products': list(scanned_products)})

        if product_exists:
            ScannedProduct1.objects.create(model_no=model_no, serial_no=serial_no, part_no=part_no)
            product = Product.objects.get(serial_no=serial_no, part_no=part_no) #change table name and field(same as above)
            product_data = {
                'category': product.category, #change field name
                'model_no': product.model_no,
                'part_no': product.part_no,
                'serial_no': product.serial_no
            }
            return JsonResponse({'status': 'ok', 'product': product_data, 'scanned_products': list(scanned_products)})
        else:
            return JsonResponse({'status': 'ng'})

    return render(request, 'app/match_product.html')

def add_part(request):
    if request.method == "POST":
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('part_list')
    else:
        form = PartForm()
    return render(request, 'app/add_part.html', {'form': form})

def part_list(request):
    parts = Product.objects.all() #change table name
    return render(request, 'app/part_list.html', {'parts': parts})

@csrf_exempt
def generate_barcode(request):
    if request.method == 'POST':
        input_data = request.POST.get('input_data')
        barcode = Code128(input_data, writer=ImageWriter())
        file_path = os.path.join(settings.MEDIA_ROOT, 'barcodes', f'{input_data}.png')
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        barcode.save(file_path)
        return JsonResponse({'file_path': f'/media/barcodes/{input_data}.png'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
