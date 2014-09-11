
class Constants():
	
#-----------------------------------------	
	#main
	main_wait_time = 0.01

#-----------------------------------------	
	#screen
	screen_width = 800
	screen_height = 600
	screen_window_text = "Taller 2"

#-----------------------------------------	
	#logical dimensions
	logical_width = 800
	logical_height = 600
#-----------------------------------------
	#text_bar colors
	text_bar_color = (0,0,0)
	text_bar_color_background = (100,100,100)

#-----------------------------------------
	#prompt limits
	prompt_inf_x = 0
	prompt_inf_y = 0
	prompt_sup_x = logical_width
	prompt_sup_y = logical_height

	#prompt proportions
	#   _______________________
	#  |title_________________ |
	#  | prompt text           |
	#  |                       |
	#  |                _______|
	#  |_______________|button_|
	prompt_color_title = (0,0,0) 
	prompt_color_title_background = (0,0,255)
	prompt_color_text = (0,0,0)
	prompt_color_text_background = (200,200,200)
	prompt_text_pt = 20 #si no entra se achica solo

	prompt_default_width=400
	prompt_default_height=200

	prompt_title_x=1/400.0
	prompt_title_y=1/200.0
	prompt_title_width=398/400.0
	prompt_title_height=28/200.0

	prompt_text_x=1/400.0
	prompt_text_y=30/200.0
	prompt_text_width=398/400.0
	prompt_text_height=149/200.0

	prompt_button_x=300/400.0
	prompt_button_y=150/200.0
	prompt_button_width=99/400.0
	prompt_button_height=49/200.0

	#text_prompt proportions
	#   _______________________
	#  |title_________________ |
	#  | prompt text           |
	#  |                       |
	#  |  ___________   _______|
	#  |_|input_text|__|button_|

	prompt_input_text_x=2/400.0
	prompt_input_text_y=150/200.0
	prompt_input_text_width=296/400.0
	prompt_input_text_height=49/200.0
