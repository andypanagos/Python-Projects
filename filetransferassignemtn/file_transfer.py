


import tkinter as tk
from tkinter import *
import os
import time
import shutil
import tkinter.filedialog as filedialog





class ParentWindow(Frame):
    def __init__(self, master):
        Frame. __init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(500, 250))
        self.master.title('File Transfer')

        
        self.lblSource = Label(self.master, text='Source Folder:')
        self.lblSource.pack(pady=5)
        
       
        self.txtSource = Entry(self.master, text='', width=70)
        self.txtSource.pack(pady=5)
        
        
        self.btBrowse = Button(self.master, text='Browse', command=lambda: get_source(self))
        self.btBrowse.pack(pady=5)

     
        
        self.lblDestination = Label(self.master, text='Destination Folder:')
        self.lblDestination.pack(pady=5)
        
        self.txtDestination = Entry(self.master, text='', width=70)
        self.txtDestination.pack(pady=5)
        
        self.btBrowse2 = Button(self.master, text='Browse', command=lambda: destination(self))
        self.btBrowse2.pack(pady=5)

        self.btCopyButton = Button(self.master, text='Copy Files to Destination', width=60, command=lambda: copy_files(self))
        self.btCopyButton.pack(pady=5)





def get_source(self):
    self.lblSource = tk.filedialog.askdirectory()
    self.txtSource.delete(0, END)
    self.txtSource.insert(0, self.lblSource)


def destination(self):
    self.lblDestination = tk.filedialog.askdirectory()
    self.txtDestination.delete(0, END)
    self.txtDestination.insert(0, self.lblDestination)
    

       
def copy_files(self):
    getSource = self.txtSource.get()
    getDestination = self.txtDestination.get()
    source = getSource + '/'                
    destination = getDestination + '/'      
    for fname in os.listdir(source):
        src_fname = os.path.join(source, fname)
        if last_mod_time(src_fname) > before:
            destination_fname = os.path.join(destination, fname)
            shutil.copy(source+fname, destination)
            

# Time 
SECONDS_IN_DAY = 24 * 60 * 60
now = time.time()
before = now - SECONDS_IN_DAY

def last_mod_time(fname):
    return os.path.getmtime(fname)









if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
