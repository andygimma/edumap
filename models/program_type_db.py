import os
import datetime
import urllib
from google.appengine.ext import db
from google.appengine.api import users

class ProgramType(db.Expando):
    program_type = db.StringProperty(required=True)
    
def CheckAndAdd(program_type):
  gql_string = 'SELECT * From ProgramType WHERE program_type=:1'
  q = db.GqlQuery(gql_string, program_type)
  if not q.get():
    pt = ProgramType(program_type = program_type)
    pt.put()
    
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
    