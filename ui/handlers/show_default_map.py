import jinja2
import base

from google.appengine.ext.webapp import template
from workers.get_template_path import get_template_path as get_template_path
from models import region_db

TEMPLATE_URI = 'ui/templates/regions.html'
LEAFLET_TEMPLATE_URL = 'map/templates/leaflet_map.html'
class ShowDefaultMap(base.RequestHandler):
    def get(self):
	# show list of all locations on an HTML
	q = region_db.Region.all()
	query = q.fetch(1000)
	data = {
            "regions_list": query,
        }
        self.response.out.write(template.render(get_template_path(TEMPLATE_URI), data)) 
        #self.redirect('/map/newyorkcity')       
        