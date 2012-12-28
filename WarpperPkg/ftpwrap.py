'''
Created on 2012. 12. 21.

@author: mheo
'''

import ftplib

ftp = ftplib.FTP()

def connect(fUser, fPass, fHost, fPort=22):
    ftp.connect(fHost, fPort)
    ftp.login(fUser, fPass)
    
def close():
    ftp.close()
    
def __get_dir_list(fRoot):
    return ftp.nlst(fRoot)
    