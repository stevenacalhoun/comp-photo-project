import sys
import os
import re
import ctypes
from ctypes import byref

from variables import *

if sys.platform == 'darwin':
    libgphoto2dll = 'libgphoto2.dylib'
    os.system("killall PTPCamera")
elif sys.platform == 'linux2':
    libgphoto2dll = "libgphoto2.so"
else:
    raise Exception("Platform not supported by gphoto2.")

gp = ctypes.CDLL(libgphoto2dll)
gp.gp_context_new.restype = ctypes.c_void_p
context = ctypes.c_void_p(gp.gp_context_new())

retries = 1
GP_CAPTURE_IMAGE = 0
GP_FILE_TYPE_NORMAL = 1

class CameraFilePath(ctypes.Structure):
    _fields_ = [('name', (ctypes.c_char * 128)),
                ('folder', (ctypes.c_char * 1024))]

class Camera(object):
    def __init__(self, auto_init = True):
        self._cam = ctypes.c_void_p()
        self._leave_locked = False
        _check_result(gp.gp_camera_new(byref(self._cam)))
        self.initialized = False
        if auto_init:
            self.init()

    def init(self):
        if self.initialized:
            print "Camera is already initialized."
        ans = 0
        for i in range(1 + retries):
            ans = gp.gp_camera_init(self._cam, context)
            if ans == 0:
                break
            elif ans == -60:
                print "***", unmount_cmd
                os.system(unmount_cmd)
                time.sleep(1)
                print "Camera.init() retry #%d..." % (i)
        _check_result(ans)
        self.initialized = True

    def download_file(self, srcfolder, srcfilename, destpath):
        cfile = CameraFile(self._cam, srcfolder, srcfilename)
        cfile.save(destpath)
        gp.gp_file_unref(cfile._cf)

    def close(self):
        if self.initialized:
            self._exit()
            self._free()
            self.initialized = False

    def capture_image(self, destpath = None):
        path = CameraFilePath()

        ans = 0
        for i in range(1 + retries):
            ans = gp.gp_camera_capture(self._cam, GP_CAPTURE_IMAGE, byref(path), context)
            if ans == 0: break
            else: print "capture_image(%s) retry #%d..." % (destpath, i)
        _check_result(ans)

        if destpath:
            self.download_file(path.folder, path.name, destpath)
        else:
            return (path.folder, path.name)

    def _exit(self):
        _check_result(gp.gp_camera_exit(self._cam, context))

    def _free(self):
        _check_result(gp.gp_camera_free(self._cam))

class CameraFile(object):
    def __init__(self, cam = None, srcfolder = None, srcfilename = None):
        self._cf = ctypes.c_void_p()
        _check_result(gp.gp_file_new(byref(self._cf)))
        if cam:
            _check_unref(gp.gp_camera_file_get(cam, srcfolder, srcfilename, GP_FILE_TYPE_NORMAL, self._cf, context), self)


    def open(self, filename):
        _check_result(gp.gp_file_open(byref(self._cf), filename))

    def save(self, filename = None):
        if filename is None:
            filename = self.name

        file = open(filename, 'wb')
        file.write(self.to_pixbuf())
        file.close()

    def to_pixbuf(self):
        mimetype = ctypes.c_char_p()
        gp.gp_file_get_mime_type(self._cf, ctypes.byref(mimetype))
        print ctypes.string_at(mimetype)

        """Returns data for GdkPixbuf.PixbufLoader.write()."""
        data = ctypes.c_char_p()
        size = ctypes.c_ulong()
        gp.gp_file_get_data_and_size(self._cf, ctypes.byref(data),
                                     ctypes.byref(size))

        print size.value
        return ctypes.string_at(data, size.value)

def _check_unref(result, camfile):
    if result!=0:
        gp.gp_file_unref(camfile._cf)
        gp.gp_result_as_string.restype = ctypes.c_char_p
        message = gp.gp_result_as_string(result)
        raise libgphoto2error(result, message)

def _check_result(result):
    if result < 0:
        gp.gp_result_as_string.restype = ctypes.c_char_p
        message = gp.gp_result_as_string(result)
        raise libgphoto2error(result, message)
    return result

# Snap an image
def captureImage(camera, captureType, captureTime):
  camera.capture_image("output/out.jpg")
  camera.close()

  fileName = 'output/' + time.strftime("%Y_%m_%d-%H_%M_%S") + "-" + captureType + '_' + str(captureTime) + ".jpg"

  return fileName

# Trigger inrared camera remote
def triggerRemote():
  if PI_SETUP:
    wiringpi.pinMode(CAMERA_PIN, 1)
    wiringpi.digitalWrite(CAMERA_PIN, 1)
    wait(0.1)
    wiringpi.digitalWrite(CAMERA_PIN, 0)
  else:
    print "Can't trigger remote, not pi"

if __name__ == "__main__":
    camera = Camera()
    camera.capture_image("out.jpg")
    camera.close()
