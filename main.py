import os
import webapp2

import jinja2

from wtforms import Form, BooleanField, TextField, validators, PasswordField, ValidationError

from webapp2_extras import routes

import ui.handlers.show_index as show_index
import ui.handlers.show_about as show_about
import ui.handlers.show_map as show_map
import ui.handlers.show_default_map as show_default_map



class Route(routes.RedirectRoute):
  def __init__(self, *args, **kwargs):
    # This causes a URL to redirect to its canonical version without a slash.
    # See http://webapp-improved.appspot.com/api/webapp2_extras/routes.html#webapp2_extras.routes.RedirectRoute

    if 'strict_slash' not in kwargs:
        #print 45
      kwargs['strict_slash'] = True
    routes.RedirectRoute.__init__(self, *args, **kwargs)
    

app = webapp2.WSGIApplication([
    Route(r'/', show_index.ShowIndex, name='show_index'),
    Route(r'/about', show_about.ShowAbout, name='show_about'),
    Route(r'/map/<region>', show_map.ShowMap, name='show_map'),
    Route(r'/map/', show_default_map.ShowDefaultMap, name='show_default_map'),
    
    
    
        
    ],
debug=True)
                              
                              