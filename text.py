
from element import element
import pygame

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

	def draw(self,screen):
		self.cursor+=1
		self.cursor%=20
		text = ""
		if (self.cursor < 10):
			text = self.text[0:self.pos]+'|'+self.text[self.pos:(len(self.text)-1)]
		else:
			text = self.text
		
		
				
		rend = self.font.render(text,True,self.color)
		screen.blit(rend,(self.x,self.y,self.width,self.height))
				
