#import models.users_db as users_db
import jinja2
import os
import base
from models import member_db
from workers.get_hash import get_hash
from google.appengine.ext import db
from gaesessions import get_current_session


from google.appengine.ext.webapp import template
from workers.get_template_path import get_template_path
from workers.check_login import check_login


TEMPLATE_URI = 'ui/templates/authentication.html'
class ShowAuthentication(base.RequestHandler):
    def get(self):
      destination = self.request.get("destination")
      data = {
	"destination": destination,
	"message": self.request.get("message"),
	"logged_in": check_login(),

      }
      self.response.out.write(template.render(get_template_path(TEMPLATE_URI), data))         
      
    def post(self):
      email = self.request.get("email")
      password = self.request.get("password")
      password_hash = get_hash(password)
      destination = self.request.get("destination")
      
      q = db.Query(member_db.Member)
      q.filter("email =", email)
      q.filter("password_hash =", password_hash)
      existing_member = q.get()
      
      if existing_member:
        # create gae sessions
        session = get_current_session()
        session['email'] = existing_member.email
        session['permissions_list'] = existing_member.permissions_list
        if not destination:
	  self.redirect("/")
	  return
        self.redirect(destination)
      else:
	self.redirect("/authentication?message=Email and Password not recognized")
	