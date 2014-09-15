class element():
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.alive = True

	def kill(self):
		self.alive = False
	
	def is_alive(self):
		return self.alive

	def set_x(self,x):
		self.x=x

	def set_y(self,y):
		self.y=y
	
	def set_width(self,w):
		self.width=w

	def set_height(self,h):
		self.height=h

	def get_dimensions(self):
		return (self.x,self.y,self.width,self.height)

	def in_me(self,x,y):
		return (( self.x <= x ) and ( self.x + self.width >= x ) and ( self.y <= y ) and ( self.y + self.height >= y))


	def update(self,press_char,unpress_char,mouse):
		pass
	
	def draw(self,screen):
		pass
