'''
Created on 2012. 12. 21.

@author: wemade
'''

from optparse import OptionParser
import ConfigParser
import WrapperPkg.ftpwrap
import WrapperPkg.svnwrap
import logging
import os

def main(opt, arg):
	if opt.game == None:
		logging.info("Input game title")
		return
	if opt.type == None:
		logging.info("Input build type")
		return
	if opt.version == None:
		logging.info("Input build version")
		return
	
	logging.debug('Options = %s' % opt)
		
	config = ConfigParser.RawConfigParser()
	ftpConfig = config.read('../config/ftpConfig.ini')
	config.read('../config/McConfig.ini')
	
	ftp = WrapperPkg.ftpwrap
	svn = WrapperPkg.svnwrap
	
	#ftp.connect(config.get(opt.game, 'SrcFtpUser'), config.get(opt.game, 'SrcFtpPasswd'), config.get(opt.game, 'SrcFtpUrl'), config.get(opt.game, 'SrcFtpPort'))
	#ftp.cwd(config.get(opt.game, 'SrcFtpRoot'))
	
	#dirList = ftp.__get_dir_list()
	#print dirList
	print("========== Start Download (%s) ==========" % config.get(opt.game, 'SrcFtpUrl'))
	
	#ftp.download(opt.version)
	#print("========== Finished Download ==========")
	#ftp.close()
	
	#ftp.connect(config.get(opt.game, 'DstFtpUser'), config.get(opt.game, 'DstFtpPasswd'), config.get(opt.game, 'DstFtpUrl'), config.get(opt.game, 'DstFtpPort'))
	
	print("========== Start Upload (%s) ==========" % config.get(opt.game, 'DstFtpUrl'))
	#ftp.upload(opt.version)
	print("========== Finished Download ==========")
	#ftp.close()
	
	svn.importSVN(opt.version, config.get('SVN', 'uri'))
	#svn.commit(opt.version, config.get('SVN', 'uri'))
	svn.add("D:\\svn\\repos\\WGMS20\\sacheonpang")
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
	
	main(opt, arg)