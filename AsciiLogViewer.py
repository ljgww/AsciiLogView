# -*- coding: utf-8 -*-
'''
    Textual log viewer

    Usage: AsciiLogViewer filename

    if file name is not provided, it shall show navigator

'''

__author__ = 'LjGww'
application_title = "Text Log Viewer"

import sys
import os
from Tkinter import *
import tkMessageBox
import tkFileDialog


################################################################
#  Main window
################################################################

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(expand=1, fill=BOTH)
        self.createWidgets()
        if len(sys.argv)==1:
            self.showFileNavigator()
        if len(sys.argv)==2:
            # display file name
            self.viewFile(sys.argv[1])

    def showFileNavigator(self):
        fname = tkFileDialog.askopenfilename(title="Select file to view:",defaultextension=".*",initialfile="",parent=self.master)
        if fname:
            self.viewFile(fname)
        else:
            tkMessageBox.showinfo(application_title,"No file selected.")
            self.master.destroy()

    def viewFile(self,fname):
        self.desc['text'] += fname
        if os.path.isfile(fname):
            f = open(fname,"rt")
            for line in f:
                self.outT.insert(END,line)

    def createWidgets(self):
		self.desc = Label(self,text='Viewing file: ')
		self.desc['anchor']="w"
		self.desc['justify']="left"
		self.desc.pack(side="top",fill=X)

		self.OutFrame = Frame(self)

		self.outT = Text(master=self.OutFrame)
		self.outT.pack(fill=BOTH, expand=1, side="left")

		self.scrollbar1 = Scrollbar(master=self.OutFrame,orient=VERTICAL)
		self.scrollbar1.pack(side="right", fill="y")

		self.outT["yscrollcommand"] = self.scrollbar1.set
		self.scrollbar1["command"]=self.outT.yview

		self.OutFrame.pack(expand=1, fill=BOTH)

		self.doClose = Button(self)
		self.doClose["text"] = "Close"
		self.doClose["command"] = self.master.destroy
		# self.doClose.pack({"side": "left"})
		self.doClose.pack(fill=X)


################################################################
#  Application Startup
################################################################


if __name__=="__main__":
    if len(sys.argv)==1 or len(sys.argv)==2:
        root = Tk()
        root.title(application_title)
        app = Application(master=root)
        app.mainloop()
        try:
            root.destroy()
        except:
            pass
    else:
        print __doc__
        print raw_input("Press Enter to continue...")
else:
    # not used as module
    pass
