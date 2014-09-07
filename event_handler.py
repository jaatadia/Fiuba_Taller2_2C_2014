import pygame
from pygame.locals import *

class Event_handler():
	""" clase que maneja los eventos de entrada y salida """
	def __init__(self):
		""" inicializador de la clase """
		self.mouse=[-1,-1,0,0,0] #x,y,boton1 press, boton2 press, boton3 press
		self.mouse[0],self.mouse[1]=pygame.mouse.get_pos()
		self.mouse[2],self.mouse[3],self.mouse[4]=pygame.mouse.get_pressed()
	
	def convert_char(self,key):
		""" convierte el key si concuerda con el de un caracter """
	
		ascii_a = ord('a')
		ascii_z = ord('z')
		ascii_key = key - pygame.K_a + ascii_a

		if ((ascii_key >= ascii_a) and (ascii_key<=ascii_z)):
			return chr(ascii_key)			
		
		ascii_0 = ord('0')
		ascii_9 = ord('9')
		ascii_key = key - pygame.K_0 + ascii_0

		if ((ascii_key >= ascii_0) and (ascii_key<=ascii_9)):
			return chr(ascii_key)			
		

	def handle_events(self):
		""" tratar los eventos """
		salir = False
		pressed_char = []
		unpressed_char = []

		for event in pygame.event.get():
			if event.type == QUIT:
				salir = True
			
			elif event.type == pygame.KEYDOWN:
				char = self.convert_char(event.key)
				if(char <> ''):
					pressed_char = pressed_char + [char]			

			elif event.type == pygame.KEYUP:
				char = self.convert_char(event.key)
				if(char <> ''):
					unpressed_char = pressed_char + [char]			
			
			elif (event.type == MOUSEMOTION)or(event.type == MOUSEBUTTONUP)or(event.type == MOUSEBUTTONDOWN):
				self.mouse[0],self.mouse[1]=pygame.mouse.get_pos()
				self.mouse[2],self.mouse[3],self.mouse[4]=pygame.mouse.get_pressed()



		return salir,pressed_char,unpressed_char,self.mouse
			
	
