#!/usr/bin/python

from event_handler import Event_handler
from state_machine import State_machine
import pygame, time


def init():
	pygame.init()
	
def close():
	pygame.quit()

def main(): 
	init()
	myMachine = State_machine()
	myHandler = Event_handler()
	
	salir = False
	while (not salir):
		salir,press_char,unpress_char,mouse= myHandler.handle_events() #capturo la entrada
		myMachine.update(press_char,unpress_char,mouse) #updateo el estado
		myMachine.draw() #dibujo
		time.sleep(0.1)	#duermo
		
	close()

main()
	
