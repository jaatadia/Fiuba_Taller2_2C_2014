
from element import element
import pygame


class plain_text(element):
	""" texto plano """
	def __init__(self,x,y,width,height,text = "Hola",initial=20,color = (0,0,0)):
		element.__init__(self,x,y,width,height)
		self.text = text
		self.color = color
		self.__segment_text__(initial)

	def __segment_text__(self,initial):
		pt=initial
		found=False
		while (not found and pt>0):
			vector = []
			total_height=0
			i=0
			j=0
			font = pygame.font.SysFont("def",pt)
			while (j<=len(self.text)):
				width,height=font.size(self.text[i:j])
				if (width>self.width):
					vector += [self.text[i:j-1]]
					i = j-1
					total_height += height
				j += 1

			if (self.text[i:j]<>""):
				vector += [self.text[i:j]]
				width,height=font.size(self.text[i:j])
				total_height += height
			
			if(total_height<=self.height):
				found=True
			else:
				pt-=1

		self.font = font
		self.text = tuple(vector)


	def draw(self,screen):
		""" dibuja el objeto """
		start_y = self.y
		for text in self.text:		
			rend = self.font.render(text,True,self.color)
			screen.blit(rend,(self.x,start_y))
			start_y += rend.get_height()


class text_bar(element):
	""" barrita de texto """
	def __init__(self,x,y,width,height,text = "Hola"):
		element.__init__(self,x,y,width,height)
		
		self.text = text
		self.pos = len(text)
		self.cursor = 0

		self.chars_on_display = 10
		self.font = pygame.font.SysFont("def",height)
		self.color = (255,255,255)
		
		self.__set_events__()

	def __get_init_final_positions__(self):
		""" calcula la primer y la ultima posicion a mostrar """ 
		#si entra todo => perfecto
		temp_text=self.text+' '
		
		if (self.font.size(temp_text)[0]<=self.width):
			return 0,len(temp_text)

		#si entra desde 0 hasta la posicion => tengo que encontrar a partir de que posicion deja de verse el principio
		if(self.font.size(temp_text[0:self.pos+1])[0]<=self.width):
			i = self.pos+1
			found = False
			while (i<=len(temp_text)) and  (not found):
				width,height=self.font.size(temp_text[0:i])			
				if(width>=self.width):
					found = True
					i-=1
				else:
					i+=1
			return 0,i
			
		#sino tengo que encontrar hasta que posicion anterior de la actual entra
		i = self.pos+1
		found = False
		while (i>=0) and  (not found):
			width,height=self.font.size(temp_text[i:self.pos+1])			
			if(width>=self.width):
				found = True
				i+=1
			else:
				i-=1

		return i,self.pos+1

	def draw(self,screen):
		""" dibuja el objeto """
		self.cursor+=1
		self.cursor%=100

		ini,end = self.__get_init_final_positions__()
		rend = self.font.render((self.text+' ')[ini:end],True,self.color)		
		desp_y=(self.height-rend.get_height())/2
		if self.cursor < 50:
			width,height=self.font.size(self.text[ini:self.pos])			
			p1=(width,0)
			p2=(width,height)
			pygame.draw.line(rend,self.color,p1,p2,2)		
		screen.fill((230,0,230),(self.x,self.y,self.width,self.height))
		screen.blit(rend,(self.x,self.y+desp_y),(0,0,self.width,self.height))

	def __recalc_pos__(self,x,y):
		ini,end=self.__get_init_final_positions__()
		found = False
		for i in range (ini,end):
			width,height=self.font.size(self.text[ini:i+1])
			if (x<width):
				found = True
				width2,height2=self.font.size(self.text[i:i+1])
				if (x<=width-width2/2.0):
					self.pos=i
				else:
					self.pos=i+1
				break
		if not found:
			self.pos=len(self.text)
	
	def __set_events__(self):
		self.events={}
		self.events["ENTER"]=self.__enter__
		self.events["UP"]=self.__up__
		self.events["DOWN"]=self.__down__
		self.events["LEFT"]=self.__left__
		self.events["RIGHT"]=self.__right__
		self.events["DEL"]=self.__del__
		self.events["BACK"]=self.__back__

	def __enter__(self):
		pass

	def __up__(self):
		pass

	def __down__(self):
		pass

	def __left__(self):
		if (self.pos-1>=0):
			self.pos-=1

	def __right__(self):
		if (self.pos+1<=len(self.text)):
			self.pos+=1

	def __back__(self):
		if (self.pos-1>=0):
			self.text=self.text[0:self.pos-1]+self.text[self.pos:len(self.text)]
			self.pos-=1

	def __del__(self):
		self.text=self.text[0:self.pos]+self.text[self.pos+1:len(self.text)]

	def __text__(self):
		self.text=self.text[0:self.pos]+self.char+self.text[self.pos:len(self.text)]
		self.pos+=1



	def update(self,press_char,unpress_char,mouse):
		for i in press_char:		
			self.char=i
			self.events.get(i,self.__text__)()
		if (mouse[2]==1) and (self.in_me(mouse[0],mouse[1])):
			self.__recalc_pos__(mouse[0]-self.x,mouse[1]-self.y)

		return element.update(self,press_char,unpress_char,mouse)
		
