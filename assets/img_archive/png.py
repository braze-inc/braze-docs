from PIL import Image
import os
import subprocess
import glob
filelist = glob.iglob('*.*')
for filename in filelist:
    basename, ext = os.path.splitext(filename)
    if ext.lower() == ".png" or ext.lower() == ".pdf" or ext.lower() == ".gif" or ext.lower() == ".otf" or ext.lower() == ".py":
        continue
    img = Image.open(filename)
    img.save(basename + ".png")
    subprocess.call(["/Applications/ImageOptim.app/Contents/MacOS/ImageOptim", basename+".png"])
subprocess.call(["rm", "*.otf"])
subprocess.call(["rm", "*.jpg"])



