import pygame

from element import element

class button(element):
	""" clase que representa un boton de la pantalla """
	def __init__(self,x,y,width,height):
		element.__init__(self)
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.state = "released"
		self.colores = {"released":(0,0,255),"hover":(0,255,0),"pressed":(255,0,0)}
	
	def in_me(self,x,y):
		return (( self.x <= x ) and ( self.x + self.width >= x ) and ( self.y <= y ) and ( self.y + self.height >= y))

	def __act__(self):
		print "Estoy actuando!!!!"
		
	def draw(self,screen):
		screen.fill(self.colores[self.state],(self.x,self.y,self.width,self.height))

	def update(self,press_char,unpress_char,mouse):
		if self.in_me(mouse[0],mouse[1]):
			if(mouse[2]==1):			
				self.state = "pressed"
			else:
				if(self.state == "pressed"):
					self.__act__()
				self.state = "hover"
		else:
			if(self.state == "pressed"):
				self.__act__()
			self.state = "released"
		
class round_button(button):
	def in_me(self,x,y):
		center_x=self.x+self.width/2
		center_y=self.y+self.height/2

		return ((x-center_x)/(self.width/2.0))**2+((y-center_y)/(self.height/2.0))**2<=1

	def draw(self,screen):
		pygame.draw.ellipse(screen,self.colores[self.state],(self.x,self.y,self.width,self.height))
		
		
