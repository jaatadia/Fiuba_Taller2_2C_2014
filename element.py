class element():
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height

	def set_x(self,x):
		self.x=x

	def set_y(self,y):
		self.y=y

	def in_me(self,x,y):
		return (( self.x <= x ) and ( self.x + self.width >= x ) and ( self.y <= y ) and ( self.y + self.height >= y))

	def draw(self,screen):
		pass

	def update(self,press_char,unpress_char,mouse):
		""" le dice al objeto que se updatee segun la entrada, debe devolver: 
			(Estado,(nuevo_elemento1,nuevo_elemento2,...)) 
		Estado: True si el objeto sige vivo o False en caso contrario.
		nuevo_elementoX: nuevo elemento creado por el update"""
		return (True,())
