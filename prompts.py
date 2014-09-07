from element import element
from buttons import button


class prompt(element):
	""" clase de la ventanita que flota """
	def __init__(self,x,y,width,height,text="Mensaje default"):
		""" prompt de la pantalla """
		element.__init__(self,x,y,width,height)		
		self.text = text
		self.button = button(int(width*2/6.0+0.5),int(height*4/6.0+0.5),int(width*2/6.0+0.5),int(height/6.0+0.5))


	def draw(self,screen):
		screen.fill((200,200,200),(self.x,self.y,self.width,self.height))
		surface=screen.subsurface((self.x,self.y,self.width,self.height))
		self.button.draw(surface)

	def update(self,press_char,unpress_char,mouse):
		new_mouse=(mouse[0]-self.x,mouse[1]-self.y,mouse[2],mouse[3],mouse[4])		
		self.button.update(press_char,unpress_char,new_mouse)
	
	
		
