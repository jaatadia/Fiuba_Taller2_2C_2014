import pygame
from pygame.locals import *

class Event_handler():
	""" clase que maneja los eventos de entrada y salida """
	def __init__(self):
		""" inicializador de la clase """
		self.mouse=[-1,-1,0,0,0] #x,y,boton1 press, boton2 press, boton3 press
		self.mouse[0],self.mouse[1]=pygame.mouse.get_pos()
		self.mouse[2],self.mouse[3],self.mouse[4]=pygame.mouse.get_pressed()
		self.shifted = False
		self.mayus = False
		self.__init_hash__()
		
		pygame.key.set_repeat(500, 100)

	def __init_hash__(self):
		

		self.hash_shifted={}
		self.hash_unshifted={}
		self.hash={True:self.hash_shifted,False:self.hash_unshifted}

		ascii = ord('a')
		ascii_mayus=ord('A')
		for i in range (K_a,K_z+1):
			self.hash_unshifted[i]=chr(ascii)
			self.hash_shifted[i]=chr(ascii_mayus)
			ascii+=1
			ascii_mayus+=1

		self.hash_unshifted[K_0] ='0'
		self.hash_unshifted[K_1]='1'
		self.hash_unshifted[K_2]= '2'
		self.hash_unshifted[K_3]= '3'
		self.hash_unshifted[K_4]= '4'
		self.hash_unshifted[K_5]= '5'
		self.hash_unshifted[K_6]= '6'
		self.hash_unshifted[K_7]= '7'
		self.hash_unshifted[K_8]= '8'
		self.hash_unshifted[K_9]= '9'
		self.hash_unshifted[K_BACKQUOTE]= '`'
		self.hash_unshifted[K_MINUS]= '-'
		self.hash_unshifted[K_EQUALS]='='
		self.hash_unshifted[K_LEFTBRACKET]= '['
		self.hash_unshifted[K_RIGHTBRACKET]= ']'
		self.hash_unshifted[K_BACKSLASH]= '\\'
		self.hash_unshifted[K_SEMICOLON]= ';'
		self.hash_unshifted[K_QUOTE]= '\''
		self.hash_unshifted[K_COMMA]= ','
		self.hash_unshifted[K_PERIOD]= '.'
		self.hash_unshifted[K_SLASH]= '/'
		self.hash_unshifted[K_SPACE]= ' '
		self.hash_unshifted[K_UP]= "UP"
		self.hash_unshifted[K_LEFT]= "LEFT"
		self.hash_unshifted[K_RIGHT]="RIGHT"
		self.hash_unshifted[K_DOWN]= "DOWN"
		self.hash_unshifted[K_BACKSPACE]="BACK"
		self.hash_unshifted[13]="ENTER"
		self.hash_unshifted[K_DELETE ]="DEL"

		self.hash_shifted[K_0] =')'
		self.hash_shifted[K_1]='!'
		self.hash_shifted[K_2]= '@'
		self.hash_shifted[K_3]= '#'
		self.hash_shifted[K_4]= '$'
		self.hash_shifted[K_5]= '%'
		self.hash_shifted[K_6]= '^'
		self.hash_shifted[K_7]= '&'
		self.hash_shifted[K_8]= '*'
		self.hash_shifted[K_9]= '('
		self.hash_shifted[K_BACKQUOTE]= '~'
		self.hash_shifted[K_MINUS]= '_'
		self.hash_shifted[K_EQUALS]='+'
		self.hash_shifted[K_LEFTBRACKET]= '{'
		self.hash_shifted[K_RIGHTBRACKET]= '}'
		self.hash_shifted[K_BACKSLASH]= '|'
		self.hash_shifted[K_SEMICOLON]= ':'
		self.hash_shifted[K_QUOTE]= '"'
		self.hash_shifted[K_COMMA]= '<'
		self.hash_shifted[K_PERIOD]= '>'
		self.hash_shifted[K_SLASH]= '?'
		self.hash_shifted[K_SPACE]= ' '
		self.hash_shifted[K_UP]= "UP"
		self.hash_shifted[K_LEFT]= "LEFT"
		self.hash_shifted[K_RIGHT]="RIGHT"
		self.hash_shifted[K_DOWN]= "DOWN"
		self.hash_shifted[K_BACKSPACE]="BACK"
		self.hash_shifted[13]="ENTER"
		self.hash_shifted[K_DELETE ]="DEL"
		
	
	def __convert_char__(self,key):
		""" convierte el key si concuerda con el de un caracter """
		if (key	>= K_a and key <= K_z):		
			return self.hash[self.shifted^self.mayus].get(key,'')
		else:
			return self.hash[self.shifted].get(key,'')

				
				

	def handle_events(self):
		""" tratar los eventos """
		salir = False
		pressed_char = []
		unpressed_char = []

		for event in pygame.event.get():
			if event.type == QUIT:
				salir = True
			
			elif event.type == pygame.KEYDOWN:
				if event.key == K_LSHIFT or event.key == K_RSHIFT: 
					self.shifted = True
				elif event.key == K_CAPSLOCK:
					self.mayus = not self.mayus
				else:
					char = self.__convert_char__(event.key)
					if(char <> ''):
						pressed_char = pressed_char + [char]			

			elif event.type == pygame.KEYUP:
				if event.key == K_LSHIFT or event.key == K_RSHIFT:
					self.shifted=False
				else:
					char = self.__convert_char__(event.key)
					if(char <> ''):
						unpressed_char = pressed_char + [char]			
			
			elif (event.type == MOUSEMOTION)or(event.type == MOUSEBUTTONUP)or(event.type == MOUSEBUTTONDOWN):
				self.mouse[0],self.mouse[1]=pygame.mouse.get_pos()
				self.mouse[2],self.mouse[3],self.mouse[4]=pygame.mouse.get_pressed()



		return salir,pressed_char,unpressed_char,self.mouse
			
	
