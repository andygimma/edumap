import os
import datetime
import urllib
from google.appengine.ext import db
from google.appengine.api import users


def GetAllCached(ids = None):
  q = db.Query(model_class = Program, keys_only = True)
  ids = [key.id() for key in q.run(batch_size = 2000)]
   
class Program(db.Expando):
    name = db.StringProperty(required=False)
    name_metaphone = db.StringProperty(required=False)
    age_group = db.StringProperty()
    subject = db.StringProperty()
    address = db.StringProperty()
    city = db.StringProperty()
    state = db.StringProperty(required=False)
    full_address = db.StringProperty()
    latitude = db.FloatProperty(required=False)
    longitude =db.FloatProperty(required=False)
    contact_number = db.StringProperty()
    website = db.StringProperty()
    notes = db.TextProperty()
    location_metaphone = db.StringProperty()
    location_name = db.StringProperty()

    
    #programs, list of references

    
def toDict(Program):
  
  location_dict = {
	'id': Program.key().id(),
	'name': Program.name,
	"contact_number": Program.contact_number,
	'full_address': Program.full_address,
	'latitude': Program.latitude,
	'longitude': Program.longitude,
	'website': Program.website,
	'notes': Program.notes,
	'location_name': Program.location_name,
      }
  
  return program_dict

def getCachedById():
    pass

def putAndCache():
    pass

def importCSV():
    pass

def deleteAndResetCache():
    # delete from cache and save new cache to db
    pass
