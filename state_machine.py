import pygame,states

class State_machine():
	def __init__(self,width=800,height=600):
		""" inicializo las variables """
		self.width = width
		self.height = height
		self.window_text = "Taller2"
		
		self.screen = pygame.display.set_mode((self.width,self.height),pygame.DOUBLEBUF)
		pygame.display.set_caption(self.window_text)

		self.activo = states.initial_screen()

	def update(self,press_char,unpress_char,mouse):
		""" le dice al estado activo que se update """
		self.activo.update(press_char,unpress_char,mouse)

	def draw(self):
		""" le dice al estado activo que se dibuje """
		self.screen.fill((0,0,0))
		self.activo.draw(self.screen)
		pygame.display.flip()
		
