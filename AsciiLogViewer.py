# -*- coding: utf-8 -*-
'''
    Textual log viewer

    Usage: AsciiLogViewer filename

    if file name is not provided, it shall show navigator

'''

__author__ = 'LjGww'
application_title = "Text Log Viewer"
view_full_filename=""
view_path_only=""
view_filename_only=""


import sys
import os
from Tkinter import *
import tkMessageBox
import tkFileDialog





################################################################
#  File label popup window
################################################################

class FilePopup(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self,master=root)
        self.resizable(0,0)
        self.createWidgets()

    def createWidgets(self):
        self.doCopyFullPath = Button(self)
        self.doCopyFullPath["text"] = "Copy full path file name"
        self.doCopyFullPath["command"] = self.full
        self.doCopyFullPath.pack(fill=X)

        self.doCopyPathOnly = Button(self)
        self.doCopyPathOnly["text"] = "Copy path only"
        self.doCopyPathOnly["command"] = self.path_only
        self.doCopyPathOnly.pack(fill=X)

        self.doCopyFileOnly = Button(self)
        self.doCopyFileOnly["text"] = "Copy file name only"
        self.doCopyFileOnly["command"] = self.fn_only
        self.doCopyFileOnly.pack(fill=X)

        self.doClose = Button(self)
        self.doClose["text"] = "Close"
        self.doClose["command"] = self.destroy
        self.doClose.pack(fill=X)

    def full(self):
        root.clipboard_clear()
        root.clipboard_append(view_full_filename)
        self.destroy()

    def path_only(self):
        self.destroy()

    def fn_only(self):
        self.destroy()


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
        global view_full_filename
        view_full_filename = fname
        self.status_line['text'] += view_full_filename
        if os.path.isfile(fname):
            f = open(fname,"rt")
            for line in f:
                self.outT.insert(END,line)

    def status_left_click(self,event):
        # event structure is not interesting for use for this, it is enough to catch an event
        global view_full_filename
        root.clipboard_clear()
        root.clipboard_append(view_full_filename)

    def status_right_click(self,event):
        self.fpw = FilePopup(master=root)

    def createWidgets(self):
        # intention to replace with find box
        '''
        self.desc = Label(self,text='Viewing file: ')
        self.desc['anchor']="w"
        self.desc['justify']="left"
        self.desc.pack(side="top",fill=X)
        '''

        self.OutFrame = Frame(self)

        self.scrollbar1 = Scrollbar(master=self.OutFrame,orient=VERTICAL)
        self.scrollbar1.pack(side="right", fill="y")

        self.scrollbar2 = Scrollbar(master=self.OutFrame,orient=HORIZONTAL)
        self.scrollbar2.pack(side="bottom", fill="x")

        self.outT = Text(master=self.OutFrame,wrap=NONE)
        self.outT.pack(fill=BOTH, expand=1, side="left")

        self.outT["yscrollcommand"] = self.scrollbar1.set
        self.scrollbar1["command"]=self.outT.yview

        self.outT["xscrollcommand"] = self.scrollbar2.set
        self.scrollbar2["command"]=self.outT.xview

        self.OutFrame.pack(expand=1, fill=BOTH)

        self.doClose = Button(self)
        self.doClose["text"] = "Close"
        self.doClose["command"] = self.master.destroy
        # self.doClose.pack({"side": "left"})
        self.doClose.pack(fill=X)

        # allow some bottom space for OSX window resize to have handle, in the same time make some status info
        self.status_line = Label(self,text='Viewing file: ')
        self.status_line['anchor']="w"
        self.status_line['justify']="left"
        self.status_line.pack(fill=X)

        # labels do not have click handler, but we can observe event and act on it
        self.status_line.bind("<Button-1>", self.status_left_click)
        self.status_line.bind("<Button-2>", self.status_right_click)




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
