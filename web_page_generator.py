


import tkinter as tk
from tkinter import *
import webbrowser



class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")
        self.master.geometry('{}x{}'.format(500, 250))

        self.lblhtml = Label(self.master, text = "Enter custom text or click default HTML Button.")
        self.lblhtml.pack(pady=5)

        self.txthtml = Entry(self.master, text='', width=80)
        self.txthtml.pack(pady=5)

        self.btn = Button(self.master, text="Default HTML Page", width=20, height=2, command=self.defaultHTML)
        self.btn.pack(padx=(15,0) , pady=(30,10))

        self.txtbtn = Button(self.master, text="Submit Custom Text", width=20, height=2, command=self.update_text)
        self.txtbtn.pack(padx=(15,0) ,pady=(30,10))
        

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


    #function that takes the input from the submit button and prints it into the htnl index file

    def update_text(self):
        text = self.txthtml.get()
        htmlFile = open("index.html","w")
        html = "<html>\n<body>\n<h1>" + text + "\n</h1>\n</body>\n</html>"
        htmlFile.write(html)
        webbrowser.open_new_tab("index.html")
        




    
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
