#import models.users_db as users_db
import jinja2
import os
import base
import logging
import csv, codecs, cStringIO
from models import site_db as site_db
from models import age_group_db as age_group_db
from models import program_type_db as program_type_db
from google.appengine.ext import db
import urllib

from geopy import geocoders  
import metaphone

from models import program_db
from models import person_db
from models import location_db
from models import region_db


from google.appengine.api import logservice
logservice.AUTOFLUSH_ENABLED = False

class ImportCSV(base.RequestHandler):
    def post(self):
        csv_file = self.request.get('file')
        cr = csv.DictReader(csv_file.split('\n'))
	g = geocoders.GoogleV3()
	complete = False
	to_put = []
	regions_list=[]
	kind = None
	for row in cr:
	  try:
	    row["age_group"]
	    kind = "Program"
	  except:
	    kind = None
	  if kind == None:  
	    try:
	      row["main_focus"]
	      kind = "People"
	    except:
	      kind = None


	  
	  failures_array = []
	  if kind == "Program":
	    
	    p = program_db.Program()
	    lat = None
	    lng = None
	    address_string = row["address"] + " " + row["city"] + " " + row["state"]
	    try:
	      if len(address_string) > 10:
		try:
		  place, (lat, lng) = g.geocode(address_string.lower())
		  logging.debug(lat)
		  logging.debug(lng)
		  logging.debug(place)
		except:
		  failures_array.append(address_string)
		  continue
		  #geocodes = g.geocode(address_string.lower())
		  #raise Exception(geocodes[0])
	      
	      setattr(p, "latitude", float(lat))
	      setattr(p, "longitude", float(lng))
	      for key in row.keys():
		  initial_value = str(row[key])
		  #new_value = quoted_value = urllib.quote(initial_value.encode('utf-8'))
		  new_value = unicode(initial_value, 'utf-8')

		  setattr(p, key, new_value)
		  #if key == "name":
		    #name_metaphone = metaphone.dm(unicode(row[key]))
		    #setattr(p, "name_metaphone", str(name_metaphone[0]))
		  if key == "region":
		    regions_list.append(row[key])
	      q = program_db.Program.all()
	      q.filter('latitude = ', float(lat))
	      q.filter('longitude = ', float(lng))
	      #q.filter('name_metaphone = ', str(name_metaphone[0]))

	      if not q.get():
		to_put.append(p)
	      else:
		pass
	      complete = True
	    except:
	      failures_array.append(address_string)
	      continue
	      
	  #if kind == "Location":
	      #p = location_db.Location()

	      #lat = None
	      #lng = None
	      #address_string = row["address"] + " " + row["city"] + " " + row["state"]
	      #place, (lat, lng) = g.geocode(address_string.lower())
	      #setattr(p, "latitude", float(lat))
	      #setattr(p, "longitude", float(lng))
	      #for key in row.keys():
		  #setattr(p, key, row[key])
		  #if key == "name":
		    #name_metaphone = metaphone.dm(unicode(row[key]))
		    #setattr(p, key, str(name_metaphone))
	      #to_put.append(p)
	      #complete = True
	      
	  if kind == "People":

	      p = person_db.Person()

	      for key in row.keys():
		  setattr(p, key, row[key])
		  if key == "name":
		    name_metaphone = metaphone.dm(unicode(row[key]))
		    setattr(p, "name_metaphone", str(name_metaphone[0]))
		  if key == "program":
		    program_metaphone = metaphone.dm(unicode(row[key]))
		    setattr(p, "program_metaphone", str(program_metaphone[0]))
		  if key == "region":
		    regions_list.append(row[key])
		    
	      q = person_db.Person.all()
	      q.filter('name_metaphone = ', str(name_metaphone[0]))
	      #q.get()

	      if not q.get():
		to_put.append(p)
	      complete = True



	if complete:
	  final_list = list(set(to_put))
	  db.put(final_list)
	  q = region_db.Region.all()
	  query = q.fetch(1000)
	  saved_regions_list = []
	  for q in query:
	    saved_regions_list.append(q.name)
	    
	  final_regions_list = list(set(regions_list))
	  
	  to_save_regions = list(set(final_regions_list) - set(saved_regions_list))
	  
	  for region in to_save_regions:
	    r = region_db.Region(name=region)
	    r.put()
	  self.response.write(failures_array)

	  #self.redirect("/import?message=Import complete")
	  return
	self.redirect("/import?message=Nothing Uploaded, the CSV was not valid") 
	return
	  
        #for row in cr:

	    ##create entity here
	    #s = site_db.Site()
	    ##s.name="unused"
	    #for key in row.keys():
	      #if key == "Location 1":
		#setattr(s, "address", row[key])
	      #if key == "PROGRAM":
		#setattr(s, "program", row[key])
	      #if key == "SITE NAME":
		#setattr(s, "site_name", row[key])
	      #if key == "PROGRAM TYPE":
		#setattr(s, "program_type", row[key])
		#program_type_db.CheckAndAdd(row[key])
	      #if key == "AGENCY":
		#setattr(s, "agency", row[key])
	      #if key == "Contact Number":
		#setattr(s, "contact_number", row[key])
	      
	      #if key.find("COMMUNITY") > 0:
		#setattr(s, "borough", row[key])
	      #if key.find("Level") > 0:
		#setattr(s, "age_group", row[key])
		#age_group_db.CheckAndAdd(row[key])

	      ##else:
		##setattr(s, key, row[key])

	      ## use set attr
	      
	      ## set from Location 1 property, using indices
	      #setattr(s, "latitude", lat)
	      #setattr(s, "longitude", lng)
	      #to_put.append(s)
	      #complete = True
	  #else:
	    ## compare row.keys to expected keys.
	    #validator_list = ["address", "program", "site_name", "program_type", "borough", "agency", "contact_number", "age_group"]
	    #keys_list = row.keys()
	    #sorted_validator = sorted(set(validator_list))
	    #sorted_keys = sorted(set(keys_list))
	    ##if not cmp(sorted(set(validator_list)), sorted(set(keys_list))):
	      ##continue
	    #if cmp(sorted_keys, sorted_validator) != 0:
	      #continue
	    
	    #s = site_db.Site()
	    
	    #address = row['address']
	    #lat = 0.0
	    #lng = 0.0   
	  
	    #try:
	      #place, (lat, lng) = g.geocode(address.lower())
	    #except:
	      #try:
		#place, (lat, lng) = g.geocode(address.lower() + row["BOROUGH / COMMUNITY"])
	      #except:
		#print address

		#continue
	    #for key in row.keys():
	      #if key == "program_type":
		#program_type_db.CheckAndAdd(row[key])
	      #if key == "age_group":
		#age_group_db.CheckAndAdd(row[key])
		

	      #setattr(s, key, row[key])
	      #setattr(s, "latitude", lat)
	      #setattr(s, "longitude", lng)
	      #to_put.append(s)
	    #complete = True

	    
	    ### run normal csv here
	    ##pass


	  
	  

class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")

class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self
