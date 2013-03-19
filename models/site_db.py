import os
import datetime
import urllib
from google.appengine.ext import db
from google.appengine.api import users


def GetAllCached(ids = None):
  q = db.Query(model_class = Site, keys_only = True)
  ids = [key.id() for key in q.run(batch_size = 2000)]
   
class Site(db.Expando):
    name = db.StringProperty(required=False)
    site_name = db.StringProperty(required=False)
    agency = db.StringProperty(required=False)
    address = db.StringProperty(required=False)
    latitude = db.FloatProperty(required=False)
    longitude =db.FloatProperty(required=False)
    region = db.StringProperty(required=False)
    notes = db.TextProperty()
    contact_number = db.StringProperty()
    program_type = db.StringProperty()
    borough = db.StringProperty()

    
def toDict(Site):
  
  site_dict = {
	'id': Site.key().id(),
	'name': Site.name,
	'agency': Site.agency,
	'site_name': Site.site_name,
	"contact_number": Site.contact_number,
	'address': Site.address,
	'latitude': Site.latitude,
	'longitude': Site.longitude,
	'region': Site.region,
	'notes': Site.notes,
	'program_type': Site.program_type,
	"age_group": Site.age_group,
	"borough": Site.borough,
      }
  
  return site_dict

def getCachedById():
    pass

def putAndCache():
    pass

def importCSV():
    pass

def deleteAndResetCache():
    # delete from cache and save new cache to db
    pass
