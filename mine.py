from app import *



##from tkinter import *
##import time
##import os
##root = Tk()
##
##frameCnt = 100
##
##def update(ind,counter,neg):
##    global labels
##    frames = framesQ[counter]
##    frame = frames[ind]
##    ind += 1 * neg
##    if ind == frameCnt:
##        ind = frameCnt - 1
##        neg = -1
##    elif(ind == 0):
##        ind = 0
##        neg = 1
##        
##    labels[counter].configure(image=frame)
##    root.after(60, update, ind, counter, neg)
##    
##labels = []
##
##def readGif(fileName):
##    global framesQ
##    framesQ.append([PhotoImage(file=fileName,format = 'gif -index %i' %(i)) for i in range(frameCnt)])
##   
##    
##framesQ = []
##threads = []
##pictures = []
##
##for i in range(20):
##    pictures.append("./images/common_planet_"+str(i%3 + 1)+".gif")
##
##for pic in pictures:
##    readGif(pic)
##
##for i in range(len(pictures)):
##    label = Label(root,text = str(i))
##    label.pack(side=LEFT)
##    labels.append(label)
##    root.after(0, update, 0, i, 1)
##
##root.mainloop()
