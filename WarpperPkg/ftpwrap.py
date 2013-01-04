'''
Created on 2012. 12. 21.

@author: mheo
'''

import ftplib
import os
import logging
import socket

ftp = ftplib.FTP()

def connect(fUser, fPass, fHost, fPort=21):
    server_connect = False
    try:
        ftp.connect(fHost, fPort)
        server_connect = True
    except socket.gaierror, e:
        logging.info("ERROR -- Could not connect to (%s): %s" % (fHost, str(e.args)))
    except IOError, e:
        logging.info("ERROR -- File not found: %s" % (str(e.args)))
    except socket.error, e:
        logging.info("ERROR -- Could not connect to (%s): %s" % (fHost, str(e.args)))
        
    if server_connect:
        try:
            ftp.login(fUser, fPass)
            logging.info("Login into (%s) as (%s)" % (fHost, fUser))
            return True
        except ftplib.error_perm, e:
            logging.info("ERROR -- Check Username/Password: %s" % (str(e.args)))
            return False
        except e:
            logging.info("ERROR -- Check login info: %s" % (str(e.args)))
            return False
    else:
        logging.info("Closing Connection")
        return False
    
def close():
    logging.info("FTP disconnected")
    ftp.close()
    
def cwd(path):
    ftp.cwd(path)
    
def pwd():
    return ftp.pwd()

def __get_dir_list():
    return ftp.nlst()

def __is_file(filename):
    try:
        ftp.cwd(filename)
    except:
        return True
    return False

def download(fname):
    curpath = pwd()
    
    if __is_file(fname):
        print('download - %s/%s' % (curpath,fname))
        f = open(fname, 'wb')
        ftp.retrbinary('RETR ' + fname, f.write)
        f.close()
    else:
        current = os.getcwd()
            
        if False == os.path.isdir(fname):
            os.mkdir(fname)
        os.chdir(fname)
        
        entries = __get_dir_list()
        for entry in entries:
            download(entry)
            
        os.chdir(current)
        ftp.cwd(curpath)

def upload(fname):
    curpath = pwd()
    absPath = os.path.abspath(fname)
    
    if not os.path.isdir(absPath):
        print('upload - %s/%s' % (curpath, fname))
        f = open(fname, 'rb')
        ftp.storbinary('STOR ' + fname, f)
        f.close()
    else:
        lPath = os.getcwd()
        
        if __is_file(fname):
            ftp.mkd(fname)
            ftp.cwd(fname)
        os.chdir(fname)
        
        entries = os.listdir(absPath)
        logging.debug("entries : %s" % entries)
        for entry in entries:
            upload(entry)
        
        os.chdir(lPath)
        ftp.cwd(curpath)
    