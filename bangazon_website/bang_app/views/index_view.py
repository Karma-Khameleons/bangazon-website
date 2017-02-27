from django.views.generic.base import TemplateView

class IndexView(TemplateView):

	'''
		Purpose-
			This class provides the base template for bang_app 

		Methods-
			None

		Author:
			Abby
	'''
	template_name = "index.html"
