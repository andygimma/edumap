import jinja2
import base
from models import program_db
from models import person_db


from google.appengine.ext.webapp import template
from workers.get_template_path import get_template_path
from workers.check_login import check_login

TEMPLATE_URI = 'ui/templates/site.html'
class ShowSite(base.RequestHandler):
    def get(self, site_id):
        site = program_db.Program.get_by_id(int(site_id))
        program_metaphone = site.name_metaphone
        
	q = person_db.Person.all()
	q.filter('program_metaphone = ', program_metaphone)
	people = q.run()
	
	#for p in people:
	  #raise Exception(p.name)
	
	
        data = {
            "site": site,
            "message": self.request.get("message"),
            "logged_in": check_login(),
            "people": people,
        }
        self.response.out.write(template.render(get_template_path(TEMPLATE_URI), data))         
        