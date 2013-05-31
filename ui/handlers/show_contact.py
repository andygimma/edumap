#import models.users_db as users_db
import jinja2
import base
from models import site_db
from models import member_db
from gaesessions import get_current_session
from workers.get_hash import get_hash
from workers.check_login import check_login
from google.appengine.ext.webapp import template
from workers.get_template_path import get_template_path

from google.appengine.ext import db


TEMPLATE_URI = 'ui/templates/contact.html'

class ShowContact(base.RequestHandler):
    def get(self):
	#gql_string = 'SELECT * From Site'# WHERE status >= %s", where_string
	#q = db.GqlQuery(gql_string)
	#for site in q.run():
	  #db.delete(site.key())
        data = {
	  "contact_page_current": True,
	  "message": self.request.get("message"),
	  "logged_in": check_login(),
	}
        self.response.out.write(template.render(get_template_path(TEMPLATE_URI), data))         
        