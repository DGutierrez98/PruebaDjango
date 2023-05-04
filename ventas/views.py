from re import template
from django.shortcuts import render


def ventas(request):
    context={}
    template_name="ventas_index.html"

    return render(request, template_name, context)
