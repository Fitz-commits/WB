from Mots import Mots

with open('data.txt', 'r') as mon_fichier:
        texte = mon_fichier.read()
mon_fichier.close()

text = texte.split("\n")

wb = [[], [], [], []]
tl = []
tle = []
thl = []
thle=[]
fl =[]
fle=[]
fil=[]
file=[]
sl=[]
sle=[]
sel=[]
sele=[]
el=[]
ele=[]
nl=[]
nle=[]
tel=[]
tele=[]


def encodage():
	for j in range(4):
		for i in range(4):
			mdpe = input("Lettre : ")
			wb[j].append(mdpe)

def two_letter_words():
	for j in range(4):
		for i in range(4):
			if j>0 and i >0 :
				tl.append(Mots(wb[j][i]+wb[j-1][i-1],(j,i),(j-1,i-1)))
			if j>0 :
				tl.append(Mots(wb[j][i]+wb[j-1][i],(j,i),(j-1,i)))
			if j>0 and i<3 :
				tl.append(Mots(wb[j][i]+wb[j-1][i+1],(j,i),(j-1,i+1)))
			if i>0 :
				tl.append(Mots(wb[j][i]+wb[j][i-1],(j,i),(j,i-1)))
			if i<3 :
				tl.append(Mots(wb[j][i]+wb[j][i+1],(j,i),(j,i+1)))
			if i>0 and j<3:
				tl.append(Mots(wb[j][i]+wb[j+1][i-1],(j,i),(j+1,i-1)))
			if j<3:
				tl.append(Mots(wb[j][i]+wb[j+1][i],(j,i),(j+1,i)))
			if i<3 and j<3:
				tl.append(Mots(wb[j][i]+wb[j+1][i+1],(j,i),(j+1,i+1)))

	for object in tl :
		for e in text:
			if object.mot in e and object.mot[0]==e[0] :
				tle.append(object)
				break
				
				
def three_letter_words():
	k=0
	for object in tle:
		if object.checkForAdd(1):
			thl.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				thl[k-1].posint.append((x,y))
		if object.checkForAdd(2):
			thl.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1])))	
			k+=1
			for (x,y) in object.posint:
				thl[k-1].posint.append((x,y))
				
		if object.checkForAdd(3):
			thl.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				thl[k-1].posint.append((x,y))
				
		if object.checkForAdd(4):
			thl.append(Mots(object.mot+wb[object.posactu[0]][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0],object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				thl[k-1].posint.append((x,y))
				
		if object.checkForAdd(5):
			thl.append(Mots(object.mot+wb[object.posactu[0]][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0],object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				thl[k-1].posint.append((x,y))
				
		if object.checkForAdd(6):
			thl.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				thl[k-1].posint.append((x,y))
			
		if object.checkForAdd(7):
			thl.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1])))	
			k+=1
			for (x,y) in object.posint:
				thl[k-1].posint.append((x,y))
				
		if object.checkForAdd(8):
			thl.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				thl[k-1].posint.append((x,y))
	for object in thl :
		for e in text:
			if object.mot in e :
				thle.append(object)
				break


def four_letter_words():
	k=0
	for object in thle:
		if object.checkForAdd(1):
			fl.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				fl[k-1].posint.append((x,y))
		if object.checkForAdd(2):
			fl.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1])))	
			k+=1
			for (x,y) in object.posint:
				fl[k-1].posint.append((x,y))
				
		if object.checkForAdd(3):
			fl.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				fl[k-1].posint.append((x,y))
				
		if object.checkForAdd(4):
			fl.append(Mots(object.mot+wb[object.posactu[0]][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0],object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				fl[k-1].posint.append((x,y))
				
		if object.checkForAdd(5):
			fl.append(Mots(object.mot+wb[object.posactu[0]][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0],object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				fl[k-1].posint.append((x,y))
				
		if object.checkForAdd(6):
			fl.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				fl[k-1].posint.append((x,y))
			
		if object.checkForAdd(7):
			fl.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1])))	
			k+=1
			for (x,y) in object.posint:
				fl[k-1].posint.append((x,y))
				
		if object.checkForAdd(8):
			fl.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				fl[k-1].posint.append((x,y))
	for object in fl :
		for e in text:
			if object.mot in e :
				fle.append(object)
				break

