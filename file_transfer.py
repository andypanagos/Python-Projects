


import tkinter as tk
from tkinter import *
import os
import time
import shutil
import tkinter.filedialog as filedialog


class ParentWindow(Frame):
    def __init__(self, master, *args):
        Frame.__init__(self)



        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(500, 250))
        self.master.title('File Transfer')
        
        self.lblSource = Label(self.master, text='Select Source Folder:')
        self.lblSource.pack(pady=5)

        self.txtSource = Entry(self.master, text='', width=80)
        self.txtSource.pack(pady=5)

        self.btBrowse = Button(self.master, text='Browse Folders', command=lambda: get_source(self))
        self.btBrowse.pack(pady=5)

        self.lblDestination = Label(self.master, text='Select Destination Folder:')
        self.lblDestination.pack(pady=5)

        self.txtDestination = Entry(self.master, text='', width=80)
        self.txtDestination.pack(pady=5)

        self.btBrowse2 = Button(self.master, text='Browse', command=lambda: destination(self))
        self.btBrowse2.pack(pady=5)

        self.btCopyButton = Button(self.master, text ='Send Files to Destination Folder', width= 70, command=lambda: copy_files(self))
        self.btCopyButton.pack(pady=5)

    
        # Function to browse and select source folder
def get_source(self):
    self.lblSource = tk.filedialog.askdirectory()
    self.txtSource.delete(0, tk.END)
    self.txtSource.insert(0, self.lblSource)

# Function to browse and select destination folder
def destination(self):
    self.lblDestination = tk.filedialog.askdirectory()
    self.txtDestination.delete(0, tk.END)
    self.txtDestination.insert(0, self.lblDestination)
    

# Method to copy modified files from one folder to another        
def copy_files(self):
  source = get_source('C:','') + '/'
  destination = destination('C:','') + '/'
  files = os.listdir(source)
  for i in files:
    if i[-3:] == 'txt':
      shutil.move(source+i, destination)
        
    

def on_off_auto(On_the_run):
  time.every(86400).seconds.do(move_files)  
  while On_the_run:
    schedule.run_pending()
    time.sleep(1)




    

if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
