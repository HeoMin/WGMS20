'''
Created on 2013. 01. 01.

@author: mheo
'''
import logging

LOGGING_LEVELS = {'critical': logging.CRITICAL,
				  'error': logging.ERROR,
				  'warning': logging.WARNING,
				  'info': logging.INFO,
				  'debug': logging.DEBUG}

def info(level, logfile):
	logging_level = LOGGING_LEVELS.get(level, logging.NOTSET)
	logging.basicConfig(level=logging_level, filename=logfile,
					format='%(asctime)s [%(levelname)s]: %(message)s',
					datefmt='%Y-%m-%d %H:%M:%S')