from element import element
from buttons import button,bar
from text import plain_text,text_bar
from constants import Constants

def none():
	pass

class prompt(element):
	""" clase de la ventanita que flota """

	def __init__(self,x,y,text="Mensaje default" , bar_text="Input" , function=none , width=Constants.prompt_default_width , height=Constants.prompt_default_height):
		""" prompt de la pantalla """
		element.__init__(self,x,y,width,height)
		self.alive = True
		self.function = function
		
		bx=Constants.prompt_title_x
		by=Constants.prompt_title_y
		bw=Constants.prompt_title_width
		bh=Constants.prompt_title_height

		tx=Constants.prompt_text_x
		ty=Constants.prompt_text_y
		tw=Constants.prompt_text_width
		th=Constants.prompt_text_height

		bux=Constants.prompt_button_x
		buy=Constants.prompt_button_y
		buw=Constants.prompt_button_width
		buh=Constants.prompt_button_height
	
		self.bar = bar(int(width*bx),int(height*by),int(width*bw),int(height*bh),bar_text,Constants.prompt_color_title,Constants.prompt_color_title_background,self.move)	
			
		self.text = plain_text(int(width*tx),int(height*ty),int(width*tw),int(height*th),text,Constants.prompt_text_pt,Constants.prompt_color_text)

		self.button = button(int(width*bux),int(height*buy),int(width*buw),int(height*buh),self.__die__)
		


	def move(self,desp_x,desp_y):
		if (self.x+desp_x >Constants.prompt_inf_x) and (self.x+self.width+desp_x < Constants.prompt_sup_x):
			self.set_x(self.x+desp_x)
		if (self.y+desp_y >Constants.prompt_inf_y) and (self.y+self.height+desp_y < Constants.prompt_sup_y):
			self.set_y(self.y+desp_y)


	def __die__(self):
		self.alive=False
		self.function()

	def draw(self,screen):
		screen.fill(Constants.prompt_color_text_background,(self.x,self.y,self.width,self.height))
		surface=screen.subsurface((self.x,self.y,self.width,self.height))
		self.button.draw(surface)
		self.text.draw(surface)
		self.bar.draw(surface)

	def update(self,press_char,unpress_char,mouse):
		new_mouse=(mouse[0]-self.x,mouse[1]-self.y,mouse[2],mouse[3],mouse[4])		
		self.button.update(press_char,unpress_char,new_mouse)
		self.bar.update(press_char,unpress_char,new_mouse)
		
		return self.alive,()


#-------------------------------------------------

def none_text(text):
	print text
	
class input_prompt(prompt):

	def __init__(self,x,y,text="Mensaje default" , bar_text="Input" , function=none_text , width=Constants.prompt_default_width , height=Constants.prompt_default_height):
		prompt.__init__(self,x,y,text,bar_text,function, width, height)
		
		tx=Constants.prompt_input_text_x
		ty=Constants.prompt_input_text_y
		tw=Constants.prompt_input_text_width
		th=Constants.prompt_input_text_height

		self.text_bar = text_bar(int(width*tx),int(height*ty),int(width*tw),int(height*th),"")	

	def update(self,press_char,unpress_char,mouse):
		new_mouse=(mouse[0]-self.x,mouse[1]-self.y,mouse[2],mouse[3],mouse[4])		
		self.text_bar.update(press_char,unpress_char,new_mouse)
		prompt.update(self,press_char,unpress_char,mouse)
		
		return self.alive,()

	def __die__(self):
		self.alive=False
		self.function(self.text_bar.get_text())

	def draw(self,screen):
		prompt.draw(self,screen)
		surface=screen.subsurface((self.x,self.y,self.width,self.height))
		self.text_bar.draw(surface)
