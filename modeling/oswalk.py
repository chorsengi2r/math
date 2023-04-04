import os

root_dir = "./../MATH/test"

for subdir, dir, files in os.walk(root_dir):
    print (subdir)
    print (dir)
    #print (files)
    print ('--------------------------------')
