import states
import buttons
import prompts
import text


delim = "#"

#---------------------------------------------
#parse functions

def button(line,state):
	params=line.split(delim)
	return buttons.button(int(params[1]),int(params[2]),int(params[3]),int(params[4]))

def input_button(line,state):
	params=line.split(delim)
	return buttons.input_button(int(params[1]),int(params[2]),int(params[3]),int(params[4]),state.__set_next_state__,params[5])


#---------------------------------------------
#parse hash

parse_hash={}
parse_hash["button"]=button
parse_hash["input_button"]=input_button

def none(line,state):
	pass

def parse(line,state):
	return	parse_hash.get(line.split(delim)[0],none)(line,state)


#---------------------------------------------
#actual parser

def state_parser(file_name):

	new_state=states.state()

	f = open(file_name, "r")
	line = f.readline()
	while line:
		new_state.add(parse(line,new_state))
		line = f.readline()

	f.close()

	return new_state

