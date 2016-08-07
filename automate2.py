#!/usr/bin/python3.4
# -*-coding:UTF-8 -*
'''
Created on 01 08 2016
 
@author: Assamba 
'''
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

import urllib.request as ur
import re
import json #we will convert links into JSON format
#this class has to pull all link conatained in a web page
class Automate:
	ur = __import__('urllib.request')
	re = __import__('re')
	def __init__(self, url_list): #txt file containing urls to open
		self.url_list = url_list
		self.link = ""
		self.pathlink = ""
		
		#our list of media for JSON format
		medialist = {};
		medialist["website"] = self.url_list;
		medialist["links"] = [];
		
		#opening files
		f = open(currentdir+'/web_sourcecode.txt', 'w+');
		f2 = open(currentdir+'/media_links.csv', 'w+');
		#print('web site;media link', file=f2);
			
		lines_list = list([self.url_list]); #making a list (array of links)
		
		for links in lines_list:#retrieving every links in the list
			#print(links);
			try: 
				req = ur.Request(links.rstrip(), headers={'User-Agent': "Mozilla/5.0' (X11; Windows x86_64) Chrome/12.0.742.112"});
				self.s = ur.urlopen(req);
				self.sl = self.s.read();
				print(self.sl, file=f);
				f.seek(0,0);#restart to the beginning
				self.lines = f.read();
				if self.lines.find('<a href="') != -1:
					self.expression = r"<a href=\"";
					array = [m.start() for m in re.finditer(self.expression, self.lines)]
					#print(array);
					for l in range(0, len(array)):
						j = array[l];
						while (self.lines[j+9] != '"'):
							self.link += self.lines[j+9];
							j = j+1;
						if self.link.lower().find('/media')!=-1 or self.link.lower().find('/multimedia')!=-1 or self.link.lower().find('/tv')!=-1 or self.link.lower().find('/television')!=-1 or self.link.lower().find('/serie')!=-1 or self.link.lower().find('_serie')!=-1 or self.link.lower().find('serie_')!=-1 or self.link.lower().find('/game')!=-1 or self.link.lower().find('_game')!=-1 or self.link.lower().find('game_')!=-1 or self.link.lower().find('/movie')!=-1 or self.link.lower().find('_movie')!=-1 or self.link.lower().find('movie_')!=-1 or self.link.lower().find('/categories')!=-1 or self.link.lower().find('/shows') !=-1 or self.link.lower().find('/video')!=-1 or self.link.lower().find('/film')!=-1 or self.link.lower().find('_tv')!=-1 or self.link.lower().find('news')!=-1 or self.link.lower().find('tv_')!=-1 or self.link.lower().find('live')!=-1 or self.link.lower().find('_live')!=-1 or self.link.lower().find('live_')!=-1 or self.link.lower().find('radio')!=-1 or self.link.lower().find('/playlist')!=-1 or self.link.lower().find('/game')!=-1or self.link.lower().find('podcast')!=-1 or self.link.lower().find('webinar')!=-1 or self.link.lower().find('animation')!=-1 or self.link.lower().find('documentarie')!=-1 or self.link.lower().find('/caf')!=-1:
							if self.link.find('http://') == -1 and self.link.find('https://') == -1:
								self.link = self.url_list + self.link;
							if self.link.find('../')!=-1:
								self.link = self.link.replace('../', '/');
							if self.link.rstrip().endswith('/'): #xxxxx/ is the same thing as xxxx. so we remove the last / in an url.
								self.link = self.link.rstrip()[:-1];
								
							#adding to JSON object if not exists
							if self.link.rstrip() not in medialist["links"]:
								if self.url_list in self.link:
									medialist["links"].append(self.link.rstrip());
									print(self.link.rstrip());
							
						if self.link.rstrip()!='#':
							if self.link.find('http://') == -1 and self.link.find('https://') == -1:
								self.link = self.url_list + self.link;
							if self.link.find('../')!=-1:
								self.link = self.link.replace('../', '/');
							#print(self.link.rstrip().replace("//", "/"), file=fi)
							if self.link.rstrip().endswith('/'): #xxxxx/ is the same thing as xxxx. so we remove the last / in an url.
								self.link = self.link.rstrip()[:-1];
							if self.link.rstrip() not in lines_list: #adding a link to the list if not exist
								if self.url_list.rstrip() in self.link.rstrip():
									lines_list.append(self.link.rstrip());
									#print(self.url_list +';' + self.link.rstrip(), file=f2)
									#print('-----'+self.link.rstrip());
						self.link = "";
				else: #not href found= not link found in that page
					print ('false: not link found in that page ');
			except (ur.HTTPError, ValueError, ur.URLError) as e:
				pass
		#we have to store that list into a file called json_feed.json
		with open('json_feed.json', 'w', encoding='utf-8') as fjson:
			json.dump(medialist, fjson, indent=4)
		#print(json.dumps(medialist)) #printing the medialist in JSON format
		f.close();
		#fi.close();
		f2.close();
