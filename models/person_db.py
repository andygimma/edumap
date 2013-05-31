import os
import datetime
import urllib
from google.appengine.ext import db
from google.appengine.api import users


def GetAllCached(ids = None):
  q = db.Query(model_class = Person, keys_only = True)
  ids = [key.id() for key in q.run(batch_size = 2000)]
   
class Person(db.Expando):
    name = db.StringProperty(required=False)
    name_metaphone = db.StringProperty(required=False)
    main_focus = db.StringProperty()
    specific_focus = db.StringProperty()
    city = db.StringProperty()
    state = db.StringProperty(required=False)
    latitude = db.FloatProperty(required=False)
    longitude =db.FloatProperty(required=False)
    contact_number = db.StringProperty()
    twitter = db.StringProperty()
    linked_in = db.StringProperty()
    website = db.StringProperty()
    notes = db.TextProperty()

    
    #programs, list of references

    
def toDict(Person):
  
  person_dict = {
	'id': Person.key().id(),
	'name': Person.name,
	'main_focus': Person.main_focus,
	'city': Person.city,
	'state': Person.state,
	"contact_number": Person.contact_number,
	'latitude': Person.latitude,
	'longitude': Person.longitude,
	'notes': Person.notes,
	'twitter': Person.twitter,
	'linked_in': Person.linked_in,
	'website': Person.website,
      }
  
  return person_dict

def getCachedById():
    pass

def putAndCache():
    pass

def importCSV():
    pass

def deleteAndResetCache():
    # delete from cache and save new cache to db
    pass
