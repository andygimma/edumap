from google.appengine.ext import webapp
#import model
from google.appengine.api import memcache
import logging
#from controllers.datastore_results import datastore_results
from gaesessions import get_current_session
register = webapp.template.create_template_register()

#@register.simple_tag

    
@register.filter(name="region_title")
def region_title(region):
    region = region.replace("_", " ")
    region = region.title()
    return region