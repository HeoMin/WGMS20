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
    
def cwd(path):
    ftp.cwd(path)
    
def pwd():		
	return ftp.pwd()

def __get_dir_list():
    return ftp.nlst()

def __is_file(filename):
    current = pwd()
    try:
        ftp.cwd(filename)
    except:
        ftp.cwd(current)
        return True
    ftp.cwd(current)
    return False

def download(fname):
    if __is_file(fname):
        curpath = pwd()
        print('download - ' + curpath + fname)
        f = open(fname, 'wb')
        ftp.retrbinary('RETR ' + fname, f.write)
    else:
        current = os.getcwd()
        current_ftp = pwd()
            
        if False == os.path.isdir(fname):
            os.mkdir(fname)
        os.chdir(fname)
        ftp.cwd(fname)
        
        entries = __get_dir_list()
        for entry in entries:
            download(entry)
            
        os.chdir(current)
        ftp.cwd(current_ftp)