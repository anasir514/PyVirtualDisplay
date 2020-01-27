"""
two calls

This can be error
"""
import logging

from easyprocess import EasyProcess

from pyvirtualdisplay.smartdisplay import SmartDisplay

logging.basicConfig(level=logging.DEBUG)


backend1 = "wx"
backend2 = "wx"


with SmartDisplay(visible=0, bgcolor="black") as disp:
    disp.pyscreenshot_backend = backend1
    with EasyProcess("xmessage test1"):
        img1 = disp.waitgrab()

with SmartDisplay(visible=0, bgcolor="black") as disp:
    disp.pyscreenshot_backend = backend2
    with EasyProcess("xmessage test2"):
        img2 = disp.waitgrab()

img1.show()
img2.show()
