'''
Created on 2012. 12. 21.

@author: wemade
'''

from optparse import OptionParser
import ConfigParser
import WarpperPkg.ftpwrap
import WarpperPkg.logwrap

def main(opt, arg):
	logPrint = WarpperPkg.logwrap
	
	if opt.game == None:
		logPrint.info('info', 'log.txt')
		return
	if opt.type == None:
		print "Input build type"
		return
	if opt.version == None:
		print "Input build version"
		return
	
	print 'debugging...'
	logPrint.info('debug', 'debug.txt')
	config = ConfigParser.RawConfigParser()
	config.read('../config/ftpConfig.ini')
	
	ftp = WarpperPkg.ftpwrap
	ftp.connect(config.get(opt.game, 'FtpUser'), config.get(opt.game, 'FtpPasswd'), config.get(opt.game, 'FtpUrl'), config.get(opt.game, 'FtpPort'))
	dirList = ftp.__get_dir_list(config.get(opt.game, 'FtpRoot'))
	print dirList
	ftp.close()
	pass

if __name__ == '__main__':
	parser = OptionParser()
	
	parser.add_option( '-g', '--game', help='game title')
	parser.add_option( '-t', '--type', help='build type')
	parser.add_option( '-v', '--version', help='build version')
	
	opt, arg = parser.parse_args()
	
	main(opt, arg)