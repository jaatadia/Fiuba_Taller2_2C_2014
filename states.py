import buttons

class state():
	def __init__(self):	
		self.elements=[]

	def draw(self,screen):
		for i in self.elements:
			i.draw(screen)

	def update(self,press_char,unpress_char,mouse):
		for i in self.elements:
			i.update(press_char,unpress_char,mouse)

class initial_screen(state):
	def __init__(self):
		state.__init__(self)
		self.elements=self.elements+[buttons.button(50,50,50,50)]
		self.elements=self.elements+[buttons.round_button(125,50,150,150)]
		
