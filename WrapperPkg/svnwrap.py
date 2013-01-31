'''
Created on 2012. 12. 21.

@author: mheo
'''

from subprocess import *
import pysvn
import logging
import os

## callback function
def ssl_server_trust_prompt(trust_dict):
    return True, trust_dict['failures'], True

client = pysvn.Client()
client.callback_ssl_server_trust_prompt = ssl_server_trust_prompt

## wrapper function
def svnLogin(user="", passwd=""):
    def get_login(realm, username, may_save):
        retcode = True
        username = user
        password = passwd
        save = True
        return retcode, username, password, save
    
    try:
        client.callback_get_login = get_login
        logging.info("SVN login success: %s" % user)
    except:
        logging.error("SVN login error: %s" % user)
        return False
    return True
    
    
    
def importSVN(fname, uri):
    try:
        absPath = os.path.abspath(fname)
        call(['../bin/svn.exe', 'import', '-m', 'import SVN', absPath, uri, '--username', 'nike1710@gmail.com', '--password', 'Hb6WN6dZ4Sv5']) 
    except:
        logging.error("process execute error")
        return False
    return True


def add(repoDir):
    try:
        tStatus = client.status(repoDir,recurse=True)
        for item in tStatus:
            if item.text_status == pysvn.wc_status_kind.unversioned:
                client.add(item.path)
                logging.info("Add item: %s , status: %s" % (item.path, item.text_status) )
    except:
        logging.error("Can not add item: %s" % repoDir)
        
def commit(repoDir, comment):
    try:
        tStatus = client.status(repoDir,recurse=True)
        for item in tStatus:
            if item.text_status == pysvn.wc_status_kind.modified or item.text_status == pysvn.wc_status_kind.added:
                client.checkin(repoDir, "Build Version: %s" % comment)
                logging.info("Commit item: %s , status: %s" % (item.path, item.text_status) )
    except:
        logging.error("Can not commit item: %s" % repoDir)

def delete(repoDir):
    tStatus = client.status(repoDir,recurse=True)
    for item in tStatus:
        if item.text_status == pysvn.wc_status_kind.deleted:
            client.remove(item.path)
            logging.info("Delete item: %s , status: %s" % (item.path, item.text_status) )