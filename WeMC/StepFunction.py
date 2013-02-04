'''
Created on 2012. 12. 21.

@author: wemade
'''
import WrapperPkg.ftpwrap
import WrapperPkg.svnwrap
import logging

def DownloadBuild(game, version, config):
    ftp = WrapperPkg.ftpwrap
    
    isConnet = ftp.connect(config.get(game, 'SrcFtpUser'), config.get(game, 'SrcFtpPasswd'), config.get(game, 'SrcFtpUrl'), config.get(game, 'SrcFtpPort'))
    
    if isConnet:
        ftp.cwd(config.get(game, 'SrcFtpRoot'))
    
        print("========== Start Download (%s) ==========" % config.get(game, 'SrcFtpUrl'))
        ftp.download(version)
        print("========== Finished Download ==========")
    
        ftp.close()
    else:
        logging.error("ftp connect error. check ftp configuration.")
        assert(False)
        
def CommitSrc