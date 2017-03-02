from django.views.generic.base import TemplateView
from bang_app.models import Customer, Product, ProductType, CustomerOrder
from django.shortcuts import render


class IndexView(TemplateView):
  '''
  Purpose-
  This class provides the base template & home page for bang_app

  Methods-
  get - retrieves 5 products from each category to list them on the home page

  Author:
  Abby, @whitneycormack, @lsales
  '''
  template_name = "index.html"

  def get(self, request):
    self.categories = ProductType.objects.order_by('id')
    for c in self.categories:
      c.products = Product.objects.filter(product_type_id=c.id)[:5]
    return render(request, self.template_name, {'categories': self.categories})

