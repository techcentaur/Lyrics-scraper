#lyrics scraped from the web, contains singers names and chorus number in [] form.
#this file removes the singers name and thus gives clear data

import re

def clear_it():
	filename = input("Enter the data file name: ")
	ch = int(input("Enter 1->to overwrite, 0->to write in new file: "))
	f1 = open('data.txt','r+')
	raw = f1.read()
	raw=raw.replace('[','<')
	raw=raw.replace(']','>')
	raw=re.sub('<[^>]+>','',raw)

	if(ch==1):
		f1.write(raw)
	else:
		f2 = open("new_clear_"+filename,'w')
		f2.write(raw)
		f2.close()

	f1.close()

if __name__ == "__main__":
    clear_it()

#this code is contributed by 'techcentaur'