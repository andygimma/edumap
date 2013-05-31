import jinja2
import base
from models import site_db

from google.appengine.ext.webapp import template
from workers.get_template_path import get_template_path
from workers.check_login import check_login

TEMPLATE_URI = 'ui/templates/site.html'
class ShowSite(base.RequestHandler):
    def get(self, site_id):
        site = site_db.Site.get_by_id(int(site_id))
        data = {
            "site": site,
            "message": self.request.get("message"),
            "logged_in": check_login(),
        }
        self.response.out.write(template.render(get_template_path(TEMPLATE_URI), data))         
        