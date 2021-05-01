from tkinter import *
#creating the application main window
root= Tk()




#creating a button widget
redbutton = Button (root, text = "LEFT" , fg = "green")

#shoving it into the screen
redbutton.pack( side = LEFT)

greenbutton = Button(root , text = "RIGHT" , fg = "black")
greenbutton.pack( side = RIGHT)
bluebutton = Button(root, text = "TOP" , fg = "blue")
bluebutton.pack( side = TOP)
blackbutton = Button(root , text = "BOTTOM" , fg = "red")
blackbutton.pack( side = BOTTOM)

root.mainloop()





