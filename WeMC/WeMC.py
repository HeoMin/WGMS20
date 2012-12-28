'''
Created on 2012. 12. 21.

@author: wemade
'''

from optparse import OptionParser
import sys
import WarpperPkg.ftpwrap
import ConfigParser

option0 = { 'name' : ('-g', '--game'),   'help' : 'game title'}
option1 = { 'name' : ('-t', '--type'),      'help' : 'build type'}
option2 = { 'name' : ('-v', '--version'),   'help' : 'build version'}

options = [option0, option1, option2]

def main(opt, arg):
    if opt.game == None:
        print "Input game title"
        
    if opt.type == None:
        print "Input build type"
    
    if opt.version == None:
        print "Input build version"
        
    print 'debugging...'
    print 'Options = %s' % opt
    print 'Arguments = %s' % arg
    
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
    for option in options:
        param = option['name']
        del option['name']
        parser.add_option(*param, **option)
        
    opt, arg = parser.parse_args()
    sys.argv[:] = arg
    main(opt, arg)