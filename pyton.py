from Tkinter import *
from tkFileDialog import *
import os
import omdb
import json

movie_path=""
class Application(Frame):
	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()
	def create_widgets(self):
		self.label = Label(self, text = "Browse to your movie folder")
		self.label.grid()
		self.button = Button(self, text = "Browse", command = self.loadtemplate)
		self.button.grid()

   	def loadtemplate(self): 
        	movie_path = askdirectory()
		print movie_path
		
        	
root = Tk()

root.title("Get Ratings")
root.geometry("400x200")

app = Application(root)

root.mainloop()

os.system(os.path.join("ls ",movie_path,">pyton.txt"))
print os.path.join("ls ",movie_path,">pyton.txt")
file_path = os.path.join(movie_path,"/pyton.txt")
print file_path
with open(file_path) as f:
	content = f.readlines()

file = open(file_path, "w")

def title_search(movie):
	print movie
	my_dict = omdb.get(title=movie, fullplot=True, tomatoes=True)
	if my_dict.get('imdb_rating'):
		print my_dict.get('imdb_rating')
	else:
		print 'ankit'
	return

def replace_dot(title):
	i=0
	final=""
	while i<len(title):
		if title[i]==".":
			final+=" "
		else:
			final+=title[i]	 
		i+=1
	#print final	
	if len(final) != 0:
		title_search(final)
	return

def trim(line):
	title=""
	i=0
	while line[i] == " " or line[i] == "-":
		i+=1

	if line[i] == '[' or line[i] == '(' or line[i]=='{':
		while i<len(line) and (line[i] != ']' and line[i] != ')' and line[i]!='}') :
			i+=1
		i+=1
	
	while line[i] == " " or line[i] == "-":
		i+=1
	
	while i<len(line) and (line[i] != '(' and line[i] != '[' and line[i] != '{') and line[i] != '\n' :
		
		year=0;
		while i<len(line) and (ord(line[i])>=ord('0') and ord(line[i])<=ord('9')):
			year=year*10+int(line[i])			
			i+=1
		if (year>=1950 and year<=2017) or year==1080 or year==720 or year==480 :
			break
		if year!=0:
			title+=str(year)
		
		if line[i]=='.':
			temp=line[i:i+4]
			if temp==".mkv" or temp==".avi" or temp==".mp4": 
				break
		title += line[i]
		i+=1
	
	replace_dot(title)
	
	return

for line in content:
	print line
	trim(line)	

file.close()