def five_letter_words():
	k=0
	for object in fle:
		if object.checkForAdd(1):
			fil.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				fil[k-1].posint.append((x,y))
		if object.checkForAdd(2):
			fil.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1])))	
			k+=1
			for (x,y) in object.posint:
				fil[k-1].posint.append((x,y))
				
		if object.checkForAdd(3):
			fil.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				fil[k-1].posint.append((x,y))
				
		if object.checkForAdd(4):
			fil.append(Mots(object.mot+wb[object.posactu[0]][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0],object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				fil[k-1].posint.append((x,y))
				
		if object.checkForAdd(5):
			fil.append(Mots(object.mot+wb[object.posactu[0]][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0],object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				fil[k-1].posint.append((x,y))
				
		if object.checkForAdd(6):
			fil.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				fil[k-1].posint.append((x,y))
			
		if object.checkForAdd(7):
			fil.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1])))	
			k+=1
			for (x,y) in object.posint:
				fil[k-1].posint.append((x,y))
				
		if object.checkForAdd(8):
			fil.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				fil[k-1].posint.append((x,y))
	for object in fil :
		for e in text:
			if object.mot in e :
				file.append(object)
				break
def six_letter_words():
	k=0
	for object in fle:
		if object.checkForAdd(1):
			sl.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				sl[k-1].posint.append((x,y))
		if object.checkForAdd(2):
			sl.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1])))	
			k+=1
			for (x,y) in object.posint:
				sl[k-1].posint.append((x,y))
				
		if object.checkForAdd(3):
			sl.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				sl[k-1].posint.append((x,y))
				
		if object.checkForAdd(4):
			sl.append(Mots(object.mot+wb[object.posactu[0]][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0],object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				sl[k-1].posint.append((x,y))
				
		if object.checkForAdd(5):
			sl.append(Mots(object.mot+wb[object.posactu[0]][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0],object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				sl[k-1].posint.append((x,y))
				
		if object.checkForAdd(6):
			sl.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				sl[k-1].posint.append((x,y))
			
		if object.checkForAdd(7):
			sl.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1])))	
			k+=1
			for (x,y) in object.posint:
				sl[k-1].posint.append((x,y))
				
		if object.checkForAdd(8):
			sl.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				sl[k-1].posint.append((x,y))
	for object in sl :
		for e in text:
			if object.mot in e :
				sle.append(object)
				break
def seven_letter_words():
	k=0
	for object in sle:
		if object.checkForAdd(1):
			sel.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				sel[k-1].posint.append((x,y))
		if object.checkForAdd(2):
			sel.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1])))	
			k+=1
			for (x,y) in object.posint:
				sel[k-1].posint.append((x,y))
				
		if object.checkForAdd(3):
			sel.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				sel[k-1].posint.append((x,y))
				
		if object.checkForAdd(4):
			sel.append(Mots(object.mot+wb[object.posactu[0]][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0],object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				sel[k-1].posint.append((x,y))
				
		if object.checkForAdd(5):
			sel.append(Mots(object.mot+wb[object.posactu[0]][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0],object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				sel[k-1].posint.append((x,y))
				
		if object.checkForAdd(6):
			sel.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				sel[k-1].posint.append((x,y))
			
		if object.checkForAdd(7):
			sel.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1])))	
			k+=1
			for (x,y) in object.posint:
				sel[k-1].posint.append((x,y))
				
		if object.checkForAdd(8):
			sel.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				sel[k-1].posint.append((x,y))
	for object in sel :
		for e in text:
			if object.mot in e :
				sele.append(object)
				break
def eight_letter_words():
	k=0
	for object in sele:
		if object.checkForAdd(1):
			el.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				el[k-1].posint.append((x,y))
		if object.checkForAdd(2):
			el.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1])))	
			k+=1
			for (x,y) in object.posint:
				el[k-1].posint.append((x,y))
				
		if object.checkForAdd(3):
			el.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				el[k-1].posint.append((x,y))
				
		if object.checkForAdd(4):
			el.append(Mots(object.mot+wb[object.posactu[0]][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0],object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				el[k-1].posint.append((x,y))
				
		if object.checkForAdd(5):
			el.append(Mots(object.mot+wb[object.posactu[0]][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0],object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				el[k-1].posint.append((x,y))
				
		if object.checkForAdd(6):
			el.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				el[k-1].posint.append((x,y))
			
		if object.checkForAdd(7):
			el.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1])))	
			k+=1
			for (x,y) in object.posint:
				el[k-1].posint.append((x,y))
				
		if object.checkForAdd(8):
			el.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				el[k-1].posint.append((x,y))
	for object in el :
		for e in text:
			if object.mot in e :
				ele.append(object)
				break
