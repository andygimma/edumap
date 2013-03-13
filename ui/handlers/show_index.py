#import models.users_db as users_db
import jinja2
import base

from google.appengine.ext.webapp import template
from workers.get_template_path import get_template_path as get_template_path

TEMPLATE_URI = 'ui/templates/index.html'

class ShowIndex(base.RequestHandler):
    def get(self):
        self.response.out.write(template.render(get_template_path(TEMPLATE_URI), {}))         
        