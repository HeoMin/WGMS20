'''
Created on 2012. 12. 21.

@author: wemade
'''

from optparse import OptionParser
import ConfigParser
import WarpperPkg.ftpwrap
import logging

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
	
	print 'debugging...'
	logging.info('Options = %s' % opt)
	
	config = ConfigParser.RawConfigParser()
	config.read('../config/ftpConfig.ini')
	
	ftp = WarpperPkg.ftpwrap
	ftp.connect(config.get(opt.game, 'FtpUser'), config.get(opt.game, 'FtpPasswd'), config.get(opt.game, 'FtpUrl'), config.get(opt.game, 'FtpPort'))
	ftp.cwd(config.get(opt.game, 'FtpRoot'))
	dirList = ftp.__get_dir_list()
	print dirList
	ftp.download(opt.version)
	ftp.close()
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