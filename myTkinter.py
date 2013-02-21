from Tkinter import * 
import Tkinter
'''
master = Tk()
w = Canvas(master, width = 200, height = 100)
w.pack()

w.create_line(0,0, 200,100)
mainloop()
'''

import Tkinter
tk=Tkinter
root=tk.Tk()
root.title("Alpha Space Station")

myCanvas = tk.Canvas(root, width = 1033, height = 498)
photo = tk.PhotoImage(file="convex.gif")
myCanvas.create_image(250,250, image=photo)
myCanvas.pack()

root.mainloop()
