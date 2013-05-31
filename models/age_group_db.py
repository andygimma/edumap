import os
import datetime
import urllib
from google.appengine.ext import db
from google.appengine.api import users

class AgeGroup(db.Expando):
    age_group = db.StringProperty(required=True)
    
def CheckAndAdd(age_group):
  gql_string = 'SELECT * From AgeGroup WHERE age_group=:1'
  q = db.GqlQuery(gql_string, age_group)
  if not q.get():
    ag = AgeGroup(age_group = age_group)
    ag.put()
    

def getAllCached():
    pass

def getCachedById():
    pass

def putAndCache():
    pass

def importCSV():
    pass

def deleteAndResetCache():
    # delete from cache and save new cache to db
    pass
    