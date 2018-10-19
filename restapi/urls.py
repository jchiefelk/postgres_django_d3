from django.conf.urls import url
from django.views import generic

urlpatterns = [url(r'^', generic.TemplateView.as_view(template_name='index.html'))]
