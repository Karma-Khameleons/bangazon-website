from django.views.generic.base import TemplateView

class ProductListView(TemplateView):
	template_name = "product_list.html"