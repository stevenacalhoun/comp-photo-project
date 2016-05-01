import dropbox
from dropboxSecrets import *

class DropboxInstance():
  def __init__(self):
    self.client = dropbox.client.DropboxClient(app_token)

  def saveFile(self, inputName, outputName):
    f = open(inputName, 'rb')
    response = self.client.put_file(outputName, f)
    print "Uploaded:", response

if __name__ == "__main__":
  dropboxInstance = DropboxInstance()
  dropboxInstance.saveFile("test.txt")
