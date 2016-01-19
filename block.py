from graphics import *
	
class Block(Rectangle):
	
	BLOCK_SIZE=30
	OUTLINE_WIDTH=3
	
	def __init__(self, pos, color):
		
		
			self.x = pos.x
			self.y = pos.y
			
			p1 = Point(pos.x*Block.BLOCK_SIZE,pos.y*Block.BLOCK_SIZE)
			p2 = Point(p1.x + Block.BLOCK_SIZE, p1.y + Block.BLOCK_SIZE)
			
			Rectangle.__init__(self, p1, p2)
			self.setWidth(Block.OUTLINE_WIDTH)
			self.setFill(color)

class Shape:
	
	def __init__(self,coords,color):
		self.coords=coords
		self.color=color
	
	def draw(self,win):
		print len(self.coords)
		for i in range(0,len(self.coords)):
			#print self.coords[i].x,self.coords[i].y
			b=Block(self.coords[i],self.color)
			b.draw(win)
	
	


class I_shape(Shape):
	
	def __init__(self,center):
		coords = [Point(center.x -2, center.y), Point(center.x -1, center.y), Point(center.x , center.y), Point(center.x + 1, center.y)]
		Shape.__init__(self, coords, "blue")
		
	
	


def main():
	#represents a 5*5 board
	win=GraphWin("Tetrominoes",200,150)
	#block=Block(Point(100,100),'red')
	#block.draw(win)
	shape=I_shape(Point(3,1))
	shape.draw(win)
	win.mainloop()
	
main()
