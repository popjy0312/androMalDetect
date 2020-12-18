#
#   dataset from AndroZoo
#   https://androzoo.uni.lu/
#   https://orbilu.uni.lu/bitstream/10993/27396/1/androzoo.pdf
#
#   contact: androzoo@uni.lu
#

import os
from consts import APIKEY, DATASET_CNT

dataLists = open('./lists.csv','rb')
dataLists.readline()
#b'sha256,sha1,md5,dex_date,apk_size,pkg_name,vercode,vt_detection,vt_scan_date,dex_size,markets\n'
for i in range(DATASET_CNT):
    print(i)
#b'000002B63FAD4B030787F6DE4081DC1E12325026EB7DDAD146C52F5F4FC2D525,DD723B32EDD9F70AADBD66846621967157DF9BD4,985E601C17F0A9346590AE92A5AD664E,1980-01-01 00:00:00,4300370,"com.deperu.sitiosarequipa",10000,0,2017-12-03 06:50:28,4211104,play.google.com\n'
    t = dataLists.readline()
    t = str(t).split(',')
    cmd = 'curl -O --remote-header-name -G -d apikey={0} -d sha256={1} https://androzoo.uni.lu/api/download'.format(APIKEY, str(t[0])[2:])
    os.system(cmd)