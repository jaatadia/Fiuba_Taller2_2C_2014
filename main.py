#!/usr/bin/python

import sys
sys.path.insert(0, './src')


from event_handler import Event_handler
from state_machine import State_machine
from constants import Constants
import pygame, time


def init():
	pygame.init()
	
def close():
	pygame.quit()

def main(): 
	init()
	myMachine = State_machine(Constants.screen_width,Constants.screen_height,Constants.screen_window_text)
	myHandler = Event_handler()
	
	salir = False
	while (not salir):
		salir,press_char,unpress_char,mouse= myHandler.handle_events() #capturo la entrada
		myMachine.update(press_char,unpress_char,mouse) #updateo el estado
		myMachine.draw() #dibujo
		time.sleep(Constants.main_wait_time)#duermo
		
	close()

main()
	
