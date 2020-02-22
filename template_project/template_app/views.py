from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = { 'text':'hello world', 'number':2020}
    return render(request, 'template_app/index.html',context=context_dict)


def other(request):
    return render(request, 'template_app/other.html')


def relative(request):
    return render(request, 'template_app/relative_url_templates.html')
