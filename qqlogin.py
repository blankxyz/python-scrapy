import qqlib
import urllib

qqCode = 3607609
qqPwd = 'baiyuling26'

qq = qqlib.QQ(qqCode, qqPwd)
qq.login()

initinal_page = 'user.qzone.qq.com/3607609'

wp = urllib.urlopen(initinal_page)
print ('start download...')
content = wp.read()