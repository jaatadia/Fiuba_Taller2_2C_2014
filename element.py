class element():
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
	
	def in_me(self,x,y):
		return (( self.x <= x ) and ( self.x + self.width >= x ) and ( self.y <= y ) and ( self.y + self.height >= y))

	def draw(self,screen):
		pass

	def update(self,press_char,unpress_char,mouse):
		pass
