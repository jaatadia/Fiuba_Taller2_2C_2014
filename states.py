import buttons
import prompts
import text

class state():
	def __init__(self):	
		self.elements=[]

	def draw(self,screen):
		for i in self.elements:
			i.draw(screen)

	def update(self,press_char,unpress_char,mouse):
		dead_list=[]
		new_list=[]
		for i in self.elements:
			state,elements=i.update(press_char,unpress_char,mouse)
			new_list+=list(elements) 

			if(not state):
				dead_list+=[i]

		for i in dead_list:
			self.elements.remove(i)
		self.elements+=new_list
				

class initial_screen(state):
	def __init__(self):
		state.__init__(self)
		self.elements+=[buttons.button(50,50,50,50)]
		self.elements+=[buttons.round_button(125,50,150,150)]
		self.elements+=[text.text_bar(300,300,100,20)]
		self.elements+=[prompts.prompt(300,100,200,100)]
		
