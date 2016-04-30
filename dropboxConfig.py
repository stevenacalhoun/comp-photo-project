import dropbox
from dropboxSecrets import *

class DropboxInstance():
  def __init__(self):
    self.client = dropbox.client.DropboxClient(app_token)

  def saveFile(self, fileName):
    f = open(fileName, 'rb')
    response = self.client.put_file(fileName, f)
    print "Uploaded:", response

if __name__ == "__main__":
  dropboxInstance = DropboxInstance()
  dropboxInstance.saveFile("test.txt")
