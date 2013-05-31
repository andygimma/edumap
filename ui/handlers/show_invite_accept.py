#import models.users_db as users_db
import jinja2
import base
from models import member_db
from models import invite_db
from workers.get_hash import get_hash
from google.appengine.ext import db



from google.appengine.ext.webapp import template
from workers.get_template_path import get_template_path
from workers.check_login import check_login

TEMPLATE_URI = 'ui/templates/invite_accept.html'

class ShowInviteAccept(base.RequestHandler):
    def get(self, invite_hash):
      data = {
	"invite_hash": invite_hash,
	"message": self.request.get("message"),
	"logged_in": check_login(),

      }
      self.response.out.write(template.render(get_template_path(TEMPLATE_URI), data))
      
    def post(self, invite_hash):
      password = self.request.get("password")
      password2 = self.request.get("password2")
      if not password == password2:
	self.redirect("/invite/" + invite_hash + "?message=Passwords aren't identical, please try again")
	
      
      # add to member entity
      q = db.Query(invite_db.Invite)
      q.filter("invite_hash =", invite_hash)
      existing_invite = q.get()
      if not existing_invite:
	self.redirect("/invite/" + invite_hash + "?message=No invite exists at this link")
	return
      # get email
      password_hash = get_hash(password)
      m = member_db.Member(email = existing_invite.email, password_hash = password_hash, permissions_list = [existing_invite.permission])
      m.put()
      # delete invite entity
      db.delete(existing_invite.key())
      self.redirect("/?message=You are now a member, thank you")
      # redirect home