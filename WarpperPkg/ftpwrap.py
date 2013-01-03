'''
Created on 2012. 12. 21.

@author: mheo
'''

import ftplib
import os
import logging

ftp = ftplib.FTP()

def connect(fUser, fPass, fHost, fPort=22):
    ftp.connect(fHost, fPort)
    ftp.login(fUser, fPass)
    
def close():
    ftp.close()
    
def __get_dir_list(fRoot):
    return ftp.nlst(fRoot)

def __is_file(filename):
    current = ftp.pwd()
    try:
        ftp.cwd(current)
    except:
        ftp.cwd(current)
        return True
    ftp.cwd(current)
    return False

def download(fname):
    if __is_file(fname):
        curpath = ftp.pwd()
        print('download - ' + curpath + fname)
        f = open(fname, 'wb')
        ftp.retrbinary('RETR ' + fname, f.write)
    else:
        current = os.getcwd()
        logging.debug('current : ' + current)
        current_ftp = ftp.pwd()
        logging.debug('current_ftp : ' + current_ftp)
    
        if False == os.path.isdir(fname):
            os.mkdir(fname)
        os.chdir(fname)
        ftp.cwd("/home")
        
        entries = ftp.nlst()
        for entry in entries:
            download(entry)
            
        os.chdir(current)
        ftp.cwd(current_ftp)