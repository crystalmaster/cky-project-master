import tkinter as Tk
import re
import math
from nltk.tree import Tree

def drawTree(table,sentence):

   size = len(sentence) -1
   cfg = '('
   cfg = cfg + ','.join(table[0][size][0])
   start = table[0][size][1].split(" ")
   list_r =[]
   list_r.append(table[0][size][2])
   mark = table[0][size][2].split(" ")
   n_q = 1
   n_left_q = 0
   check = 0
   n_left_s = 0
   
   while len(list_r) >= 0:
      x = int(start[0])
      y = int(start[1]) - 1
      
      if len(table[x][y]) <= 2 :
         cfg = cfg + ' (' + ','.join(table[x][x]) +' '+ sentence[x] + ')'
         if check == 1:
            if n_left_q > 1:#Limited of node is 2
               n_left_q = 1
            cfg = cfg + ')'* n_left_q
            n_q = n_q - n_left_q
            n_left_s = n_left_s - n_left_q
            n_left_q = 0

         if len(list_r) != 0 :
            check = 1
            start = list_r.pop().split(' ')
            if start == mark:
               cfg = cfg + ')'*(n_left_s)
               n_q = n_q - n_left_s
               n_left_s = 0
            
         else: 
            break #over loop
      else:
         
         n_left_s = n_left_s + 1

         n_q = n_q + 1
        
         if check == 1:
            check = 0
            n_left_q = n_left_q + 1
         cfg = cfg + ' (' + str(table[x][y][0]) + ' '
         start = table[x][y][1].split(' ')
         list_r.append(table[x][y][2])
   cfg = cfg + ')'*(n_q)
   print(cfg)
   t = Tree.fromstring(cfg)
   t.draw()
def drawTable(table,sentence, container):
   dt = container
   size = len (sentence)

   xx,yy = 20 , 30
   for index in range(size + 1):
      if index == 0 :
         RB = Tk.Button(dt, bd =8, width = 12, text = index,fg = 'black')
         RB.place(x=xx, y = yy)
         xx = xx + 130
      else: 
         RB = Tk.Button(dt, bd =8, width = 12, text = str(index) + ' '+sentence[index - 1] ,fg = 'black')
         RB.place(x=xx, y = yy)
         xx = xx + 130
   xx = 20
   yy = yy + 60
   for index  in range(size):
      CB = Tk.Button(dt, bd =8, width = 12, text = index,fg = 'black')
      CB.place(x=xx, y = yy)
      xx = xx + 130
      for jdex in range(size):
         C = Tk.Button(dt, bd =8, width = 12, text = table[index][jdex],fg = 'black')
         C.place(x=xx, y = yy)
         xx = xx + 130
      yy = yy + 60
      xx = 20 
def drawTable1(table,sentence):
   dt = Tk.Tk()
   size = len (sentence)
   dt.geometry("1280x600+50+50")
   dt.title("CKY algorithm step by step")

   xx,yy = 20 , 30
   for index in range(size + 1):
      if index == 0 :
         RB = Tk.Button(dt, bd =8, width = 12, text = index,fg = 'black')
         RB.place(x=xx, y = yy)
         xx = xx + 130
      else: 
         RB = Tk.Button(dt, bd =8, width = 12, text = str(index) + ' '+sentence[index - 1] ,fg = 'black')
         RB.place(x=xx, y = yy)
         xx = xx + 130
   xx = 20
   yy = yy + 60
   for index  in range(size):
      CB = Tk.Button(dt, bd =8, width = 12, text = index,fg = 'black')
      CB.place(x=xx, y = yy)
      xx = xx + 130
      for jdex in range(size):
         if len(table[index][jdex]) == 1:
            C = Tk.Button(dt, bd =8, width = 12, text = table[index][jdex] ,fg = 'black')
            C.place(x=xx, y = yy)
         elif len(table[index][jdex]) == 2:
            C = Tk.Button(dt, bd =8, width = 12, text = table[index][jdex] ,fg = 'black')
            C.place(x=xx, y = yy)
         elif len(table[index][jdex]) >= 3:
            C = Tk.Button(dt, bd =8, width = 12, text = table[index][jdex][-3] +' = ('+ table[index][jdex][-2] +') + ('+ table[index][jdex][-1]+')' ,fg = 'black')
            C.place(x=xx, y = yy)
         xx = xx + 130
      yy = yy + 60
      xx = 20
   
   Q = Tk.Button(dt, text = "Next",fg = 'red', command = dt.destroy)
   Q.pack(side = Tk.BOTTOM)