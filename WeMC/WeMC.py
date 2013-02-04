'''
Created on 2012. 12. 21.

@author: wemade
'''

from optparse import OptionParser
import ConfigParser
from StepFunction import *
import logging
import os

def GetStepFunc(opt, config):
	return (
		{'fn':'DownloadBuild', 'param':[opt.game, opt.version, config]},
		{'fn':'ConnetSvn', 'param':[]},
		{'fn':'CommitSrc', 'param':[]}
		)


def Main(opt, arg):
	if opt.game == None:
		logging.error("Input game title")
		return
	if opt.type == None:
		logging.error("Input build type")
		return
	if opt.version == None:
		logging.error("Input build version")
		return
	
	logging.debug('Options = %s' % opt)
		
	config = ConfigParser.RawConfigParser()
	config.read('../config/ftpConfig.ini')
	config.read('../config/svnConfig.ini')
	
	stepFunc = GetStepFunc(opt, config)
	
	for item in stepFunc:
		print item['fn'], item['param']

	#svn = WrapperPkg.svnwrap
	
	#dirList = ftp.__get_dir_list()
	#print dirList
	
	#svn.svnLogin(config.get(opt.game, 'user'), config.get(opt.game, 'passwd'))
	#svn.importSVN(opt.version, config.get('SVN', 'uri'))
	#svn.commit(opt.version, config.get('SVN', 'uri'))
	#svn.delete("D:\\svn\\repos\\WGMS20\\sacheonpang")
	pass

if __name__ == '__main__':
	parser = OptionParser()
	
	parser.add_option( '-g', '--game', help='game title')
	parser.add_option( '-t', '--type', help='build type')
	parser.add_option( '-v', '--version', help='build version')
	parser.add_option( '-l', '--logging-level', help='Logging level')
	parser.add_option( '-f', '--logging-file', help='Logging file name')
		
	LOGGING_LEVELS = {'critical': logging.CRITICAL,
                      'error': logging.ERROR,
                      'warning': logging.WARNING,
                      'info': logging.INFO,
                      'debug': logging.DEBUG}
	
	opt, arg = parser.parse_args()
	
	logging_level = LOGGING_LEVELS.get(opt.logging_level, logging.NOTSET)
	logging.basicConfig(level=logging_level, filename=opt.logging_file,
                      format='%(asctime)s [%(levelname)s]: %(message)s',
                      datefmt='%Y-%m-%d %H:%M:%S')
	
	Main(opt, arg)