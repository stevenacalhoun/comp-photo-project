import dropbox
from dropboxSecrets import *

#dropboxInstance = DropboxInstance()

class DropboxInstance():
  def __init__(self):
    self.client = dropbox.client.DropboxClient(app_token)

  def saveFile(self, inputName, outputName):
    f = open(inputName, 'rb')
    response = self.client.put_file(outputName, f)
    print "Uploaded:", response

def saveToDropbox(fileName):
  # Upload to dropbox
  dropboxInstance.saveFile('output/out.jpg', fileName)

  # Delete locally
  os.remove('output/out.jpg')

if __name__ == "__main__":
  dropboxInstance = DropboxInstance()
  dropboxInstance.saveFile("test.txt")
