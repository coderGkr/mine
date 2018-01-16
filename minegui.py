import random
import itertools
import os
import Tkinter as tk
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

class button(tk.Frame):
	def __init__(self,i,master=None,board=None):
		tk.Frame.__init__(self,master)
		self.value="  "
		self.tkv=tk.StringVar()
		self.tkv.set(self.value)
		self.board=board
		self.x=i/9
		self.y=i%9
		self.clicked=False
		self.master=master
		self.Configure()


	def __str__(self):
		return self.value

	def isMine(self):
		if self.value is "*":
			return True
		else:
			return False

	def setval(self,val):
		self.value=val

	def reveal(self):
		self.tkv.set(self.value)

	
	def click(self):
		self.reveal()
		if self.isMine():
			self.board.gameover()

	def Configure(self):
		#need to use self?
		button=tk.Button(self.master,textvariable=self.tkv,command=self.click)
		#sticky could be added
		button.grid(row=self.x,column=self.y,ipadx=2,ipady=2)


class mine:
	def __init__(self):
		# self.board=[['_']*9 for i in range(9)]
		self.window=tk.Tk()
		self.window.geometry("800x600")
		self.window.title("Minesweeper")
		self.board=[]
		for i in range(81):
			self.board.append(button(i,self.window,self))
		# #board=[['_']*9]*9 isn't working
		self.mines=list(random.sample(range(81),10))
		# print self.mines
		self.nearby=list(itertools.product([-1,0,1],repeat=2))
		self.printboard()
		for i in self.mines:
			self.board[i].setval("*")

		# for i in range(81):
		# for i in self.mines:
		# 	self.board[i/9][i%9]='*'
		
			#0,0 case has to be discarded,
		self.printboard()
		for i in [x for x in range(81) if x not in self.mines]:
			count=0
			for (j,k) in map(lambda (x,y),(a,b):(x+a,y+b),[[i/9,i%9]]*9,self.nearby):
				if j in range(9) and k in range(9):
					if self.board[j*9+k].isMine():
						count=count+1
			if count:
				self.board[i].setval(str(count))
			else:
				self.board[i].setval('#')
		self.printboard()
		self.window.mainloop()


	def gameover(self):
		for i in range(81):
			self.board[i].reveal()
		gamelabel=tk.Label(self.window,text="GAME OVER")
		gamelabel.grid(row=11,column=11)

	def printboard(self):
		for i in range(81):
			print self.board[i].value,
		print "\n"





play=mine()











					
