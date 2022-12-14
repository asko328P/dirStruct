import gi
import os
import configCreator

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class Main:
    def __init__(self):
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        gladeFile= "gladeFiles/main.glade"
        self.builder=Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)

        self.spinnerFolderDepth = self.builder.get_object("spinnerFolderDepth")
        self.spinnerFolderDepth.connect("value-changed", self.getSpinnerValues)

        self.spinnerFolderWidth = self.builder.get_object("spinnerIndentWidth")
        self.spinnerFolderWidth.connect("value-changed", self.getSpinnerValues)

        self.buttonGenerateText = self.builder.get_object("GenerateText")
        self.buttonGenerateText.connect("clicked", self.generateText)

        self.CopyText = self.builder.get_object("CopyText")
        self.CopyText.connect("clicked", self.copyText)

        self.fileTextView = self.builder.get_object("fileTextView")


        file=open("dirStructOutput.txt","r")

        self.TextViewBuffer=self.builder.get_object("textbuffer1")
        self.TextViewBuffer.set_text(file.read())
        file.close()




        window=self.builder.get_object("window1")
        window.connect("destroy",Gtk.main_quit)
        window.show()

    def getSpinnerValues(self, widget):
        configCreator.createCustomConfig(self.spinnerFolderDepth.get_value_as_int(),self.spinnerFolderWidth.get_value_as_int())

    def generateText(self, widget):
        print("clicked")
        os.system("python dirStruct.py")
        file = open("dirStructOutput.txt", "r")
        self.TextViewBuffer.set_text(file.read())
        file.close()

    def copyText(self, widget):
        self.clipboard.set_text(self.TextViewBuffer.get_text(self.TextViewBuffer.get_start_iter(),self.TextViewBuffer.get_end_iter(),False), -1)

if __name__=='__main__':
    main=Main()
    Gtk.main()
