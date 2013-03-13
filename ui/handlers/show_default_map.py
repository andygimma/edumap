import jinja2
import base

from google.appengine.ext.webapp import template
from workers.get_template_path import get_template_path as get_template_path

TEMPLATE_URI = 'ui/templates/map.html'
LEAFLET_TEMPLATE_URL = 'map/templates/leaflet_map.html'
class ShowDefaultMap(base.RequestHandler):
    def get(self):
        self.redirect('/map/newyorkcity')       
        