def nine_letter_words():
	k=0
	for object in ele:
		if object.checkForAdd(1):
			nl.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				nl[k-1].posint.append((x,y))
		if object.checkForAdd(2):
			nl.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1])))	
			k+=1
			for (x,y) in object.posint:
				nl[k-1].posint.append((x,y))
				
		if object.checkForAdd(3):
			nl.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				nl[k-1].posint.append((x,y))
				
		if object.checkForAdd(4):
			nl.append(Mots(object.mot+wb[object.posactu[0]][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0],object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				nl[k-1].posint.append((x,y))
				
		if object.checkForAdd(5):
			nl.append(Mots(object.mot+wb[object.posactu[0]][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0],object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				nl[k-1].posint.append((x,y))
				
		if object.checkForAdd(6):
			nl.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				nl[k-1].posint.append((x,y))
			
		if object.checkForAdd(7):
			nl.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1])))	
			k+=1
			for (x,y) in object.posint:
				nl[k-1].posint.append((x,y))
				
		if object.checkForAdd(8):
			nl.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				nl[k-1].posint.append((x,y))
	for object in nl :
		for e in text:
			if object.mot in e :
				nle.append(object)
				break
def ten_letter_words():
	k=0
	for object in nle:
		if object.checkForAdd(1):
			tel.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				tel[k-1].posint.append((x,y))
		if object.checkForAdd(2):
			tel.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1])))	
			k+=1
			for (x,y) in object.posint:
				tel[k-1].posint.append((x,y))
				
		if object.checkForAdd(3):
			tel.append(Mots(object.mot+wb[object.posactu[0]-1][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0]-1,object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				tel[k-1].posint.append((x,y))
				
		if object.checkForAdd(4):
			tel.append(Mots(object.mot+wb[object.posactu[0]][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0],object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				tel[k-1].posint.append((x,y))
				
		if object.checkForAdd(5):
			tel.append(Mots(object.mot+wb[object.posactu[0]][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0],object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				tel[k-1].posint.append((x,y))
				
		if object.checkForAdd(6):
			tel.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]-1],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1]-1)))	
			k+=1
			for (x,y) in object.posint:
				tel[k-1].posint.append((x,y))
			
		if object.checkForAdd(7):
			tel.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1])))	
			k+=1
			for (x,y) in object.posint:
				tel[k-1].posint.append((x,y))
				
		if object.checkForAdd(8):
			tel.append(Mots(object.mot+wb[object.posactu[0]+1][object.posactu[1]+1],(object.posactu[0],object.posactu[1]),(object.posactu[0]+1,object.posactu[1]+1)))	
			k+=1
			for (x,y) in object.posint:
				tel[k-1].posint.append((x,y))
	for object in tel :
		for e in text:
			if object.mot in e :
				tele.append(object)
				break
encodage()
two_letter_words()
three_letter_words()
four_letter_words()
five_letter_words()
six_letter_words()
seven_letter_words()
eight_letter_words()
nine_letter_words()
print("5 lettres : ")
for e in file:
	if e.mot in text:
		print(e.mot)
		print(e.posint)
print("6 lettres: ")
for e in sle:
	if e.mot in text:
		print(e.mot)
		print(e.posint)
print("7 lettres:")
for e in sele:
	if e.mot in text:
		print(e.mot)
		print(e.posint)
print("8 lettres:")
for e in ele:
	if e.mot in text:
		print(e.mot)
		print(e.posint)
print("9 lettres:")
for e in nle:
	if e.mot in text:
		print(e.mot)
		print(e.posint)	
print("10 lettres:")
for e in tele:
	if e.mot in text:
		print(e.mot)
		print(e.posint)		
        
		
	
			
			
				
				
				
	

# définir un champs de proximité en partant de deux lettres v
#tant que str in dic continue 
#interdire les position déjà utilisée v
#interdire les out of bornes v
# mots de 3 lettres ?
#Passage en orienté objet v

