from django.http import HttpResponse

def Gallery( request ) :
    return HttpResponse( u'Hello World!' )
	
from django.http import Http404
from datetime import *

def dtime( request, offset ) :
    try :
        offset = int(offset)
        dt = datetime.now() + timedelta( hours = offset )
        result = HttpResponse( u"<html><body>%s</body></html>" % dt )
        return result
    except ValueError :
        raise Http404