#import models.users_db as users_db
import jinja2
import os
import base

from google.appengine.ext.webapp import template
from workers.get_template_path import get_template_path
from workers.check_login import check_login

TEMPLATE_URI = 'ui/templates/blog.html'
class ShowBlog(base.RequestHandler):
    def get(self):
        data = {
	  "blog_page_current": True,
	  "message": self.request.get("message"),
	  "logged_in": check_login(),
	}
        self.response.out.write(template.render(get_template_path(TEMPLATE_URI), data))         
        