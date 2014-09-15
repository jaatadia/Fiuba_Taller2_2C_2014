import buttons
import prompts
import text
import state_parser

def is_alive(object):
	return object.is_alive()

class state():
	def __init__(self):	
		self.elements=[]
		self.views=[]
		self.next=self

	def draw(self,screen):
		for i in self.elements:
			i.draw(screen)

	def update(self,press_char,unpress_char,mouse):
		for i in self.elements:
			i.update(press_char,unpress_char,mouse)	
		self.elements = filter(is_alive,self.elements)		
	
	def __set_next_state__(self,state):
		self.next = state_parser.state_parser(state)

	def get_next_state(self):
		return self.next
	
	def add(self,element):
		self.elements+=[element]
		

class initial_screen(state):
	def __init__(self):
		state.__init__(self)

		self.add(buttons.button(50,50,50,50,self.__next__))
		self.add(buttons.round_button(125,50,150,150))
		self.add(prompts.prompt(300,100))
		self.add(text.text_bar(300,300,100,20))
		self.add(prompts.input_prompt(50,200))

	def __next__(self):
		self.next = state_parser.state_parser("./states/prueba.sts")
						

class second_screen(state):
	def __init__(self):
		state.__init__(self)

		self.add(text.plain_text(100,100,200,200,"esto es un texto que te parece?",20,(0,255,255)))

