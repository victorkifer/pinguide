from django.http import HttpResponse
from django.template import RequestContext, loader

def index(req):
    template = loader.get_template('web/index.html')
    context = RequestContext(req, {
    })
    return HttpResponse(template.render(context))
