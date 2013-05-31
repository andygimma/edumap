import strings
import logging
from google.appengine.api import mail
from google.appengine.api import users

def send_invite(email, invite_hash):
  logging.debug("send_invite")
  body = strings.EMAIL_BODY
  link = strings.EMAIL_LINK + invite_hash
  content = body + link
  #try:
  sender = "Education Map Invite <%s>" % strings.EMAIL_SENDER
  logging.debug("sender" + sender)

  message = mail.EmailMessage(sender=sender,
  subject=strings.EMAIL_SUBJECT)
  
  message.to = "%s <%s>" % (email, email)
  message.body = content
      
  message.send()
  return True
  #except:
    #return False
