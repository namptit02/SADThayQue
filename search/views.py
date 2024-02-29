# views.py trong ứng dụng "search"
from django.http import JsonResponse
from product.models import Product

def search(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', '')
        # Thực hiện tìm kiếm trong cơ sở dữ liệu
        books = Product.objects.filter(title__icontains=keyword)
        # Trả về kết quả dưới dạng JSON
        data = [{'title': book.title, 'price': book.price} for book in books]
        return JsonResponse(data, safe=False)
