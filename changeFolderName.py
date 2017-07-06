import os
import sys

path = "/opt/yocto/www/projects/Fast"
files = os.listdir(path)
for name in files:
    a = os.path.split(name)
    newName = a[1].replace('内测','')
    os.rename(name, newName)

