'''
Created on 2012. 12. 21.

@author: mheo
'''

from subprocess import *

def importSVN(src, uri):
    p = Popen(['import', src, uri])
    

