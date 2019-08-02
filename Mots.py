class Mots:     
	def __init__(self, mot, posinit, posactu):
		self.mot=mot
		self.posint = [posinit]
		self.posactu=posactu

		
	def PosInt(self,j,i):
		self.posint.append((j,i))
	
	def checkPosInt(self,j,i):
		if (self.posactu[0]+j,self.posactu[1]+i)in self.posint :
			return False
		else : 
			return True
		
	def checkIn(self):
		
		for word in text :
			if self.mot in word :
				return True
	def checkIs(self):
		for word in text :
			if self.mot is word :
				return True
				
	def checkForAdd(self, chiffre):
		if chiffre==1:
			if (self.posactu[0]>0 and self.posactu[1]>0 and self.checkPosInt(-1,-1)):
				return True
			else :
				return False
		if chiffre==2:
			if (self.posactu[0]>0 and self.checkPosInt(-1,0)):
				return True 
			else :
				return False
		if chiffre==3:
			if(self.posactu[0]>0 and self.posactu[1]<3 and self.checkPosInt(-1,1)):
				return True 
			else :
				return False
		if chiffre==4:
			if(self.posactu[1]>0 and self.checkPosInt(0,-1)):
				return True 
			else :
				return False
		if chiffre==5:
			if(self.posactu[1]<3 and self.checkPosInt(0,1)):
				return True 
			else :
				return False
		if chiffre==6:
			if(self.posactu[0]<3 and self.posactu[1]>0 and self.checkPosInt(1,-1)):
				return True 
			else :
				return False
		if chiffre==7:
			if (self.posactu[0]<3 and self.checkPosInt(1,0)):
				return True 
			else :
				return False
		if chiffre==8:
			if(self.posactu[0]<3 and self.posactu[1]<3 and self.checkPosInt(1,1)):
				return True 
			else :
				return False
		
		