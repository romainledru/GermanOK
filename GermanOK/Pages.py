from tkinter import *
from Book import Word
import time

class App(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        MainMenu(self)
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0,weight=1)
        self.container.grid_columnconfigure(0,weight=1)
        
        self.frames = {}
        self.showFrame(StartPage)
    def showFrame(self,context):
        """Loading Pages: running all pages class
        And display the StartPage
        """

        for F in (StartPage, PagePlay, PageOption, PageAdd, PageRemove):
            frame = F(self.container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        frame = self.frames[context]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        label = Label(self, text="Start Page")
        label.pack(padx=10, pady=10)
        playB = Button(self, text="Page Play",command = lambda:controller.showFrame(PagePlay))
        playB.pack()
        optionB = Button(self, text="Page Option",command = lambda:controller.showFrame(PageOption))
        optionB.pack()


class PagePlay(Frame):
    def __init__(self,parent,controller):

        self.word = Word()
        self.question,self.answer = self.word.pickWord()

        Frame.__init__(self,parent)
        self.bind_all("<Return>",self.enterPressed)

        label = Label(self, text="Page Play")
        label.pack(padx=10, pady=10)
        self.labelQuestion = Label(self,text=self.question)
        self.labelQuestion.pack()
        self.entryAnswer = Entry(self,text="")
        self.entryAnswer.pack()
        self.labelReponse = Label(self,text="None")
        self.labelReponse.pack()
        startB = Button(self, text="Start Page",command = lambda:controller.showFrame(StartPage))
        startB.pack()
    
    def enterPressed(self,event):
        """Validation Function: when a word is guessed, The user press on "Enter" to validate
        the word will be compared, edited (scores) and call a new word to be guessed
        """

        if event.keysym:
            compared = self.word.compareWord(self.question,self.entryAnswer.get())
            if compared:
                self.labelReponse.configure(text="Richtig!")
            else:
                self.labelReponse.configure(text="Falsch...")
            self.word.updateWord(self.question,compared)
            self.newQuestion()
    
    def newQuestion(self):
        """class Word() is called to reload the actual data.json
        frame is cleaned up
        """
        self.word = Word()
        self.question,self.answer = self.word.pickWord()
        self.labelQuestion.configure(text= self.question)
        self.entryAnswer.delete(0,END)
        self.entryAnswer.pack()


class PageOption(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        label = Label(self, text="Page Option")
        label.pack(padx=10, pady=10)
        addB = Button(self, text="Page Add",command = lambda:controller.showFrame(PageAdd))
        addB.pack()
        removeB = Button(self, text="Page Remove",command = lambda:controller.showFrame(PageRemove))
        removeB.pack()
        startB = Button(self, text="Start Page",command = lambda:controller.showFrame(StartPage))
        startB.pack()


class PageAdd(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        label = Label(self, text="Page Add")
        label.pack(padx=10, pady=10)
        labelAdd = Label(self, text="Enter in German")
        labelAdd.pack()
        self.entryDE = Entry(self, text="")
        self.entryDE.pack()
        labelAdd = Label(self, text="Enter in French")
        labelAdd.pack()
        self.entryFR = Entry(self, text="")
        self.entryFR.pack()
        submit = Button(self, text="Confirm", command = self.submitMethod)
        submit.pack()
        startB = Button(self, text="Start Page",command = lambda:controller.showFrame(StartPage))
        startB.pack()

    def submitMethod(self):
        """data.json Edit Function: To add a word to the json
        """

        self.word = Word()
        if self.entryDE.get() != "" and self.entryFR.get() != "":
            self.word.newWord(self.entryDE.get(),self.entryFR.get())
        else:
            print("Enter a correct value")
        self.reload()

    def reload(self):
        """Page is cleaned up in case the user wants to add another word
        """

        self.entryDE.delete(0,END)
        self.entryDE.pack()
        self.entryFR.delete(0,END)
        self.entryFR.pack()


class PageRemove(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        label = Label(self, text="Page Remove")
        label.pack(padx=10, pady=10)
        labelAdd = Label(self, text="Enter in German")
        labelAdd.pack()
        self.entryDE = Entry(self, text="")
        self.entryDE.pack()
        submit = Button(self, text="Confirm", command = self.submitMethod)
        submit.pack()
        startB = Button(self, text="Start Page",command = lambda:controller.showFrame(StartPage))
        startB.pack()
    
    def submitMethod(self):
        """data.json Edit Function: To add a word to the json
        """

        word = Word()
        if self.entryDE.get() != "":
            word.deleteWord(self.entryDE.get())
        else:
            print("Enter a correct value")
        self.reload()

    def reload(self):
        """Page is cleaned up in case the user wants to add another word
        """

        self.entryDE.delete(0,END)
        self.entryDE.pack()


class MainMenu:
    def __init__(self,master):
        menubar = Menu(master)
        filemenu = Menu(menubar,tearoff=0)
        filemenu.add_command(label="Exit", command = master.quit)
        menubar.add_cascade(label="File", menu = filemenu)
        master.config(menu = menubar)
