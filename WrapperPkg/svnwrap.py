'''
Created on 2012. 12. 21.

@author: mheo
'''

from subprocess import *
import pysvn
import logging
import os

def ssl_server_trust_prompt(trust_dict):
    return True, trust_dict['failures'], True

client = pysvn.Client()
client.callback_ssl_server_trust_prompt = ssl_server_trust_prompt

def importSVN(fname, uri):
    try:
        absPath = os.path.abspath(fname)
        call(['../bin/svn.exe', 'import', '-m', 'import SVN', absPath, uri, '--username', 'nike1710@gmail.com', '--password', 'Hb6WN6dZ4Sv5']) 
    except:
        logging.debug("process execute error")
        return False
    return True


def add(fname):
    try:
        tStatus = client.status(fname,recurse=True)
        for item in tStatus:
            if os.path.isdir(item.path):
                continue
            if item.text_status == pysvn.wc_status_kind.unversioned:
                logging.debug("addItem: %s , status: %s" % (item.path, item.text_status) )
                client.add(item.path)        
    except:
        logging.info("Can not add item: %s" % fname)

def commit(fname, uri):
    try:
        absPath = os.path.abspath(fname)
        add("sacheonpang")
        call(['../bin/svn.exe', 'commit', '-m', fname, "D:\\svn\\repos\\WGMS20\\"])
    except:
        logging.debug("process execute error: source commit error")
        return False
    return True


