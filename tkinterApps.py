from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter.ttk as tkrtk
from PIL import ImageTk, Image, ImageSequence, ImageDraw
from tkinter.filedialog import askopenfile

class tkinterCreate():
    
    def __init__(self):
        self.root = Tk()
        self.root.title('Planet Exploration Systems')
        self.root.geometry('1260x785+0+0')

        
        self.FRAMES = {}
        self.StringVariables = {"noteInsert":StringVar(),
                           }
     
        self.loginBool = False
        self.registered = False
        
    def createNoteBook(self,tabs):
        self.notebook = ttk.Notebook(self.root)
        self.frameTabs = []
        for tab in tabs:
            newTab = Frame(self.notebook)
            self.frameTabs.append(newTab)
            self.notebook.add(newTab, text=tab)
        self.notebook.pack()
        
    def setup(self):
        leftFrame = Frame(self.frameTabs[0], width = 260, height = 785, relief = SUNKEN,
                          bd = 5, bg = 'black')
        leftFrame.propagate(0)
        leftFrame.pack(side = LEFT)
        self.FRAMES["leftFrame"] = leftFrame
        
        
        profFrame = Frame(self.FRAMES["leftFrame"], width = 260, height = 200, relief = RAISED,
                          bd = 5, bg = '#a9a9a9', highlightbackground= 'black', highlightcolor='black')
        profFrame.propagate(0)
        profFrame.pack(side = TOP)
        self.FRAMES["profFrame"] = profFrame
        

        self.profCanv = Canvas(self.FRAMES["profFrame"], width = 250, height = 165, relief = RAISED,
                               highlightbackground = 'black')
        self.profCanv.propagate(0)
        self.profCanv.pack()

        self.btnUploadPic = Button(self.FRAMES["profFrame"], width = 35, height = 1, relief = RAISED,
                              bd = 3, text = 'UPLOAD PIC', command = self.open_picfile,
                                   font = 'consolas 10 bold',fg = 'black', state = DISABLED)
        self.btnUploadPic.pack(side = BOTTOM)

    def leftPanel():
        start_img = 'start_img'
        img = Image.open(f'images/{start_img}.jpg')
        img2 = img.resize((250, 220))
        self.prof_img = ImageTk.PhotoImage(img2)

        self.profCanv.create_image(0,95, anchor = W, image = self.prof_img)

        self.rightFrame = Frame(TabControl1, width = 1000, height = 200, relief = SUNKEN,
                           bd = 5, bg = '#a9a9a9')
        self.rightFrame.pack(side = RIGHT)

        self.rightTitle = Frame(self.rightFrame, width = 1000, height = 55, relief = RAISED,
                            bd = 5, bg = '#1d3557')
        self.rightTitle.propagate(0)
        self.rightTitle.pack(side = TOP)

        title = Label(self.rightTitle, width = 200, height = 2, bg = '#1d3557', relief = RAISED,
                      bd = 5, text = 'Student Success Dashboard', font = 'Consolas 16 bold', fg = 'cornsilk')
        title.propagate(0)
        title.pack()
        

    

app = tkinterCreate()
app.createNoteBook(["Student Managment Dashboard","Student Ranking and Missions"])
app.setup()
app.leftPanel()
app.root.mainloop()
