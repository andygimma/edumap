import os
import datetime
import urllib
from google.appengine.ext import db
from google.appengine.api import users

class Invite(db.Expando):
    email = db.StringProperty(required=True)
    invite_hash = db.StringProperty(required=True)
    permission = db.StringProperty()
    
    
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
    