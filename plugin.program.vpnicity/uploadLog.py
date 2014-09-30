import os
import re
import sys
import urllib
import urllib2
from xbmc import getCondVisibility as condition, translatePath as translate
import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon(id='plugin.program.vpnicity')
ADDON_TITLE = addon.getAddonInfo('name')
ADDON_VERSION = addon.getAddonInfo('version')

DEBUG = False


UPLOAD_LINK = 'http://xbmclogs.com/show.php?id=%s'
UPLOAD_URL = 'http://xbmclogs.com/'

REPLACES = (
    ('//.+?:.+?@', '//USER:PASSWORD@'),
    ('<user>.+?</user>', '<user>USER</user>'),
    ('<pass>.+?</pass>', '<pass>PASSWORD</pass>'),
)


# Open Settings on first run


class LogUploader(object):

    def __init__(self):
        self.__log('started')
        self.get_settings()
        found_logs = self.__get_logs()
        uploaded_logs = []
        for logfile in found_logs:
            if self.ask_upload(logfile['title']):
                paste_id = self.upload_file(logfile['path'])
                if paste_id:
                    uploaded_logs.append({
                        'paste_id': paste_id,
                        'title': logfile['title']
                    })
                    self.report_msg(paste_id)
        if uploaded_logs and self.email_address:
            self.report_mail(self.email_address, uploaded_logs)
            pass

    def get_settings(self):
        self.email_address = addon.getSetting('email')
        self.__log('settings: len(email)=%d' % len(self.email_address))


    def upload_file(self, filepath):
        self.__log('reading log...')
        file_content = open(filepath, 'r').read()
        for pattern, repl in REPLACES:
            file_content = re.sub(pattern, repl, file_content)
        self.__log('starting upload "%s"...' % filepath)
        post_dict = {
            'paste_data': file_content,
            'api_submit': True,
            'mode': 'xml',
            'paste_lang': 'xbmc'
        }
        post_data = urllib.urlencode(post_dict)
        req = urllib2.Request(UPLOAD_URL, post_data)
        response = urllib2.urlopen(req).read()
        self.__log('upload done.')
        r_id = re.compile('<id>([0-9]+)</id>', re.DOTALL)
        m_id = re.search(r_id, response)
        if m_id:
            paste_id = m_id.group(1)
            self.__log('paste_id=%s' % paste_id)
            return paste_id
        else:
            self.__log('upload failed with response: %s' % repr(response))

    def ask_upload(self, logfile):
        Dialog = xbmcgui.Dialog()
        msg1 = ('Do you want to upload "%s"?') % logfile
        if self.email_address:
            msg2 = ('Email will be sent to: %s') % self.email_address
        else:
            msg2 = ('No email will be sent (No email is configured)')
        return Dialog.yesno(ADDON_TITLE, msg1, '', msg2)

    def report_msg(self, paste_id):
        url = UPLOAD_LINK % paste_id
        Dialog = xbmcgui.Dialog()
        msg1 = ('Uploaded with ID: [B]%s[/B]') % paste_id
        msg2 = ('URL: [B]%s[/B]') % url
        return Dialog.ok(ADDON_TITLE, msg1, '', msg2)

    def report_mail(self, mail_address, uploaded_logs):
        url = 'http://xbmclogs.com/xbmc-addon.php'
        if not mail_address:
            raise Exception('No Email set!')
        post_dict = {'email': mail_address}
        for logfile in uploaded_logs:
            if logfile['title'] == 'xbmc.log':
                post_dict['xbmclog_id'] = logfile['paste_id']
            elif logfile['title'] == 'xbmc.old.log':
                post_dict['oldlog_id'] = logfile['paste_id']
            elif logfile['title'] == 'crash.log':
                post_dict['crashlog_id'] = logfile['paste_id']
        post_data = urllib.urlencode(post_dict)
        if DEBUG:
            print post_data
        req = urllib2.Request(url, post_data)
        response = urllib2.urlopen(req).read()
        if DEBUG:
            print response

    def __get_logs(self):
        log_path = translate('special://logpath')
        vpn_logpath  = translate('special://profile/addon_data/plugin.program.vpnicity/')
        crashlog_path = None
        crashfile_match = None
        if condition('system.platform.osx') or condition('system.platform.ios'):
            crashlog_path = os.path.join(
                os.path.expanduser('~'),
                'Library/Logs/CrashReporter'
            )
            crashfile_match = 'XBMC'
        elif condition('system.platform.windows'):
            crashlog_path = log_path
            crashfile_match = '.dmp'
        elif condition('system.platform.linux'):
            crashlog_path = os.path.expanduser('~')
            crashfile_match = 'xbmc_crashlog'
        # get fullpath for xbmc.log and xbmc.old.log
        log = os.path.join(log_path, 'xbmc.log')
        log_old = os.path.join(log_path, 'xbmc.old.log')
        vpn_log = os.path.join(vpn_logpath, 'openvpn.log')
        # check for XBMC crashlogs
        log_crash = None
        if crashlog_path and os.path.isdir(crashlog_path) and crashfile_match:
            crashlog_files = [s for s in os.listdir(crashlog_path)
                              if os.path.isfile(os.path.join(crashlog_path, s))
                              and crashfile_match in s]
            if crashlog_files:
                # we have crashlogs, get fullpath from the last one by time
                crashlog_files = self.__sort_files_by_date(crashlog_path,
                                                           crashlog_files)
                log_crash = os.path.join(crashlog_path, crashlog_files[-1])
        found_logs = []
        if os.path.isfile(log):
            found_logs.append({
                'title': 'xbmc.log',
                'path': log
            })
        if os.path.isfile(vpn_log):
            found_logs.append({
                'title': 'openvpn.log',
                'path': vpn_log
            })
        if log_crash and os.path.isfile(log_crash):
            found_logs.append({
                'title': 'crash.log',
                'path': log_crash
            })
        return found_logs

    def __sort_files_by_date(self, path, files):
        files.sort(key=lambda f: os.path.getmtime(os.path.join(path, f)))
        return files

    def __log(self, msg):
        import xbmc
        xbmc.log(u'%s: %s' % (ADDON_TITLE, msg))




if __name__ == '__main__':
    Uploader = LogUploader()
