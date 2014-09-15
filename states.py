import buttons
import prompts
import text
import views

def is_alive(object):
	return object.is_alive()

class state():
	def __init__(self):	
		self.elements=[]
		self.views=[]

	def draw(self,screen):
		for i in self.elements:
			i.draw(screen)

	def update(self,press_char,unpress_char,mouse):
		for i in self.elements:
			i.update(press_char,unpress_char,mouse)	
		self.elements = filter(is_alive,self.elements)		
	
		
						

class initial_screen(state):
	def __init__(self):
		state.__init__(self)

		self.elements+=[buttons.button(50,50,50,50)]
		self.elements+=[buttons.round_button(125,50,150,150)]
		self.elements+=[prompts.prompt(300,100)]
		self.elements+=[text.text_bar(300,300,100,20)]
		self.elements+=[prompts.input_prompt(50,200)]

