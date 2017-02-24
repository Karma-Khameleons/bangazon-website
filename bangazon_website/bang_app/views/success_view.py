from django.views.generic.base import TemplateView


class Success(TemplateView):
	template_name = "success.html"