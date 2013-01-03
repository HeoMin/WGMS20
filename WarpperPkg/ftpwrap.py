'''
Created on 2012. 12. 21.

@author: mheo
'''

import ftplib
import os
import logging
import traceback

ftp = ftplib.FTP()

def connect(fUser, fPass, fHost, fPort=21):
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
        f.close()
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

def upload(fname):
	'''
	print ftp.getwelcome()
	
	try:
		try:
			logging.info("currently in : " + ftp.pwd())
			print os.getcwd()
			f = open(fname, "rb")
			print "Uploading..."
			ftp.storbinary('STOR ' + fname, f)
			f.close()
		finally:
			print "Quitting..."
	except:
		traceback.print_exe()
	'''
	if False == os.path.isdir(fname):
		curpath = pwd()
		print('upload - ' + curpath + fname)
		f = open(fname, 'rb')
		ftp.retrbinary('STOR ' + fname, f)
		f.close()
	else:
		current = os.getcwd()
		current_ftp = pwd()
			
		if False == __is_file(fname):
			ftp.mkd('min1')
		os.chdir(fname)
		ftp.cwd(fname)
		
		entries = os.listdir(fname)
		for entry in entries:
			upload(entry)
			
		os.chdir(current)
		ftp.cwd(current_ftp)