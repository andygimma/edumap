import os
import datetime
import urllib
from google.appengine.ext import db
from google.appengine.api import users


def GetAllCached(ids = None):
  q = db.Query(model_class = Region, keys_only = True)
  ids = [key.id() for key in q.run(batch_size = 2000)]
   
class Region(db.Expando):
    name = db.StringProperty(required=False)

    
def toDict(Person):
  
  person_dict = {
	'id': Region.key().id(),
	'name': Region.name,
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
