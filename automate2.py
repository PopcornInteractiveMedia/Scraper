import urllib.request as ur
import re
#this class has to pull all link conatained in a web page
class Automate:
	ur = __import__('urllib.request')
	re = __import__('re')
	def __init__(self, url_list): #txt file containing urls to open
		self.url_list = url_list
		self.link = ""
		self.pathlink = ""
		
		#opening files
		f = open('C:/Users/pasquierase/Desktop/Projet UpWork AI/SIRI/web_sourcecode.txt', 'w+');
		f2 = open('C:/Users/pasquierase/Desktop/Projet UpWork AI/SIRI/media_links.csv', 'w+');
		print('web site;media link', file=f2);
		#fi = open(self.url_list, 'a+');
		#header of the csv file
		#fi.seek(0,0);
		#with open(self.url_list) as fi:
		#	lines_list = fi.read().splitlines(); #making a list (array of links)
			
		lines_list = list([self.url_list]); #making a list (array of links)
		
		for links in lines_list:#retrieving every links in the list
			print(links);
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
						if self.link.lower().find('/media')!=-1 or self.link.lower().find('/multimedia')!=-1 or self.link.lower().find('/tv')!=-1 or self.link.lower().find('/movie')!=-1 or self.link.lower().find('/categories')!=-1 or self.link.lower().find('/shows') !=-1 or self.link.lower().find('/video')!=-1 or self.link.lower().find('/film')!=-1 or self.link.lower().find('_tv')!=-1 or self.link.lower().find('news')!=-1 or self.link.lower().find('tv_')!=-1 or self.link.lower().find('live')!=-1 or self.link.lower().find('_live')!=-1 or self.link.lower().find('live_')!=-1 or self.link.lower().find('radio')!=-1 or self.link.lower().find('/playlist')!=-1 or self.link.lower().find('/game')!=-1or self.link.lower().find('podcast')!=-1 or self.link.lower().find('webinar')!=-1 or self.link.lower().find('animation')!=-1 or self.link.lower().find('documentarie')!=-1 or self.link.lower().find('/caf')!=-1:
							if self.link.find('http://') == -1:
								self.link = self.url_list + self.link;
							if self.link.find('../')!=-1:
								self.link = self.link.replace('../', '/');
						if self.link.rstrip()!='#':
							#print(self.link.rstrip().replace("//", "/"), file=fi)
							if self.link.rstrip().endswith('/'): #xxxxx/ is the same thing as xxxx. so we remove the last / in an url.
								self.link = self.link.rstrip()[:-1];
							if self.link.rstrip() not in lines_list: #adding a link to the list if not exist
								lines_list.append(self.link.rstrip());
								print(self.url_list +';' + self.link.rstrip(), file=f2)
						self.link = ""
				else: #not href found= not link found in that page
					print ('false: not link found in that page ');
			except (ur.HTTPError, ValueError, ur.URLError) as e:
				pass
			
		f.close();
		#fi.close();
		f2.close();
		
def main():
	aut = Automate('http://www.wwitv.com');
	
if  __name__ =='__main__':
	main()