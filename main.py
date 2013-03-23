import os
import webapp2

import jinja2

from wtforms import Form, BooleanField, TextField, validators, PasswordField, ValidationError

from webapp2_extras import routes

import ui.handlers.show_index as show_index
import ui.handlers.show_about as show_about
import ui.handlers.show_map as show_map
import ui.handlers.show_default_map as show_default_map
import ui.handlers.show_blog as show_blog
import ui.handlers.show_charts as show_charts
import ui.handlers.show_ckan as show_ckan
import ui.handlers.show_import as show_import
import ui.handlers.show_invite as show_invite
import ui.handlers.show_invite_accept as show_invite_accept
import ui.handlers.show_authentication as show_authentication
import ui.handlers.show_site as show_site
import ui.handlers.show_contact as show_contact

import workers.import_csv as import_csv
import workers.public_site_ajax_handler as public_site_ajax_handler
import workers.logout_handler as logout_handler






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
    Route(r'/blog', show_blog.ShowBlog, name='show_blog'),
    Route(r'/charts', show_charts.ShowCharts, name='show_charts'),
    Route(r'/ckan', show_ckan.ShowCkan, name='show_ckan'),
    Route(r'/import_csv', import_csv.ImportCSV, name='import_csv'),
    Route(r'/import', show_import.ShowImport, name='show_import'),
    Route(r'/invite', show_invite.ShowInvite, name='show_invite'),
    Route(r'/invite/<invite_hash>', show_invite_accept.ShowInviteAccept, name='show_invite_accept'),
    Route(r'/authentication', show_authentication.ShowAuthentication, name='show_authentication'),        
    Route(r'/public_site_ajax_handler', public_site_ajax_handler.PublicSiteAjaxHandler, name='public_site_ajax_handler'),        
    Route(r'/site/<site_id>', show_site.ShowSite, name='show_site'),
    Route(r'/contact', show_contact.ShowContact, name='show_contact'),
    Route(r'/logout', logout_handler.LogoutHandler, name='logout_handler'),


    ],
debug=True)
                              
                              