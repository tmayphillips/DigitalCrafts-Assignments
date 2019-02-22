import tkinter

m=tkinter.Tk()
m.title('Counting Seconds') 
button = tkinter.Button(m, text='Stop', width=25, command=m.destroy) 
button.pack()
m.mainloop()

from tkinter import *
root = Tk() 
scrollbar = Scrollbar(root) 
scrollbar.pack( side = RIGHT, fill = Y ) 
mylist = Listbox(root, yscrollcommand = scrollbar.set ) 
for line in range(100): 
   mylist.insert(END, 'This is line number' + str(line)) 
mylist.pack( side = LEFT, fill = BOTH ) 
scrollbar.config( command = mylist.yview ) 
mainloop()

from tkinter import *
main = Tk() 
ourMessage ='This is our Message'
messageVar = Message(main, text = ourMessage) 
messageVar.config(bg='lightgreen') 
messageVar.pack( ) 
main.mainloop( ) 

from tkinter import *
master = Tk() 
w = Spinbox(master, from_ = 0, to = 10) 
w.pack() 
mainloop()
print(w)