#import models.users_db as users_db
import jinja2
import base
from models import site_db
from gaesessions import get_current_session

from google.appengine.ext.webapp import template
from workers.check_login import check_login
from workers.get_template_path import get_template_path

TEMPLATE_URI = 'ui/templates/import.html'

class ShowImport(base.RequestHandler):
  def get(self):
    session = get_current_session()
    try:
      email = session['email']
      permissions_list = session['permissions_list']
    except:
      self.redirect("/authentication?destination=/import")
      return
      
    if not email and permissions_list:
      self.redirect("/authentication?destination=/invite")
      return
      
    if not any("Import CSV" in s for s in permissions_list) and not any("Administrator" in s for s in permissions_list):
      self.redirect("/authentication?destination=/invite&message=You do not have permission to view this page, if this is in error contact us")
      return
    data = {
      "message": self.request.get("message"),
      "logged_in": check_login(),
    }
    
    
    self.response.out.write(template.render(get_template_path(TEMPLATE_URI), data))         
    