# System libraries.
import datetime
import jinja2
import json
import logging
import os
from google.appengine.ext.db import to_dict
from google.appengine.ext import db
from google.appengine.api import memcache
from google.appengine.ext.db import Query
from collections import OrderedDict
# Local libraries.
import base
from models import site_db as site_db


PAGE_OFFSET = 100

dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None

class PublicSiteAjaxHandler(base.RequestHandler):      
  def get(self):
    logging.debug("PublicMapAjaxHandler")
    page = self.request.get("page")
    try:
      page_int = int(page)
    except:
      logging.error("int(page)")
      return
    where_string = "Open"
    gql_string = 'SELECT * From Site'# WHERE status >= %s", where_string
    q = db.GqlQuery(gql_string)


    this_offset = page_int * PAGE_OFFSET
    logging.debug("this_offset = " + str(this_offset))
	
    sites = q.fetch(PAGE_OFFSET, offset = this_offset)
    self.response.out.write(json.dumps([site_db.toDict(s) for s in sites]))

    return
        

    
