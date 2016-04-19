import dropbox
from dropboxSecrets import *

class DropboxInstance():
  def __init__():
    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
    authorize_url = flow.start()
    print 'Go to: ' + authorize_url
    code = raw_input("Enter the authorization code here: ").strip()

    access_token, user_id = flow.finish(code)
    self.client = dropbox.client.DropboxClient(access_token)

  def saveFile(fileName):
    f = open(fileName, 'rb')
    response = client.put_file(fileName, f)
    print "Uploaded:", response
