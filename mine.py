import random
import itertools

#definition for itertools.product
#-------------------------------------------------------------------
# def product(*args, repeat=1):
#     # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
#     # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
#     pools = [tuple(pool) for pool in args] * repeat
#     result = [[]]
#     for pool in pools:
#         result = [x+[y] for x in result for y in pool]
#     for prod in result:
#         yield tuple(prod)
#--------------------------------------------------------------------


class mine:
	def __init__(self):
		self.board=[['_']*9 for i in range(9)]
		#board=[['_']*9]*9 isn't working
		self.mines=list(random.sample(range(81),10))
		print self.mines
		self.played=[]
		for i in self.mines:
			self.board[i/9][i%9]='*'
		self.nearby=list(itertools.product([-1,0,1],repeat=2))
		for i in [x for x in range(81) if x not in self.mines]:
			#0,0 case has to be discarded,
			count=0
			for (j,k) in map(lambda (x,y),(a,b):(x+a,y+b),[[i/9,i%9]]*9,self.nearby):
				if j in range(9) and k in range(9):
					if self.board[j][k] is "*":
						count=count+1
			if count:
				self.board[i/9][i%9]=str(count)
			else:
				self.board[i/9][i%9]='#'
	#only if flag=1 ful board, otherwise it would display the whole board
	def printboard(self,flag=0):
		print "\n   ",
		for x in range(9):
			print str(x)+' ',
		print "\n"
		for i in range(9):
			print str(i)+"  ",
			for j in range(9):
				if not flag:
					if (i,j) in self.played:
						print self.board[i][j]+' ',
					else:
						print "_ ",
				else:
					print self.board[i][j]+' ',
			print "\n"
	def play(self,coord):
		x,y=coord
		if coord not in self.played:
			self.played.append(coord)
			if self.board[x][y] is "*":
				print "**********GAME OVER**********\n"
				self.printboard(1)
				exit(0)
			else:
				return 0
		else:
			return 1

play=mine()
play.printboard()
while True:
	play.printboard()
	#expect to be added
	a,b=[int(x) for x in raw_input("\nEnter Input coordinates").split()]
	print a
	print b
	if a in range(9) and b in range(9):
		if play.play((a,b)):
			print "Entered already!!! Enter again"
	else:
		print "out of Range, enter again"
		#modify this case as error handling












					
