from gaesessions import get_current_session
import base

class LogoutHandler(base.RequestHandler):      
  def get(self):
    session = get_current_session()
    session.clear()
    self.redirect("/")