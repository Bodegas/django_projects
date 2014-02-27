from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    htlm_algo = "<html><body>Son as %s.</body></html>"% now
    #return HttpResponse("<html><body>Son as %s.</body></html>"% now)
    return HttpResponse(htlm_algo)

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>Dentro de %d seran as %s. </body></html>'% (offset, dt)
    return HttpResponse(html)
