from django.shortcuts import render

# Create your views here.
def handler404(request, exception):
    context = {}
    response = render(request, "pages/errors/404.html", context=context)
    response.status_code = 404
    return response


def handler500(request):
    context = {}
    response = render(request, "pages/errors/500.html", context=context)
    response.status_code = 500
    return response