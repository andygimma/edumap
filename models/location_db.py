import os
import datetime
import urllib
from google.appengine.ext import db
from google.appengine.api import users


def GetAllCached(ids = None):
  q = db.Query(model_class = Location, keys_only = True)
  ids = [key.id() for key in q.run(batch_size = 2000)]
   
class Location(db.Expando):
    name = db.StringProperty(required=False)
    name_metaphone = db.StringProperty(required=False)
    city = db.StringProperty()
    state = db.StringProperty()
    zip_code = db.StringProperty()
    full_address = db.StringProperty(required=False)
    latitude = db.FloatProperty(required=False)
    longitude =db.FloatProperty(required=False)
    notes = db.TextProperty()
    contact_number = db.StringProperty()
    #programs, list of references

    
def toDict(Location):
  
  location_dict = {
	'id': Location.key().id(),
	'name': Location.name,
	'city': Location.city,
	'state': Location.state,
	"contact_number": Location.contact_number,
	'address': Location.address,
	'full_address': Location.full_address,
	'latitude': Location.latitude,
	'longitude': Location.longitude,
	'zip_code': Location.zip_code,
	'notes': Location.notes,
      }
  
  return location_dict

def getCachedById():
    pass

def putAndCache():
    pass

def importCSV():
    pass

def deleteAndResetCache():
    # delete from cache and save new cache to db
    pass
