import pygame

from element import element

def act():
	print("Estoy actuando")
		
#----------------------------------------------------------------------
#----------------------------------------------------------------------

class button(element):
	""" clase que representa un boton de la pantalla """
	def __init__(self,x,y,width,height,func = act):
		element.__init__(self,x,y,width,height)
		self.func=func
		self.state = "released"
		self.colores = {"released":(0,0,255),"hover":(0,255,0),"pressed":(255,0,0)}
	
	def __act__(self):
		self.func()
		
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
			self.state = "released"
		
		return element.update(self,press_char,unpress_char,mouse)

#----------------------------------------------------------------------
#----------------------------------------------------------------------		

class round_button(button):
	def in_me(self,x,y):
		center_x=self.x+self.width/2
		center_y=self.y+self.height/2

		return ((x-center_x)/(self.width/2.0))**2+((y-center_y)/(self.height/2.0))**2<=1

	def draw(self,screen):
		pygame.draw.ellipse(screen,self.colores[self.state],(self.x,self.y,self.width,self.height))



#----------------------------------------------------------------------
#----------------------------------------------------------------------
def move(x,y):
	print("Debo desplazarme: "+str(x)+" en X , "+str(y)+" en Y.") 		
class bar(element):
	def __init__(self,x,y,width,height,text = "Error",color = (0,0,0),background=(0,255,0),msg=move):
		element.__init__(self,x,y,width,height)
		
		self.msg=msg

		self.text = text		
		self.font = pygame.font.SysFont("def",height)

		self.font_color = color
		self.color = background

		self.prev_mouse_status = "Unclicked"
		self.status = "Unclicked"
		self.click = (-1,-1)


	def draw(self,screen):
		screen.fill(self.color,(self.x,self.y,self.width,self.height))
		rend = self.font.render(self.text,True,self.font_color)
		desp_y=(self.height-rend.get_height())/2
		screen.blit(rend,(self.x,self.y+desp_y))

	def update(self,press_char,unpress_char,mouse):
		if (mouse[2]==1):
			if (self.status == "Clicked"):
				desp_x = mouse[0] - self.click[0] 
				desp_y = mouse[1] - self.click[1] 
				self.msg(desp_x,desp_y)
			elif (self.prev_mouse_status == "Unclicked"):
				self.prev_mouse_status = "Clicked"
				if self.in_me(mouse[0],mouse[1]):
					self.status="Clicked"
					self.click=(mouse[0],mouse[1])
		else:			
			self.status = "Unclicked"
			self.prev_mouse_status = "Unclicked"
		
		
		return element.update(self,press_char,unpress_char,mouse)
		
		
		
