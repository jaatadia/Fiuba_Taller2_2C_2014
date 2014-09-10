import pygame,states
from constants import Constants

class State_machine():
	def __init__(self,width,height,window_text):
		""" inicializo las variables """
		self.width = width
		self.height = height
		self.window_text = window_text
		
		self.screen = pygame.display.set_mode((self.width,self.height),pygame.DOUBLEBUF)
		pygame.display.set_caption(self.window_text)

		self.activo = states.initial_screen()

	def update(self,press_char,unpress_char,mouse):
		""" le dice al estado activo que se update """
		self.activo.update(press_char,unpress_char,mouse)

	def draw(self):
		""" le dice al estado activo que se dibuje """
		surface = pygame.Surface((Constants.logical_width,Constants.logical_height))
		self.activo.draw(surface)
		pygame.transform.scale(surface,(self.width,self.height),self.screen)
		pygame.display.flip()
		
