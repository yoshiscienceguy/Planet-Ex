import matplotlib as plt
import matplotlib.pyplot as plt2
import numpy as np
from tkinter import *
# from tkcalendar import *
#import pymysql
from tkinter import ttk
import random
import tkinter.messagebox
import time
import tkinter.ttk as tkrtk
import tkinter as tkr
from PIL import ImageTk, Image, ImageSequence, ImageDraw
import csv
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox
import os.path
import datetime as dt
import pandas as pd
import statistics
import seaborn as sns
#import ttkbootstrap as ttkB
#from ttkbootstrap import *
#import emoji
from datetime import date, datetime
import random
from tkinter.filedialog import askopenfile
import time
plt.use('TkAgg')
#plt2.style.use('ggplot')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk)
import matplotlib.gridspec as grid_spec
from sklearn.neighbors import KernelDensity

class Planet_Ex():

    def __init__(self, root):

        self.root = root
        self.root.title('Planet Exploration Systems')
        self.root.geometry('1260x785+0+0')

        notebook = ttk.Notebook(self.root)
        TabControl1 = ttk.Frame(notebook)
        TabControl2 = ttk.Frame(notebook)
        #TabControl3 = ttk.Frame(notebook)

        notebook.add(TabControl1, text='Student Managment Dashboard')
        notebook.add(TabControl2, text='Student Ranking and Missions')
        #notebook.add(TabControl3, text='Planet Inventory')

        notebook.pack()
        ###############################################################################################################
        ###############################################################################################################
        ###############################################################################################################
        ###############################################################################################################
        ###############################################################################################################
         #######################
        # Front Page Key players and Actors
        self.noteInsert = StringVar()
        self.loginBool = False
        self.registered = False

        ######################
        leftFrame = Frame(TabControl1, width = 260, height = 785, relief = SUNKEN,
                          bd = 5, bg = 'black')
        leftFrame.propagate(0)
        leftFrame.pack(side = LEFT)

        profFrame = Frame(leftFrame, width = 260, height = 200, relief = RAISED,
                          bd = 5, bg = '#a9a9a9', highlightbackground= 'black', highlightcolor='black')
        profFrame.propagate(0)
        profFrame.pack(side = TOP)

        self.profCanv = Canvas(profFrame, width = 250, height = 165, relief = RAISED,
                               highlightbackground = 'black')
        self.profCanv.propagate(0)
        self.profCanv.pack()

        self.btnUploadPic = Button(profFrame, width = 35, height = 1, relief = RAISED,
                              bd = 3, text = 'UPLOAD PIC', command = self.open_picfile,
                                   font = 'consolas 10 bold',fg = 'black', state = DISABLED)
        self.btnUploadPic.pack(side = BOTTOM)

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

        # Get the username after logging in.
        self.lblName = Label(title, width = 15, height = 1, bg = '#1d3557', text = '',
                             font = 'Consolas 12 bold', fg = 'cornsilk', justify = LEFT)
        self.lblName.place(x = -5, y = 4)

        self.rightFrame2 = PanedWindow(self.rightFrame, width = 1000, height = 245, relief = RAISED,
                            bd = 5, bg = '#a9a9a9') #bg = '#a9a9a9',
        self.rightFrame2.propagate(0)
        self.rightFrame2.pack(side = TOP)

        rightFrame1 = Frame(self.rightFrame, width = 1000, height = 265, relief = SUNKEN,
                            bd = 5, bg = '#a9a9a9')
        rightFrame1.propagate(0)
        rightFrame1.pack(side = TOP)

        self.rightFrame1A = LabelFrame(rightFrame1, width = 265, height = 265, relief = RAISED,
                            bd = 5, text = 'Student Criteria Radar', font = 'consolas 10',
                                       bg = '#a9a9a9')
        self.rightFrame1A.propagate(0)
        self.rightFrame1A.pack(side = LEFT)

        self.rightFrame1B = LabelFrame(rightFrame1, width = 450, height = 265, relief = RAISED,
                            bd = 5, text = 'Distribution Ridge Plot', font = 'consolas 10',
                                       bg = '#a9a9a9')
        self.rightFrame1B.propagate(0)
        self.rightFrame1B.pack(side = LEFT)

        self.rightFrame1C = LabelFrame(rightFrame1, width = 265, height = 265, relief = RAISED,
                            bd = 5, text = 'Pie Chart', font = 'consolas 10',
                                       bg = '#a9a9a9')
        self.rightFrame1C.propagate(0)
        self.rightFrame1C.pack(side = LEFT)

        rightFrame3 = Frame(self.rightFrame, width = 1000, height = 285, relief = SUNKEN,
                            bd = 5, bg = 'grey')
        rightFrame3.propagate(0)
        rightFrame3.pack(side = TOP)

        self.rightFrame3A = LabelFrame(rightFrame3, width = 395, height = 285, relief = RAISED,
                            bd = 5, bg = 'grey80', font = 'consolas 10', text = 'Total Scores')
        self.rightFrame3A.propagate(0)
        self.rightFrame3A.pack(side = LEFT, fill = BOTH, expand = True)

        self.rightFrame3A1 = Frame(self.rightFrame3A, width = 250, height = 285, relief = RAISED,
                            bd = 5, bg = 'grey80')
        self.rightFrame3A1.propagate(0)
        self.rightFrame3A1.pack(side = LEFT)

        self.rightFrame3B = LabelFrame(rightFrame3, width = 595, height = 189, relief = RAISED,
                            bd = 5, bg = 'grey80', font = 'consolas 10', text = 'Task Master')
        self.rightFrame3B.propagate(0)
        self.rightFrame3B.pack(side = RIGHT)

        detFrame1 = Frame(leftFrame, width = 272, height = 555, bg = '#1d3557', relief = RAISED,
                         bd = 5)
        detFrame1.propagate(0)
        detFrame1.pack(side = BOTTOM)

        detFrame1A = Frame(detFrame1, width = 106, height = 390, bg = '#1d3557', relief = SUNKEN,
                         bd = 0)
        detFrame1A.propagate(0)
        detFrame1A.pack(side = LEFT, anchor = NW)

        detFrame1B = Frame(detFrame1, width = 146, height = 390, bg = '#1d3557', relief = SUNKEN,
                         bd = 0)
        detFrame1B.propagate(0)
        detFrame1B.pack(side = RIGHT, anchor = NE)

        #####################################################################################################
        #####################################################################################################

        lblFirstName = Label(detFrame1A, width = 11, height = 1, text = 'First Name:', font = 'consolas 12 bold',
                        fg = 'white', bg = '#1d3557', anchor = W, justify = LEFT)
        lblFirstName.pack(side = TOP, padx = 3, pady = 2)

        self.OneFirst = StringVar()

        self.entFName = Entry(detFrame1B, width = 20, bg = 'white', fg = 'black', textvariable = self.OneFirst)
        self.entFName.pack(side = TOP, pady = (6,3))

        lblLastName = Label(detFrame1A, width = 11, height = 1, text = 'Last Name:', font = 'consolas 12 bold',
                        fg = 'white', bg = '#1d3557', anchor = W, justify = LEFT)
        lblLastName.pack(side = TOP, padx = 3, pady = 2)

        self.OneLast = StringVar()

        self.entLName = Entry(detFrame1B, width = 20, bg = 'white', fg = 'black', textvariable = self.OneLast)
        self.entLName.pack(side = TOP, pady = (7,3))

        lblGradeLevel = Label(detFrame1A, width = 11, height = 1, text = 'Grade Lvl:', font = 'consolas 12 bold',
                        fg = 'white', bg = '#1d3557', anchor = W, justify = LEFT)
        lblGradeLevel.pack(side = TOP, padx = 3, pady = 2)
        
        self.gradeLevel = StringVar()

        self.cboGradeLevel = ttk.Combobox(detFrame1B, width = 17, textvariable = self.gradeLevel,
                                          height = 1)
        self.cboGradeLevel['values'] = ('6th Grade','7th Grade','8th Grade',
                                        '9th Grade','10th Grade','11th Grade',
                                        '12th Grade')
        self.cboGradeLevel.pack(side = TOP, pady = (7,3))

        lblPronoun = Label(detFrame1A, width = 11, text  = 'Pronoun:', font = 'consolas 12 bold',
                           fg = 'white', bg = '#1d3557', anchor = W, justify = LEFT)
        lblPronoun.pack(side = TOP, padx = 3, pady = 2)

        self.studPronoun = StringVar()

        self.cboPronoun = ttk.Combobox(detFrame1B, width = 17, textvariable = self.studPronoun,
                                          height = 1)
        self.cboPronoun['values'] = ('She/Her','He/His','Them/They')
        self.cboPronoun.pack(side = TOP, pady = (5,3))

        lblDOB = Label(detFrame1A, width = 11, text  = 'Birth Date:', font = 'consolas 12 bold',
                           fg = 'white', bg = '#1d3557', anchor = W, justify = LEFT)
        lblDOB.pack(side = TOP, padx = 3, pady = 1)

        self.studDOB = StringVar()

        self.entDOB = Entry(detFrame1B, width = 20, bg = 'white', fg = 'black', textvariable = self.studDOB)
        self.entDOB.pack(side = TOP, pady = (5,3))

        lblEmail = Label(detFrame1A, width = 11, text  = 'Email:', font = 'consolas 12 bold',
                           fg = 'white', bg = '#1d3557', anchor = W, justify = LEFT)
        lblEmail.pack(side = TOP, padx = 3, pady = 2)

        self.studEmail = StringVar()

        self.entEmail = Entry(detFrame1B, width = 20, bg = 'white', fg = 'black', textvariable = self.studEmail)
        self.entEmail.pack(side = TOP, pady = (5,3))

        lblOS = Label(detFrame1A, width = 11, text  = 'Comp OS:', font = 'consolas 12 bold',
                           fg = 'white', bg = '#1d3557', anchor = W, justify = LEFT)
        lblOS.pack(side = TOP, padx = 3, pady = 1)

        self.studOS = StringVar()

        self.cboOS = ttk.Combobox(detFrame1B, width = 17, textvariable = self.studOS,
                                          height = 1)
        self.cboOS['values'] = ('Mac OS','Windows')
        self.cboOS.pack(side = TOP, pady = (5,3))

        lblGuardianName = Label(detFrame1A, width = 11, text  = 'P/G Name:', font = 'consolas 12 bold',
                           fg = 'white', bg = '#1d3557', anchor = W, justify = LEFT)
        lblGuardianName.pack(side = TOP, padx = 3, pady = 1)

        self.OneGuard = StringVar()

        self.entGuardianName = Entry(detFrame1B, width = 20, bg = 'white', fg = 'black', textvariable = self.OneGuard)
        self.entGuardianName.pack(side = TOP, pady = (5,3))

        lblGuardianType = Label(detFrame1A, width = 11, text  = 'Guardian:', font = 'consolas 12 bold',
                           fg = 'white', bg = '#1d3557', anchor = W, justify = LEFT)
        lblGuardianType.pack(side = TOP, padx = 3, pady = 1)

        self.OneGuardType = StringVar()

        self.entGuardianType = Entry(detFrame1B, width = 20, bg = 'white', fg = 'black',
                                     textvariable = self.OneGuardType)
        self.entGuardianType.pack(side = TOP, pady = (5,3))

        lblPGPhone = Label(detFrame1A, width = 11, text  = 'P/G Phone:', font = 'consolas 12 bold',
                           fg = 'white', bg = '#1d3557', anchor = W, justify = LEFT)
        lblPGPhone.pack(side = TOP, padx = 3, pady = 1)

        self.PGPhone = StringVar()

        self.entPGPhone = Entry(detFrame1B, width = 20, bg = 'white', fg = 'black', textvariable = self.PGPhone)
        self.entPGPhone.pack(side = TOP, pady = (5,3))

        lblPGEmail = Label(detFrame1A, width = 11, text  = 'P/G Email:', font = 'consolas 12 bold',
                           fg = 'white', bg = '#1d3557', anchor = W, justify = LEFT)
        lblPGEmail.pack(side = TOP, padx = 3, pady = 1)

        self.PGEmail = StringVar()

        self.entPGEmail = Entry(detFrame1B, width = 20, bg = 'white', fg = 'black', textvariable = self.PGEmail)
        self.entPGEmail.pack(side = TOP, pady = (5,3))

        lblClassReg = Label(detFrame1A, width = 11, text  = 'Enrolled:', font = 'consolas 12 bold',
                           fg = 'white', bg = '#1d3557', anchor = W, justify = LEFT)
        lblClassReg.pack(side = TOP, padx = 2, pady = 1)

        self.ClassReg = StringVar()

        self.cboClassReg = ttk.Combobox(detFrame1B, width = 17, textvariable = self.ClassReg,
                                          height = 2)
        self.cboClassReg['values'] = ('Level 1','Level 2','Level 3', 'Level 4',
                                      'Level 5','Level 6','Level 7', 'Level 8',
                                      'Level 9','Level 10','Level 11', 'Level 12',
                                      'Level 13','Level 14','Level 15', 'Level 16',)
        self.cboClassReg.pack(side = TOP, pady = (3,3))

        lblUserName = Label(detFrame1A, width = 11, text  = 'Username:', font = 'consolas 12 bold',
                           fg = 'white', bg = '#1d3557', anchor = W, justify = LEFT)
        lblUserName.pack(side = TOP, padx = 3, pady = 1)

        self.userName = StringVar()

        self.entUserName = Entry(detFrame1B, width = 20, bg = 'white', fg = 'black', textvariable = self.userName)
        self.entUserName.pack(side = TOP, pady = (5,3))

        lblPassword = Label(detFrame1A, width = 11, text  = 'Password:', font = 'consolas 12 bold',
                           fg = 'white', bg = '#1d3557', anchor = W, justify = LEFT)
        lblPassword.pack(side = TOP, padx = 3, pady = 1)

        self.passWord = StringVar()

        self.entPassWord = Entry(detFrame1B, width = 20, bg = 'white', fg = 'black', textvariable = self.passWord,
                                 show="*")
        self.entPassWord.pack(side = TOP, pady = (5,3))

        ################################################################################################
        ################################################################################################
        #################################################################################################
        #################################################################################################

        self.dataCanv = Canvas(self.rightFrame1A, width = 50, height = 170, bg = '#a9a9a9',
                               highlightbackground = '#a9a9a9')
        self.dataCanv.pack(side = LEFT)

        self.dataCanv2 = Canvas(self.rightFrame1C, width = 200, height = 370, bg = '#a9a9a9',
                                highlightbackground = '#a9a9a9')
        self.dataCanv2.pack(side = RIGHT)

        self.dataCanv3 = Canvas(self.rightFrame2, width = 100, height = 470, bg = '#a9a9a9',
                                highlightbackground = '#a9a9a9')
        self.rightFrame2.add(self.dataCanv3, stretch = 'never')
        self.rightFrame2.config(opaqueresize = False)

        self.dataCanv4 = Canvas(self.rightFrame2, width = 100, height = 470, bg = '#a9a9a9',
                                highlightbackground = '#a9a9a9')
        self.rightFrame2.add(self.dataCanv4, stretch = 'never')
        self.rightFrame2.config(opaqueresize = False)

        ############################################################################
        ############################################################################
        ############################################################################

        # This part checks if the file exists. So if the login password is incorrect.
        # Which means that the page should begin with an empty file at the get go
        file_exists = os.path.exists('events.txt')
        if not file_exists:
            with open('events.txt', 'w', newline = '') as f:
                writer = csv.writer(f)

        ################################################################################

        self.student1 = 'Lannon Khau'
        header = [self.student1, 'Mission No.', 'Date','Application', 'Readability', 'Quality',
                  'Creativity', 'Cleanliness', 'Content', 'Originality','Body Language', 'Structure', 'Delivery',
                  'Google C.', 'Teachable', 'Quiz Taken', 'Presentation Check', 'Officer', 'Notes',
                  'Planet Acquired','Planet Name','Planet Type']

        file_exists = os.path.exists('missionRecords4.csv')
        if not file_exists:
            with open('missionRecords4.csv', 'w', newline = '') as f:
                writer = csv.writer(f)
                writer.writerow(header)

        self.btnRefresh = Button(self.rightTitle, width=8, height=1, text='Refresh',
                                 font='consolas 10 ', bg='grey30', fg='white',bd = 3,
                                 command=self.refresh)
        self.btnRefresh.place(x=902, y=10)

        self.btnRegister = Button(self.rightTitle, width=8, height=1, text='Register',
                                 font='consolas 10 ', bg='grey30', fg='white',bd = 3,
                                  command = self.register)
        self.btnRegister.place(x=830, y=10)

        self.btnLogin1 = Button(self.rightTitle, width=8, height=1, text='Login',
                                 font='consolas 10 ', bg='grey30', fg='white',bd = 3,
                               command = self.login)
        self.btnLogin1.place(x=758, y=10)

        file_exists = os.path.exists('studentRegister.csv')
        if not file_exists:
            self.btnRegister.configure(state = NORMAL)
        else:
            self.btnRegister.configure(state = DISABLED)

        self.canvTask = Canvas(self.rightFrame3B, width = 585, height = 180, bg = 'grey80',
                               highlightbackground = 'grey', relief = RAISED, bd = 4)
        self.canvTask.pack()

        self.canvTask.create_text(25,25,anchor = 'w', fill = 'orange', font = 'consolas 12 bold')

        #######################################################################################################
        #######################################################################################################
        # Place a label Here to show Total Scores

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('red.Horizontal.TProgressbar', background='#1F487E',
                    troughcolor='black', bordercolor='white',
                    darkcolor='black')


        #self.get_avail_scores()
        # if self.grand_avail_total == 0:
        #     self.grand_avail_total = 1

        self.availPointsProjects = 0
        self.totalPointsProjects = 1
        self.progressProjects = ttk.Progressbar(self.rightFrame3A1, orient = 'horizontal',
                                                mode = 'determinate', length = 220,
                                                style='red.Horizontal.TProgressbar')
        self.progressProjects.pack(side = TOP, padx = 8, pady = (15,0))
        ## Testing
        self.progressProjects['value'] = (self.availPointsProjects / self.totalPointsProjects) * 100
        self.lblPBProjects = Label(self.rightFrame3A1, width = 320, height = 1,
                            text = 'Mission Objectives Score: ' + f'{self.availPointsProjects}/{self.totalPointsProjects}',
                            font = 'consolas 10',
                            bg = 'grey80')
        self.lblPBProjects.pack(side = TOP, padx = 8)
        #++++++++
        # self.availPointsTests = 0
        # self.totalPointsTests = 1
        # self.progressTests = ttk.Progressbar(self.rightFrame3A1, orient = 'horizontal',
        #                                         mode = 'determinate', length = 320,
        #                                      style='red.Horizontal.TProgressbar')
        # self.progressTests.pack(side = TOP, padx = 8)
        #
        # self.progressTests['value'] = (self.availPointsTests / self.totalPointsTests) * 100
        # self.lblPBTests = Label(self.rightFrame3A1, width = 320, height = 1,
        #                         text='Tests Score Percentage: ' + f'{self.availPointsTests}/{self.totalPointsTests}',
        #                         font = 'consolas 10',
        #                         bg = 'grey80')
        # self.lblPBTests.pack(side=TOP, padx=8)
        #++++++++
        # if self.grand_avail_total_present == 0:
        #     self.grand_avail_total_present = 1

        self.availPointsParts = 0
        self.totalPointsParts = 1

        self.progressPart = ttk.Progressbar(self.rightFrame3A1, orient = 'horizontal',
                                                mode = 'determinate', length = 220,
                                            style='red.Horizontal.TProgressbar')
        self.progressPart.pack(side = TOP, padx = 8)
        self.progressPart['value'] = (self.availPointsParts / self.totalPointsParts) * 100
        self.lblPBPart = Label(self.rightFrame3A1, width=320, height=1,
                               text='Presentation Score: ' + f'{self.availPointsParts}/{self.totalPointsParts}',
                               font='consolas 10',
                               bg = 'grey80')
        self.lblPBPart.pack(side=TOP, padx=8)

        # ++++++++

        self.availPointsTotal = 0
        self.totalPointsGrand = 1
        self.progressTotalScore = ttk.Progressbar(self.rightFrame3A1, orient = 'horizontal',
                                                mode = 'determinate', length = 220,
                                                  style='red.Horizontal.TProgressbar')
        self.progressTotalScore.pack(side = TOP, padx = 8)
        self.progressTotalScore['value'] = (self.availPointsTotal / self.totalPointsGrand) * 100
        self.lblPBTotalScore = Label(self.rightFrame3A1, width=320, height=1,
                               text='Total Score: ' + f'{self.availPointsTotal}/{self.totalPointsGrand}',
                               font='consolas 10',
                               bg = 'grey80')
        self.lblPBTotalScore.pack(side=TOP, padx=8)

        #____________________________________________________________________________

        # panedWindow = PanedWindow(self.rightFrame3A , relief = SOLID, bd = 0,
        #                           width = 150, height = 215, bg = 'grey75')
        # panedWindow.pack(side = RIGHT)

        self.letterCanv = Canvas(self.rightFrame3A, width = 145, height = 210, relief = RAISED,
                            bd = 5, bg = 'grey75')
        self.letterCanv.pack(side = RIGHT)

        self.letterRank = 'X'
        self.letterPerc = 'X%'

        self.canvText = self.letterCanv.create_text(71, 47, text=self.letterRank, font='Helvetica 30 bold')
        self.letterCanv.create_line(28, 75, 106, 75, fill="black", width=5)
        self.canvText2 = self.letterCanv.create_text(67, 105, text=self.letterPerc, font='Helvetica 30 bold')


        # self.rank_imgA = ImageTk.PhotoImage(Image.open('images/rank_img1.png'))
        # self.letterCanv.create_image(25, 165, anchor = W, image = self.rank_imgA)

        ###############################################################################################################
        ###############################################################################################################
        ###############################################################################################################
        ###############################################################################################################
        ###############################################################################################################

        #Veginning Notebook3 stuff

        # invTopFrame = Frame(TabControl3, width = 1260, height = 785, relief = SUNKEN, bd = 5,
        #                     bg = 'grey75')
        # invTopFrame.pack()

        # Can you add a scrollbar to a canvas?

        ###############################################################################################################
        ###############################################################################################################
        ###############################################################################################################
        ###############################################################################################################
        ###############################################################################################################

        # Create a first save checker
        self.firstSave = 0
        self.countOne = ''
        self.clicked = 1
        self.is_on = False
        self.anim_tracker = 0
        self.planet_tracker = 0
        self.task_tracker = 0
        #self.enterMission1 = 0
        self.chatBox1 = StringVar()
        self.Miss1 = IntVar()

        ############################# Main Frame Statuses ########################################
        # rightMiss Frames
        self.rightMissFrames = False

        # The notes text box
        self.txtNotesOn = False

        # The notes display on lblTest
        self.lblTestbox = True

        # The code display is on
        self.sourceOn = False

        ##########################################################################################

        self.all_commands = ['/open_notes.exe','123456','/take_notes.exe','/save_note','/open_source.txt',
                             '/planet_inv.exe']

        self.scale1 = IntVar()
        self.scale2 = IntVar()
        self.scale3 = IntVar()
        self.scale4 = IntVar()
        self.scale5 = IntVar()
        self.scale6 = IntVar()
        self.scale7 = IntVar()
        self.scale8 = IntVar()
        self.scale9 = IntVar()
        self.scale10 = IntVar()

        self.GclassCheck = IntVar()
        self.teachCheck = IntVar()
        self.QuizCheck = IntVar()
        self.CritCheck = IntVar()
        self.CC_Officers = StringVar()

        # Mission 2 Key Players and Actors ############################################################
        self.TwoScale1 = IntVar()
        self.TwoScale2 = IntVar()
        self.TwoScale3 = IntVar()
        self.TwoScale4 = IntVar()
        self.TwoScale5 = IntVar()
        self.TwoScale6 = IntVar()
        self.TwoScale7 = IntVar()
        self.TwoScale8 = IntVar()
        self.TwoScale9 = IntVar()
        self.TwoScale10 = IntVar()

        self.TwoGClassCheck = IntVar()
        self.TwoTeachCheck = IntVar()
        self.TwoQuizCheck = IntVar()
        self.TwoCritCheck = IntVar()
        self.TwoCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.ThreeScale1 = IntVar()
        self.ThreeScale2 = IntVar()
        self.ThreeScale3 = IntVar()
        self.ThreeScale4 = IntVar()
        self.ThreeScale5 = IntVar()
        self.ThreeScale6 = IntVar()
        self.ThreeScale7 = IntVar()
        self.ThreeScale8 = IntVar()
        self.ThreeScale9 = IntVar()
        self.ThreeScale10 = IntVar()

        self.ThreeGClassCheck = IntVar()
        self.ThreeTeachCheck = IntVar()
        self.ThreeQuizCheck = IntVar()
        self.ThreeCritCheck = IntVar()
        self.ThreeCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.FourScale1 = IntVar()
        self.FourScale2 = IntVar()
        self.FourScale3 = IntVar()
        self.FourScale4 = IntVar()
        self.FourScale5 = IntVar()
        self.FourScale6 = IntVar()
        self.FourScale7 = IntVar()
        self.FourScale8 = IntVar()
        self.FourScale9 = IntVar()
        self.FourScale10 = IntVar()

        self.FourGClassCheck = IntVar()
        self.FourTeachCheck = IntVar()
        self.FourQuizCheck = IntVar()
        self.FourCritCheck = IntVar()
        self.FourCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.FiveScale1 = IntVar()
        self.FiveScale2 = IntVar()
        self.FiveScale3 = IntVar()
        self.FiveScale4 = IntVar()
        self.FiveScale5 = IntVar()
        self.FiveScale6 = IntVar()
        self.FiveScale7 = IntVar()
        self.FiveScale8 = IntVar()
        self.FiveScale9 = IntVar()
        self.FiveScale10 = IntVar()

        self.FiveGClassCheck = IntVar()
        self.FiveTeachCheck = IntVar()
        self.FiveQuizCheck = IntVar()
        self.FiveCritCheck = IntVar()
        self.FiveCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.SixScale1 = IntVar()
        self.SixScale2 = IntVar()
        self.SixScale3 = IntVar()
        self.SixScale4 = IntVar()
        self.SixScale5 = IntVar()
        self.SixScale6 = IntVar()
        self.SixScale7 = IntVar()
        self.SixScale8 = IntVar()
        self.SixScale9 = IntVar()
        self.SixScale10 = IntVar()

        self.SixGClassCheck = IntVar()
        self.SixTeachCheck = IntVar()
        self.SixQuizCheck = IntVar()
        self.SixCritCheck = IntVar()
        self.SixCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.SevenScale1 = IntVar()
        self.SevenScale2 = IntVar()
        self.SevenScale3 = IntVar()
        self.SevenScale4 = IntVar()
        self.SevenScale5 = IntVar()
        self.SevenScale6 = IntVar()
        self.SevenScale7 = IntVar()
        self.SevenScale8 = IntVar()
        self.SevenScale9 = IntVar()
        self.SevenScale10 = IntVar()

        self.SevenGClassCheck = IntVar()
        self.SevenTeachCheck = IntVar()
        self.SevenQuizCheck = IntVar()
        self.SevenCritCheck = IntVar()
        self.SevenCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.EightScale1 = IntVar()
        self.EightScale2 = IntVar()
        self.EightScale3 = IntVar()
        self.EightScale4 = IntVar()
        self.EightScale5 = IntVar()
        self.EightScale6 = IntVar()
        self.EightScale7 = IntVar()
        self.EightScale8 = IntVar()
        self.EightScale9 = IntVar()
        self.EightScale10 = IntVar()

        self.EightGClassCheck = IntVar()
        self.EightTeachCheck = IntVar()
        self.EightQuizCheck = IntVar()
        self.EightCritCheck = IntVar()
        self.EightCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.NineScale1 = IntVar()
        self.NineScale2 = IntVar()
        self.NineScale3 = IntVar()
        self.NineScale4 = IntVar()
        self.NineScale5 = IntVar()
        self.NineScale6 = IntVar()
        self.NineScale7 = IntVar()
        self.NineScale8 = IntVar()
        self.NineScale9 = IntVar()
        self.NineScale10 = IntVar()

        self.NineGClassCheck = IntVar()
        self.NineTeachCheck = IntVar()
        self.NineQuizCheck = IntVar()
        self.NineCritCheck = IntVar()
        self.NineCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.TenScale1 = IntVar()
        self.TenScale2 = IntVar()
        self.TenScale3 = IntVar()
        self.TenScale4 = IntVar()
        self.TenScale5 = IntVar()
        self.TenScale6 = IntVar()
        self.TenScale7 = IntVar()
        self.TenScale8 = IntVar()
        self.TenScale9 = IntVar()
        self.TenScale10 = IntVar()

        self.TenGClassCheck = IntVar()
        self.TenTeachCheck = IntVar()
        self.TenQuizCheck = IntVar()
        self.TenCritCheck = IntVar()
        self.TenCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.ElevenScale1 = IntVar()
        self.ElevenScale2 = IntVar()
        self.ElevenScale3 = IntVar()
        self.ElevenScale4 = IntVar()
        self.ElevenScale5 = IntVar()
        self.ElevenScale6 = IntVar()
        self.ElevenScale7 = IntVar()
        self.ElevenScale8 = IntVar()
        self.ElevenScale9 = IntVar()
        self.ElevenScale10 = IntVar()

        self.ElevenGClassCheck = IntVar()
        self.ElevenTeachCheck = IntVar()
        self.ElevenQuizCheck = IntVar()
        self.ElevenCritCheck = IntVar()
        self.ElevenCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.TwelveScale1 = IntVar()
        self.TwelveScale2 = IntVar()
        self.TwelveScale3 = IntVar()
        self.TwelveScale4 = IntVar()
        self.TwelveScale5 = IntVar()
        self.TwelveScale6 = IntVar()
        self.TwelveScale7 = IntVar()
        self.TwelveScale8 = IntVar()
        self.TwelveScale9 = IntVar()
        self.TwelveScale10 = IntVar()

        self.TwelveGClassCheck = IntVar()
        self.TwelveTeachCheck = IntVar()
        self.TwelveQuizCheck = IntVar()
        self.TwelveCritCheck = IntVar()
        self.TwelveCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.ThirteenScale1 = IntVar()
        self.ThirteenScale2 = IntVar()
        self.ThirteenScale3 = IntVar()
        self.ThirteenScale4 = IntVar()
        self.ThirteenScale5 = IntVar()
        self.ThirteenScale6 = IntVar()
        self.ThirteenScale7 = IntVar()
        self.ThirteenScale8 = IntVar()
        self.ThirteenScale9 = IntVar()
        self.ThirteenScale10 = IntVar()

        self.ThirteenGClassCheck = IntVar()
        self.ThirteenTeachCheck = IntVar()
        self.ThirteenQuizCheck = IntVar()
        self.ThirteenCritCheck = IntVar()
        self.ThirteenCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.FourteenScale1 = IntVar()
        self.FourteenScale2 = IntVar()
        self.FourteenScale3 = IntVar()
        self.FourteenScale4 = IntVar()
        self.FourteenScale5 = IntVar()
        self.FourteenScale6 = IntVar()
        self.FourteenScale7 = IntVar()
        self.FourteenScale8 = IntVar()
        self.FourteenScale9 = IntVar()
        self.FourteenScale10 = IntVar()

        self.FourteenGClassCheck = IntVar()
        self.FourteenTeachCheck = IntVar()
        self.FourteenQuizCheck = IntVar()
        self.FourteenCritCheck = IntVar()
        self.FourteenCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.FifteenScale1 = IntVar()
        self.FifteenScale2 = IntVar()
        self.FifteenScale3 = IntVar()
        self.FifteenScale4 = IntVar()
        self.FifteenScale5 = IntVar()
        self.FifteenScale6 = IntVar()
        self.FifteenScale7 = IntVar()
        self.FifteenScale8 = IntVar()
        self.FifteenScale9 = IntVar()
        self.FifteenScale10 = IntVar()

        self.FifteenGClassCheck = IntVar()
        self.FifteenTeachCheck = IntVar()
        self.FifteenQuizCheck = IntVar()
        self.FifteenCritCheck = IntVar()
        self.FifteenCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.SixteenScale1 = IntVar()
        self.SixteenScale2 = IntVar()
        self.SixteenScale3 = IntVar()
        self.SixteenScale4 = IntVar()
        self.SixteenScale5 = IntVar()
        self.SixteenScale6 = IntVar()
        self.SixteenScale7 = IntVar()
        self.SixteenScale8 = IntVar()
        self.SixteenScale9 = IntVar()
        self.SixteenScale10 = IntVar()

        self.SixteenGClassCheck = IntVar()
        self.SixteenTeachCheck = IntVar()
        self.SixteenQuizCheck = IntVar()
        self.SixteenCritCheck = IntVar()
        self.SixteenCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.SeventeenScale1 = IntVar()
        self.SeventeenScale2 = IntVar()
        self.SeventeenScale3 = IntVar()
        self.SeventeenScale4 = IntVar()
        self.SeventeenScale5 = IntVar()
        self.SeventeenScale6 = IntVar()
        self.SeventeenScale7 = IntVar()
        self.SeventeenScale8 = IntVar()
        self.SeventeenScale9 = IntVar()
        self.SeventeenScale10 = IntVar()

        self.SeventeenGClassCheck = IntVar()
        self.SeventeenTeachCheck = IntVar()
        self.SeventeenQuizCheck = IntVar()
        self.SeventeenCritCheck = IntVar()
        self.SeventeenCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.EighteenScale1 = IntVar()
        self.EighteenScale2 = IntVar()
        self.EighteenScale3 = IntVar()
        self.EighteenScale4 = IntVar()
        self.EighteenScale5 = IntVar()
        self.EighteenScale6 = IntVar()
        self.EighteenScale7 = IntVar()
        self.EighteenScale8 = IntVar()
        self.EighteenScale9 = IntVar()
        self.EighteenScale10 = IntVar()

        self.EighteenGClassCheck = IntVar()
        self.EighteenTeachCheck = IntVar()
        self.EighteenQuizCheck = IntVar()
        self.EighteenCritCheck = IntVar()
        self.EighteenCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.NineteenScale1 = IntVar()
        self.NineteenScale2 = IntVar()
        self.NineteenScale3 = IntVar()
        self.NineteenScale4 = IntVar()
        self.NineteenScale5 = IntVar()
        self.NineteenScale6 = IntVar()
        self.NineteenScale7 = IntVar()
        self.NineteenScale8 = IntVar()
        self.NineteenScale9 = IntVar()
        self.NineteenScale10 = IntVar()

        self.NineteenGClassCheck = IntVar()
        self.NineteenTeachCheck = IntVar()
        self.NineteenQuizCheck = IntVar()
        self.NineteenCritCheck = IntVar()
        self.NineteenCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.TwentyScale1 = IntVar()
        self.TwentyScale2 = IntVar()
        self.TwentyScale3 = IntVar()
        self.TwentyScale4 = IntVar()
        self.TwentyScale5 = IntVar()
        self.TwentyScale6 = IntVar()
        self.TwentyScale7 = IntVar()
        self.TwentyScale8 = IntVar()
        self.TwentyScale9 = IntVar()
        self.TwentyScale10 = IntVar()

        self.TwentyGClassCheck = IntVar()
        self.TwentyTeachCheck = IntVar()
        self.TwentyQuizCheck = IntVar()
        self.TwentyCritCheck = IntVar()
        self.TwentyCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.TwentyOneScale1 = IntVar()
        self.TwentyOneScale2 = IntVar()
        self.TwentyOneScale3 = IntVar()
        self.TwentyOneScale4 = IntVar()
        self.TwentyOneScale5 = IntVar()
        self.TwentyOneScale6 = IntVar()
        self.TwentyOneScale7 = IntVar()
        self.TwentyOneScale8 = IntVar()
        self.TwentyOneScale9 = IntVar()
        self.TwentyOneScale10 = IntVar()

        self.TwentyOneGClassCheck = IntVar()
        self.TwentyOneTeachCheck = IntVar()
        self.TwentyOneQuizCheck = IntVar()
        self.TwentyOneCritCheck = IntVar()
        self.TwentyOneCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.TwentyTwoScale1 = IntVar()
        self.TwentyTwoScale2 = IntVar()
        self.TwentyTwoScale3 = IntVar()
        self.TwentyTwoScale4 = IntVar()
        self.TwentyTwoScale5 = IntVar()
        self.TwentyTwoScale6 = IntVar()
        self.TwentyTwoScale7 = IntVar()
        self.TwentyTwoScale8 = IntVar()
        self.TwentyTwoScale9 = IntVar()
        self.TwentyTwoScale10 = IntVar()

        self.TwentyTwoGClassCheck = IntVar()
        self.TwentyTwoTeachCheck = IntVar()
        self.TwentyTwoQuizCheck = IntVar()
        self.TwentyTwoCritCheck = IntVar()
        self.TwentyTwoCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.TwentyThreeScale1 = IntVar()
        self.TwentyThreeScale2 = IntVar()
        self.TwentyThreeScale3 = IntVar()
        self.TwentyThreeScale4 = IntVar()
        self.TwentyThreeScale5 = IntVar()
        self.TwentyThreeScale6 = IntVar()
        self.TwentyThreeScale7 = IntVar()
        self.TwentyThreeScale8 = IntVar()
        self.TwentyThreeScale9 = IntVar()
        self.TwentyThreeScale10 = IntVar()

        self.TwentyThreeGClassCheck = IntVar()
        self.TwentyThreeTeachCheck = IntVar()
        self.TwentyThreeQuizCheck = IntVar()
        self.TwentyThreeCritCheck = IntVar()
        self.TwentyThreeCC_Officers = StringVar()
        # Mission 3 Key Players and Actors ############################################################
        self.TwentyFourScale1 = IntVar()
        self.TwentyFourScale2 = IntVar()
        self.TwentyFourScale3 = IntVar()
        self.TwentyFourScale4 = IntVar()
        self.TwentyFourScale5 = IntVar()
        self.TwentyFourScale6 = IntVar()
        self.TwentyFourScale7 = IntVar()
        self.TwentyFourScale8 = IntVar()
        self.TwentyFourScale9 = IntVar()
        self.TwentyFourScale10 = IntVar()

        self.TwentyFourGClassCheck = IntVar()
        self.TwentyFourTeachCheck = IntVar()
        self.TwentyFourQuizCheck = IntVar()
        self.TwentyFourCritCheck = IntVar()
        self.TwentyFourCC_Officers = StringVar()
        # Mission Strings##############################################################################

        self.commands = '''
1. /open_notes.exe
2. /take_notes.exe
3. /save_note
4. /planet_inv.exe
5. passkey
'''
        self.com_planet1_desc = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Planet Name: Vinci                  \n\
        ⮞ Planet Type: Super Earth              \n\
        ⮞ Rarity: Common Planet            \n\
        ⮞ Planet Size: 38.9 times Earth          \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Planet Description]: The planet Vinci, named after a 
 famous scientist, is a terrestial planet in a fairly 
 small solar system with seven other planets. Vinci is 
 about 38.9 times bigger than Earth and its gravity is 
 about 10.96 times that of Earth.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Living Organisms]: The plant-like organisms on this 
 planet are exclusively various types of fungi. Many are 
 small, much like you'd find on Earth. But others are 
 towering high above the clouds, similar to trees on 
 Earth.

 Although diverse in colors, shapes and sizes, none of 
 the organisms have developed much. Most are still in a 
 very crude form and those that did start to develop 
 specialized parts have still a long way to go.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.com_planet2_desc = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Planet Name: Skaro                  \n\
        ⮞ Planet Type: Super Earth              \n\
        ⮞ Rarity: Common Planet            \n\
        ⮞ Planet Size: 6.0 times Earth          \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Planet Description]: The planet Skaro, named after a 
famous scientist, is a terrestrial planet in a densely 
populated solar system with twenty-two other planets.

Skaro is about 6.0 times bigger than Earth and its 
gravity is about 1.83 times that of Earth.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Living Organisms]: By far the most interesting animals 
on this planet are the aquatic mammals. They may not be 
as majestic as the birds or as fierce as some of the 
land mammals, but they are the only species who have a 
sentient member. This member of the aquatic species is 
roughly comparable to a mixture of seals and squids. 
They form huge colonies and actively take care of each 
other. They even build makeshift homes out of the 
available materials on the sea floors.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.com_planet3_desc = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Planet Name: Krypton                  \n\
        ⮞ Planet Type: Super Earth              \n\
        ⮞ Rarity: Common Planet            \n\
        ⮞ Planet Size: 30.6 times Earth          \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Planet Description]: The planet Krypton, named so for 
 the planet's properties, is an iron planet in a small 
 solar system with ten other planets. Krypton is about 
 30.6 times bigger than Earth and its gravity is about 
 6.79 times that on Earth. 

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Living Organisms]: Many of the creatures on this planet
 have evolved into gliders, so to speak. Most of the 
 fish and aquatic mammals, despite coming in various 
 shapes and sizes, tend to glide through the water 
 without effort, similar to how manta's glide on Earth. 
 However, the surface species are more astonishing. 
 Similar to the flying squirrels or the vultures of 
 Earth, many of the species on this planet have 
 developed ways to effortlessly move from one place to 
 another by using the winds. But there is one species 
 which shows signs of sentience. These species, a type 
 of bird, love to play and have become masters of 
 flight. Similar to how dolphins play, explore and 
 learn, these species use their intellect and courage 
 to play and sometimes challenge each other to death 
 defying tricks.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.rar_planet1_desc = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Planet Name: Naboo                  \n\
        ⮞ Planet Type: Super Earth              \n\
        ⮞ Rarity: Rare Planet            \n\
        ⮞ Planet Size: 2.40 times Earth          \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Planet Description]: The planet Naboo, as it's called 
 by most scientists, is a terrestial planet in a vast 
 solar system with twenty-seven other planets. Naboo is 
 about 0.8 times bigger than Earth and its gravity is 
 about 2.40 times that of Earth.

 A single day lasts 22.02 hours and a year lasts 130 
 days. The planet is made up of 3 continents, which 
 make up 80% of the planet's landmass.
 5 moon(s) orbit the planet and Naboo itself orbits a 
 red sun in a circular orbit.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Living Organisms]: Amphibians are the rulers of this 
 planet. While none of them are sentient, their shapes, 
 sizes and ways of life makes them interesting 
 nonetheless. Many of them are colorful, much like the 
 chameleon's of Earth, but their sizes are close to that 
 of the smaller dinosaurs. They share this planet with 
 plenty of insects and fish, but the amphibians are far 
 more numerous and advanced than the other species.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.rar_planet2_desc = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Planet Name: Omicron Persei 8          \n\
        ⮞ Planet Type: Gaseous Super Earth        \n\
        ⮞ Rarity: Rare Planet                      \n\
        ⮞ Planet Size: 7.20 times Earth           \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Planet Description]: The planet Omicron Persei 8, named 
 so for its similarities to the fictional version, is an 
 iron planet in a densely populated solar system with 
 seventeen other planets. Omicron Persei 8 is about 7.2 
 times bigger than Earth and its gravity is about 4.80 
 times that of Earth. A single day lasts 16.25 hours and 
 a year lasts 444 days. The planet is made up of 4 
 continents, which make up 76% of the planet's landmass. 
 3 moons orbit the planet and Omicron Persei 8 itself 
 orbits a red sun in a fairly circular orbit.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Living Organisms]: Hidden in the depths of this planet's
 oceans are a species of sentient creatures who made 
 their home in the most hostile environments imaginable. 
 These creatures look like a cross between jellyfish and 
 giant squids, but have the intelligence comparable to 
 that of dolphins. These intelligent creatures are 
 surrounded by a plethora of fish, crustaceans and other 
 aquatic creatures unseen on Earth. 
 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.rar_planet3_desc = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Planet Name: Amazonia          \n\
        ⮞ Planet Type: Carbon Planet        \n\
        ⮞ Rarity: Rare Planet                      \n\
        ⮞ Planet Size: 7.20 times Earth           \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Planet Description]: A single day lasts 16.40 hours and 
 a year lasts 156 days. The planet is made up of 13 
 continents, which make up 70% of the planet's landmass.
 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Living Organisms]: Hidden in the depths of this 
 planet's water are many gorgeous corals. Almost every 
 species is completely different from the other. 
 Hundreds, if not thousands of shapes and sizes and 
 countless of colors make the underwater world an 
 amazing spectacle. However, finding these spectacles is 
 difficult, as they only seem to grow in very specific 
 places with the right conditions.
 By far the most interesting animals on this planet are 
 the aquatic mammals. They may not be as majestic as the 
 birds or as fierce as some of the land mammals, but 
 they are the only species who have a sentient member. 
 This member of the aquatic species is roughly 
 comparable to a mixture of seals and squids. They form
 huge colonies and actively take care of each other. 
 They even build makeshift homes out of the available 
 materials on the sea floors. 
 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.ult_planet1_desc = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Planet Name: Wormulon         \n\
        ⮞ Planet Type: Ice Planet        \n\
        ⮞ Rarity: Ultra Rare Planet       \n\
        ⮞ Planet Size: 10.50 times Earth           \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Planet Description]: The planet Wormulon, as it's 
 called by most of the natives, is an ice planet in a 
 thinly populated solar system with only five other 
 planets. Wormulon is about 10.5 times bigger than Earth 
 and its gravity is about 3.98 times that of Earth.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Living Organisms]: The underwater plants too are not 
 much more than the very basic lifeforms you'd expect on 
 young planets, but their colors are suprisingly varied 
 and bright. A handful of species is already showing the 
 first steps to higher organism forms, but they have 
 still a long way to go.
 
 Insects, insects and more insects. That's what you'll 
 find on this planet in terms of animal life. There are 
 a few dozen fish species, but everything else is either 
 a microbe or an insect. However, the insects on this 
 planet are gorgeous and thanks to the right conditions, 
 most of the insects are enormous.
 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.ult_planet2_desc = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Planet Name: Tatooine         \n\
        ⮞ Planet Type: Terrestrial Planet        \n\
        ⮞ Rarity: Ultra Rare Planet              \n\
        ⮞ Planet Size: 2.10 times Earth           \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Planet Description]: A single day lasts 16.52 hours and 
 a year lasts 189 days. The planet is made up of 14 
 continents, which make up 12% of the planet's landmass.
 2 moons orbit the planet and Tatooine itself orbits a 
 blue sun in a circular orbit.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Living Organisms]: The water plants on this planet are 
 very different from what we're used to on Earth. While 
 they roughly share the same colors, or lack thereof, 
 these plants have developed into mostly flesh eating 
 species. Almost no aquatic creature is safe, even the 
 bigger ones can sometimes get caught in these death 
 traps.

 War is something that has been part of human history 
 since its dawn and while humans aren't the only 
 species who engage in war, they are by far the most 
 skilled in it. This planet is no different. The higher 
 intelligence of these sentient species has 
 unfortunately lead to almost nothing but war. 
 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.hyp_planet1_desc = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Planet Name: Tarantulon         \n\
        ⮞ Planet Type: Terrestrial Planet        \n\
        ⮞ Rarity: Hyper Rare Planet              \n\
        ⮞ Planet Size: 20.6 times Earth           \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Planet Description]: The planet Tarantulon, named so by 
 its discoverer, is a terrestial planet in a huge solar 
 system filled with fourteen other planets. Tarantulon 
 is about 20.6 times bigger than Earth and its gravity 
 is about 7.78 times that of Earth.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Living Organisms]: Almost all organisms want to prevent 
 being eaten and many do so by growing thorns or 
 excreting horrible tasting fluids, but there's one 
 species which, in a way, needs to be eaten to make 
 sure the species survives. Once this species has grown 
 to a mature size, it will stop regrowing. Instead it 
 will begin storing energy, which makes it more 
 appealing to animals. Once animals begin eating it and 
 eat enough of it, the energy stored deep within will 
 be transferred to all the seeds, which will be 
 released simultaneously. The seeds get stuck to the 
 animals, who are too busy eating the parent, and are 
 taken with them. The extra energy stored within them 
 will give a temporary growth boost in the vital first 
 weeks.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.hyp_planet2_desc = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Planet Name: IO         \n\
        ⮞ Planet Type: Terrestrial Planet        \n\
        ⮞ Rarity: Hyper Rare Planet              \n\
        ⮞ Planet Size: 20.6 times Earth           \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Planet Description]: A single day lasts 39.96 hours and 
 a year lasts 429 days. The planet is made up of 1 
 continents, which make up 66% of the planet's landmass.
 5 moons orbit the planet and Vinci itself orbits an 
 orange sun in an almost perfectly circular orbit.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Living Organisms]: When we think of higher intelligence 
 on other planets we often think of technologically 
 advanced species in a world far beyond that of ours. 
 Unfortunately, this planet is nothing like that. The 
 intelligent species on this planet, though intelligent, 
 aren't much more advanced than humans were during the 
 late stone age. While they do have a language, they 
 have yet to create a written version of it, which makes 
 potential communications between them and other alien 
 species a bigger challenge. These species do show a 
 great interest in space, they adore and often worship 
 the night sky, many of them even make crude drawings 
 of constellations, the surrounding planets and their 
 moons.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.hyp_planet3_desc = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Planet Name: Draconis         \n\
        ⮞ Planet Type: Lava World        \n\
        ⮞ Rarity: Hyper Rare Planet        \n\
        ⮞ Planet Size: 13.0 times Earth      \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Planet Description]: A single day lasts 26.35 hours and 
 a year lasts 131 days. The planet is made up of 7 
 continents, which make up 40% of the planet's landmass.
 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Living Organisms]: The intelligent lifeforms on this 
 planet are comparable to the humans of the bronze age, 
 except that they are already more inclined to try to 
 explain the mysteries of their world. 
 
 Unfortunately ,they are quite violent, so they tend to 
 live in smaller communities which they will protect at 
 all costs. There are no signs of teamwork between the 
 different communities, which would've been of benefit 
 to them. This could lead to interesting developments 
 in language and customs, but only time will tell how 
 this will turn out.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.god_planet1_desc = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Planet Name: Eternium         \n\
        ⮞ Planet Type: Celestial Anamoly        \n\
        ⮞ Rarity: God Tier Planet                 \n\
        ⮞ Planet Size: 203.4 times Earth           \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Planet Description]: The planet Eternium, as it's 
 called by most scientists, is an iron planet in a 
 thinly populated solar system with only six other 
 planets. Eternium is about 203.4 times bigger than 
 Earth and its gravity is about 0.39 times that of Earth.

 A single day lasts 38.44 hours and a year lasts 489 
 days. The planet is made up of 1 continents, which 
 make up 27% of the planet's landmass. 3 moon(s) orbit 
 the planet and Eternium itself orbits an orange sun 
 in a fairly circular orbit.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Living Organisms]: Although diverse in colors, shapes 
 and sizes, none of the organisms have developed much. 
 Most are still in a very crude form and those that did 
 start to develop specialized parts have still a long 
 way to go.
    
 Some Ancient Astronaut Theorists believe that Eternium 
 is the home to a singular or multiple celestial god-like
 beings because of the sudden shifts of observable 
 physics that take place on this planet. It is not yet 
 known the origin of these phenomenons. Microbes are 
 often observed to undergo series of evolutionary 
 changes within a matter of seconds that would normally 
 take eons. 

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''

        self.mission_statement1A = '''              
[Space Force Armada Commander]:\n
Welcome to the Space Force, Space Cadet. You have been hand picked to complete a set of rigorous yet exciting series of missions that will test your skills. Sending you mission details now. 
'''
        self.mission_statement1B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #001         \n\
        ⮞ Mission Name: Hello First Name      \n\
        ⮞ Difficulty: ✦             \n\
        ⮞ Save File: objectives/objective1.py    \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Concepts Acquired]: Variables, Datatypes, 
 Print Statements, Input Statements. 

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user's first name and 
 display the output message.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter your first name: Lannon

[Output Message]: 

    ⮞ Welcome, Lannon

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement2A = '''              
[Space Force Armada Commander]:\n
Well done! You've completed your first Mission Objective. \
In this next mission, you'll learn how to combine two \
strings together using concatenation. 
'''
        self.mission_statement2B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #002         \n\
        ⮞ Mission Name: Hello Full Name      \n\
        ⮞ Difficulty: ✦             \n\
        ⮞ Save File: objectives/objective2.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Concepts Acquired]: Variables, Datatypes, 
 Print Statements, Input Statements. 

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user's first name and then 
 ask the user's last name. Then display the output 
 message: 

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter your first name: Lannon
    ⮞ Please enter your Khau name: Khau

[Output Message]: 

    ⮞ Welcome, Lannon Khau

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

'''
        self.mission_statement3A = '''              
[Space Force Armada Commander]:\n
Congratulations! In this next Mission Objective, you'll \
be able to display more than one line of output using \
only one line of code! Its called a multi-line string. 
'''
        self.mission_statement3B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #003         \n\
        ⮞ Mission Name: Tell a Joke      \n\
        ⮞ Difficulty: ✦             \n\
        ⮞ Save File: objectives/objective3.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Concepts Acquired]: String Manipulation, multiline 
 strings. 

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Write code that will display the 
 joke "Knock Knock" and on the next line "Whose there?" 
 and on the next line "Orange" and on the next line 
 "Orange who? and on the last line "Orange you glad I 
 brought skittles?". Hint: use only one line of code 
 to display five output messages.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Output Message]: 

    ⮞ Knock Knock
      Whose there?
      Orange
      Orange who?
      Orange you glad I brought skittles? 

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement4A = '''
[Space Force Armada Commander]:\n
Great work. You're doing an excellent job. In this Mission \
Objective, you'll be able to tell the difference between \
the addition symbol and the concatenation symbol. 
'''
        self.mission_statement4B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #004         \n\
        ⮞ Mission Name: The Total Is...      \n\
        ⮞ Difficulty: ✦             \n\
        ⮞ Save File: objectives/objective4.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user to enter two numbers. 
 Add them together and display the answer. 

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter your first number: 45
    ⮞ Please enter your first number: 12

[Output Message]: 

    ⮞ The total is: 67

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement5A = '''
[Space Force Armada Commander]:\n
Moving forward, let's combine what we've learned so far \
to display the correct answer to the user. In a user \
friendly way of course. 
'''
        self.mission_statement5B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #005         \n\
        ⮞ Mission Name: The Answer Is...      \n\
        ⮞ Difficulty: ✦✦          \n\
        ⮞ Save File: objectives/objective5.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user to enter three numbers. 
 Add together the first two numbers and then multiply 
 this total by the third number. Display the total. 
 Hint: Use parentheses to add together the first two 
 numbers and on the same line multiply by the third 
 number.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter your first number: 2
    ⮞ Please enter your second number: 4
    ⮞ Please enter your third number: 3

[Output Message]: 

    ⮞ The answer is: 18

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement6A = '''
[Space Force Armada Commander]:\n
Excellent track record! I'm starting to get \
hungry just thinking about this next mission. \
You'll be using your math skills to complete \
this mission. 
'''
        self.mission_statement6B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #006         \n\
        ⮞ Mission Name: Pizza Slices      \n\
        ⮞ Difficulty: ✦          \n\
        ⮞ Save File: objectives/objective6.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Concepts Acquired]: Variables, Datatypes, Print 
Statements, Input Statements and Arithmetic Operators. 

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask how many slices of pizza the 
 astronauts have in space and ask how many slices they 
 have eaten. Work out how many slices they have left 
 and display the answer in a user friendly format.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter the number of pizza slices: 24

[Output Message]: 

    ⮞ The total number of slices left is: 6

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement7A = '''
[Space Force Armada Commander]:\n
You'll make a excellent planetary space officer. Using \
what you've learned in the previous objectives you \
can also tell the user how old they'll be after one \
rotation around our sun. 
'''
        self.mission_statement7B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #007         \n\
        ⮞ Mission Name: A Trip Around the Sun \n\
        ⮞ Difficulty: ✦          \n\
        ⮞ Save File: objectives/objective7.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user for the name and their 
 age. Add 1 to their age and display the output message. 

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter your name: Bender
    ⮞ Please enter your age: 4

[Output Message]: 

    ⮞ Bender, next birthday you will be 5

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement8A = '''
[Space Force Armada Commander]:\n
Let's try something new! Imagine you and all \
of your astronaut friends are going out to a \
space diner. How will you split the bill evenly?
'''
        self.mission_statement8B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #008         \n\
        ⮞ Mission Name: Dinner Bill \n\
        ⮞ Difficulty: ✦          \n\
        ⮞ Save File: objectives/objective8.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask for the total price of the bill, 
 then ask how many diners there are. Divide the total 
 bill by the number of diners and show how much each 
 person must pay.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter the total price of the bill: 809
    ⮞ Please enter the total number of diners: 10

[Output Message]: 

    ⮞ Each person must pay $80.90 

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement9A = '''
[Space Force Armada Commander]:\n
Let's keep it moving space cadet! Working with data \
is incredibly important. Here's how you'll be \
converting information from days to seconds. 
'''
        self.mission_statement9B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #009         \n\
        ⮞ Mission Name: Days to Seconds \n\
        ⮞ Difficulty: ✦✦          \n\
        ⮞ Save File: objectives/objective9.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Write a program that will ask for a 
 number of days and then will show how many hours, 
 minutes, and seconds are in that number of days.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter the number of days: 2

[Output Message]: 

    ⮞ In 2 Days there are
      48 Hours or 
      2880 Minutes or 
      172800 Seconds
      
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement10A = '''
[Space Force Armada Commander]:
Alright!! We've got great momentum now. We are \
taking soil samples and would like to find out \
the total weight of our findings on Mars. 
'''
        self.mission_statement10B = '''\
            Mission Objective #010\n
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #010         \n\
        ⮞ Mission Name: Kilograms to Pounds \n\
        ⮞ Difficulty: ✦✦          \n\
        ⮞ Save File: objectives/objective10.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: First ask the user to enter either 
 [1] for kilograms to pounds or [2] for pounds to 
 kilograms. Then ask the user to enter the weight that 
 they would like to convert.  

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Enter [1] for kg to lbs or [2] for lbs to kg: 2
    ⮞ Please enter the weight that you would like to 
        convert: 24
    
[Output Message]: 

    ⮞ 24 pounds = 10.8862 kilograms 
      
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement11A = '''
[Space Force Armada Commander]:
We're on a very positive trajectory over the \
computer science learning curve. Here on Mars \ 
we've planted a bunch of potatos. We call them \
eggs because well.. we really miss our earth eggs. 
'''
        self.mission_statement11B = '''\
            Mission Objective #010\n
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #011         \n\
        ⮞ Mission Name: Egg Farmer \n\
        ⮞ Difficulty: ✦✦          \n\
        ⮞ Save File: objectives/objective11.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Help a chicken coop farmer by asking 
 him how many eggs he has in total. Find out how many 
 dozens of eggs (egg carts) he can sell. Ask how much
 the price is for each egg carton. First, tell the 
 farmer (in a user friendly format) how many egg carts 
 he has and then tell him how much money he can earn if 
 he sold all of his egg carts. Hint: Your answer should 
 include a dollar sign.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter the total amount of eggs: 925
    ⮞ Please enter the price per egg carton: 6.50

[Output Message]: 

    ⮞ You can make $501.04 for selling 77 egg carts. You
       also have 2 eggs left over for breakfast! 
      
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement12A = '''
[Space Force Armada Commander]:
We've got two almost idential potatoes. Which \
one is bigger? Let us know by creating a program \
that automates that job. 
'''
        self.mission_statement12B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #012         \n\
        ⮞ Mission Name: Two Numbers \n\
        ⮞ Difficulty: ✦         \n\
        ⮞ Save File: objectives/objective12.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user for two numbers. If the 
 first one is larger than the second number, display the 
 first number first, then the second. Otherwise, print 
 the second number first followed by the first number.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter your first number: 
    ⮞ Please enter your second number: 
    
[Output Message]: 

    ⮞ 32 is larger than 23
      
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement13A = '''
[Space Force Armada Commander]:
When we are descending onto an unknown planet, we \
use our PDV (Planetary Descent Vehicle). Let our \
astronauts know we have entered the planet's \
atmosphere. 
'''
        self.mission_statement13B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #013         \n\
        ⮞ Mission Name: Under Twenty \n\
        ⮞ Difficulty: ✦         \n\
        ⮞ Save File: objectives/objective13.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user to enter a number that 
 is under 20. If they enter a number that is 20 or more, 
 display the message Too High. Otherwise, display Thanks. 

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter a number under 20: 40
    
[Output Message]: 

    ⮞ Too High
      
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement14A = '''
[Space Force Armada Commander]:
Precision counts when you're in space. Let us know \
if our Hab material is within the threshold that it \
was designed to hold! 
'''
        self.mission_statement14B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #014         \n\
        ⮞ Mission Name: Between 10 and 20 \n\
        ⮞ Difficulty: ✦         \n\
        ⮞ Save File: objectives/objective14.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user to enter a number 
 between 10 and 20 (inclusive). If they enter a number 
 within this range, display the message Thank you!, 
 otherwise display Incorrect Answer.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter a number between 10 and 20: 15
    
[Output Message]: 

    ⮞ Thank you!
      
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement15A = '''
[Space Force Armada Commander]:
It's hard being an astronaut. You don't have many \
options when it comes to choosing your favorite \
food. What is your favorite food? 
'''
        self.mission_statement15B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #015         \n\
        ⮞ Mission Name: Favorite Food \n\
        ⮞ Difficulty: ✦✦         \n\
        ⮞ Save File: objectives/objective15.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user to enter their favorite 
 food. If they enter noodles, or NOODLES or Noodles 
 display the message I love noodles too!, otherwise 
 display the message I don't like [fav_food], 
 I prefer noodles.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter your favorite food: NoOdLeS
    
[Output Message]: 

    ⮞ I love noodles too!
      
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement16A = '''
[Space Force Armada Commander]:
It's important to know exactly what the current \
planet's weather is like. Let us know if it is \
either raining or windy on this planet. Or both. 
'''
        self.mission_statement16B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #016         \n\
        ⮞ Mission Name: Is It Raining? \n\
        ⮞ Difficulty: ✦✦         \n\
        ⮞ Save File: objectives/objective16.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user if it is raining and 
 convert the answer to lower case so it does not matter 
 what case they type it in. If they answer yes, ask if 
 it is windy. If they answer yes to this second 
 question, display the answer It is too windy for an 
 umbrella, otherwise display the message Take an 
 umbrella. If they did not answer yes to the first 
 question, display the answer Enjoy your day!

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Is it raining outside? [yes] or [no]: yes 
    ⮞ Is it windy outside? [yes] or [no]: no 
    
[Output Message]: 

    ⮞ Take an umbrella 
      
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement17A = '''
[Space Force Armada Commander]: 
Great work, Mission Specialist 1. We'd like you to \
know what types of interesting opportunities are \
available for you during this mission. 
'''
        self.mission_statement17B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #017         \n\
        ⮞ Mission Name: What is Your Age? \n\
        ⮞ Difficulty: ✦         \n\
        ⮞ Save File: objectives/objective17.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user's age. If they are 18 
 or over, display the message You can vote!, if they are 
 aged 17, display the message You can learn to drive, 
 if they are 16, display the message You can buy a 
 lottery ticket, if they are under 16, display the 
 message You can go Trick or Treating.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter your name: 67

[Output Message]: 

    ⮞ You can vote!
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement18A = '''
[Space Force Armada Commander]:
You're doing a stellar job. This program will allow \
us to see if our rock samples are exactly the right \
size. 
'''
        self.mission_statement18B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #018         \n\
        ⮞ Mission Name: Just the Right Number \n\
        ⮞ Difficulty: ✦         \n\
        ⮞ Save File: objectives/objective18.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Create an if statement that checks 
 whether the amount of money contained in the variable 
 is between 100 and 500 or between 1000 and 5000. If it 
 is, then display You can either buy a really nice pair 
 of shoes or a really old car.. Otherwise, display I'm 
 not sure how much money you currently have.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter any amount of money: 250
        
[Output Message]: 

    ⮞ You can either buy a really nice pair of shoes or
        a really old car.
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement19A = '''
[Space Force Armada Commander]:
Keep pushing. You're almost at the final Mission \
Objective until you successfully graduate to a \
fully fledged member of Mission Specialist II. 
'''
        self.mission_statement19B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #019         \n\
        ⮞ Mission Name: Thank You Player One \n\
        ⮞ Difficulty: ✦✦        \n\
        ⮞ Save File: objectives/objective19.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user how many ninjas are in 
 the arena. Create an if statement that prints the 
 string That's too many. I need back up., if the 
 variable ninjas contains a number that is greater than 
 or equal to 50, prints It'll be a struggle, but I can 
 handle 'em if its between 30 and 50 (exclusive), and 
 prints Easy Peezy ᕙ(⇀‸↼‶)ᕗ, if it's less than or 
 equal to 30 and greater than 0, There are no ninjas 
 in sight! If it is equal to 0, otherwise display I 
 can't fight a negative amount of ninjas..

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter the number of ninjas on site: 32
        
[Output Message]: 

    ⮞ It'll be a struggle, but I can handle 'em
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement20A = '''
[Space Force Armada Commander]:
Now you've learned about how to using different \
built in functions. How will you get the length \
of the user's name? 
'''
        self.mission_statement20B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #020         \n\
        ⮞ Mission Name: Length of Name \n\
        ⮞ Difficulty: ✦        \n\
        ⮞ Save File: objectives/objective20.py  \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user to enter their first 
name and then display the length of their name.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter your name: Lannon
    
[Output Message]: 

    ⮞ The length of Lannon is: 6
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement21A = '''
[Space Force Armada Commander]:
Alright! Great work, you'll need to recall what \
you've learned about concatenation to complete \ 
this next mission. 
'''
        self.mission_statement21B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #021         \n\
        ⮞ Mission Name: Length of Full Name \n\
        ⮞ Difficulty: ✦        \n\
        ⮞ Save File: objectives/objective21.py \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user to enter their first 
 name and then ask them to enter their last name. Join 
 them together with a space between and display the 
 name and the length of the whole name.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Output Message]: 

    ⮞ Please enter your first name: Lannon
    ⮞ Please enter your last name: Khau
    
[Output Message]: 

    ⮞ The length of Lannon Khau is: 11
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement22A = '''
[Space Force Armada Commander]:
Back on Earth, mission command allowed astronauts \
to bring 1 digital copy of their all time favorite \
movie. 
'''
        self.mission_statement22B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #022         \n\
        ⮞ Mission Name: Favorite Movie Title \n\
        ⮞ Difficulty: ✦        \n\
        ⮞ Save File: objectives/objective22.py \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Concepts Acquired]: String Manipulation, Escape
 Characters, Strings and Numbers as Variables,
 Concatenation, Type Casting, Multi-line Strings, 
 Length Function, Indexing, Slicing, and
 String Methods. 

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user to enter their favorite 
 movie title in lowercase. Change the case to title case.
 Display the finished result.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Output Message]: 

    ⮞ Please enter your favorite movie: 50 first dates
    
[Output Message]: 

    ⮞ Your movie in title case: 50 First Dates
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement23A = '''
[Space Force Armada Commander]:
Just two more missions to go. Before you complete \
the entire series of Mission Specialist I, what \
quote brought you through to the end? 
'''
        self.mission_statement23B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #023         \n\
        ⮞ Mission Name: Favorite Quote \n\
        ⮞ Difficulty: ✦✦        \n\
        ⮞ Save File: objectives/objective23.py \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user to type in a famous 
 quote. Make sure to manipulate the string to include 
 quotations in your string. Ask for the starting number 
 and an ending number and then display just the slice 
 of the text and remember that Python starts counting 
 from 0 and not 1.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter a famous quote: Be the change you 
        seek in the world 
    ⮞ Please enter your first number: 7
    ⮞ Please enter your second number: 13
    
[Output Message]: 

    ⮞ change
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        self.mission_statement24A = '''
[Space Force Armada Commander]: 
YOU DID IT! YOU'RE AT THE FINAL MISSION!
'''
        self.mission_statement24B = '''\
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ⮞ Mission Objective: #023         \n\
        ⮞ Mission Name: Screaming Caps \n\
        ⮞ Difficulty: ✦        \n\
        ⮞ Save File: objectives/objective23.py \n\
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Mission Briefing]: Ask the user to type in any word 
 and display it in uppercase:

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[Input]: 

    ⮞ Please enter any word or phrase in lower case: 
        theres a snake in my boots!
    
[Output Message]: 

    ⮞ THERES A SNAKE IN MY BOOTS!
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
        ##############################################################################################
        ##############################################################################################
        ##############################################################################################
        ##############################################################################################
        ##############################################################################################

        self.MAINFRAME_SD = Frame(TabControl2, bd=12, relief=RAISED,
                                  bg='grey', width=1110, height=300)
        self.MAINFRAME_SD.pack(fill='both', expand=1)

        sd_frame_col = 'grey50'

        # Creating All The Individual Frames for each student on the Leader board.
        self.leftFrame_SD = Frame(self.MAINFRAME_SD, bd=10, relief=SUNKEN,
                                bg=sd_frame_col, width=600, height=735)
        self.leftFrame_SD.pack(side=LEFT)

        # Creating All The Individual Frames for each student on the Leader board.
        self.leftFrame_SD1 = Frame(self.leftFrame_SD, bd=5, relief=SUNKEN,
                                   bg=sd_frame_col, width=600, height=90)
        self.leftFrame_SD1.propagate(0)

        self.leftFrame_SD1.pack(side=TOP)

        self.SD1_btn = Button(self.leftFrame_SD1, bd=3, relief=RAISED,
                              bg='grey10', width=3, height=1, text='1',
                              font=('consolas', 10, 'bold'), fg='green2',
                              command=self.popup_rank1, state = DISABLED)

        self.SD1_btn.pack(side=LEFT, anchor=NW)

        #################
        self.canvas_rank1 = Canvas(
            self.leftFrame_SD1,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank1.pack(side=LEFT, padx=8)

        self.rank_img1 = ImageTk.PhotoImage(Image.open('images/rank_img1.png'))
        self.canvas_rank1.create_image(
            -10,
            40,
            anchor=W,
            image= self.rank_img1
        )
        #################

        self.lblRankDesc1 = Label(self.leftFrame_SD1,
                                  width=45, height=4,
                                  text='Rank: Mission Specialist 1\n\
Completed: 25 Python Mission Objectives\n\
Points Earned: 750 Total Points            ',
                                  font=('consolas', 11),
                                  bg='grey75', fg='black',
                                  justify=LEFT, relief=SUNKEN,
                                  bd=10, wraplength=365)
        self.lblRankDesc1.pack(side=LEFT, pady=2)

        #################
        self.canvas_rank1B = Canvas(
            self.leftFrame_SD1,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank1B.pack(side=RIGHT)
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.seq_sd1 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open('images/robo_dead_rank1.gif'))]

        self.image_rank1 = self.canvas_rank1B.create_image(45, 35, image=self.seq_sd1[0])

        self.animate_rank1(0)
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        # self.canvas_rank1B.pack(side = RIGHT)
        # rank_img1B = ImageTk.PhotoImage(Image.open('images/robo_dead.gif'))
        # self.canvas_rank1B.create_image(
        #     -10,
        #     40,
        #     anchor=W,
        #     image=rank_img1B
        # )
        #################
        sd_frame_col = 'grey50'

        self.leftFrame_SD2 = Frame(self.leftFrame_SD, bd=5, relief=SUNKEN,
                                   bg=sd_frame_col, width=600, height=90)

        self.leftFrame_SD2.propagate(0)

        self.leftFrame_SD2.pack(side=TOP)

        self.SD2_btn = Button(self.leftFrame_SD2, bd=3, relief=RAISED,
                              bg='grey10', width=3, height=1, text='2',
                              font=('consolas', 10, 'bold'), fg='green2',
                              command=self.popup_rank2,state = DISABLED)

        self.SD2_btn.pack(side=LEFT, anchor=NW)

        #################

        self.canvas_rank2 = Canvas(
            self.leftFrame_SD2,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank2.pack(side=LEFT, padx=8)
        self.rank_img2 = ImageTk.PhotoImage(Image.open('images/rank_img2.png'))
        self.canvas_rank2.create_image(
            -10,
            40,
            anchor=W,
            image= self.rank_img2
        )

        #################

        self.lblRankDesc2 = Label(self.leftFrame_SD2,
                                  width=45, height=4,
                                  text='Rank: Mission Specialist 2\n\
Completed: 50 Python Mission Objectives\n\
Points Earned: 1,000 Total Points          ',
                                  font=('consolas', 11),
                                  bg='grey75', fg='black',
                                  justify=LEFT, relief=SUNKEN,
                                  bd=10, wraplength=365)
        self.lblRankDesc2.pack(side=LEFT, pady=2)

        #################
        self.canvas_rank2B = Canvas(
            self.leftFrame_SD2,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank2B.pack(side=RIGHT)
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.seq_sd2 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open('images/robo_dead_rank1.gif'))]

        self.image_rank2 = self.canvas_rank2B.create_image(45, 35, image=self.seq_sd2[0])

        self.animate_rank2(0)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.leftFrame_SD3 = Frame(self.leftFrame_SD, bd=5, relief=SUNKEN,
                                   bg=sd_frame_col, width=600, height=90)

        self.leftFrame_SD3.propagate(0)

        self.leftFrame_SD3.pack(side=TOP)

        self.SD3_btn = Button(self.leftFrame_SD3, bd=3, relief=RAISED,
                              bg='grey10', width=3, height=1, text='3',
                              font=('consolas', 10, 'bold'), fg='green2',
                              state = DISABLED)

        self.SD3_btn.pack(side=LEFT, anchor=NW)

        #################

        self.canvas_rank3 = Canvas(
            self.leftFrame_SD3,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank3.pack(side=LEFT, padx=8)
        self.rank_img3 = ImageTk.PhotoImage(Image.open('images/rank_img3.png'))
        self.canvas_rank3.create_image(
            -10,
            40,
            anchor=W,
            image=self.rank_img3
        )

        #################

        self.lblRankDesc3 = Label(self.leftFrame_SD3,
                                  width=45, height=4,
                                  text='Rank: Mission Specialist 3\n\
Completed: 70 Python Mission Objectives\n\
Points Earned: 2,000 Total Points          ',
                                  font=('consolas', 11),
                                  bg='grey75', fg='black',
                                  justify=LEFT, relief=SUNKEN,
                                  bd=10, wraplength=365)
        self.lblRankDesc3.pack(side=LEFT, pady=2)

        #################
        self.canvas_rank3B = Canvas(
            self.leftFrame_SD3,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank3B.pack(side=RIGHT)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.seq_sd3 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open('images/robo_dead_rank1.gif'))]

        self.image_rank3 = self.canvas_rank3B.create_image(45, 35, image=self.seq_sd3[0])

        self.animate_rank3(0)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        #################

        self.leftFrame_SD4 = Frame(self.leftFrame_SD, bd=5, relief=SUNKEN,
                                   bg=sd_frame_col, width=600, height=90)

        self.leftFrame_SD4.propagate(0)

        self.leftFrame_SD4.pack(side=TOP)

        self.SD4_btn = Button(self.leftFrame_SD4, bd=3, relief=RAISED,
                              bg='grey10', width=3, height=1, text='4',
                              font=('consolas', 10, 'bold'), fg='green2',
                              state = DISABLED)

        self.SD4_btn.pack(side=LEFT, anchor=NW)

        #################
        self.canvas_rank4 = Canvas(
            self.leftFrame_SD4,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank4.pack(side=LEFT, padx=8)
        self.rank_img4 = ImageTk.PhotoImage(Image.open('images/rank_img4.png'))
        self.canvas_rank4.create_image(
            -10,
            40,
            anchor=W,
            image=self.rank_img4
        )
        #################
        self.lblRankDesc4 = Label(self.leftFrame_SD4,
                                  width=45, height=4,
                                  text='Rank: Mission Specialist 4\n\
Completed: 90 Python Mission Objectives\n\
Points Earned: 3,000 Total Points          ',
                                  font=('consolas', 11),
                                  bg='grey75', fg='black',
                                  justify=LEFT, relief=SUNKEN,
                                  bd=10, wraplength=365)
        self.lblRankDesc4.pack(side=LEFT, pady=2)
        #################
        self.canvas_rank4B = Canvas(
            self.leftFrame_SD4,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank4B.pack(side=RIGHT)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.seq_sd4 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open('images/robo_dead_rank1.gif'))]

        self.image_rank4 = self.canvas_rank4B.create_image(45, 35, image=self.seq_sd4[0])

        self.animate_rank4(0)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        #################

        self.leftFrame_SD5 = Frame(self.leftFrame_SD, bd=5, relief=SUNKEN,
                                   bg=sd_frame_col, width=600, height=90)

        self.leftFrame_SD5.propagate(0)

        self.leftFrame_SD5.pack(side=TOP)

        self.SD5_btn = Button(self.leftFrame_SD5, bd=3, relief=RAISED,
                              bg='grey10', width=3, height=1, text='5',
                              font=('consolas', 10, 'bold'), fg='green2',
                              state = DISABLED)

        self.SD5_btn.pack(side=LEFT, anchor=NW)

        #################

        self.canvas_rank5 = Canvas(
            self.leftFrame_SD5,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank5.pack(side=LEFT, padx=8)
        self.rank_img5 = ImageTk.PhotoImage(Image.open('images/rank_img5.png'))
        self.canvas_rank5.create_image(
            -10,
            40,
            anchor=W,
            image=self.rank_img5
        )
        #################
        self.lblRankDesc5 = Label(self.leftFrame_SD5,
                                  width=45, height=4,
                                  text='Rank: Space Force Technical Sargeant\n\
Completed: 110 Python Mission Objectives\n\
Points Earned: 4,000 Total Points          ',
                                  font=('consolas', 11),
                                  bg='grey75', fg='black',
                                  justify=LEFT, relief=SUNKEN,
                                  bd=10, wraplength=365)
        self.lblRankDesc5.pack(side=LEFT, pady=2)

        #################
        self.canvas_rank5B = Canvas(
            self.leftFrame_SD5,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank5B.pack(side=RIGHT)
        rank_img5B = ImageTk.PhotoImage(Image.open('images/robo_dead.gif'))
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.seq_sd5 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open('images/robo_dead_rank1.gif'))]

        self.image_rank5 = self.canvas_rank5B.create_image(45, 35, image=self.seq_sd5[0])

        self.animate_rank5(0)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.leftFrame_SD6 = Frame(self.leftFrame_SD, bd=5, relief=SUNKEN,
                                   bg=sd_frame_col, width=600, height=90)
        self.leftFrame_SD6.propagate(0)

        self.leftFrame_SD6.pack(side=TOP)

        self.SD6_btn = Button(self.leftFrame_SD6, bd=3, relief=RAISED,
                              bg='grey10', width=3, height=1, text='6',
                              font=('consolas', 10, 'bold'), fg='green2',
                              state = DISABLED)

        self.SD6_btn.pack(side=LEFT, anchor=NW)

        #################

        self.canvas_rank6 = Canvas(
            self.leftFrame_SD6,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank6.pack(side=LEFT, padx=8)
        self.rank_img6 = ImageTk.PhotoImage(Image.open('images/rank_img6.png'))
        self.canvas_rank6.create_image(
            -10,
            40,
            anchor=W,
            image=self.rank_img6
        )

        #################

        self.lblRankDesc6 = Label(self.leftFrame_SD6,
                                  width=45, height=4,
                                  text='Rank: Space Force Senior Master Sargeant\n\
Completed: 130 Python Mission Objectives\n\
Points Earned: 5,000 Total Points          ',
                                  font=('consolas', 11),
                                  bg='grey75', fg='black',
                                  justify=LEFT, relief=SUNKEN,
                                  bd=10, wraplength=365)
        self.lblRankDesc6.pack(side=LEFT, pady=2)

        #################
        self.canvas_rank6B = Canvas(
            self.leftFrame_SD6,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank6B.pack(side=RIGHT)
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.seq_sd6 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open('images/robo_dead_rank1.gif'))]

        self.image_rank6 = self.canvas_rank6B.create_image(45, 35, image=self.seq_sd6[0])

        self.animate_rank6(0)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        #################

        self.leftFrame_SD7 = Frame(self.leftFrame_SD, bd=5, relief=SUNKEN,
                                   bg=sd_frame_col, width=600, height=90)

        self.leftFrame_SD7.propagate(0)
        self.leftFrame_SD7.pack(side=TOP)

        self.SD7_btn = Button(self.leftFrame_SD7, bd=3, relief=RAISED,
                              bg='grey10', width=3, height=1, text='7',
                              font=('consolas', 10, 'bold'), fg='green2',
                              state = DISABLED)

        self.SD7_btn.pack(side=LEFT, anchor=NW)

        #################

        self.canvas_rank7 = Canvas(
            self.leftFrame_SD7,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank7.pack(side=LEFT, padx=8)

        self.rank_img7 = ImageTk.PhotoImage(Image.open('images/rank_img7.png'))
        self.canvas_rank7.create_image(
            -10,
            40,
            anchor=W,
            image=self.rank_img7
        )
        self.lblRankDesc7 = Label(self.leftFrame_SD7,
                                  width=45, height=4,
                                  text='Rank: Space Force Chief Master Sargeant\n\
Completed: 150 Python Mission Objectives\n\
Points Earned: 6,000 Total Points          ',
                                  font=('consolas', 11),
                                  bg='grey75', fg='black',
                                  justify=LEFT, relief=SUNKEN,
                                  bd=10, wraplength=365)
        self.lblRankDesc7.pack(side=LEFT, pady=2)

        self.canvas_rank7B = Canvas(
            self.leftFrame_SD7,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank7B.pack(side=RIGHT)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.seq_sd7 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open('images/robo_dead_rank1.gif'))]

        self.image_rank7 = self.canvas_rank7B.create_image(45, 35, image=self.seq_sd7[0])

        self.animate_rank7(0)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        #################

        self.leftFrame_SD8 = Frame(self.leftFrame_SD, bd=5, relief=SUNKEN,
                                   bg=sd_frame_col, width=600, height=90)

        self.leftFrame_SD8.propagate(0)

        self.leftFrame_SD8.pack(side=TOP)

        self.SD8_btn = Button(self.leftFrame_SD8, bd=3, relief=RAISED,
                              bg='grey10', width=3, height=1, text='8',
                              font=('consolas', 10, 'bold'), fg='green2',
                              state = DISABLED)

        self.SD8_btn.pack(side=LEFT, anchor=NW)

        #################

        self.canvas_rank8 = Canvas(
            self.leftFrame_SD8,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank8.pack(side=LEFT, padx=8)
        self.rank_img8 = ImageTk.PhotoImage(Image.open('images/rank_img8.png'))
        self.canvas_rank8.create_image(
            -10,
            40,
            anchor=W,
            image=self.rank_img8
        )
        self.lblRankDesc8 = Label(self.leftFrame_SD8,
                                  width=45, height=4,
                                  text='Rank: Space Force Second Lieutenant\n\
Completed: 180 Python Mission Objectives\n\
Points Earned: 7,000 Total Points          ',
                                  font=('consolas', 11),
                                  bg='grey75', fg='black',
                                  justify=LEFT, relief=SUNKEN,
                                  bd=10, wraplength=365)
        self.lblRankDesc8.pack(side=LEFT, pady=2)

        self.canvas_rank8B = Canvas(
            self.leftFrame_SD8,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank8B.pack(side=RIGHT)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.seq_sd8 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open('images/robo_dead_rank1.gif'))]

        self.image_rank8 = self.canvas_rank8B.create_image(45, 35, image=self.seq_sd8[0])

        self.animate_rank8(0)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        #################

        # Creating All The Individual Frames for each student on the Leader board.
        self.rightFrame_SD = Frame(self.MAINFRAME_SD, bd=10, relief=SUNKEN,
                                   bg=sd_frame_col, width=620, height=735)
        self.rightFrame_SD.pack(side=RIGHT)

        # Creating All The Individual Frames for each student on the Leader board.
        self.rightFrame_SD1 = Frame(self.rightFrame_SD, bd=5, relief=SUNKEN,
                                    bg=sd_frame_col, width=600, height=90)

        self.rightFrame_SD1.propagate(0)
        self.rightFrame_SD1.pack(side=TOP)

        self.SD9_btn = Button(self.rightFrame_SD1, bd=3, relief=RAISED,
                              bg='grey10', width=3, height=1, text='9',
                              font=('consolas', 10, 'bold'), fg='green2',
                              state = DISABLED)

        self.SD9_btn.pack(side=LEFT, anchor=NW)

        #################

        self.canvas_rank9 = Canvas(
            self.rightFrame_SD1,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank9.pack(side=LEFT, padx=13)
        self.rank_img9 = ImageTk.PhotoImage(Image.open('images/rank_img9.png'))
        self.canvas_rank9.create_image(
            -10,
            40,
            anchor=W,
            image=self.rank_img9
        )
        self.lblRankDesc9 = Label(self.rightFrame_SD1,
                                  width=45, height=4,
                                  text='Rank: Space Force First Lieutenant\n\
Completed: 200 Python Mission Objectives\n\
Points Earned: 8,000 Total Points         ',
                                  font=('consolas', 11),
                                  bg='grey75', fg='black',
                                  justify=LEFT, relief=SUNKEN,
                                  bd=10, wraplength=365)
        self.lblRankDesc9.pack(side=LEFT, pady=2)

        self.canvas_rank9B = Canvas(
            self.rightFrame_SD1,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank9B.pack(side=RIGHT)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.seq_sd9 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open('images/robo_dead_rank1.gif'))]

        self.image_rank9 = self.canvas_rank9B.create_image(45, 35, image=self.seq_sd9[0])

        self.animate_rank9(0)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        #################

        self.rightFrame_SD2 = Frame(self.rightFrame_SD, bd=5, relief=SUNKEN,
                                    bg=sd_frame_col, width=600, height=90)

        self.rightFrame_SD2.propagate(0)
        self.rightFrame_SD2.pack(side=TOP)

        self.SD10_btn = Button(self.rightFrame_SD2, bd=3, relief=RAISED,
                               bg='grey10', width=3, height=1, text='10',
                               font=('consolas', 10, 'bold'), fg='green2',
                               state = DISABLED)

        self.SD10_btn.pack(side=LEFT, anchor=NW)

        #################

        self.canvas_rank10 = Canvas(
            self.rightFrame_SD2,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank10.pack(side=LEFT, padx=13)
        self.rank_img10 = ImageTk.PhotoImage(Image.open('images/rank_img10.png'))
        self.canvas_rank10.create_image(
            -10,
            40,
            anchor=W,
            image=self.rank_img10
        )
        self.lblRankDesc10 = Label(self.rightFrame_SD2,
                                   width=45, height=4,
                                   text='Rank: Space Force Captain\n\
Completed: 250 Python Mission Objectives\n\
Points Earned: 10,000 Total Points         ',
                                   font=('consolas', 11),
                                   bg='grey75', fg='black',
                                   justify=LEFT, relief=SUNKEN,
                                   bd=10, wraplength=365)
        self.lblRankDesc10.pack(side=LEFT, pady=2)

        self.canvas_rank10B = Canvas(
            self.rightFrame_SD2,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank10B.pack(side=RIGHT)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.seq_sd10 = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(
                Image.open('images/robo_dead_rank1.gif'))]

        self.image_rank10 = self.canvas_rank10B.create_image(45, 35, image=self.seq_sd10[0])

        self.animate_rank10(0)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        #################

        self.rightFrame_SD3 = Frame(self.rightFrame_SD, bd=5, relief=SUNKEN,
                                    bg=sd_frame_col, width=600, height=90)
        self.rightFrame_SD3.propagate(0)
        self.rightFrame_SD3.pack(side=TOP)

        self.SD11_btn = Button(self.rightFrame_SD3, bd=3, relief=RAISED,
                               bg='grey10', width=3, height=1, text='11',
                               font=('consolas', 10, 'bold'), fg='green2',
                               state = DISABLED)

        self.SD11_btn.pack(side=LEFT, anchor=NW)

        #################
        self.canvas_rank11 = Canvas(
            self.rightFrame_SD3,
            width=85,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank11.pack(side=LEFT, padx=8)
        self.rank_img11 = ImageTk.PhotoImage(Image.open('images/rank_img11.png'))
        self.canvas_rank11.create_image(
            -10,
            40,
            anchor=W,
            image=self.rank_img11
        )
        self.lblRankDesc11 = Label(self.rightFrame_SD3,
                                   width=45, height=4,
                                   text='Rank: Space Force Major\n\
Completed: 300 Python Mission Objectives\n\
Points Earned: 12,000 Total Points         ',
                                   font=('consolas', 11),
                                   bg='grey75', fg='black',
                                   justify=LEFT, relief=SUNKEN,
                                   bd=10, wraplength=365)
        self.lblRankDesc11.pack(side=LEFT, pady=2)
        #################

        self.canvas_rank11B = Canvas(
            self.rightFrame_SD3,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank11B.pack(side=RIGHT)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.seq_sd11 = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(
                Image.open('images/robo_dead_rank1.gif'))]

        self.image_rank11 = self.canvas_rank11B.create_image(45, 35, image=self.seq_sd11[0])

        self.animate_rank11(0)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.rightFrame_SD4 = Frame(self.rightFrame_SD, bd=5, relief=SUNKEN,
                                    bg=sd_frame_col, width=600, height=90)
        self.rightFrame_SD4.propagate(0)
        self.rightFrame_SD4.pack(side=TOP)

        self.SD12_btn = Button(self.rightFrame_SD4, bd=3, relief=RAISED,
                               bg='grey10', width=3, height=1, text='12',
                               font=('consolas', 10, 'bold'), fg='green2',
                               state = DISABLED)

        self.SD12_btn.pack(side=LEFT, anchor=NW)
        #################
        self.canvas_rank12 = Canvas(
            self.rightFrame_SD4,
            width=85,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank12.pack(side=LEFT, padx=8)
        self.rank_img12 = ImageTk.PhotoImage(Image.open('images/rank_img12.png'))
        self.canvas_rank12.create_image(
            -10,
            40,
            anchor=W,
            image=self.rank_img12
        )
        self.lblRankDesc12 = Label(self.rightFrame_SD4,
                                   width=45, height=4,
                                   text='Rank: Space Force Colonel\n\
Completed: 350 Python Mission Objectives\n\
Points Earned: 14,000 Total Points         ',
                                   font=('consolas', 11),
                                   bg='grey75', fg='black',
                                   justify=LEFT, relief=SUNKEN,
                                   bd=10, wraplength=365)
        self.lblRankDesc12.pack(side=LEFT, pady=2)
        #################
        self.canvas_rank12B = Canvas(
            self.rightFrame_SD4,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank12B.pack(side=RIGHT)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.seq_sd12 = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(
                Image.open('images/robo_dead_rank1.gif'))]

        self.image_rank12 = self.canvas_rank12B.create_image(45, 35, image=self.seq_sd12[0])

        self.animate_rank12(0)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.rightFrame_SD5 = Frame(self.rightFrame_SD, bd=5, relief=SUNKEN,
                                    bg=sd_frame_col, width=600, height=90)
        self.rightFrame_SD5.propagate(0)
        self.rightFrame_SD5.pack(side=TOP)

        self.SD13_btn = Button(self.rightFrame_SD5, bd=3, relief=RAISED,
                               bg='grey10', width=3, height=1, text='13',
                               font=('consolas', 10, 'bold'), fg='green2',
                               state = DISABLED)

        self.SD13_btn.pack(side=LEFT, anchor=NW)

        #################
        self.canvas_rank13 = Canvas(
            self.rightFrame_SD5,
            width=85,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank13.pack(side=LEFT, padx=8)
        self.rank_img13 = ImageTk.PhotoImage(Image.open('images/rank_img13.png'))
        self.canvas_rank13.create_image(
            -10,
            40,
            anchor=W,
            image=self.rank_img13
        )
        #################

        self.lblRankDesc13 = Label(self.rightFrame_SD5,
                                   width=45, height=4,
                                   text='Rank: Space Force Brigadier General\n\
Completed: 400 Python Mission Objectives\n\
Points Earned: 16,000 Total Points         ',
                                   font=('consolas', 11),
                                   bg='grey75', fg='black',
                                   justify=LEFT, relief=SUNKEN,
                                   bd=10, wraplength=365)
        self.lblRankDesc13.pack(side=LEFT, pady=2)

        #################
        self.canvas_rank13B = Canvas(
            self.rightFrame_SD5,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank13B.pack(side=RIGHT)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.seq_sd13 = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(
                Image.open('images/robo_dead_rank1.gif'))]

        self.image_rank13 = self.canvas_rank13B.create_image(45, 35, image=self.seq_sd13[0])

        self.animate_rank13(0)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.rightFrame_SD6 = Frame(self.rightFrame_SD, bd=5, relief=SUNKEN,
                                    bg=sd_frame_col, width=600, height=90)
        self.rightFrame_SD6.propagate(0)
        self.rightFrame_SD6.pack(side=TOP)

        self.SD14_btn = Button(self.rightFrame_SD6, bd=3, relief=RAISED,
                               bg='grey10', width=3, height=1, text='14',
                               font=('consolas', 10, 'bold'), fg='green2',
                               state = DISABLED)

        self.SD14_btn.pack(side=LEFT, anchor=NW)

        #################
        self.canvas_rank14 = Canvas(
            self.rightFrame_SD6,
            width=85,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank14.pack(side=LEFT, padx=8)
        self.rank_img14 = ImageTk.PhotoImage(Image.open('images/rank_img14.png'))
        self.canvas_rank14.create_image(
            -10,
            40,
            anchor=W,
            image=self.rank_img14
        )

        self.lblRankDesc14 = Label(self.rightFrame_SD6,
                                   width=45, height=4,
                                   text='Rank: Space Force Major General\n\
Completed: 400 Python Mission Objectives\n\
Points Earned: 18,000 Total Points         ',
                                   font=('consolas', 11),
                                   bg='grey75', fg='black',
                                   justify=LEFT, relief=SUNKEN,
                                   bd=10, wraplength=365)
        self.lblRankDesc14.pack(side=LEFT, pady=2)
        #################
        self.canvas_rank14B = Canvas(
            self.rightFrame_SD6,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank14B.pack(side=RIGHT)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.seq_sd14 = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(
                Image.open('images/robo_dead_rank1.gif'))]

        self.image_rank14 = self.canvas_rank14B.create_image(45, 35, image=self.seq_sd14[0])

        self.animate_rank14(0)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.rightFrame_SD7 = Frame(self.rightFrame_SD, bd=5, relief=SUNKEN,
                                    bg=sd_frame_col, width=600, height=90)
        self.rightFrame_SD7.propagate(0)
        self.rightFrame_SD7.pack(side=TOP)

        self.SD15_btn = Button(self.rightFrame_SD7, bd=3, relief=RAISED,
                               bg='grey10', width=3, height=1, text='15',
                               font=('consolas', 10, 'bold'), fg='green2',
                               state = DISABLED)

        self.SD15_btn.pack(side=LEFT, anchor=NW)

        #################
        self.canvas_rank15 = Canvas(
            self.rightFrame_SD7,
            width=85,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank15.pack(side=LEFT, padx=8)
        self.rank_img15 = ImageTk.PhotoImage(Image.open('images/rank_img15.png'))
        self.canvas_rank15.create_image(
            -10,
            40,
            anchor=W,
            image=self.rank_img15
        )

        self.lblRankDesc15 = Label(self.rightFrame_SD7,
                                   width=45, height=4,
                                   text='Rank: Space Force Lieutenant General\n\
Completed: 450 Python Mission Objectives\n\
Points Earned: 20,000 Total Points         ',
                                   font=('consolas', 11),
                                   bg='grey75', fg='black',
                                   justify=LEFT, relief=SUNKEN,
                                   bd=10, wraplength=365)
        self.lblRankDesc15.pack(side=LEFT, pady=2)

        #################
        self.canvas_rank15B = Canvas(
            self.rightFrame_SD7,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank15B.pack(side=RIGHT)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.seq_sd15 = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(
                Image.open('images/robo_dead_rank1.gif'))]

        self.image_rank15 = self.canvas_rank15B.create_image(45, 35, image=self.seq_sd15[0])

        self.animate_rank15(0)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        #################

        self.rightFrame_SD8 = Frame(self.rightFrame_SD, bd=5, relief=SUNKEN,
                                    bg=sd_frame_col, width=600, height=90)
        self.rightFrame_SD8.propagate(0)
        self.rightFrame_SD8.pack(side=TOP)

        self.SD16_btn = Button(self.rightFrame_SD8, bd=3, relief=RAISED,
                               bg='grey10', width=3, height=1, text='16',
                               font=('consolas', 10, 'bold'), fg='green2',
                               state = DISABLED)

        self.SD16_btn.pack(side=LEFT, anchor=NW)

        #################
        self.canvas_rank16 = Canvas(
            self.rightFrame_SD8,
            width=85,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank16.pack(side=LEFT, padx=8)
        self.rank_img16 = ImageTk.PhotoImage(Image.open('images/rank_img16.png'))
        self.canvas_rank16.create_image(
            -10,
            40,
            anchor=W,
            image=self.rank_img16
        )
        #################

        self.lblRankDesc16 = Label(self.rightFrame_SD8,
                                   width=45, height=4,
                                   text='Rank: Space Force Commander          \n\
Completed: 500 Python Mission Objectives   \n\
Points Earned: 22,000 Total Points        ',
                                   #             text = 'testing testing testing 16 testing testing testing 16 testing \
                                   # testing testing 16 testing testing testing 16',
                                   font=('consolas', 11),
                                   bg='grey75', fg='black',
                                   justify=LEFT, relief=SUNKEN,
                                   bd=10, wraplength=345)
        self.lblRankDesc16.pack(side=LEFT, pady=2)

        #################
        self.canvas_rank16B = Canvas(
            self.rightFrame_SD8,
            width=75,
            height=75,
            bg='grey50',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.canvas_rank16B.pack(side=RIGHT)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.seq_sd16 = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(
                Image.open('images/robo_dead_rank1.gif'))]

        self.image_rank16 = self.canvas_rank16B.create_image(45, 35, image=self.seq_sd16[0])

        self.animate_rank16(0)

    def popup_rank1(self):

        self.SD1_btn.configure(state = DISABLED)
        self.top = Toplevel(root, bg='#4a4e69')
        self.top.geometry("800x674")
        self.top.title("Creative Core Codex")

        frameOne = Frame(self.top, width=800, height=75, relief=RAISED, bd=7,
                         bg='grey20')
        frameOne.propagate(0)
        frameOne.pack(side=TOP)

        y = 9
        col = 'grey40'
        col2 = 'black'

        self.MissionSelect = Frame(self.top, width=800, height=35, relief=SUNKEN, bd=5,
                                   bg='grey40')
        self.MissionSelect.pack(side=TOP)

        leftFrameDown = Frame(self.top, width=375, height=522, relief=RAISED, bd=7,
                              bg='grey20')
        leftFrameDown.propagate(0)
        leftFrameDown.pack(side=LEFT)

        self.leftFrameDown1 = Frame(leftFrameDown,
                                         width=350, height=355, relief=SUNKEN, bd=7,
                                         bg='black')
        self.leftFrameDown1.propagate(0)
        self.leftFrameDown1.pack(side=TOP)

        self.chatEntry = Entry(self.leftFrameDown1, width = 40, text = 'test', font = 'consolas 12',
                                bg = 'black', fg = 'green2', textvariable = self.chatBox1)
        self.chatEntry.pack(side = BOTTOM)

        self.Miss1_RBtn = Radiobutton(self.MissionSelect, text="1", variable=self.Miss1,
                                 value=1, bg=col, fg='black', font='consolas 12 bold',
                                      selectcolor = 'white')
        self.Miss1_RBtn.select()
        self.Miss1_RBtn.grid(row=1, column=1, padx=y, pady=2)

        self.Miss1_RBtn2 = Radiobutton(self.MissionSelect, text="2", variable=self.Miss1,
                                  value=2, bg=col, fg=col2, font='consolas 12 bold',
                                       state = DISABLED)
        self.Miss1_RBtn2.grid(row=1, column=2, padx=y, pady=2)

        self.Miss1_RBtn3 = Radiobutton(self.MissionSelect, text="3", variable=self.Miss1,
                                  value=3, bg=col, fg=col2, font='consolas 12 bold',
                                       state = DISABLED)
        self.Miss1_RBtn3.grid(row=1, column=3, padx=y, pady=2)

        self.Miss1_RBtn4 = Radiobutton(self.MissionSelect, text="4", variable=self.Miss1,
                                  value=4, bg=col, fg=col2, font='consolas 12 bold',
                                       state = DISABLED)
        self.Miss1_RBtn4.grid(row=1, column=4, padx=y, pady=2)

        self.Miss1_RBtn5 = Radiobutton(self.MissionSelect, text="5", variable=self.Miss1,
                                  value=5, bg=col, fg=col2, font='consolas 12 bold',
                                       state = DISABLED)
        self.Miss1_RBtn5.grid(row=1, column=5, padx=y, pady=2)

        self.Miss1_RBtn6 = Radiobutton(self.MissionSelect, text="6", variable=self.Miss1,
                                  value=6, bg=col, fg=col2, font='consolas 12 bold',
                                       state = DISABLED)
        self.Miss1_RBtn6.grid(row=1, column=6, padx=y, pady=2)

        self.Miss1_RBtn7 = Radiobutton(self.MissionSelect, text="7", variable=self.Miss1,
                                  value=7, bg=col, fg=col2, font='consolas 12 bold',
                                       state = DISABLED)
        self.Miss1_RBtn7.grid(row=1, column=7, padx=y, pady=2)

        self.Miss1_RBtn8 = Radiobutton(self.MissionSelect, text="8", variable=self.Miss1,
                                  value=8, bg=col, fg=col2, font='consolas 12 bold',
                                       state = DISABLED)
        self.Miss1_RBtn8.grid(row=1, column=8, padx=y, pady=2)

        self.Miss1_RBtn9 = Radiobutton(self.MissionSelect, text="9", variable=self.Miss1,
                                  value=9, bg=col, fg=col2, font='consolas 12 bold',
                                       state = DISABLED)
        self.Miss1_RBtn9.grid(row=1, column=9, padx=y, pady=2)

        self.Miss1_RBtn10 = Radiobutton(self.MissionSelect, text="10", variable=self.Miss1,
                                   value=10, bg=col, fg=col2, font='consolas 12 bold',
                                        state = DISABLED)
        self.Miss1_RBtn10.grid(row=1, column=10, padx=y, pady=2)

        self.Miss1_RBtn11 = Radiobutton(self.MissionSelect, text="11", variable=self.Miss1,
                                   value=11, bg=col, fg=col2, font='consolas 12 bold',
                                        state = DISABLED)
        self.Miss1_RBtn11.grid(row=1, column=11, padx=y, pady=2)

        self.Miss1_RBtn12 = Radiobutton(self.MissionSelect, text="12", variable=self.Miss1,
                                   value=12, bg=col, fg=col2, font='consolas 12 bold',
                                        state = DISABLED)
        self.Miss1_RBtn12.grid(row=1, column=12, padx=y, pady=2)

        self.Miss1_RBtn13 = Radiobutton(self.MissionSelect, text="13", variable=self.Miss1,
                                   value=13, bg=col, fg=col2, font='consolas 12 bold',
                                        state = DISABLED)
        self.Miss1_RBtn13.grid(row=2, column=1, padx=y, pady=2)

        self.Miss1_RBtn14 = Radiobutton(self.MissionSelect, text="14", variable=self.Miss1,
                                   value=14, bg=col, fg=col2, font='consolas 12 bold',
                                        state = DISABLED)
        self.Miss1_RBtn14.grid(row=2, column=2, padx=y, pady=2)

        self.Miss1_RBtn15 = Radiobutton(self.MissionSelect, text="15", variable=self.Miss1,
                                   value=15, bg=col, fg=col2, font='consolas 12 bold',
                                        state = DISABLED)
        self.Miss1_RBtn15.grid(row=2, column=3, padx=y, pady=2)

        self.Miss1_RBtn16 = Radiobutton(self.MissionSelect, text="16", variable=self.Miss1,
                                   value=16, bg=col, fg=col2, font='consolas 12 bold',
                                        state = DISABLED)
        self.Miss1_RBtn16.grid(row=2, column=4, padx=y, pady=2)

        self.Miss1_RBtn17 = Radiobutton(self.MissionSelect, text="17", variable=self.Miss1,
                                   value=17, bg=col, fg=col2, font='consolas 12 bold',
                                        state = DISABLED)
        self.Miss1_RBtn17.grid(row=2, column=5, padx=y, pady=2)

        self.Miss1_RBtn18 = Radiobutton(self.MissionSelect, text="18", variable=self.Miss1,
                                   value=18, bg=col, fg=col2, font='consolas 12 bold',
                                        state = DISABLED)
        self.Miss1_RBtn18.grid(row=2, column=6, padx=y, pady=2)

        self.Miss1_RBtn19 = Radiobutton(self.MissionSelect, text="19", variable=self.Miss1,
                                   value=19, bg=col, fg=col2, font='consolas 12 bold',
                                        state = DISABLED)
        self.Miss1_RBtn19.grid(row=2, column=7, padx=y, pady=2)

        self.Miss1_RBtn20 = Radiobutton(self.MissionSelect, text="20", variable=self.Miss1,
                                   value=20, bg=col, fg=col2, font='consolas 12 bold',
                                        state = DISABLED)
        self.Miss1_RBtn20.grid(row=2, column=8, padx=y, pady=2)

        self.Miss1_RBtn21 = Radiobutton(self.MissionSelect, text="21", variable=self.Miss1,
                                   value=21, bg=col, fg=col2, font='consolas 12 bold',
                                        state = DISABLED)
        self.Miss1_RBtn21.grid(row=2, column=9, padx=y, pady=2)

        self.Miss1_RBtn22 = Radiobutton(self.MissionSelect, text="22", variable=self.Miss1,
                                   value=22, bg=col, fg=col2, font='consolas 12 bold',
                                        state = DISABLED)
        self.Miss1_RBtn22.grid(row=2, column=10, padx=y, pady=2)

        self.Miss1_RBtn23 = Radiobutton(self.MissionSelect, text="23", variable=self.Miss1,
                                   value=23, bg=col, fg=col2, font='consolas 12 bold',
                                        state = DISABLED)
        self.Miss1_RBtn23.grid(row=2, column=11, padx=y, pady=2)

        self.Miss1_RBtn24 = Radiobutton(self.MissionSelect, text="24", variable=self.Miss1,
                                   value=24, bg=col, fg=col2, font='consolas 12 bold',
                                        state = DISABLED)
        self.Miss1_RBtn24.grid(row=2, column=12, padx=y, pady=2)

        self.lblScreen = Label(self.leftFrameDown1, text='test', bg='black', font='consolas 12 bold',
                               fg='green2')
        self.lblScreen.propagate(0)
        self.lblScreen.pack(fill=BOTH, expand=True)

        file_exists = os.path.exists('missionRecords4.csv')
        if not file_exists:
            self.Miss1_RBtn.configure(state = NORMAL)
            # Set all the radio buttons to false
        else:
            load_data = pd.read_csv("missionRecords4.csv")
            df = pd.DataFrame(load_data)
            mission_nums = []
            mission = 1
            if df['Mission No.'].empty:
                pass
            else:
                max_num = max(df['Mission No.'])
                for x in range(1, max_num + 1, 1):
                    try:
                        level1_rows = df.loc[(df['Mission No.'] == x)]
                        last_row = level1_rows.iloc[0]
                        Mission_No = last_row['Mission No.']
                        if Mission_No == x:
                            mission_nums.append(x)
                    except:
                        pass
                for x in mission_nums:
                    if x == 1:
                        self.Miss1_RBtn2.configure(state = NORMAL)
                    if x == 2:
                        self.Miss1_RBtn3.configure(state=NORMAL)
                    if x == 3:
                        self.Miss1_RBtn4.configure(state=NORMAL)
                    if x == 4:
                        self.Miss1_RBtn5.configure(state=NORMAL)
                    if x == 5:
                        self.Miss1_RBtn6.configure(state=NORMAL)
                    if x == 6:
                        self.Miss1_RBtn7.configure(state=NORMAL)
                    if x == 7:
                        self.Miss1_RBtn8.configure(state=NORMAL)
                    if x == 8:
                        self.Miss1_RBtn9.configure(state=NORMAL)
                    if x == 9:
                        self.Miss1_RBtn10.configure(state=NORMAL)
                    if x == 10:
                        self.Miss1_RBtn11.configure(state=NORMAL)
                    if x == 11:
                        self.Miss1_RBtn12.configure(state=NORMAL)
                    if x == 12:
                        self.Miss1_RBtn13.configure(state=NORMAL)
                    if x == 13:
                        self.Miss1_RBtn14.configure(state=NORMAL)
                    if x == 14:
                        self.Miss1_RBtn15.configure(state=NORMAL)
                    if x == 15:
                        self.Miss1_RBtn16.configure(state=NORMAL)
                    if x == 16:
                        self.Miss1_RBtn17.configure(state=NORMAL)
                    if x == 17:
                        self.Miss1_RBtn18.configure(state=NORMAL)
                    if x == 18:
                        self.Miss1_RBtn19.configure(state=NORMAL)
                    if x == 19:
                        self.Miss1_RBtn20.configure(state=NORMAL)
                    if x == 20:
                        self.Miss1_RBtn21.configure(state=NORMAL)
                    if x == 21:
                        self.Miss1_RBtn22.configure(state=NORMAL)
                    if x == 22:
                        self.Miss1_RBtn23.configure(state=NORMAL)
                    if x == 23:
                        self.Miss1_RBtn24.configure(state=NORMAL)
                    if x == 24:
                        self.SD2_btn.configure(state = NORMAL)

        self.leftMiss = Button(frameOne, text='<<<', font='Consolas 15 bold',
                          width=17, height=2, bd=8,
                          bg='grey20', fg='cornsilk', command=self.miss1Back,
                               state = DISABLED)
        self.leftMiss.pack(side=LEFT)

        self.launchBtn = Button(frameOne, text='Mission Specialist 1',
                           font='Consolas 15 bold', width=32, height=2, bd=8,
                           bg='grey20', fg='cornsilk', command=self.launch)
        self.launchBtn.pack(side = LEFT)

        self.rightMiss = Button(frameOne, text='>>>', font='Consolas 15 bold',
                           width=17, height=2, bd=8,
                           bg='grey20', fg='cornsilk', command=self.miss1For,
                                state = DISABLED)
        self.rightOn = True
        self.rightMiss.pack(side=LEFT)

        #################
        self.date = dt.datetime.now()
        self.lblDateTime = Label(leftFrameDown, width = 30, height = 1, bg = 'black',
                                 font = 'consolas 10 bold', relief = SUNKEN, bd = 2,
                                 text=f"{self.date:%A, %B %d, %Y}", fg = 'green2')

        self.lblDateTime.place(x = 72, y = 362)
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        self.keyboardCanv = Canvas(
            leftFrameDown,
            width=425,
            height=120,
            bg='grey30',
            # highlightbackground = 'black',
            relief=RAISED,
            highlightthickness=0,
        )
        self.keyboardCanv.propagate(0)
        self.keyboardCanv.pack(side=BOTTOM)
        self.keyboard_img1 = ImageTk.PhotoImage(Image.open('images/newkeyboard.png'))
        self.keyboardCanv.create_image(
            -5,
            60,
            anchor=W,
            image=self.keyboard_img1
        )

        self.btnEnter = Button(self.keyboardCanv, width = 1, height = 1, bg = 'grey50',
                               text = '', bd = 0, command = self.clickEnter1)
        self.btnEnter.place(x = 220, y = 51)

        self.btnHide = Button(self.keyboardCanv, width = 1, height = 1, bg = '#c9c9c9',
                               bd = 0, command = self.hideText)
        self.btnHide.place(x = 240, y = 66)
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

        self.rightFrameDown = Frame(self.top, width=425, height=475, relief=SUNKEN, bd=7,
                               bg='grey20')
        self.rightFrameDown.pack(side=RIGHT, expand = True, fill = BOTH)

        self.lbltest = Label(self.rightFrameDown, text='', font='consolas 12 bold',
                             width=50, height=50, bg='cornsilk',justify = LEFT, anchor = NW)
        self.lbltest.pack(side=TOP, fill = BOTH, expand = True)

        # def print_general(self, message, duration, size, wraplen, font_n, col, loc):

        self.print_general('''

[Please Select a Mission]

''', 20, 12, 350, 'consolas', 'green2', self.lblScreen)

        print(self.Miss1)

    def hideText(self):
        # Determine is on or off
        if self.is_on:
            self.chatEntry.configure(show='')
            self.is_on = False
        else:
            self.chatEntry.configure(show='*')
            self.is_on = True

    def launch(self):
        self.date = dt.datetime.now()
        self.lblDateTime.configure(text=f"{self.date:%A, %B %d, %Y}")
        #self.lblTestbox = True

        if self.planet_tracker != 0:
            self.planet_canv.destroy()

        self.leftMiss.configure(state=DISABLED)
        self.lblScreen.pack_forget()
        self.launchBtn.configure(state = DISABLED)
        # Turn off the right button when launch is clicked
        self.rightMiss.configure(state = DISABLED)

        if self.txtNotesOn:
            self.txtNotesOn = False
            self.txtNotes.pack_forget()

        if self.task_tracker == 0:
            self.lbltest.pack_forget()

            self.lbltest = Label(self.rightFrameDown, text='', font='consolas 12 bold',
                                 width=50, height=50, bg='cornsilk',justify = LEFT, anchor = NW)
            self.lbltest.pack(side=TOP, fill = BOTH, expand = True)
            self.lblTestbox = True

        elif self.task_tracker != 0 or self.lblTestbox != True:
            ##Close up all of the forward packed stuff
            self.titleFrameFor.pack_forget()
            self.dataFrameFor.pack_forget()
            self.dataFrame2B.pack_forget()
            self.dataFrame3.pack_forget()

            self.lbltest.pack_forget()

            self.lbltest = Label(self.rightFrameDown, text='', font='consolas 12 bold',
                                 width=50, height=50, bg='cornsilk', justify = LEFT, anchor = NW)
            self.lbltest.pack(side=TOP, fill = BOTH, expand = True)
            self.lblTestbox = True

        # if self.lblTestbox != True:
        #     self.lbltest = Label(self.rightFrameDown, text='', font='consolas 12 bold',
        #                          width=50, height=50, bg='cornsilk')
        #     self.lbltest.pack(side=TOP)
        #
        #     self.lblTestbox = True

        self.lblScreen = Label(self.leftFrameDown1, text='test', bg='black', font='consolas 12 bold',
                               fg='green2', width=10, height=10)
        self.lblScreen.pack(fill=BOTH, expand=True)

        self.select = self.Miss1.get()
        if self.select == 1:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement1A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement1B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 2:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement2A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement2B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 3:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement3A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement3B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 4:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement4A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement4B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 5:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement5A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement5B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 6:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement6A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement6B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 7:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement7A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement7B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 8:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement8A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement8B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 9:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement9A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement9B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 10:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement10A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement10B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 11:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement11A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement11B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 12:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement12A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement12B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 13:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement13A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement13B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 14:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement14A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement14B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 15:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement15A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement15B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 16:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement16A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement16B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 17:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement17A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement17B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 18:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement18A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement18B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 19:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement19A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement19B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 20:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement20A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement20B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 21:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement21A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement21B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 22:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement22A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement22B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 23:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement23A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement23B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        elif self.select == 24:
            self.lblScreen.configure(text='')
            self.lbltest.configure(text='')
            self.print_general(self.mission_statement24A, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.print_general(self.mission_statement24B, 1, 10, 400, 'consolas', 'black', self.lbltest)
        else:
            self.Miss1 = 1

        self.launchBtn.configure(state=NORMAL)
        self.rightMiss.configure(state=NORMAL)

    def miss1Back(self):
        self.date = dt.datetime.now()
        self.lblDateTime.configure(text=f"{self.date:%A, %B %d, %Y}")
        if self.planet_tracker != 0:
            self.planet_canv.destroy()

        self.planet_tracker += 1
        self.select = self.Miss1.get()
        self.leftMiss.configure(state=DISABLED)
        self.lblScreen.pack_forget()
        self.launchBtn.configure(state=DISABLED)
        self.rightMiss.configure(state=DISABLED)
        self.planet_canv = Canvas(
            self.leftFrameDown1, bg='black', width=10, height=10
            , highlightbackground='black')
        self.planet_canv.pack(fill=BOTH, expand=True)

        if self.task_tracker != 0:
            ##Close up all of the forward packed stuff
            self.titleFrameFor.pack_forget()
            self.dataFrameFor.pack_forget()
            self.dataFrame2B.pack_forget()
            self.dataFrame3.pack_forget()
            self.lbltest.pack_forget()
            self.lbltest = Label(self.rightFrameDown, text='', font='consolas 12 bold',
                                 width=50, height=50, bg='cornsilk', justify = LEFT, anchor = NW)
            self.lbltest.pack(side=TOP, expand = True, fill = BOTH)

        load_data = pd.read_csv("missionRecords4.csv")
        df = pd.DataFrame(load_data)

        if self.select == 1:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 1) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']

                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background.png'))
                self.planet_canv.create_image(0,0,anchor=W,image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                    for img in ImageSequence.Iterator(
                        Image.open(f'images/{self.planet_name}.gif'))]
                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)

                self.check_description(self.planet_name)
                # The planet description associated with this particular planet name.
                self.print_general(self.planet_desc, 1, 10, 407, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 2:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 2) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']

                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W,image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]
                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)

                self.check_description(self.planet_name)

                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 3:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 3) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']

                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background.png'))
                self.planet_canv.create_image(0,0,anchor=W,image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]
                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)

                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 4:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 4) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']

                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background.png'))
                self.planet_canv.create_image(0,0,anchor=W,image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]
                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 5:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 5) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']

                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W,image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]
                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 6:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 6) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']

                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background.png'))
                self.planet_canv.create_image(0,0,anchor=W,image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]
                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 7:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 7) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']

                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background.png'))
                self.planet_canv.create_image(0,0,anchor=W,image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]
                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 8:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 8) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']

                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background3.png'))
                self.planet_canv.create_image(0,0,anchor=W,image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]
                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 9:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 9) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']

                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W, image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]

                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 10:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 10) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']

                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W, image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]

                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 11:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 11) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']

                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W, image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]

                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 12:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 12) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']

                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W, image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]

                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 13:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 13) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']

                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W, image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]

                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 14:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 14) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']
                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W, image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]

                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 15:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 15) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']
                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W, image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]

                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 16:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 16) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']
                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W, image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]

                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 17:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 17) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']
                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W, image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]

                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 18:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 18) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']
                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W, image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]

                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 19:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 19) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']
                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W, image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]

                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 20:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 20) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']
                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W, image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]

                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 21:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 21) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']
                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W, image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]

                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 22:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 22) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']
                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W, image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]

                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 23:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 23) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']
                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W, image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]

                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        elif self.select == 24:
            try:
                level1_rows = df.loc[(df['Mission No.'] == 24) & (df['Planet Acquired'] == True)]
                last_row = level1_rows.iloc[0]
                self.planet_name = last_row['Planet Name']
                self.planet_background = ImageTk.PhotoImage(Image.open('images/Space Background2.png'))
                self.planet_canv.create_image(0,0,anchor=W, image=self.planet_background)
                self.seq_planet1 = [ImageTk.PhotoImage(img)
                                        for img in ImageSequence.Iterator(
                            Image.open(f'images/{self.planet_name}.gif'))]

                self.image_planet1 = self.planet_canv.create_image(165, 155, image=self.seq_planet1[0])
                self.animate_planet1(0)
                self.check_description(self.planet_name)
                self.print_general(self.planet_desc, 1, 10, 400, 'consolas','black', self.lbltest)
            except:
                self.print_general('Planet Not Found', 1, 12, 400, 'consolas', 'black', self.lbltest)

        #self.rightMiss.configure(state=NORMAL)
        self.launchBtn.configure(state=NORMAL)
        self.anim_tracker += 1

    def miss1For(self):
        self.rightMissFrames = True

        if self.txtNotesOn:
            self.txtNotes.pack_forget()
            self.txtNotesOn = False

        self.date = dt.datetime.now()
        self.lblDateTime.configure(text=f"{self.date:%A, %B %d, %Y}")
        self.task_tracker += 1
        self.lbltest.pack_forget()

        self.select = self.Miss1.get()

        self.titleFrameFor = Frame(self.rightFrameDown, width=465, height=75, relief=RAISED,
                                   bd=6, bg='grey25')
        self.titleFrameFor.pack(side=TOP, anchor=N)

        self.dataFrameFor = Frame(self.rightFrameDown, width=465, height=275, relief=RAISED,
                                  bd=6, bg='grey25')
        self.dataFrameFor.pack(side=TOP, anchor=N, expand=True, fill=BOTH)

        # for the outer criteria Frame
        self.dataFrame2B = LabelFrame(self.rightFrameDown, width=435, height=100,
                                      bg='grey25', fg='black', relief=RAISED, bd=6)
        self.dataFrame2B.pack(side=TOP, fill = BOTH, expand = True)

        # for the outer notes frame
        self.dataFrame3 = Frame(self.rightFrameDown, width=465, height=275, relief=RAISED,
                                bd=6, bg='grey25')
        self.dataFrame3.pack(side=BOTTOM, anchor=N, fill = BOTH, expand = True)

        officerFrame = Frame(self.dataFrameFor, width=195, height=150, bg='grey75',
                                  bd=1)
        officerFrame.pack(side=LEFT, expand=True, fill=BOTH)

        forFrame3 = Frame(self.dataFrameFor, width=465, height=265,
                               bg='grey70')
        forFrame3.propagate(0)
        forFrame3.pack(side=RIGHT, expand=True, fill=BOTH)

        forFrame2 = Frame(self.dataFrame2B, width=460, height=105,
                               bg='grey70')
        forFrame2.grid_propagate()
        forFrame2.pack(expand=True, fill=BOTH)

        # ++++++++++++++++++++++++++++++++++
        # Inside crit5 frame: forFrame2

        critScaleCol = 'grey70'
        critScaleFG = 'black'

        self.CritScala1 = Scale(forFrame2, from_=5, to=0, bg=critScaleCol, length=50,
                                variable = self.scale1, fg = critScaleFG, highlightbackground = 'black',
                                relief = RAISED, bd = 2)
        self.CritScala1.set(0)
        self.CritScala1.grid(row=0, column=0, padx=0, pady=(6,2))

        self.CritScala2 = Scale(forFrame2, from_=5, to=0, bg=critScaleCol, length=50,
                                variable = self.scale2, fg = critScaleFG, highlightbackground = 'black',
                                relief = RAISED, bd = 2)
        self.CritScala2.set(0)
        self.CritScala2.grid(row=0, column=1, padx=0, pady=(6,2))

        self.CritScala3 = Scale(forFrame2, from_=5, to=0, bg=critScaleCol, length=50,
                                variable = self.scale3, fg = critScaleFG, highlightbackground = 'black',
                                relief = RAISED, bd = 2)
        self.CritScala3.set(0)
        self.CritScala3.grid(row=0, column=2, padx=0, pady=(6,2))

        self.CritScala4 = Scale(forFrame2, from_=5, to=0, bg=critScaleCol, length=50,
                                variable = self.scale4, fg = critScaleFG, highlightbackground = 'black',
                                relief = RAISED, bd = 2)
        self.CritScala4.set(0)
        self.CritScala4.grid(row=0, column=3, padx=0, pady=(6,2))

        self.CritScala5 = Scale(forFrame2, from_=5, to=0, bg=critScaleCol, length=50,
                                variable = self.scale5, fg = critScaleFG, highlightbackground = 'black',
                                relief = RAISED, bd = 2)
        self.CritScala5.set(0)
        self.CritScala5.grid(row=0, column=4, padx=0, pady=(6,2))
        #######################################################################
        self.CritScala6 = Scale(forFrame2, from_=5, to=0, bg=critScaleCol, length=50,
                                fg = critScaleFG, highlightbackground = 'black',
                                relief = RAISED, bd = 2,
                                variable = self.scale6)
        self.CritScala6.set(0)
        self.CritScala6.grid(row=2, column=0, padx=0, pady=2)

        self.CritScala7 = Scale(forFrame2, from_=5, to=0, bg=critScaleCol, length=50,
                                fg = critScaleFG, highlightbackground = 'black',
                                relief = RAISED, bd = 2,
                                variable = self.scale7)
        self.CritScala7.set(0)
        self.CritScala7.grid(row=2, column=1, padx=0, pady=2)

        self.CritScala8 = Scale(forFrame2, from_=5, to=0, bg=critScaleCol, length=50,
                                fg = critScaleFG, highlightbackground = 'black',
                                relief = RAISED, bd = 2,
                                variable = self.scale8)
        self.CritScala8.set(0)
        self.CritScala8.grid(row=2, column=2, padx=0, pady=2)

        self.CritScala9 = Scale(forFrame2, from_=5, to=0, bg=critScaleCol, length=50,
                                fg = critScaleFG, highlightbackground = 'black',
                                relief = RAISED, bd = 2,
                                variable = self.scale9)
        self.CritScala9.set(0)
        self.CritScala9.grid(row=2, column=3, padx=0, pady=2)

        self.CritScala10 = Scale(forFrame2, from_=5, to=0, bg=critScaleCol, length=50,
                                 fg = critScaleFG, highlightbackground = 'black',
                                 relief = RAISED, bd = 2,
                                variable = self.scale10)
        self.CritScala10.set(0)
        self.CritScala10.grid(row=2, column=4, padx=0, pady=2)

        # ++++++++++++++++++++++++++++++++++
        # Inside crit5 frame: forFrame2

        lblCrit1 = Label(forFrame2, text='Conc.', font='consolas 10', width=6,
                         height=1, bg='grey70', fg = critScaleFG)
        lblCrit1.grid(row=1, column=0, padx=15, pady=2)

        lblCrit2 = Label(forFrame2, text='Read.', font='consolas 10', width=6,
                         height=1, bg='grey70', fg = critScaleFG)
        lblCrit2.grid(row=1, column=1, padx=15, pady=2)

        lblCrit3 = Label(forFrame2, text='Qual.', font='consolas 10', width=6,
                         height=1, bg='grey70', fg = critScaleFG)
        lblCrit3.grid(row=1, column=2, padx=15, pady=2)

        lblCrit4 = Label(forFrame2, text='Innov.', font='consolas 10', width=6,
                         height=1, bg='grey70', fg = critScaleFG)
        lblCrit4.grid(row=1, column=3, padx=15, pady=2)

        lblCrit5 = Label(forFrame2, text='Simpl.', font='consolas 10', width=6,
                         height=1, bg='grey70', fg = critScaleFG)
        lblCrit5.grid(row=1, column=4, padx=15, pady=2)


        lblCrit6 = Label(forFrame2, text='Cont.', font='consolas 10', width=6,
                         height=1, bg='grey70', fg = critScaleFG)
        lblCrit6.grid(row=3, column=0, padx=15, pady=2)

        lblCrit7 = Label(forFrame2, text='Origin.', font='consolas 10', width=6,
                         height=1, bg='grey70', fg = critScaleFG)
        lblCrit7.grid(row=3, column=1, padx=15, pady=2)

        lblCrit8 = Label(forFrame2, text='BodyL.', font='consolas 10', width=6,
                         height=1, bg='grey70', fg = critScaleFG)
        lblCrit8.grid(row=3, column=2, padx=15, pady=2)

        lblCrit9 = Label(forFrame2, text='Struct.', font='consolas 10', width=6,
                         height=1, bg='grey70', fg = critScaleFG)
        lblCrit9.grid(row=3, column=3, padx=15, pady=2)

        lblCrit10 = Label(forFrame2, text='Deliv.', font='consolas 10', width=6,
                         height=1, bg='grey70', fg = critScaleFG)
        lblCrit10.grid(row=3, column=4, padx=15, pady=2)
        # ++++++++++++++++++++++++++++++++++

        self.officerCanv = Canvas(officerFrame, width=195, height=150, bg='black', relief=SUNKEN,
                                  bd=5, highlightbackground = 'black')
        self.officerCanv.pack(expand=True, fill=BOTH)

        forFrame5 = Frame(self.dataFrame3, width=435, height=200,
                               bg='grey25')
        forFrame5.grid(row=2, column=0, columnspan=2)

        # ****************************#
        self.btnLoadOne = Button(self.titleFrameFor, text='Load', width=7, height=1,
                            bg='grey20', fg='cornsilk', bd=3, font='consolas 16 bold',
                                 command = self.loadRecordA1, state = NORMAL)
        self.btnLoadOne.pack(side=LEFT)
        # if there's been a saved variable set to True or >= 1
            # state of button btnLoadOne is NORMAL

        lblTaskMaster = Button(self.titleFrameFor, text='Task Master', width=16, height=1,
                               bg='grey20', fg='cornsilk', relief=RAISED,
                               bd=3, font='consolas 16 bold', command=self.task_master)
        lblTaskMaster.pack(side=LEFT)

        self.btnSaveOne = Button(self.titleFrameFor, text='Save', width=7, height=1,
                            bg='grey20', fg='cornsilk', bd=3, font='consolas 16 bold',
                            command = self.SaveRecord1A, state = DISABLED)
        self.btnSaveOne.pack(side=LEFT)
        # This button is enabled only when a mentor/instructor has entered the password

        #################################################################################

        lblGClass = Label(forFrame3, font='consolas 10 bold', width=5, height=1,
                          text='1.', bg='grey70', fg=critScaleFG)
        lblGClass.grid(row=0, column=0, padx=5, pady=5)

        self.chkGClass = Checkbutton(forFrame3, font='consolas 10', text='Uploaded',
                                width=10, height=1, fg=critScaleFG, bg='grey70',
                                     variable = self.GclassCheck)
        self.chkGClass.deselect()
        self.chkGClass.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        lblTeachable = Label(forFrame3, font='consolas 10 bold', width=5, height=1,
                             text='2.', bg='grey70', fg=critScaleFG)
        lblTeachable.grid(row=1, column=0, padx=5, pady=5)

        self.chkTeachable = Checkbutton(forFrame3, font='consolas 10', text='Teachable',
                                   width=10, height=1, fg=critScaleFG, bg='grey70',
                                        variable = self.teachCheck)
        self.chkTeachable.deselect()
        self.chkTeachable.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        lblQuiz = Label(forFrame3, font='consolas 10 bold', width=5, height=1,
                        text='3.', bg='grey70', fg=critScaleFG)
        lblQuiz.grid(row=2, column=0, padx=5, pady=5)

        self.chkQuiz = Checkbutton(forFrame3, font='consolas 10', text='Quiz',
                              width=10, height=1, fg=critScaleFG, bg='grey70',
                                   variable = self.QuizCheck)
        self.chkQuiz.deselect()
        self.chkQuiz.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        lblCrit = Label(forFrame3, font='consolas 10 bold', width=5, height=1,
                        text='4.', bg='grey70', fg=critScaleFG)
        lblCrit.grid(row=3, column=0, padx=5, pady=5)

        self.chkCrit = Checkbutton(forFrame3, font='consolas 10', text='Criteria',
                              width=10, height=1, fg=critScaleFG, bg='grey70',
                                   variable = self.CritCheck)
        self.chkCrit.deselect()
        self.chkCrit.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        lblOfficer = Label(forFrame3, font='consolas 10 bold', width=5, height=1,
                           text='5.', bg='grey70', fg=critScaleFG)
        lblOfficer.grid(row=4, column=0, padx=5, pady=5)

        officerList = ['Lannon Khau', 'Benny Chiu', 'Fernando Galvez', 'Joshua Sanchez']
        self.officerCheck = ttk.Combobox(forFrame3, values=officerList, width=13, textvariable=self.CC_Officers)
        self.officerCheck.set('Officers')
        self.officerCheck.grid(row=4, column=1, padx=5, pady=5)

        # self.officer_img1 = ImageTk.PhotoImage(Image.open('images/spaceforce3.png'))
        # self.officerCanv.create_image(-5, 112,
        #                               anchor=W,
        #                               image=self.officer_img1)
        # btnSubmit1A = Button(forFrame3, height = 1, width = 6,
        #                      text = 'Submit', bg = 'indianred', font = 'consolas 10 bold')
        # btnSubmit1A.grid(row = 2, column = 2, padx = 5, pady = 5)

        self.notesEntry1A = Text(forFrame5,
                            height=3, bg='cornsilk', fg='black',
                            font='consolas 12', width=43)
        self.notesEntry1A.pack(anchor=SW, padx=5, pady=2)

        header = [self.student1, 'Mission No.', 'Date','Application', 'Readability', 'Quality',
                  'Creativity', 'Cleanliness', 'Content', 'Originality','Body Language', 'Structure', 'Delivery',
                  'Google C.', 'Teachable', 'Quiz Taken', 'Presentation Check', 'Officer', 'Notes',
                  'Planet Acquired','Planet Name','Planet Type']

        file_exists = os.path.exists('missionRecords4.csv')
        if not file_exists:
            self.btnLoadOne.configure(state = DISABLED)
            with open('missionRecords4.csv', 'w', newline = '') as f:
                writer = csv.writer(f)
                writer.writerow(header)

        if self.select == 1:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)

            if not (1 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

        if self.select == 2:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)

            if not (2 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.TwoScale1)
            self.CritScala2.configure(variable=self.TwoScale2)
            self.CritScala3.configure(variable=self.TwoScale3)
            self.CritScala4.configure(variable=self.TwoScale4)
            self.CritScala5.configure(variable=self.TwoScale5)
            self.CritScala6.configure(variable=self.TwoScale6)
            self.CritScala7.configure(variable=self.TwoScale7)
            self.CritScala8.configure(variable=self.TwoScale8)
            self.CritScala9.configure(variable=self.TwoScale9)
            self.CritScala10.configure(variable=self.TwoScale10)

            self.chkGClass.configure(variable=self.TwoGClassCheck)
            self.chkTeachable.configure(variable=self.TwoTeachCheck)
            self.chkQuiz.configure(variable=self.TwoQuizCheck)
            self.chkCrit.configure(variable=self.TwoCritCheck)
            self.officerCheck.configure(textvariable=self.TwoCC_Officers)
            self.officerCheck.set('Officers')

        elif self.select == 3:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (3 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.ThreeScale1)
            self.CritScala2.configure(variable=self.ThreeScale2)
            self.CritScala3.configure(variable=self.ThreeScale3)
            self.CritScala4.configure(variable=self.ThreeScale4)
            self.CritScala5.configure(variable=self.ThreeScale5)
            self.CritScala6.configure(variable=self.ThreeScale6)
            self.CritScala7.configure(variable=self.ThreeScale7)
            self.CritScala8.configure(variable=self.ThreeScale8)
            self.CritScala9.configure(variable=self.ThreeScale9)
            self.CritScala10.configure(variable=self.ThreeScale10)

            self.chkGClass.configure(variable=self.ThreeGClassCheck)
            self.chkTeachable.configure(variable=self.ThreeTeachCheck)
            self.chkQuiz.configure(variable=self.ThreeQuizCheck)
            self.chkCrit.configure(variable=self.ThreeCritCheck)
            self.officerCheck.configure(textvariable=self.ThreeCC_Officers)

        elif self.select == 4:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (4 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.FourScale1)
            self.CritScala2.configure(variable=self.FourScale2)
            self.CritScala3.configure(variable=self.FourScale3)
            self.CritScala4.configure(variable=self.FourScale4)
            self.CritScala5.configure(variable=self.FourScale5)
            self.CritScala6.configure(variable=self.FourScale6)
            self.CritScala7.configure(variable=self.FourScale7)
            self.CritScala8.configure(variable=self.FourScale8)
            self.CritScala9.configure(variable=self.FourScale9)
            self.CritScala10.configure(variable=self.FourScale10)
            #
            self.chkGClass.configure(variable=self.FourGClassCheck)
            self.chkTeachable.configure(variable=self.FourTeachCheck)
            self.chkQuiz.configure(variable=self.FourQuizCheck)
            self.chkCrit.configure(variable=self.FourCritCheck)
            self.officerCheck.configure(textvariable=self.FourCC_Officers)

        elif self.select == 5:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (5 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.FiveScale1)
            self.CritScala2.configure(variable=self.FiveScale2)
            self.CritScala3.configure(variable=self.FiveScale3)
            self.CritScala4.configure(variable=self.FiveScale4)
            self.CritScala5.configure(variable=self.FiveScale5)
            self.CritScala6.configure(variable=self.FiveScale6)
            self.CritScala7.configure(variable=self.FiveScale7)
            self.CritScala8.configure(variable=self.FiveScale8)
            self.CritScala9.configure(variable=self.FiveScale9)
            self.CritScala10.configure(variable=self.FiveScale10)
            #
            self.chkGClass.configure(variable=self.FiveGClassCheck)
            self.chkTeachable.configure(variable=self.FiveTeachCheck)
            self.chkQuiz.configure(variable=self.FiveQuizCheck)
            self.chkCrit.configure(variable=self.FiveCritCheck)
            self.officerCheck.configure(textvariable=self.FiveCC_Officers)

        elif self.select == 6:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (6 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.SixScale1)
            self.CritScala2.configure(variable=self.SixScale2)
            self.CritScala3.configure(variable=self.SixScale3)
            self.CritScala4.configure(variable=self.SixScale4)
            self.CritScala5.configure(variable=self.SixScale5)
            self.CritScala6.configure(variable=self.SixScale6)
            self.CritScala7.configure(variable=self.SixScale7)
            self.CritScala8.configure(variable=self.SixScale8)
            self.CritScala9.configure(variable=self.SixScale9)
            self.CritScala10.configure(variable=self.SixScale10)
            #
            #
            self.chkGClass.configure(variable=self.SixGClassCheck)
            self.chkTeachable.configure(variable=self.SixTeachCheck)
            self.chkQuiz.configure(variable=self.SixQuizCheck)
            self.chkCrit.configure(variable=self.SixCritCheck)
            self.officerCheck.configure(textvariable=self.SixCC_Officers)

        elif self.select == 7:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (7 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.SevenScale1)
            self.CritScala2.configure(variable=self.SevenScale2)
            self.CritScala3.configure(variable=self.SevenScale3)
            self.CritScala4.configure(variable=self.SevenScale4)
            self.CritScala5.configure(variable=self.SevenScale5)
            self.CritScala6.configure(variable=self.SevenScale6)
            self.CritScala7.configure(variable=self.SevenScale7)
            self.CritScala8.configure(variable=self.SevenScale8)
            self.CritScala9.configure(variable=self.SevenScale9)
            self.CritScala10.configure(variable=self.SevenScale10)
            #
            self.chkGClass.configure(variable=self.SevenGClassCheck)
            self.chkTeachable.configure(variable=self.SevenTeachCheck)
            self.chkQuiz.configure(variable=self.SevenQuizCheck)
            self.chkCrit.configure(variable=self.SevenCritCheck)
            self.officerCheck.configure(textvariable=self.SevenCC_Officers)

        elif self.select == 8:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (8 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.EightScale1)
            self.CritScala2.configure(variable=self.EightScale2)
            self.CritScala3.configure(variable=self.EightScale3)
            self.CritScala4.configure(variable=self.EightScale4)
            self.CritScala5.configure(variable=self.EightScale5)
            self.CritScala6.configure(variable=self.EightScale6)
            self.CritScala7.configure(variable=self.EightScale7)
            self.CritScala8.configure(variable=self.EightScale8)
            self.CritScala9.configure(variable=self.EightScale9)
            self.CritScala10.configure(variable=self.EightScale10)
            #
            #
            self.chkGClass.configure(variable=self.EightGClassCheck)
            self.chkTeachable.configure(variable=self.EightTeachCheck)
            self.chkQuiz.configure(variable=self.EightQuizCheck)
            self.chkCrit.configure(variable=self.EightCritCheck)
            self.officerCheck.configure(textvariable=self.EightCC_Officers)

        elif self.select == 9:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (9 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.NineScale1)
            self.CritScala2.configure(variable=self.NineScale2)
            self.CritScala3.configure(variable=self.NineScale3)
            self.CritScala4.configure(variable=self.NineScale4)
            self.CritScala5.configure(variable=self.NineScale5)
            self.CritScala6.configure(variable=self.NineScale6)
            self.CritScala7.configure(variable=self.NineScale7)
            self.CritScala8.configure(variable=self.NineScale8)
            self.CritScala9.configure(variable=self.NineScale9)
            self.CritScala10.configure(variable=self.NineScale10)
            #
            self.chkGClass.configure(variable=self.NineGClassCheck)
            self.chkTeachable.configure(variable=self.NineTeachCheck)
            self.chkQuiz.configure(variable=self.NineQuizCheck)
            self.chkCrit.configure(variable=self.NineCritCheck)
            self.officerCheck.configure(textvariable=self.NineCC_Officers)

        elif self.select == 10:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (10 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.TenScale1)
            self.CritScala2.configure(variable=self.TenScale2)
            self.CritScala3.configure(variable=self.TenScale3)
            self.CritScala4.configure(variable=self.TenScale4)
            self.CritScala5.configure(variable=self.TenScale5)
            self.CritScala6.configure(variable=self.TenScale6)
            self.CritScala7.configure(variable=self.TenScale7)
            self.CritScala8.configure(variable=self.TenScale8)
            self.CritScala9.configure(variable=self.TenScale9)
            self.CritScala10.configure(variable=self.TenScale10)
            #
            self.chkGClass.configure(variable=self.TenGClassCheck)
            self.chkTeachable.configure(variable=self.TenTeachCheck)
            self.chkQuiz.configure(variable=self.TenQuizCheck)
            self.chkCrit.configure(variable=self.TenCritCheck)
            self.officerCheck.configure(textvariable=self.TenCC_Officers)

        elif self.select == 11:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (11 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.ElevenScale1)
            self.CritScala2.configure(variable=self.ElevenScale2)
            self.CritScala3.configure(variable=self.ElevenScale3)
            self.CritScala4.configure(variable=self.ElevenScale4)
            self.CritScala5.configure(variable=self.ElevenScale5)
            self.CritScala6.configure(variable=self.ElevenScale6)
            self.CritScala7.configure(variable=self.ElevenScale7)
            self.CritScala8.configure(variable=self.ElevenScale8)
            self.CritScala9.configure(variable=self.ElevenScale9)
            self.CritScala10.configure(variable=self.ElevenScale10)
            #
            self.chkGClass.configure(variable=self.ElevenGClassCheck)
            self.chkTeachable.configure(variable=self.ElevenTeachCheck)
            self.chkQuiz.configure(variable=self.ElevenQuizCheck)
            self.chkCrit.configure(variable=self.ElevenCritCheck)
            self.officerCheck.configure(textvariable=self.ElevenCC_Officers)

        elif self.select == 12:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (12 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.TwelveScale1)
            self.CritScala2.configure(variable=self.TwelveScale2)
            self.CritScala3.configure(variable=self.TwelveScale3)
            self.CritScala4.configure(variable=self.TwelveScale4)
            self.CritScala5.configure(variable=self.TwelveScale5)
            self.CritScala6.configure(variable=self.TwelveScale6)
            self.CritScala7.configure(variable=self.TwelveScale7)
            self.CritScala8.configure(variable=self.TwelveScale8)
            self.CritScala9.configure(variable=self.TwelveScale9)
            self.CritScala10.configure(variable=self.TwelveScale10)
            #
            self.chkGClass.configure(variable=self.TwelveGClassCheck)
            self.chkTeachable.configure(variable=self.TwelveTeachCheck)
            self.chkQuiz.configure(variable=self.TwelveQuizCheck)
            self.chkCrit.configure(variable=self.TwelveCritCheck)
            self.officerCheck.configure(textvariable=self.TwelveCC_Officers)

        elif self.select == 13:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (13 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.ThirteenScale1)
            self.CritScala2.configure(variable=self.ThirteenScale2)
            self.CritScala3.configure(variable=self.ThirteenScale3)
            self.CritScala4.configure(variable=self.ThirteenScale4)
            self.CritScala5.configure(variable=self.ThirteenScale5)
            self.CritScala6.configure(variable=self.ThirteenScale6)
            self.CritScala7.configure(variable=self.ThirteenScale7)
            self.CritScala8.configure(variable=self.ThirteenScale8)
            self.CritScala9.configure(variable=self.ThirteenScale9)
            self.CritScala10.configure(variable=self.ThirteenScale10)
            #
            self.chkGClass.configure(variable=self.ThirteenGClassCheck)
            self.chkTeachable.configure(variable=self.ThirteenTeachCheck)
            self.chkQuiz.configure(variable=self.ThirteenQuizCheck)
            self.chkCrit.configure(variable=self.ThirteenCritCheck)
            self.officerCheck.configure(textvariable=self.ThirteenCC_Officers)

        elif self.select == 14:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (14 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.FourteenScale1)
            self.CritScala2.configure(variable=self.FourteenScale2)
            self.CritScala3.configure(variable=self.FourteenScale3)
            self.CritScala4.configure(variable=self.FourteenScale4)
            self.CritScala5.configure(variable=self.FourteenScale5)
            self.CritScala6.configure(variable=self.FourteenScale6)
            self.CritScala7.configure(variable=self.FourteenScale7)
            self.CritScala8.configure(variable=self.FourteenScale8)
            self.CritScala9.configure(variable=self.FourteenScale9)
            self.CritScala10.configure(variable=self.FourteenScale10)
            #
            self.chkGClass.configure(variable=self.FourteenGClassCheck)
            self.chkTeachable.configure(variable=self.FourteenTeachCheck)
            self.chkQuiz.configure(variable=self.FourteenQuizCheck)
            self.chkCrit.configure(variable=self.FourteenCritCheck)
            self.officerCheck.configure(textvariable=self.FourteenCC_Officers)

        elif self.select == 15:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (15 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.FifteenScale1)
            self.CritScala2.configure(variable=self.FifteenScale2)
            self.CritScala3.configure(variable=self.FifteenScale3)
            self.CritScala4.configure(variable=self.FifteenScale4)
            self.CritScala5.configure(variable=self.FifteenScale5)
            self.CritScala6.configure(variable=self.FifteenScale6)
            self.CritScala7.configure(variable=self.FifteenScale7)
            self.CritScala8.configure(variable=self.FifteenScale8)
            self.CritScala9.configure(variable=self.FifteenScale9)
            self.CritScala10.configure(variable=self.FifteenScale10)
            #
            self.chkGClass.configure(variable=self.FifteenGClassCheck)
            self.chkTeachable.configure(variable=self.FifteenTeachCheck)
            self.chkQuiz.configure(variable=self.FifteenQuizCheck)
            self.chkCrit.configure(variable=self.FifteenCritCheck)
            self.officerCheck.configure(textvariable=self.FifteenCC_Officers)

        elif self.select == 16:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (16 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.SixteenScale1)
            self.CritScala2.configure(variable=self.SixteenScale2)
            self.CritScala3.configure(variable=self.SixteenScale3)
            self.CritScala4.configure(variable=self.SixteenScale4)
            self.CritScala5.configure(variable=self.SixteenScale5)
            self.CritScala6.configure(variable=self.SixteenScale6)
            self.CritScala7.configure(variable=self.SixteenScale7)
            self.CritScala8.configure(variable=self.SixteenScale8)
            self.CritScala9.configure(variable=self.SixteenScale9)
            self.CritScala10.configure(variable=self.SixteenScale10)
            #
            self.chkGClass.configure(variable=self.SixteenGClassCheck)
            self.chkTeachable.configure(variable=self.SixteenTeachCheck)
            self.chkQuiz.configure(variable=self.SixteenQuizCheck)
            self.chkCrit.configure(variable=self.SixteenCritCheck)
            self.officerCheck.configure(textvariable=self.SixteenCC_Officers)

        elif self.select == 17:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (17 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.SeventeenScale1)
            self.CritScala2.configure(variable=self.SeventeenScale2)
            self.CritScala3.configure(variable=self.SeventeenScale3)
            self.CritScala4.configure(variable=self.SeventeenScale4)
            self.CritScala5.configure(variable=self.SeventeenScale5)
            self.CritScala6.configure(variable=self.SeventeenScale6)
            self.CritScala7.configure(variable=self.SeventeenScale7)
            self.CritScala8.configure(variable=self.SeventeenScale8)
            self.CritScala9.configure(variable=self.SeventeenScale9)
            self.CritScala10.configure(variable=self.SeventeenScale10)
            #
            self.chkGClass.configure(variable=self.SeventeenGClassCheck)
            self.chkTeachable.configure(variable=self.SeventeenTeachCheck)
            self.chkQuiz.configure(variable=self.SeventeenQuizCheck)
            self.chkCrit.configure(variable=self.SeventeenCritCheck)
            self.officerCheck.configure(textvariable=self.SeventeenCC_Officers)

        elif self.select == 18:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (18 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.EighteenScale1)
            self.CritScala2.configure(variable=self.EighteenScale2)
            self.CritScala3.configure(variable=self.EighteenScale3)
            self.CritScala4.configure(variable=self.EighteenScale4)
            self.CritScala5.configure(variable=self.EighteenScale5)
            self.CritScala6.configure(variable=self.EighteenScale6)
            self.CritScala7.configure(variable=self.EighteenScale7)
            self.CritScala8.configure(variable=self.EighteenScale8)
            self.CritScala9.configure(variable=self.EighteenScale9)
            self.CritScala10.configure(variable=self.EighteenScale10)
            #
            self.chkGClass.configure(variable=self.EighteenGClassCheck)
            self.chkTeachable.configure(variable=self.EighteenTeachCheck)
            self.chkQuiz.configure(variable=self.EighteenQuizCheck)
            self.chkCrit.configure(variable=self.EighteenCritCheck)
            self.officerCheck.configure(textvariable=self.EighteenCC_Officers)

        elif self.select == 19:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (19 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.NineteenScale1)
            self.CritScala2.configure(variable=self.NineteenScale2)
            self.CritScala3.configure(variable=self.NineteenScale3)
            self.CritScala4.configure(variable=self.NineteenScale4)
            self.CritScala5.configure(variable=self.NineteenScale5)
            self.CritScala6.configure(variable=self.NineteenScale6)
            self.CritScala7.configure(variable=self.NineteenScale7)
            self.CritScala8.configure(variable=self.NineteenScale8)
            self.CritScala9.configure(variable=self.NineteenScale9)
            self.CritScala10.configure(variable=self.NineteenScale10)
            #
            self.chkGClass.configure(variable=self.NineteenGClassCheck)
            self.chkTeachable.configure(variable=self.NineteenTeachCheck)
            self.chkQuiz.configure(variable=self.NineteenQuizCheck)
            self.chkCrit.configure(variable=self.NineteenCritCheck)
            self.officerCheck.configure(textvariable=self.NineteenCC_Officers)

        elif self.select == 20:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (20 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.TwentyScale1)
            self.CritScala2.configure(variable=self.TwentyScale2)
            self.CritScala3.configure(variable=self.TwentyScale3)
            self.CritScala4.configure(variable=self.TwentyScale4)
            self.CritScala5.configure(variable=self.TwentyScale5)
            self.CritScala6.configure(variable=self.TwentyScale6)
            self.CritScala7.configure(variable=self.TwentyScale7)
            self.CritScala8.configure(variable=self.TwentyScale8)
            self.CritScala9.configure(variable=self.TwentyScale9)
            self.CritScala10.configure(variable=self.TwentyScale10)
            #
            self.chkGClass.configure(variable=self.TwentyGClassCheck)
            self.chkTeachable.configure(variable=self.TwentyTeachCheck)
            self.chkQuiz.configure(variable=self.TwentyQuizCheck)
            self.chkCrit.configure(variable=self.TwentyCritCheck)
            self.officerCheck.configure(textvariable=self.TwentyCC_Officers)

        elif self.select == 21:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (21 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.TwentyOneScale1)
            self.CritScala2.configure(variable=self.TwentyOneScale2)
            self.CritScala3.configure(variable=self.TwentyOneScale3)
            self.CritScala4.configure(variable=self.TwentyOneScale4)
            self.CritScala5.configure(variable=self.TwentyOneScale5)
            self.CritScala6.configure(variable=self.TwentyOneScale6)
            self.CritScala7.configure(variable=self.TwentyOneScale7)
            self.CritScala8.configure(variable=self.TwentyOneScale8)
            self.CritScala9.configure(variable=self.TwentyOneScale9)
            self.CritScala10.configure(variable=self.TwentyOneScale10)
            #
            self.chkGClass.configure(variable=self.TwentyOneGClassCheck)
            self.chkTeachable.configure(variable=self.TwentyOneTeachCheck)
            self.chkQuiz.configure(variable=self.TwentyOneQuizCheck)
            self.chkCrit.configure(variable=self.TwentyOneCritCheck)
            self.officerCheck.configure(textvariable=self.TwentyOneCC_Officers)

        elif self.select == 22:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (22 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.TwentyTwoScale1)
            self.CritScala2.configure(variable=self.TwentyTwoScale2)
            self.CritScala3.configure(variable=self.TwentyTwoScale3)
            self.CritScala4.configure(variable=self.TwentyTwoScale4)
            self.CritScala5.configure(variable=self.TwentyTwoScale5)
            self.CritScala6.configure(variable=self.TwentyTwoScale6)
            self.CritScala7.configure(variable=self.TwentyTwoScale7)
            self.CritScala8.configure(variable=self.TwentyTwoScale8)
            self.CritScala9.configure(variable=self.TwentyTwoScale9)
            self.CritScala10.configure(variable=self.TwentyTwoScale10)
            #
            self.chkGClass.configure(variable=self.TwentyTwoGClassCheck)
            self.chkTeachable.configure(variable=self.TwentyTwoTeachCheck)
            self.chkQuiz.configure(variable=self.TwentyTwoQuizCheck)
            self.chkCrit.configure(variable=self.TwentyTwoCritCheck)
            self.officerCheck.configure(textvariable=self.TwentyTwoCC_Officers)

        elif self.select == 23:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (23 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.TwentyThreeScale1)
            self.CritScala2.configure(variable=self.TwentyThreeScale2)
            self.CritScala3.configure(variable=self.TwentyThreeScale3)
            self.CritScala4.configure(variable=self.TwentyThreeScale4)
            self.CritScala5.configure(variable=self.TwentyThreeScale5)
            self.CritScala6.configure(variable=self.TwentyThreeScale6)
            self.CritScala7.configure(variable=self.TwentyThreeScale7)
            self.CritScala8.configure(variable=self.TwentyThreeScale8)
            self.CritScala9.configure(variable=self.TwentyThreeScale9)
            self.CritScala10.configure(variable=self.TwentyThreeScale10)
            #
            self.chkGClass.configure(variable=self.TwentyThreeGClassCheck)
            self.chkTeachable.configure(variable=self.TwentyThreeTeachCheck)
            self.chkQuiz.configure(variable=self.TwentyThreeQuizCheck)
            self.chkCrit.configure(variable=self.TwentyThreeCritCheck)
            self.officerCheck.configure(textvariable=self.TwentyThreeCC_Officers)

        elif self.select == 24:
            load_data = pd.read_csv('missionRecords4.csv')
            df = pd.DataFrame(load_data)
            if not (24 in set(df['Mission No.'])):
                self.btnLoadOne.configure(state=DISABLED)

            self.CritScala1.configure(variable=self.TwentyFourScale1)
            self.CritScala2.configure(variable=self.TwentyFourScale2)
            self.CritScala3.configure(variable=self.TwentyFourScale3)
            self.CritScala4.configure(variable=self.TwentyFourScale4)
            self.CritScala5.configure(variable=self.TwentyFourScale5)
            self.CritScala6.configure(variable=self.TwentyFourScale6)
            self.CritScala7.configure(variable=self.TwentyFourScale7)
            self.CritScala8.configure(variable=self.TwentyFourScale8)
            self.CritScala9.configure(variable=self.TwentyFourScale9)
            self.CritScala10.configure(variable=self.TwentyFourScale10)
            #
            self.chkGClass.configure(variable=self.TwentyFourGClassCheck)
            self.chkTeachable.configure(variable=self.TwentyFourTeachCheck)
            self.chkQuiz.configure(variable=self.TwentyFourQuizCheck)
            self.chkCrit.configure(variable=self.TwentyFourCritCheck)
            self.officerCheck.configure(textvariable=self.TwentyFourCC_Officers)

        self.CritScala1.set(0)
        self.CritScala2.set(0)
        self.CritScala3.set(0)
        self.CritScala4.set(0)
        self.CritScala5.set(0)
        self.CritScala6.set(0)
        self.CritScala7.set(0)
        self.CritScala8.set(0)
        self.CritScala9.set(0)
        self.CritScala10.set(0)

        self.chkGClass.deselect()
        self.chkTeachable.deselect()
        self.chkQuiz.deselect()
        self.chkCrit.deselect()
        self.officerCheck.set('Officers')

        self.rightMiss.configure(state=DISABLED)
        self.launchBtn.configure(state=NORMAL)

        # student details for mission 1
        # def details_mission1(self, student1)
    def clickEnter1(self):
        if self.planet_tracker != 0:
            self.planet_canv.pack_forget()

        self.planet_tracker += 1
        self.select = self.Miss1.get()
        self.chat = self.chatBox1.get()

        self.leftMiss.configure(state=DISABLED)
        self.lblScreen.destroy()
        self.lbltest.configure(text = '')
        self.launchBtn.configure(state=DISABLED)

        self.planet_canv = Canvas(
            self.leftFrameDown1, bg='black', width=10, height=10
            , highlightbackground='black')
        self.planet_canv.pack(fill=BOTH, expand=True)

        if self.select == 1:
            try:
                self.planet_canv.pack_forget()

                self.CritScala1.configure(variable=self.scale1)
                self.CritScala2.configure(variable=self.scale2)
                self.CritScala3.configure(variable=self.scale3)
                self.CritScala4.configure(variable=self.scale4)
                self.CritScala5.configure(variable=self.scale5)
                self.CritScala6.configure(variable=self.scale6)
                self.CritScala7.configure(variable=self.scale7)
                self.CritScala8.configure(variable=self.scale8)
                self.CritScala9.configure(variable=self.scale9)
                self.CritScala10.configure(variable=self.scale10)

                self.chkGClass.configure(variable=self.GclassCheck)
                self.chkTeachable.configure(variable=self.teachCheck)
                self.chkQuiz.configure(variable=self.QuizCheck)
                self.chkCrit.configure(variable=self.CritCheck)
                self.officerCheck.configure(textvariable=self.CC_Officers)

                if self.chat == '123456':
                    self.planet_canv = Canvas(
                        self.leftFrameDown1, bg='black', width=10, height=10
                        , highlightbackground='black')
                    self.planet_canv.pack(fill=BOTH, expand=True)

                    #self.lblScreen.destroy()
                    officer = self.CC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)
                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.scale1.get())
                    b = int(self.scale2.get())
                    c = int(self.scale3.get())
                    d = int(self.scale4.get())
                    e = int(self.scale5.get())
                    f = int(self.scale6.get())
                    g = int(self.scale7.get())
                    h = int(self.scale8.get())
                    i = int(self.scale9.get())
                    j = int(self.scale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)
                    self.right_on = False

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat == '/open_source.txt':
                    self.lbltest.pack_forget()
                    self.txtNotesOn = True
                    self.show_text('/open_source.txt')

                if self.chat == '/planet_inv.exe':
                    self.lbltest.pack_forget()
                    self.txtNotesOn = False
                    self.show_text('/planet_inv.exe')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 2:
            try:
                #self.planet_canv.pack_forget()

                self.CritScala1.configure(variable=self.TwoScale1)
                self.CritScala2.configure(variable=self.TwoScale2)
                self.CritScala3.configure(variable=self.TwoScale3)
                self.CritScala4.configure(variable=self.TwoScale4)
                self.CritScala5.configure(variable=self.TwoScale5)
                self.CritScala6.configure(variable=self.TwoScale6)
                self.CritScala7.configure(variable=self.TwoScale7)
                self.CritScala8.configure(variable=self.TwoScale8)
                self.CritScala9.configure(variable=self.TwoScale9)
                self.CritScala10.configure(variable=self.TwoScale10)

                self.chkGClass.configure(variable=self.TwoGClassCheck)
                self.chkTeachable.configure(variable=self.TwoTeachCheck)
                self.chkQuiz.configure(variable=self.TwoQuizCheck)
                self.chkCrit.configure(variable=self.TwoCritCheck)
                self.officerCheck.configure(textvariable=self.TwoCC_Officers)

                if self.chat == '123456':

                    officer = self.TwoCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)
                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.TwoScale1.get())
                    b = int(self.TwoScale2.get())
                    c = int(self.TwoScale3.get())
                    d = int(self.TwoScale4.get())
                    e = int(self.TwoScale5.get())
                    f = int(self.TwoScale6.get())
                    g = int(self.TwoScale7.get())
                    h = int(self.TwoScale8.get())
                    i = int(self.TwoScale9.get())
                    j = int(self.TwoScale10.get())

                    print('Showing spider!!')
                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 3:
            try:
                self.CritScala1.configure(variable=self.ThreeScale1)
                self.CritScala2.configure(variable=self.ThreeScale2)
                self.CritScala3.configure(variable=self.ThreeScale3)
                self.CritScala4.configure(variable=self.ThreeScale4)
                self.CritScala5.configure(variable=self.ThreeScale5)
                self.CritScala6.configure(variable=self.ThreeScale6)
                self.CritScala7.configure(variable=self.ThreeScale7)
                self.CritScala8.configure(variable=self.ThreeScale8)
                self.CritScala9.configure(variable=self.ThreeScale9)
                self.CritScala10.configure(variable=self.ThreeScale10)

                self.chkGClass.configure(variable=self.ThreeGClassCheck)
                self.chkTeachable.configure(variable=self.ThreeTeachCheck)
                self.chkQuiz.configure(variable=self.ThreeQuizCheck)
                self.chkCrit.configure(variable=self.ThreeCritCheck)
                self.officerCheck.configure(textvariable=self.ThreeCC_Officers)

                if self.chat == '123456':
                    officer = self.ThreeCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    officer = self.ThreeCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)
                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.ThreeScale1.get())
                    b = int(self.ThreeScale2.get())
                    c = int(self.ThreeScale3.get())
                    d = int(self.ThreeScale4.get())
                    e = int(self.ThreeScale5.get())
                    f = int(self.ThreeScale6.get())
                    g = int(self.ThreeScale7.get())
                    h = int(self.ThreeScale8.get())
                    i = int(self.ThreeScale9.get())
                    j = int(self.ThreeScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')
                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')
                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))

            except:
                self.show_text(str(self.chat))

        elif self.select == 4:

            try:
                self.CritScala1.configure(variable=self.FourScale1)
                self.CritScala2.configure(variable=self.FourScale2)
                self.CritScala3.configure(variable=self.FourScale3)
                self.CritScala4.configure(variable=self.FourScale4)
                self.CritScala5.configure(variable=self.FourScale5)
                self.CritScala6.configure(variable=self.FourScale6)
                self.CritScala7.configure(variable=self.FourScale7)
                self.CritScala8.configure(variable=self.FourScale8)
                self.CritScala9.configure(variable=self.FourScale9)
                self.CritScala10.configure(variable=self.FourScale10)

                self.chkGClass.configure(variable=self.FourGClassCheck)
                self.chkTeachable.configure(variable=self.FourTeachCheck)
                self.chkQuiz.configure(variable=self.FourQuizCheck)
                self.chkCrit.configure(variable=self.FourCritCheck)
                self.officerCheck.configure(textvariable=self.FourCC_Officers)

                if self.chat == '123456':
                    officer = self.FourCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)
                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.FourScale1.get())
                    b = int(self.FourScale2.get())
                    c = int(self.FourScale3.get())
                    d = int(self.FourScale4.get())
                    e = int(self.FourScale5.get())
                    f = int(self.FourScale6.get())
                    g = int(self.FourScale7.get())
                    h = int(self.FourScale8.get())
                    i = int(self.FourScale9.get())
                    j = int(self.FourScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')
                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')
                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))

            except:
                self.show_text(str(self.chat))

        elif self.select == 5:

            try:
                self.CritScala1.configure(variable=self.FiveScale1)
                self.CritScala2.configure(variable=self.FiveScale2)
                self.CritScala3.configure(variable=self.FiveScale3)
                self.CritScala4.configure(variable=self.FiveScale4)
                self.CritScala5.configure(variable=self.FiveScale5)

                self.CritScala6.configure(variable=self.FiveScale6)
                self.CritScala7.configure(variable=self.FiveScale7)
                self.CritScala8.configure(variable=self.FiveScale8)
                self.CritScala9.configure(variable=self.FiveScale9)
                self.CritScala10.configure(variable=self.FiveScale10)

                self.chkGClass.configure(variable=self.FiveGClassCheck)
                self.chkTeachable.configure(variable=self.FiveTeachCheck)
                self.chkQuiz.configure(variable=self.FiveQuizCheck)
                self.chkCrit.configure(variable=self.FiveCritCheck)
                self.officerCheck.configure(textvariable=self.FiveCC_Officers)

                if self.chat == '123456':
                    officer = self.FiveCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)
                    # crit 1 scrollbutton.get
                    a = int(self.FiveScale1.get())
                    b = int(self.FiveScale2.get())
                    c = int(self.FiveScale3.get())
                    d = int(self.FiveScale4.get())
                    e = int(self.FiveScale5.get())
                    f = int(self.FiveScale6.get())
                    g = int(self.FiveScale7.get())
                    h = int(self.FiveScale8.get())
                    i = int(self.FiveScale9.get())
                    j = int(self.FiveScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')
                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')
                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 6:
            try:
                self.CritScala1.configure(variable=self.SixScale1)
                self.CritScala2.configure(variable=self.SixScale2)
                self.CritScala3.configure(variable=self.SixScale3)
                self.CritScala4.configure(variable=self.SixScale4)
                self.CritScala5.configure(variable=self.SixScale5)
                self.CritScala6.configure(variable=self.SixScale6)
                self.CritScala7.configure(variable=self.SixScale7)
                self.CritScala8.configure(variable=self.SixScale8)
                self.CritScala9.configure(variable=self.SixScale9)
                self.CritScala10.configure(variable=self.SixScale10)

                self.chkGClass.configure(variable=self.SixGClassCheck)
                self.chkTeachable.configure(variable=self.SixTeachCheck)
                self.chkQuiz.configure(variable=self.SixQuizCheck)
                self.chkCrit.configure(variable=self.SixCritCheck)
                self.officerCheck.configure(textvariable=self.SixCC_Officers)


                if self.chat == '123456':
                    officer = self.SixCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.SixScale1.get())
                    b = int(self.SixScale2.get())
                    c = int(self.SixScale3.get())
                    d = int(self.SixScale4.get())
                    e = int(self.SixScale5.get())
                    f = int(self.SixScale6.get())
                    g = int(self.SixScale7.get())
                    h = int(self.SixScale8.get())
                    i = int(self.SixScale9.get())
                    j = int(self.SixScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')
                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')
                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 7:
            try:

                self.CritScala1.configure(variable=self.SevenScale1)
                self.CritScala2.configure(variable=self.SevenScale2)
                self.CritScala3.configure(variable=self.SevenScale3)
                self.CritScala4.configure(variable=self.SevenScale4)
                self.CritScala5.configure(variable=self.SevenScale5)
                self.CritScala6.configure(variable=self.SevenScale6)
                self.CritScala7.configure(variable=self.SevenScale7)
                self.CritScala8.configure(variable=self.SevenScale8)
                self.CritScala9.configure(variable=self.SevenScale9)
                self.CritScala10.configure(variable=self.SevenScale10)

                self.chkGClass.configure(variable=self.SevenGClassCheck)
                self.chkTeachable.configure(variable=self.SevenTeachCheck)
                self.chkQuiz.configure(variable=self.SevenQuizCheck)
                self.chkCrit.configure(variable=self.SevenCritCheck)
                self.officerCheck.configure(textvariable=self.SevenCC_Officers)

                if self.chat == '123456':
                    officer = self.SevenCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.SevenScale1.get())
                    b = int(self.SevenScale2.get())
                    c = int(self.SevenScale3.get())
                    d = int(self.SevenScale4.get())
                    e = int(self.SevenScale5.get())
                    f = int(self.SevenScale6.get())
                    g = int(self.SevenScale7.get())
                    h = int(self.SevenScale8.get())
                    i = int(self.SevenScale9.get())
                    j = int(self.SevenScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')
                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')
                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 8:
            try:
                self.CritScala1.configure(variable=self.EightScale1)
                self.CritScala2.configure(variable=self.EightScale2)
                self.CritScala3.configure(variable=self.EightScale3)
                self.CritScala4.configure(variable=self.EightScale4)
                self.CritScala5.configure(variable=self.EightScale5)
                self.CritScala6.configure(variable=self.EightScale6)
                self.CritScala7.configure(variable=self.EightScale7)
                self.CritScala8.configure(variable=self.EightScale8)
                self.CritScala9.configure(variable=self.EightScale9)
                self.CritScala10.configure(variable=self.EightScale10)

                self.chkGClass.configure(variable=self.EightGClassCheck)
                self.chkTeachable.configure(variable=self.EightTeachCheck)
                self.chkQuiz.configure(variable=self.EightQuizCheck)
                self.chkCrit.configure(variable=self.EightCritCheck)
                self.officerCheck.configure(textvariable=self.EightCC_Officers)

                if self.chat == '123456':
                    officer = self.EightCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.EightScale1.get())
                    b = int(self.EightScale2.get())
                    c = int(self.EightScale3.get())
                    d = int(self.EightScale4.get())
                    e = int(self.EightScale5.get())
                    f = int(self.EightScale6.get())
                    g = int(self.EightScale7.get())
                    h = int(self.EightScale8.get())
                    i = int(self.EightScale9.get())
                    j = int(self.EightScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')
                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')
                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 9:
            try:
                self.CritScala1.configure(variable=self.NineScale1)
                self.CritScala2.configure(variable=self.NineScale2)
                self.CritScala3.configure(variable=self.NineScale3)
                self.CritScala4.configure(variable=self.NineScale4)
                self.CritScala5.configure(variable=self.NineScale5)
                self.CritScala6.configure(variable=self.NineScale6)
                self.CritScala7.configure(variable=self.NineScale7)
                self.CritScala8.configure(variable=self.NineScale8)
                self.CritScala9.configure(variable=self.NineScale9)
                self.CritScala10.configure(variable=self.NineScale10)

                self.chkGClass.configure(variable=self.NineGClassCheck)
                self.chkTeachable.configure(variable=self.NineTeachCheck)
                self.chkQuiz.configure(variable=self.NineQuizCheck)
                self.chkCrit.configure(variable=self.NineCritCheck)
                self.officerCheck.configure(textvariable=self.NineCC_Officers)

                if self.chat == '123456':
                    officer = self.NineCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.NineScale1.get())
                    b = int(self.NineScale2.get())
                    c = int(self.NineScale3.get())
                    d = int(self.NineScale4.get())
                    e = int(self.NineScale5.get())
                    f = int(self.NineScale6.get())
                    g = int(self.NineScale7.get())
                    h = int(self.NineScale8.get())
                    i = int(self.NineScale9.get())
                    j = int(self.NineScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 10:
            try:
                self.CritScala1.configure(variable=self.TenScale1)
                self.CritScala2.configure(variable=self.TenScale2)
                self.CritScala3.configure(variable=self.TenScale3)
                self.CritScala4.configure(variable=self.TenScale4)
                self.CritScala5.configure(variable=self.TenScale5)
                self.CritScala6.configure(variable=self.TenScale6)
                self.CritScala7.configure(variable=self.TenScale7)
                self.CritScala8.configure(variable=self.TenScale8)
                self.CritScala9.configure(variable=self.TenScale9)
                self.CritScala10.configure(variable=self.TenScale10)

                self.chkGClass.configure(variable=self.TenGClassCheck)
                self.chkTeachable.configure(variable=self.TenTeachCheck)
                self.chkQuiz.configure(variable=self.TenQuizCheck)
                self.chkCrit.configure(variable=self.TenCritCheck)
                self.officerCheck.configure(textvariable=self.TenCC_Officers)

                if self.chat == '123456':
                    officer = self.TenCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.TenScale1.get())
                    b = int(self.TenScale2.get())
                    c = int(self.TenScale3.get())
                    d = int(self.TenScale4.get())
                    e = int(self.TenScale5.get())
                    f = int(self.TenScale6.get())
                    g = int(self.TenScale7.get())
                    h = int(self.TenScale8.get())
                    i = int(self.TenScale9.get())
                    j = int(self.TenScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 11:
            try:
                self.CritScala1.configure(variable=self.ElevenScale1)
                self.CritScala2.configure(variable=self.ElevenScale2)
                self.CritScala3.configure(variable=self.ElevenScale3)
                self.CritScala4.configure(variable=self.ElevenScale4)
                self.CritScala5.configure(variable=self.ElevenScale5)
                self.CritScala6.configure(variable=self.ElevenScale6)
                self.CritScala7.configure(variable=self.ElevenScale7)
                self.CritScala8.configure(variable=self.ElevenScale8)
                self.CritScala9.configure(variable=self.ElevenScale9)
                self.CritScala10.configure(variable=self.ElevenScale10)

                self.chkGClass.configure(variable=self.ElevenGClassCheck)
                self.chkTeachable.configure(variable=self.ElevenTeachCheck)
                self.chkQuiz.configure(variable=self.ElevenQuizCheck)
                self.chkCrit.configure(variable=self.ElevenCritCheck)
                self.officerCheck.configure(textvariable=self.ElevenCC_Officers)

                if self.chat == '123456':
                    officer = self.ElevenCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.ElevenScale1.get())
                    b = int(self.ElevenScale2.get())
                    c = int(self.ElevenScale3.get())
                    d = int(self.ElevenScale4.get())
                    e = int(self.ElevenScale5.get())
                    f = int(self.ElevenScale6.get())
                    g = int(self.ElevenScale7.get())
                    h = int(self.ElevenScale8.get())
                    i = int(self.ElevenScale9.get())
                    j = int(self.ElevenScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 12:
            try:
                self.CritScala1.configure(variable=self.TwelveScale1)
                self.CritScala2.configure(variable=self.TwelveScale2)
                self.CritScala3.configure(variable=self.TwelveScale3)
                self.CritScala4.configure(variable=self.TwelveScale4)
                self.CritScala5.configure(variable=self.TwelveScale5)
                self.CritScala6.configure(variable=self.TwelveScale6)
                self.CritScala7.configure(variable=self.TwelveScale7)
                self.CritScala8.configure(variable=self.TwelveScale8)
                self.CritScala9.configure(variable=self.TwelveScale9)
                self.CritScala10.configure(variable=self.TwelveScale10)

                self.chkGClass.configure(variable=self.TwelveGClassCheck)
                self.chkTeachable.configure(variable=self.TwelveTeachCheck)
                self.chkQuiz.configure(variable=self.TwelveQuizCheck)
                self.chkCrit.configure(variable=self.TwelveCritCheck)
                self.officerCheck.configure(textvariable=self.TwelveCC_Officers)

                if self.chat == '123456':
                    officer = self.TwelveCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.TwelveScale1.get())
                    b = int(self.TwelveScale2.get())
                    c = int(self.TwelveScale3.get())
                    d = int(self.TwelveScale4.get())
                    e = int(self.TwelveScale5.get())
                    f = int(self.TwelveScale6.get())
                    g = int(self.TwelveScale7.get())
                    h = int(self.TwelveScale8.get())
                    i = int(self.TwelveScale9.get())
                    j = int(self.TwelveScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 13:
            try:
                self.CritScala1.configure(variable=self.ThirteenScale1)
                self.CritScala2.configure(variable=self.ThirteenScale2)
                self.CritScala3.configure(variable=self.ThirteenScale3)
                self.CritScala4.configure(variable=self.ThirteenScale4)
                self.CritScala5.configure(variable=self.ThirteenScale5)
                self.CritScala6.configure(variable=self.ThirteenScale6)
                self.CritScala7.configure(variable=self.ThirteenScale7)
                self.CritScala8.configure(variable=self.ThirteenScale8)
                self.CritScala9.configure(variable=self.ThirteenScale9)
                self.CritScala10.configure(variable=self.ThirteenScale10)

                self.chkGClass.configure(variable=self.ThirteenGClassCheck)
                self.chkTeachable.configure(variable=self.ThirteenTeachCheck)
                self.chkQuiz.configure(variable=self.ThirteenQuizCheck)
                self.chkCrit.configure(variable=self.ThirteenCritCheck)
                self.officerCheck.configure(textvariable=self.ThirteenCC_Officers)

                if self.chat == '123456':
                    officer = self.ThirteenCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.ThirteenScale1.get())
                    b = int(self.ThirteenScale2.get())
                    c = int(self.ThirteenScale3.get())
                    d = int(self.ThirteenScale4.get())
                    e = int(self.ThirteenScale5.get())
                    f = int(self.ThirteenScale6.get())
                    g = int(self.ThirteenScale7.get())
                    h = int(self.ThirteenScale8.get())
                    i = int(self.ThirteenScale9.get())
                    j = int(self.ThirteenScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 14:
            try:
                self.CritScala1.configure(variable=self.FourteenScale1)
                self.CritScala2.configure(variable=self.FourteenScale2)
                self.CritScala3.configure(variable=self.FourteenScale3)
                self.CritScala4.configure(variable=self.FourteenScale4)
                self.CritScala5.configure(variable=self.FourteenScale5)
                self.CritScala6.configure(variable=self.FourteenScale6)
                self.CritScala7.configure(variable=self.FourteenScale7)
                self.CritScala8.configure(variable=self.FourteenScale8)
                self.CritScala9.configure(variable=self.FourteenScale9)
                self.CritScala10.configure(variable=self.FourteenScale10)

                self.chkGClass.configure(variable=self.FourteenGClassCheck)
                self.chkTeachable.configure(variable=self.FourteenTeachCheck)
                self.chkQuiz.configure(variable=self.FourteenQuizCheck)
                self.chkCrit.configure(variable=self.FourteenCritCheck)
                self.officerCheck.configure(textvariable=self.FourteenCC_Officers)

                if self.chat == '123456':
                    officer = self.FourteenCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.FourteenScale1.get())
                    b = int(self.FourteenScale2.get())
                    c = int(self.FourteenScale3.get())
                    d = int(self.FourteenScale4.get())
                    e = int(self.FourteenScale5.get())
                    f = int(self.FourteenScale6.get())
                    g = int(self.FourteenScale7.get())
                    h = int(self.FourteenScale8.get())
                    i = int(self.FourteenScale9.get())
                    j = int(self.FourteenScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 15:
            try:
                self.CritScala1.configure(variable=self.FifteenScale1)
                self.CritScala2.configure(variable=self.FifteenScale2)
                self.CritScala3.configure(variable=self.FifteenScale3)
                self.CritScala4.configure(variable=self.FifteenScale4)
                self.CritScala5.configure(variable=self.FifteenScale5)
                self.CritScala6.configure(variable=self.FifteenScale6)
                self.CritScala7.configure(variable=self.FifteenScale7)
                self.CritScala8.configure(variable=self.FifteenScale8)
                self.CritScala9.configure(variable=self.FifteenScale9)
                self.CritScala10.configure(variable=self.FifteenScale10)

                self.chkGClass.configure(variable=self.FifteenGClassCheck)
                self.chkTeachable.configure(variable=self.FifteenTeachCheck)
                self.chkQuiz.configure(variable=self.FifteenQuizCheck)
                self.chkCrit.configure(variable=self.FifteenCritCheck)
                self.officerCheck.configure(textvariable=self.FifteenCC_Officers)

                if self.chat == '123456':
                    officer = self.FifteenCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.FifteenScale1.get())
                    b = int(self.FifteenScale2.get())
                    c = int(self.FifteenScale3.get())
                    d = int(self.FifteenScale4.get())
                    e = int(self.FifteenScale5.get())
                    f = int(self.FifteenScale6.get())
                    g = int(self.FifteenScale7.get())
                    h = int(self.FifteenScale8.get())
                    i = int(self.FifteenScale9.get())
                    j = int(self.FifteenScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 16:
            try:
                self.CritScala1.configure(variable=self.SixteenScale1)
                self.CritScala2.configure(variable=self.SixteenScale2)
                self.CritScala3.configure(variable=self.SixteenScale3)
                self.CritScala4.configure(variable=self.SixteenScale4)
                self.CritScala5.configure(variable=self.SixteenScale5)
                self.CritScala6.configure(variable=self.SixteenScale6)
                self.CritScala7.configure(variable=self.SixteenScale7)
                self.CritScala8.configure(variable=self.SixteenScale8)
                self.CritScala9.configure(variable=self.SixteenScale9)
                self.CritScala10.configure(variable=self.SixteenScale10)

                self.chkGClass.configure(variable=self.SixteenGClassCheck)
                self.chkTeachable.configure(variable=self.SixteenTeachCheck)
                self.chkQuiz.configure(variable=self.SixteenQuizCheck)
                self.chkCrit.configure(variable=self.SixteenCritCheck)
                self.officerCheck.configure(textvariable=self.SixteenCC_Officers)

                if self.chat == '123456':
                    officer = self.SixteenCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.SixteenScale1.get())
                    b = int(self.SixteenScale2.get())
                    c = int(self.SixteenScale3.get())
                    d = int(self.SixteenScale4.get())
                    e = int(self.SixteenScale5.get())
                    f = int(self.SixteenScale6.get())
                    g = int(self.SixteenScale7.get())
                    h = int(self.SixteenScale8.get())
                    i = int(self.SixteenScale9.get())
                    j = int(self.SixteenScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 17:
            try:
                self.CritScala1.configure(variable=self.SeventeenScale1)
                self.CritScala2.configure(variable=self.SeventeenScale2)
                self.CritScala3.configure(variable=self.SeventeenScale3)
                self.CritScala4.configure(variable=self.SeventeenScale4)
                self.CritScala5.configure(variable=self.SeventeenScale5)
                self.CritScala6.configure(variable=self.SeventeenScale6)
                self.CritScala7.configure(variable=self.SeventeenScale7)
                self.CritScala8.configure(variable=self.SeventeenScale8)
                self.CritScala9.configure(variable=self.SeventeenScale9)
                self.CritScala10.configure(variable=self.SeventeenScale10)

                self.chkGClass.configure(variable=self.SeventeenGClassCheck)
                self.chkTeachable.configure(variable=self.SeventeenTeachCheck)
                self.chkQuiz.configure(variable=self.SeventeenQuizCheck)
                self.chkCrit.configure(variable=self.SeventeenCritCheck)
                self.officerCheck.configure(textvariable=self.SeventeenCC_Officers)

                if self.chat == '123456':
                    officer = self.SeventeenCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.SeventeenScale1.get())
                    b = int(self.SeventeenScale2.get())
                    c = int(self.SeventeenScale3.get())
                    d = int(self.SeventeenScale4.get())
                    e = int(self.SeventeenScale5.get())
                    f = int(self.SeventeenScale6.get())
                    g = int(self.SeventeenScale7.get())
                    h = int(self.SeventeenScale8.get())
                    i = int(self.SeventeenScale9.get())
                    j = int(self.SeventeenScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 18:
            try:
                self.CritScala1.configure(variable=self.EighteenScale1)
                self.CritScala2.configure(variable=self.EighteenScale2)
                self.CritScala3.configure(variable=self.EighteenScale3)
                self.CritScala4.configure(variable=self.EighteenScale4)
                self.CritScala5.configure(variable=self.EighteenScale5)
                self.CritScala6.configure(variable=self.EighteenScale6)
                self.CritScala7.configure(variable=self.EighteenScale7)
                self.CritScala8.configure(variable=self.EighteenScale8)
                self.CritScala9.configure(variable=self.EighteenScale9)
                self.CritScala10.configure(variable=self.EighteenScale10)

                self.chkGClass.configure(variable=self.EighteenGClassCheck)
                self.chkTeachable.configure(variable=self.EighteenTeachCheck)
                self.chkQuiz.configure(variable=self.EighteenQuizCheck)
                self.chkCrit.configure(variable=self.EighteenCritCheck)
                self.officerCheck.configure(textvariable=self.EighteenCC_Officers)

                if self.chat == '123456':
                    officer = self.EighteenCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.EighteenScale1.get())
                    b = int(self.EighteenScale2.get())
                    c = int(self.EighteenScale3.get())
                    d = int(self.EighteenScale4.get())
                    e = int(self.EighteenScale5.get())
                    f = int(self.EighteenScale6.get())
                    g = int(self.EighteenScale7.get())
                    h = int(self.EighteenScale8.get())
                    i = int(self.EighteenScale9.get())
                    j = int(self.EighteenScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 19:
            try:
                self.CritScala1.configure(variable=self.NineteenScale1)
                self.CritScala2.configure(variable=self.NineteenScale2)
                self.CritScala3.configure(variable=self.NineteenScale3)
                self.CritScala4.configure(variable=self.NineteenScale4)
                self.CritScala5.configure(variable=self.NineteenScale5)
                self.CritScala6.configure(variable=self.NineteenScale6)
                self.CritScala7.configure(variable=self.NineteenScale7)
                self.CritScala8.configure(variable=self.NineteenScale8)
                self.CritScala9.configure(variable=self.NineteenScale9)
                self.CritScala10.configure(variable=self.NineteenScale10)

                self.chkGClass.configure(variable=self.NineteenGClassCheck)
                self.chkTeachable.configure(variable=self.NineteenTeachCheck)
                self.chkQuiz.configure(variable=self.NineteenQuizCheck)
                self.chkCrit.configure(variable=self.NineteenCritCheck)
                self.officerCheck.configure(textvariable=self.NineteenCC_Officers)

                if self.chat == '123456':
                    officer = self.NineteenCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.NineteenScale1.get())
                    b = int(self.NineteenScale2.get())
                    c = int(self.NineteenScale3.get())
                    d = int(self.NineteenScale4.get())
                    e = int(self.NineteenScale5.get())
                    f = int(self.NineteenScale6.get())
                    g = int(self.NineteenScale7.get())
                    h = int(self.NineteenScale8.get())
                    i = int(self.NineteenScale9.get())
                    j = int(self.NineteenScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 20:
            try:
                self.CritScala1.configure(variable=self.TwentyScale1)
                self.CritScala2.configure(variable=self.TwentyScale2)
                self.CritScala3.configure(variable=self.TwentyScale3)
                self.CritScala4.configure(variable=self.TwentyScale4)
                self.CritScala5.configure(variable=self.TwentyScale5)
                self.CritScala6.configure(variable=self.TwentyScale6)
                self.CritScala7.configure(variable=self.TwentyScale7)
                self.CritScala8.configure(variable=self.TwentyScale8)
                self.CritScala9.configure(variable=self.TwentyScale9)
                self.CritScala10.configure(variable=self.TwentyScale10)

                self.chkGClass.configure(variable=self.TwentyGClassCheck)
                self.chkTeachable.configure(variable=self.TwentyTeachCheck)
                self.chkQuiz.configure(variable=self.TwentyQuizCheck)
                self.chkCrit.configure(variable=self.TwentyCritCheck)
                self.officerCheck.configure(textvariable=self.TwentyCC_Officers)

                if self.chat == '123456':
                    officer = self.TwentyCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.TwentyScale1.get())
                    b = int(self.TwentyScale2.get())
                    c = int(self.TwentyScale3.get())
                    d = int(self.TwentyScale4.get())
                    e = int(self.TwentyScale5.get())
                    f = int(self.TwentyScale6.get())
                    g = int(self.TwentyScale7.get())
                    h = int(self.TwentyScale8.get())
                    i = int(self.TwentyScale9.get())
                    j = int(self.TwentyScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 21:
            try:
                self.CritScala1.configure(variable=self.TwentyOneScale1)
                self.CritScala2.configure(variable=self.TwentyOneScale2)
                self.CritScala3.configure(variable=self.TwentyOneScale3)
                self.CritScala4.configure(variable=self.TwentyOneScale4)
                self.CritScala5.configure(variable=self.TwentyOneScale5)
                self.CritScala6.configure(variable=self.TwentyOneScale6)
                self.CritScala7.configure(variable=self.TwentyOneScale7)
                self.CritScala8.configure(variable=self.TwentyOneScale8)
                self.CritScala9.configure(variable=self.TwentyOneScale9)
                self.CritScala10.configure(variable=self.TwentyOneScale10)

                self.chkGClass.configure(variable=self.TwentyOneGClassCheck)
                self.chkTeachable.configure(variable=self.TwentyOneTeachCheck)
                self.chkQuiz.configure(variable=self.TwentyOneQuizCheck)
                self.chkCrit.configure(variable=self.TwentyOneCritCheck)
                self.officerCheck.configure(textvariable=self.TwentyOneCC_Officers)

                if self.chat == '123456':
                    officer = self.TwentyOneCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.TwentyOneScale1.get())
                    b = int(self.TwentyOneScale2.get())
                    c = int(self.TwentyOneScale3.get())
                    d = int(self.TwentyOneScale4.get())
                    e = int(self.TwentyOneScale5.get())
                    f = int(self.TwentyOneScale6.get())
                    g = int(self.TwentyOneScale7.get())
                    h = int(self.TwentyOneScale8.get())
                    i = int(self.TwentyOneScale9.get())
                    j = int(self.TwentyOneScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 22:
            try:
                self.CritScala1.configure(variable=self.TwentyTwoScale1)
                self.CritScala2.configure(variable=self.TwentyTwoScale2)
                self.CritScala3.configure(variable=self.TwentyTwoScale3)
                self.CritScala4.configure(variable=self.TwentyTwoScale4)
                self.CritScala5.configure(variable=self.TwentyTwoScale5)
                self.CritScala6.configure(variable=self.TwentyTwoScale6)
                self.CritScala7.configure(variable=self.TwentyTwoScale7)
                self.CritScala8.configure(variable=self.TwentyTwoScale8)
                self.CritScala9.configure(variable=self.TwentyTwoScale9)
                self.CritScala10.configure(variable=self.TwentyTwoScale10)

                self.chkGClass.configure(variable=self.TwentyTwoGClassCheck)
                self.chkTeachable.configure(variable=self.TwentyTwoTeachCheck)
                self.chkQuiz.configure(variable=self.TwentyTwoQuizCheck)
                self.chkCrit.configure(variable=self.TwentyTwoCritCheck)
                self.officerCheck.configure(textvariable=self.TwentyTwoCC_Officers)

                if self.chat == '123456':
                    officer = self.TwentyTwoCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.TwentyTwoScale1.get())
                    b = int(self.TwentyTwoScale2.get())
                    c = int(self.TwentyTwoScale3.get())
                    d = int(self.TwentyTwoScale4.get())
                    e = int(self.TwentyTwoScale5.get())
                    f = int(self.TwentyTwoScale6.get())
                    g = int(self.TwentyTwoScale7.get())
                    h = int(self.TwentyTwoScale8.get())
                    i = int(self.TwentyTwoScale9.get())
                    j = int(self.TwentyTwoScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 23:
            try:
                self.CritScala1.configure(variable=self.TwentyThreeScale1)
                self.CritScala2.configure(variable=self.TwentyThreeScale2)
                self.CritScala3.configure(variable=self.TwentyThreeScale3)
                self.CritScala4.configure(variable=self.TwentyThreeScale4)
                self.CritScala5.configure(variable=self.TwentyThreeScale5)
                self.CritScala6.configure(variable=self.TwentyThreeScale6)
                self.CritScala7.configure(variable=self.TwentyThreeScale7)
                self.CritScala8.configure(variable=self.TwentyThreeScale8)
                self.CritScala9.configure(variable=self.TwentyThreeScale9)
                self.CritScala10.configure(variable=self.TwentyThreeScale10)

                self.chkGClass.configure(variable=self.TwentyThreeGClassCheck)
                self.chkTeachable.configure(variable=self.TwentyThreeTeachCheck)
                self.chkQuiz.configure(variable=self.TwentyThreeQuizCheck)
                self.chkCrit.configure(variable=self.TwentyThreeCritCheck)
                self.officerCheck.configure(textvariable=self.TwentyThreeCC_Officers)

                if self.chat == '123456':
                    officer = self.TwentyThreeCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.TwentyThreeScale1.get())
                    b = int(self.TwentyThreeScale2.get())
                    c = int(self.TwentyThreeScale3.get())
                    d = int(self.TwentyThreeScale4.get())
                    e = int(self.TwentyThreeScale5.get())
                    f = int(self.TwentyThreeScale6.get())
                    g = int(self.TwentyThreeScale7.get())
                    h = int(self.TwentyThreeScale8.get())
                    i = int(self.TwentyThreeScale9.get())
                    j = int(self.TwentyThreeScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        elif self.select == 24:
            try:
                self.CritScala1.configure(variable=self.TwentyFourScale1)
                self.CritScala2.configure(variable=self.TwentyFourScale2)
                self.CritScala3.configure(variable=self.TwentyFourScale3)
                self.CritScala4.configure(variable=self.TwentyFourScale4)
                self.CritScala5.configure(variable=self.TwentyFourScale5)
                self.CritScala6.configure(variable=self.TwentyFourScale6)
                self.CritScala7.configure(variable=self.TwentyFourScale7)
                self.CritScala8.configure(variable=self.TwentyFourScale8)
                self.CritScala9.configure(variable=self.TwentyFourScale9)
                self.CritScala10.configure(variable=self.TwentyFourScale10)

                self.chkGClass.configure(variable=self.TwentyFourGClassCheck)
                self.chkTeachable.configure(variable=self.TwentyFourTeachCheck)
                self.chkQuiz.configure(variable=self.TwentyFourQuizCheck)
                self.chkCrit.configure(variable=self.TwentyFourCritCheck)
                self.officerCheck.configure(textvariable=self.TwentyFourCC_Officers)

                if self.chat == '123456':
                    officer = self.TwentyFourCC_Officers.get()
                    self.btnSaveOne.configure(state=NORMAL)

                    self.disp_officer(officer)

                    # crit 1 scrollbutton.get
                    a = int(self.TwentyFourScale1.get())
                    b = int(self.TwentyFourScale2.get())
                    c = int(self.TwentyFourScale3.get())
                    d = int(self.TwentyFourScale4.get())
                    e = int(self.TwentyFourScale5.get())
                    f = int(self.TwentyFourScale6.get())
                    g = int(self.TwentyFourScale7.get())
                    h = int(self.TwentyFourScale8.get())
                    i = int(self.TwentyFourScale9.get())
                    j = int(self.TwentyFourScale10.get())

                    self.show_spider(a, f, b, g, c, h, d, i, e, j)
                    self.btnSaveOne.configure(state=NORMAL)

                if self.chat == '/open_notes.exe':
                    self.lbltest.pack_forget()
                    self.lblTestbox = False
                    self.show_text('/open_notes.exe')

                if self.chat == '/take_notes.exe':
                    if self.txtNotesOn:
                        self.txtNotes.pack_forget()
                    self.show_text('/take_notes.exe')

                if self.chat == '/save_note':
                    self.txtNotesOn = True
                    self.show_text('/save_note')

                if self.chat not in self.all_commands:
                    self.show_text(str(self.chat))
            except:
                self.show_text(str(self.chat))

        self.chatEntry.delete(0, END)
        self.launchBtn.configure(state=NORMAL)
        #self.leftMiss.configure(state=NORMAL)

    def task_master(self):
        self.select = self.Miss1.get()

        if self.select == 1:
            officer = self.CC_Officers.get()
        elif self.select == 2:
            officer = self.TwoCC_Officers.get()
        elif self.select == 3:
            officer = self.ThreeCC_Officers.get()
        elif self.select == 4:
            officer = self.FourCC_Officers.get()
        elif self.select == 5:
            officer = self.FiveCC_Officers.get()
        elif self.select == 6:
            officer = self.SixCC_Officers.get()
        elif self.select == 7:
            officer = self.SevenCC_Officers.get()
        elif self.select == 8:
            officer = self.EightCC_Officers.get()
        elif self.select == 9:
            officer = self.NineCC_Officers.get()
        elif self.select == 10:
            officer = self.TenCC_Officers.get()
        elif self.select == 11:
            officer = self.ElevenCC_Officers.get()
        elif self.select == 12:
            officer = self.TwelveCC_Officers.get()
        elif self.select == 13:
            officer = self.ThirteenCC_Officers.get()
        elif self.select == 14:
            officer = self.FourteenCC_Officers.get()
        elif self.select == 15:
            officer = self.FifteenCC_Officers.get()
        elif self.select == 16:
            officer = self.SixteenCC_Officers.get()
        elif self.select == 17:
            officer = self.SeventeenCC_Officers.get()
        elif self.select == 18:
            officer = self.EighteenCC_Officers.get()
        elif self.select == 19:
            officer = self.NineteenCC_Officers.get()
        elif self.select == 20:
            officer = self.TwentyCC_Officers.get()
        elif self.select == 21:
            officer = self.TwentyOneCC_Officers.get()
        elif self.select == 22:
            officer = self.TwentyThreeCC_Officers.get()
        elif self.select == 23:
            officer = self.TwentyThreeCC_Officers.get()
        elif self.select == 24:
            officer = self.TwentyFourCC_Officers.get()

        if officer == 'Lannon Khau':
            self.officer_img1 = ImageTk.PhotoImage(Image.open('images/spaceforce2A.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)
        elif officer == 'Benny Chiu':
            self.officer_img1 = ImageTk.PhotoImage(Image.open('images/spaceforce3.png.'))
            self.officerCanv.create_image(-5, 112,
                                          anchor=W,
                                          image=self.officer_img1)
        elif officer == 'Fernando Galvez':
            self.officer_img1 = ImageTk.PhotoImage(Image.open('images/spaceforce4.png.'))
            self.officerCanv.create_image(-5, 112,
                                          anchor=W,
                                          image=self.officer_img1)
        elif officer == 'Joshua Sanchez':
            self.officer_img1 = ImageTk.PhotoImage(Image.open('images/spaceforce5.png.'))
            self.officerCanv.create_image(-5, 112,
                                          anchor=W,
                                          image=self.officer_img1)
        else:
            self.officer_img1 = ImageTk.PhotoImage(Image.open('images/rank_high_18.png.'))
            self.officerCanv.create_image(100, 112,
                                          anchor=W,
                                          image=self.officer_img1)

    def loadRecordA1(self):

        self.lblScreen.pack_forget()
        if self.planet_tracker != 0:
            self.lblScreen.destroy()
            self.planet_canv.destroy()

        self.planet_canv = Canvas(
            self.leftFrameDown1, bg='black', width=10, height=10
            , highlightbackground='black')
        self.planet_canv.pack(fill=BOTH, expand=True)

        load_data = pd.read_csv("missionRecords4.csv")
        df = pd.DataFrame(load_data)

        self.select = self.Miss1.get()

        if self.select == 1:
            level1_rows = df.loc[df['Mission No.'] == 1]
            last_row = level1_rows.iloc[-1]

            self.critload1 = last_row['Application']
            self.CritScala1.set(self.critload1)
            self.critload2 = last_row['Readability']
            self.CritScala2.set(self.critload2)
            self.critload3 = last_row['Quality']
            self.CritScala3.set(self.critload3)
            self.critload4 = last_row['Creativity']
            self.CritScala4.set(self.critload4)
            self.critload5 = last_row['Cleanliness']
            self.CritScala5.set(self.critload5)
            self.critload6 = last_row['Content']
            self.CritScala6.set(self.critload6)
            self.critload7 = last_row['Originality']
            self.CritScala7.set(self.critload7)
            self.critload8 = last_row['Body Language']
            self.CritScala8.set(self.critload8)
            self.critload9 = last_row['Structure']
            self.CritScala9.set(self.critload9)
            self.critload10 = last_row['Delivery']
            self.CritScala10.set(self.critload10)

            self.subDate = last_row['Date']
            print(self.subDate)
            point = self.subDate.find('.')
            self.subDate1 = self.subDate[:point]
            self.lblDateTime.configure(text = self.subDate1)

            # save upload onto google classroom
            self.googCheck = last_row['Google C.']
            self.teachSave = last_row['Teachable']
            self.quizSave = last_row['Quiz Taken']
            self.critSave = last_row['Presentation Check']

            self.officerSave = last_row['Officer']
            self.officerCheck.set(self.officerSave)

            self.notes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.notes)

            # Start by filling in the checkboxes
            if self.googCheck == 1:
                self.chkGClass.select()
            if self.teachSave == 1:
                self.chkTeachable.select()
            if self.quizSave == 1:
                self.chkQuiz.select()
            if self.critSave == 1:
                self.chkCrit.select()

            if self.officerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.officerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.officerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.officerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.critload1), int(self.critload2),
                     int(self.critload3), int(self.critload4),
                     int(self.critload5), int(self.critload6),
                     int(self.critload7), int(self.critload8),
                     int(self.critload9), int(self.critload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 1)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 2:
            level1_rows = df.loc[df['Mission No.'] == 2]
            last_row = level1_rows.iloc[-1]

            self.TwoCritload1 = last_row['Application']
            self.CritScala1.set(self.TwoCritload1)
            self.TwoCritload2 = last_row['Readability']
            self.CritScala2.set(self.TwoCritload2)
            self.TwoCritload3 = last_row['Quality']
            self.CritScala3.set(self.TwoCritload3)
            self.TwoCritload4 = last_row['Creativity']
            self.CritScala4.set(self.TwoCritload4)
            self.TwoCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.TwoCritload5)
            self.TwoCritload6 = last_row['Content']
            self.CritScala6.set(self.TwoCritload6)
            self.TwoCritload7 = last_row['Originality']
            self.CritScala7.set(self.TwoCritload7)
            self.TwoCritload8 = last_row['Body Language']
            self.CritScala8.set(self.TwoCritload8)
            self.TwoCritload9 = last_row['Structure']
            self.CritScala9.set(self.TwoCritload9)
            self.TwoCritload10 = last_row['Delivery']
            self.CritScala10.set(self.TwoCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate2 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate2)

            # save upload onto google classroom
            self.TwoGoogCheck = last_row['Google C.']
            self.TwoTeachSave = last_row['Teachable']
            self.TwoQuizSave = last_row['Quiz Taken']
            self.TwoCritSave = last_row['Presentation Check']

            self.TwoOfficerSave = last_row['Officer']
            self.officerCheck.set(self.TwoOfficerSave)

            self.TwoNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.TwoNotes)

            # Start by filling in the checkboxes
            if self.TwoGoogCheck == 1:
                self.chkGClass.select()
            if self.TwoTeachSave == 1:
                self.chkTeachable.select()
            if self.TwoQuizSave == 1:
                self.chkQuiz.select()
            if self.TwoCritSave == 1:
                self.chkCrit.select()

            if self.TwoOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.TwoOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.TwoOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.TwoOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.TwoCritload1), int(self.TwoCritload2), int(self.TwoCritload3), int(self.TwoCritload4), int(self.TwoCritload5),
                     int(self.TwoCritload6), int(self.TwoCritload7), int(self.TwoCritload8), int(self.TwoCritload9), int(self.TwoCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 2)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 3:
            level1_rows = df.loc[df['Mission No.'] == 3]
            last_row = level1_rows.iloc[-1]

            self.ThreeCritload1 = last_row['Application']
            self.CritScala1.set(self.ThreeCritload1)
            self.ThreeCritload2 = last_row['Readability']
            self.CritScala2.set(self.ThreeCritload2)
            self.ThreeCritload3 = last_row['Quality']
            self.CritScala3.set(self.ThreeCritload3)
            self.ThreeCritload4 = last_row['Creativity']
            self.CritScala4.set(self.ThreeCritload4)
            self.ThreeCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.ThreeCritload5)
            self.ThreeCritload6 = last_row['Content']
            self.CritScala6.set(self.ThreeCritload6)
            self.ThreeCritload7 = last_row['Originality']
            self.CritScala7.set(self.ThreeCritload7)
            self.ThreeCritload8 = last_row['Body Language']
            self.CritScala8.set(self.ThreeCritload8)
            self.ThreeCritload9 = last_row['Structure']
            self.CritScala9.set(self.ThreeCritload9)
            self.ThreeCritload10 = last_row['Delivery']
            self.CritScala10.set(self.ThreeCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate3 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate3)

            # save upload onto google classroom
            self.ThreeGoogCheck = last_row['Google C.']
            self.ThreeTeachSave = last_row['Teachable']
            self.ThreeQuizSave = last_row['Quiz Taken']
            self.ThreeCritSave = last_row['Presentation Check']

            self.ThreeOfficerSave = last_row['Officer']
            self.officerCheck.set(self.ThreeOfficerSave)

            self.ThreeNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.ThreeNotes)

            # Start by filling in the checkboxes
            if self.ThreeGoogCheck == 1:
                self.chkGClass.select()
            if self.ThreeTeachSave == 1:
                self.chkTeachable.select()
            if self.ThreeQuizSave == 1:
                self.chkQuiz.select()
            if self.ThreeCritSave == 1:
                self.chkCrit.select()

            if self.ThreeOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.ThreeOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.ThreeOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.ThreeOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.ThreeCritload1), int(self.ThreeCritload2), int(self.ThreeCritload3), int(self.ThreeCritload4), int(self.ThreeCritload5),
                     int(self.ThreeCritload6), int(self.ThreeCritload7), int(self.ThreeCritload8), int(self.ThreeCritload9), int(self.ThreeCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 3)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 4:
            level1_rows = df.loc[df['Mission No.'] == 4]
            last_row = level1_rows.iloc[-1]

            self.FourCritload1 = last_row['Application']
            self.CritScala1.set(self.FourCritload1)
            self.FourCritload2 = last_row['Readability']
            self.CritScala2.set(self.FourCritload2)
            self.FourCritload3 = last_row['Quality']
            self.CritScala3.set(self.FourCritload3)
            self.FourCritload4 = last_row['Creativity']
            self.CritScala4.set(self.FourCritload4)
            self.FourCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.FourCritload5)
            self.FourCritload6 = last_row['Content']
            self.CritScala6.set(self.FourCritload6)
            self.FourCritload7 = last_row['Originality']
            self.CritScala7.set(self.FourCritload7)
            self.FourCritload8 = last_row['Body Language']
            self.CritScala8.set(self.FourCritload8)
            self.FourCritload9 = last_row['Structure']
            self.CritScala9.set(self.FourCritload9)
            self.FourCritload10 = last_row['Delivery']
            self.CritScala10.set(self.FourCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate4 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate4)

            # save upload onto google classroom
            self.FourGoogCheck = last_row['Google C.']
            self.FourTeachSave = last_row['Teachable']
            self.FourQuizSave = last_row['Quiz Taken']
            self.FourCritSave = last_row['Presentation Check']

            self.FourOfficerSave = last_row['Officer']
            self.officerCheck.set(self.FourOfficerSave)

            self.FourNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.FourNotes)

            # Start by filling in the checkboxes
            if self.FourGoogCheck == 1:
                self.chkGClass.select()
            if self.FourTeachSave == 1:
                self.chkTeachable.select()
            if self.FourQuizSave == 1:
                self.chkQuiz.select()
            if self.FourCritSave == 1:
                self.chkCrit.select()

            if self.FourOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.FourOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.FourOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.FourOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.FourCritload1), int(self.FourCritload2), int(self.FourCritload3), int(self.FourCritload4), int(self.FourCritload5),
                     int(self.FourCritload6), int(self.FourCritload7), int(self.FourCritload8), int(self.FourCritload9), int(self.FourCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 4)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 5:
            level1_rows = df.loc[df['Mission No.'] == 5]
            last_row = level1_rows.iloc[-1]

            self.FiveCritload1 = last_row['Application']
            self.CritScala1.set(self.FiveCritload1)
            self.FiveCritload2 = last_row['Readability']
            self.CritScala2.set(self.FiveCritload2)
            self.FiveCritload3 = last_row['Quality']
            self.CritScala3.set(self.FiveCritload3)
            self.FiveCritload4 = last_row['Creativity']
            self.CritScala4.set(self.FiveCritload4)
            self.FiveCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.FiveCritload5)
            self.FiveCritload6 = last_row['Content']
            self.CritScala6.set(self.FiveCritload6)
            self.FiveCritload7 = last_row['Originality']
            self.CritScala7.set(self.FiveCritload7)
            self.FiveCritload8 = last_row['Body Language']
            self.CritScala8.set(self.FiveCritload8)
            self.FiveCritload9 = last_row['Structure']
            self.CritScala9.set(self.FiveCritload9)
            self.FiveCritload10 = last_row['Delivery']
            self.CritScala10.set(self.FiveCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate5 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate5)

            # save upload onto google classroom
            self.FiveGoogCheck = last_row['Google C.']
            self.FiveTeachSave = last_row['Teachable']
            self.FiveQuizSave = last_row['Quiz Taken']
            self.FiveCritSave = last_row['Presentation Check']

            self.FiveOfficerSave = last_row['Officer']
            self.officerCheck.set(self.FiveOfficerSave)

            self.FiveNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.FiveNotes)

            # Start by filling in the checkboxes
            if self.FiveGoogCheck == 1:
                self.chkGClass.select()
            if self.FiveTeachSave == 1:
                self.chkTeachable.select()
            if self.FiveQuizSave == 1:
                self.chkQuiz.select()
            if self.FiveCritSave == 1:
                self.chkCrit.select()

            if self.FiveOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.FiveOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.FiveOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.FiveOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.FiveCritload1), int(self.FiveCritload2), int(self.FiveCritload3), int(self.FiveCritload4), int(self.FiveCritload5),
                     int(self.FiveCritload6), int(self.FiveCritload7), int(self.FiveCritload8), int(self.FiveCritload9), int(self.FiveCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 5)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 6:
            level1_rows = df.loc[df['Mission No.'] == 6]
            last_row = level1_rows.iloc[-1]

            self.SixCritload1 = last_row['Application']
            self.CritScala1.set(self.SixCritload1)
            self.SixCritload2 = last_row['Readability']
            self.CritScala2.set(self.SixCritload2)
            self.SixCritload3 = last_row['Quality']
            self.CritScala3.set(self.SixCritload3)
            self.SixCritload4 = last_row['Creativity']
            self.CritScala4.set(self.SixCritload4)
            self.SixCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.SixCritload5)
            self.SixCritload6 = last_row['Content']
            self.CritScala6.set(self.SixCritload6)
            self.SixCritload7 = last_row['Originality']
            self.CritScala7.set(self.SixCritload7)
            self.SixCritload8 = last_row['Body Language']
            self.CritScala8.set(self.SixCritload8)
            self.SixCritload9 = last_row['Structure']
            self.CritScala9.set(self.SixCritload9)
            self.SixCritload10 = last_row['Delivery']
            self.CritScala10.set(self.SixCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate6 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate6)

            # save upload onto google classroom
            self.SixGoogCheck = last_row['Google C.']
            self.SixTeachSave = last_row['Teachable']
            self.SixQuizSave = last_row['Quiz Taken']
            self.SixCritSave = last_row['Presentation Check']

            self.SixOfficerSave = last_row['Officer']
            self.officerCheck.set(self.SixOfficerSave)

            self.SixNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.SixNotes)

            # Start by filling in the checkboxes
            if self.SixGoogCheck == 1:
                self.chkGClass.select()
            if self.SixTeachSave == 1:
                self.chkTeachable.select()
            if self.SixQuizSave == 1:
                self.chkQuiz.select()
            if self.SixCritSave == 1:
                self.chkCrit.select()

            if self.SixOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.SixOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.SixOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.SixOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.SixCritload1), int(self.SixCritload2), int(self.SixCritload3), int(self.SixCritload4), int(self.SixCritload5),
                     int(self.SixCritload6), int(self.SixCritload7), int(self.SixCritload8), int(self.SixCritload9), int(self.SixCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 6)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)
        elif self.select == 7:
            level1_rows = df.loc[df['Mission No.'] == 7]
            last_row = level1_rows.iloc[-1]

            self.SevenCritload1 = last_row['Application']
            self.CritScala1.set(self.SevenCritload1)
            self.SevenCritload2 = last_row['Readability']
            self.CritScala2.set(self.SevenCritload2)
            self.SevenCritload3 = last_row['Quality']
            self.CritScala3.set(self.SevenCritload3)
            self.SevenCritload4 = last_row['Creativity']
            self.CritScala4.set(self.SevenCritload4)
            self.SevenCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.SevenCritload5)
            self.SevenCritload6 = last_row['Content']
            self.CritScala6.set(self.SevenCritload6)
            self.SevenCritload7 = last_row['Originality']
            self.CritScala7.set(self.SevenCritload7)
            self.SevenCritload8 = last_row['Body Language']
            self.CritScala8.set(self.SevenCritload8)
            self.SevenCritload9 = last_row['Structure']
            self.CritScala9.set(self.SevenCritload9)
            self.SevenCritload10 = last_row['Delivery']
            self.CritScala10.set(self.SevenCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate7 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate7)

            # save upload onto google classroom
            self.SevenGoogCheck = last_row['Google C.']
            self.SevenTeachSave = last_row['Teachable']
            self.SevenQuizSave = last_row['Quiz Taken']
            self.SevenCritSave = last_row['Presentation Check']

            self.SevenOfficerSave = last_row['Officer']
            self.officerCheck.set(self.SevenOfficerSave)

            self.SevenNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.SevenNotes)

            # Start by filling in the checkboxes
            if self.SevenGoogCheck == 1:
                self.chkGClass.select()
            if self.SevenTeachSave == 1:
                self.chkTeachable.select()
            if self.SevenQuizSave == 1:
                self.chkQuiz.select()
            if self.SevenCritSave == 1:
                self.chkCrit.select()

            if self.SevenOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.SevenOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.SevenOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.SevenOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.SevenCritload1), int(self.SevenCritload2), int(self.SevenCritload3), int(self.SevenCritload4), int(self.SevenCritload5),
                     int(self.SevenCritload6), int(self.SevenCritload7), int(self.SevenCritload8), int(self.SevenCritload9), int(self.SevenCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 6)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 8:
            level1_rows = df.loc[df['Mission No.'] == 8]
            last_row = level1_rows.iloc[-1]

            self.EightCritload1 = last_row['Application']
            self.CritScala1.set(self.EightCritload1)
            self.EightCritload2 = last_row['Readability']
            self.CritScala2.set(self.EightCritload2)
            self.EightCritload3 = last_row['Quality']
            self.CritScala3.set(self.EightCritload3)
            self.EightCritload4 = last_row['Creativity']
            self.CritScala4.set(self.EightCritload4)
            self.EightCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.EightCritload5)
            self.EightCritload6 = last_row['Content']
            self.CritScala6.set(self.EightCritload6)
            self.EightCritload7 = last_row['Originality']
            self.CritScala7.set(self.EightCritload7)
            self.EightCritload8 = last_row['Body Language']
            self.CritScala8.set(self.EightCritload8)
            self.EightCritload9 = last_row['Structure']
            self.CritScala9.set(self.EightCritload9)
            self.EightCritload10 = last_row['Delivery']
            self.CritScala10.set(self.EightCritload10)


            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate8 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate8)

            # save upload onto google classroom
            self.EightGoogCheck = last_row['Google C.']
            self.EightTeachSave = last_row['Teachable']
            self.EightQuizSave = last_row['Quiz Taken']
            self.EightCritSave = last_row['Presentation Check']

            self.EightOfficerSave = last_row['Officer']
            self.officerCheck.set(self.EightOfficerSave)

            self.EightNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.EightNotes)

            # Start by filling in the checkboxes
            if self.EightGoogCheck == 1:
                self.chkGClass.select()
            if self.EightTeachSave == 1:
                self.chkTeachable.select()
            if self.EightQuizSave == 1:
                self.chkQuiz.select()
            if self.EightCritSave == 1:
                self.chkCrit.select()

            if self.EightOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.EightOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.EightOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.EightOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.EightCritload1), int(self.EightCritload2), int(self.EightCritload3), int(self.EightCritload4), int(self.EightCritload5),
                     int(self.EightCritload6), int(self.EightCritload7), int(self.EightCritload8), int(self.EightCritload9), int(self.EightCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 8)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 9:
            level1_rows = df.loc[df['Mission No.'] == 9]
            last_row = level1_rows.iloc[-1]

            self.NineCritload1 = last_row['Application']
            self.CritScala1.set(self.NineCritload1)
            self.NineCritload2 = last_row['Readability']
            self.CritScala2.set(self.NineCritload2)
            self.NineCritload3 = last_row['Quality']
            self.CritScala3.set(self.NineCritload3)
            self.NineCritload4 = last_row['Creativity']
            self.CritScala4.set(self.NineCritload4)
            self.NineCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.NineCritload5)
            self.NineCritload6 = last_row['Content']
            self.CritScala6.set(self.NineCritload6)
            self.NineCritload7 = last_row['Originality']
            self.CritScala7.set(self.NineCritload7)
            self.NineCritload8 = last_row['Body Language']
            self.CritScala8.set(self.NineCritload8)
            self.NineCritload9 = last_row['Structure']
            self.CritScala9.set(self.NineCritload9)
            self.NineCritload10 = last_row['Delivery']
            self.CritScala10.set(self.NineCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate9 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate9)

            # save upload onto google classroom
            self.NineGoogCheck = last_row['Google C.']
            self.NineTeachSave = last_row['Teachable']
            self.NineQuizSave = last_row['Quiz Taken']
            self.NineCritSave = last_row['Presentation Check']

            self.NineOfficerSave = last_row['Officer']
            self.officerCheck.set(self.NineOfficerSave)

            self.NineNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.NineNotes)

            # Start by filling in the checkboxes
            if self.NineGoogCheck == 1:
                self.chkGClass.select()
            if self.NineTeachSave == 1:
                self.chkTeachable.select()
            if self.NineQuizSave == 1:
                self.chkQuiz.select()
            if self.NineCritSave == 1:
                self.chkCrit.select()

            if self.NineOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.NineOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.NineOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.NineOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.NineCritload1), int(self.NineCritload2), int(self.NineCritload3), int(self.NineCritload4), int(self.NineCritload5),
                     int(self.NineCritload6), int(self.NineCritload7), int(self.NineCritload8), int(self.NineCritload9), int(self.NineCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 9)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 10:
            level1_rows = df.loc[df['Mission No.'] == 10]
            last_row = level1_rows.iloc[-1]

            self.TenCritload1 = last_row['Application']
            self.CritScala1.set(self.TenCritload1)
            self.TenCritload2 = last_row['Readability']
            self.CritScala2.set(self.TenCritload2)
            self.TenCritload3 = last_row['Quality']
            self.CritScala3.set(self.TenCritload3)
            self.TenCritload4 = last_row['Creativity']
            self.CritScala4.set(self.TenCritload4)
            self.TenCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.TenCritload5)
            self.TenCritload6 = last_row['Content']
            self.CritScala6.set(self.TenCritload6)
            self.TenCritload7 = last_row['Originality']
            self.CritScala7.set(self.TenCritload7)
            self.TenCritload8 = last_row['Body Language']
            self.CritScala8.set(self.TenCritload8)
            self.TenCritload9 = last_row['Structure']
            self.CritScala9.set(self.TenCritload9)
            self.TenCritload10 = last_row['Delivery']
            self.CritScala10.set(self.TenCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate10 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate10)

            # save upload onto google classroom
            self.TenGoogCheck = last_row['Google C.']
            self.TenTeachSave = last_row['Teachable']
            self.TenQuizSave = last_row['Quiz Taken']
            self.TenCritSave = last_row['Presentation Check']

            self.TenOfficerSave = last_row['Officer']
            self.officerCheck.set(self.TenOfficerSave)

            self.TenNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.TenNotes)

            # Start by filling in the checkboxes
            if self.TenGoogCheck == 1:
                self.chkGClass.select()
            if self.TenTeachSave == 1:
                self.chkTeachable.select()
            if self.TenQuizSave == 1:
                self.chkQuiz.select()
            if self.TenCritSave == 1:
                self.chkCrit.select()

            if self.TenOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.TenOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.TenOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.TenOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.TenCritload1), int(self.TenCritload2), int(self.TenCritload3), int(self.TenCritload4), int(self.TenCritload5),
                     int(self.TenCritload6), int(self.TenCritload7), int(self.TenCritload8), int(self.TenCritload9),
                     int(self.TenCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 10)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 11:
            level1_rows = df.loc[df['Mission No.'] == 11]
            last_row = level1_rows.iloc[-1]

            self.ElevenCritload1 = last_row['Application']
            self.CritScala1.set(self.ElevenCritload1)
            self.ElevenCritload2 = last_row['Readability']
            self.CritScala2.set(self.ElevenCritload2)
            self.ElevenCritload3 = last_row['Quality']
            self.CritScala3.set(self.ElevenCritload3)
            self.ElevenCritload4 = last_row['Creativity']
            self.CritScala4.set(self.ElevenCritload4)
            self.ElevenCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.ElevenCritload5)
            self.ElevenCritload6 = last_row['Content']
            self.CritScala6.set(self.ElevenCritload6)
            self.ElevenCritload7 = last_row['Originality']
            self.CritScala7.set(self.ElevenCritload7)
            self.ElevenCritload8 = last_row['Body Language']
            self.CritScala8.set(self.ElevenCritload8)
            self.ElevenCritload9 = last_row['Structure']
            self.CritScala9.set(self.ElevenCritload9)
            self.ElevenCritload10 = last_row['Delivery']
            self.CritScala10.set(self.ElevenCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate11 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate11)

            # save upload onto google classroom
            self.ElevenGoogCheck = last_row['Google C.']
            self.ElevenTeachSave = last_row['Teachable']
            self.ElevenQuizSave = last_row['Quiz Taken']
            self.ElevenCritSave = last_row['Presentation Check']

            self.ElevenOfficerSave = last_row['Officer']
            self.officerCheck.set(self.ElevenOfficerSave)

            self.ElevenNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.ElevenNotes)

            # Start by filling in the checkboxes
            if self.ElevenGoogCheck == 1:
                self.chkGClass.select()
            if self.ElevenTeachSave == 1:
                self.chkTeachable.select()
            if self.ElevenQuizSave == 1:
                self.chkQuiz.select()
            if self.ElevenCritSave == 1:
                self.chkCrit.select()

            if self.ElevenOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.ElevenOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.ElevenOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.ElevenOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.ElevenCritload1), int(self.ElevenCritload2), int(self.ElevenCritload3), int(self.ElevenCritload4), int(self.ElevenCritload5),
                     int(self.ElevenCritload6), int(self.ElevenCritload7), int(self.ElevenCritload8), int(self.ElevenCritload9),int(self.ElevenCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 11)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 12:
            level1_rows = df.loc[df['Mission No.'] == 12]
            last_row = level1_rows.iloc[-1]

            self.TwelveCritload1 = last_row['Application']
            self.CritScala1.set(self.TwelveCritload1)
            self.TwelveCritload2 = last_row['Readability']
            self.CritScala2.set(self.TwelveCritload2)
            self.TwelveCritload3 = last_row['Quality']
            self.CritScala3.set(self.TwelveCritload3)
            self.TwelveCritload4 = last_row['Creativity']
            self.CritScala4.set(self.TwelveCritload4)
            self.TwelveCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.TwelveCritload5)
            self.TwelveCritload6 = last_row['Content']
            self.CritScala6.set(self.TwelveCritload6)
            self.TwelveCritload7 = last_row['Originality']
            self.CritScala7.set(self.TwelveCritload7)
            self.TwelveCritload8 = last_row['Body Language']
            self.CritScala8.set(self.TwelveCritload8)
            self.TwelveCritload9 = last_row['Structure']
            self.CritScala9.set(self.TwelveCritload9)
            self.TwelveCritload10 = last_row['Delivery']
            self.CritScala10.set(self.TwelveCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate12 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate12)

            # save upload onto google classroom
            self.TwelveGoogCheck = last_row['Google C.']
            self.TwelveTeachSave = last_row['Teachable']
            self.TwelveQuizSave = last_row['Quiz Taken']
            self.TwelveCritSave = last_row['Presentation Check']

            self.TwelveOfficerSave = last_row['Officer']
            self.officerCheck.set(self.TwelveOfficerSave)

            self.TwelveNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.TwelveNotes)

            # Start by filling in the checkboxes
            if self.TwelveGoogCheck == 1:
                self.chkGClass.select()
            if self.TwelveTeachSave == 1:
                self.chkTeachable.select()
            if self.TwelveQuizSave == 1:
                self.chkQuiz.select()
            if self.TwelveCritSave == 1:
                self.chkCrit.select()

            if self.TwelveOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.TwelveOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.TwelveOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.TwelveOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.TwelveCritload1), int(self.TwelveCritload2), int(self.TwelveCritload3), int(self.TwelveCritload4), int(self.TwelveCritload5),
                     int(self.TwelveCritload6), int(self.TwelveCritload7), int(self.TwelveCritload8), int(self.TwelveCritload9),int(self.TwelveCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 12)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 13:
            level1_rows = df.loc[df['Mission No.'] == 13]
            last_row = level1_rows.iloc[-1]

            self.ThirteenCritload1 = last_row['Application']
            self.CritScala1.set(self.ThirteenCritload1)
            self.ThirteenCritload2 = last_row['Readability']
            self.CritScala2.set(self.ThirteenCritload2)
            self.ThirteenCritload3 = last_row['Quality']
            self.CritScala3.set(self.ThirteenCritload3)
            self.ThirteenCritload4 = last_row['Creativity']
            self.CritScala4.set(self.ThirteenCritload4)
            self.ThirteenCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.ThirteenCritload5)
            self.ThirteenCritload6 = last_row['Content']
            self.CritScala6.set(self.ThirteenCritload6)
            self.ThirteenCritload7 = last_row['Originality']
            self.CritScala7.set(self.ThirteenCritload7)
            self.ThirteenCritload8 = last_row['Body Language']
            self.CritScala8.set(self.ThirteenCritload8)
            self.ThirteenCritload9 = last_row['Structure']
            self.CritScala9.set(self.ThirteenCritload9)
            self.ThirteenCritload10 = last_row['Delivery']
            self.CritScala10.set(self.ThirteenCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate13 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate13)

            # save upload onto google classroom
            self.ThirteenGoogCheck = last_row['Google C.']
            self.ThirteenTeachSave = last_row['Teachable']
            self.ThirteenQuizSave = last_row['Quiz Taken']
            self.ThirteenCritSave = last_row['Presentation Check']

            self.ThirteenOfficerSave = last_row['Officer']
            self.officerCheck.set(self.ThirteenOfficerSave)

            self.ThirteenNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.ThirteenNotes)

            # Start by filling in the checkboxes
            if self.ThirteenGoogCheck == 1:
                self.chkGClass.select()
            if self.ThirteenTeachSave == 1:
                self.chkTeachable.select()
            if self.ThirteenQuizSave == 1:
                self.chkQuiz.select()
            if self.ThirteenCritSave == 1:
                self.chkCrit.select()

            if self.ThirteenOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.ThirteenOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.ThirteenOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.ThirteenOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.ThirteenCritload1), int(self.ThirteenCritload2), int(self.ThirteenCritload3), int(self.ThirteenCritload4), int(self.ThirteenCritload5),
                     int(self.ThirteenCritload6), int(self.ThirteenCritload7), int(self.ThirteenCritload8),int(self.ThirteenCritload9), int(self.ThirteenCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 13)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 14:
            level1_rows = df.loc[df['Mission No.'] == 14]
            last_row = level1_rows.iloc[-1]

            self.FourteenCritload1 = last_row['Application']
            self.CritScala1.set(self.FourteenCritload1)
            self.FourteenCritload2 = last_row['Readability']
            self.CritScala2.set(self.FourteenCritload2)
            self.FourteenCritload3 = last_row['Quality']
            self.CritScala3.set(self.FourteenCritload3)
            self.FourteenCritload4 = last_row['Creativity']
            self.CritScala4.set(self.FourteenCritload4)
            self.FourteenCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.FourteenCritload5)
            self.FourteenCritload6 = last_row['Content']
            self.CritScala6.set(self.FourteenCritload6)
            self.FourteenCritload7 = last_row['Originality']
            self.CritScala7.set(self.FourteenCritload7)
            self.FourteenCritload8 = last_row['Body Language']
            self.CritScala8.set(self.FourteenCritload8)
            self.FourteenCritload9 = last_row['Structure']
            self.CritScala9.set(self.FourteenCritload9)
            self.FourteenCritload10 = last_row['Delivery']
            self.CritScala10.set(self.FourteenCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate14 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate14)

            # save upload onto google classroom
            self.FourteenGoogCheck = last_row['Google C.']
            self.FourteenTeachSave = last_row['Teachable']
            self.FourteenQuizSave = last_row['Quiz Taken']
            self.FourteenCritSave = last_row['Presentation Check']

            self.FourteenOfficerSave = last_row['Officer']
            self.officerCheck.set(self.FourteenOfficerSave)

            self.FourteenNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.FourteenNotes)

            # Start by filling in the checkboxes
            if self.FourteenGoogCheck == 1:
                self.chkGClass.select()
            if self.FourteenTeachSave == 1:
                self.chkTeachable.select()
            if self.FourteenQuizSave == 1:
                self.chkQuiz.select()
            if self.FourteenCritSave == 1:
                self.chkCrit.select()

            if self.FourteenOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.FourteenOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.FourteenOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.FourteenOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.FourteenCritload1), int(self.FourteenCritload2), int(self.FourteenCritload3), int(self.FourteenCritload4), int(self.FourteenCritload5),
                     int(self.FourteenCritload6), int(self.FourteenCritload7), int(self.FourteenCritload8),
                     int(self.FourteenCritload9), int(self.FourteenCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 14)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 15:
            level1_rows = df.loc[df['Mission No.'] == 15]
            last_row = level1_rows.iloc[-1]

            self.FifteenCritload1 = last_row['Application']
            self.CritScala1.set(self.FifteenCritload1)
            self.FifteenCritload2 = last_row['Readability']
            self.CritScala2.set(self.FifteenCritload2)
            self.FifteenCritload3 = last_row['Quality']
            self.CritScala3.set(self.FifteenCritload3)
            self.FifteenCritload4 = last_row['Creativity']
            self.CritScala4.set(self.FifteenCritload4)
            self.FifteenCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.FifteenCritload5)
            self.FifteenCritload6 = last_row['Content']
            self.CritScala6.set(self.FifteenCritload6)
            self.FifteenCritload7 = last_row['Originality']
            self.CritScala7.set(self.FifteenCritload7)
            self.FifteenCritload8 = last_row['Body Language']
            self.CritScala8.set(self.FifteenCritload8)
            self.FifteenCritload9 = last_row['Structure']
            self.CritScala9.set(self.FifteenCritload9)
            self.FifteenCritload10 = last_row['Delivery']
            self.CritScala10.set(self.FifteenCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate15 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate15)

            # save upload onto google classroom
            self.FifteenGoogCheck = last_row['Google C.']
            self.FifteenTeachSave = last_row['Teachable']
            self.FifteenQuizSave = last_row['Quiz Taken']
            self.FifteenCritSave = last_row['Presentation Check']

            self.FifteenOfficerSave = last_row['Officer']
            self.officerCheck.set(self.FifteenOfficerSave)

            self.FifteenNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.FifteenNotes)

            # Start by filling in the checkboxes
            if self.FifteenGoogCheck == 1:
                self.chkGClass.select()
            if self.FifteenTeachSave == 1:
                self.chkTeachable.select()
            if self.FifteenQuizSave == 1:
                self.chkQuiz.select()
            if self.FifteenCritSave == 1:
                self.chkCrit.select()

            if self.FifteenOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.FifteenOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.FifteenOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.FifteenOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.FifteenCritload1), int(self.FifteenCritload2), int(self.FifteenCritload3), int(self.FifteenCritload4), int(self.FifteenCritload5),
                     int(self.FifteenCritload6), int(self.FifteenCritload7), int(self.FifteenCritload8),
                     int(self.FifteenCritload9), int(self.FifteenCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 15)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 16:
            level1_rows = df.loc[df['Mission No.'] == 16]
            last_row = level1_rows.iloc[-1]

            self.SixteenCritload1 = last_row['Application']
            self.CritScala1.set(self.SixteenCritload1)
            self.SixteenCritload2 = last_row['Readability']
            self.CritScala2.set(self.SixteenCritload2)
            self.SixteenCritload3 = last_row['Quality']
            self.CritScala3.set(self.SixteenCritload3)
            self.SixteenCritload4 = last_row['Creativity']
            self.CritScala4.set(self.SixteenCritload4)
            self.SixteenCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.SixteenCritload5)
            self.SixteenCritload6 = last_row['Content']
            self.CritScala6.set(self.SixteenCritload6)
            self.SixteenCritload7 = last_row['Originality']
            self.CritScala7.set(self.SixteenCritload7)
            self.SixteenCritload8 = last_row['Body Language']
            self.CritScala8.set(self.SixteenCritload8)
            self.SixteenCritload9 = last_row['Structure']
            self.CritScala9.set(self.SixteenCritload9)
            self.SixteenCritload10 = last_row['Delivery']
            self.CritScala10.set(self.SixteenCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate16 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate16)

            # save upload onto google classroom
            self.SixteenGoogCheck = last_row['Google C.']
            self.SixteenTeachSave = last_row['Teachable']
            self.SixteenQuizSave = last_row['Quiz Taken']
            self.SixteenCritSave = last_row['Presentation Check']

            self.SixteenOfficerSave = last_row['Officer']
            self.officerCheck.set(self.SixteenOfficerSave)

            self.SixteenNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.SixteenNotes)

            # Start by filling in the checkboxes
            if self.SixteenGoogCheck == 1:
                self.chkGClass.select()
            if self.SixteenTeachSave == 1:
                self.chkTeachable.select()
            if self.SixteenQuizSave == 1:
                self.chkQuiz.select()
            if self.SixteenCritSave == 1:
                self.chkCrit.select()

            if self.SixteenOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.SixteenOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.SixteenOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.SixteenOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.SixteenCritload1), int(self.SixteenCritload2), int(self.SixteenCritload3), int(self.SixteenCritload4), int(self.SixteenCritload5),
                     int(self.SixteenCritload6), int(self.SixteenCritload7), int(self.SixteenCritload8),
                     int(self.SixteenCritload9), int(self.SixteenCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 16)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 17:
            level1_rows = df.loc[df['Mission No.'] == 17]
            last_row = level1_rows.iloc[-1]

            self.SeventeenCritload1 = last_row['Application']
            self.CritScala1.set(self.SeventeenCritload1)
            self.SeventeenCritload2 = last_row['Readability']
            self.CritScala2.set(self.SeventeenCritload2)
            self.SeventeenCritload3 = last_row['Quality']
            self.CritScala3.set(self.SeventeenCritload3)
            self.SeventeenCritload4 = last_row['Creativity']
            self.CritScala4.set(self.SeventeenCritload4)
            self.SeventeenCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.SeventeenCritload5)
            self.SeventeenCritload6 = last_row['Content']
            self.CritScala6.set(self.SeventeenCritload6)
            self.SeventeenCritload7 = last_row['Originality']
            self.CritScala7.set(self.SeventeenCritload7)
            self.SeventeenCritload8 = last_row['Body Language']
            self.CritScala8.set(self.SeventeenCritload8)
            self.SeventeenCritload9 = last_row['Structure']
            self.CritScala9.set(self.SeventeenCritload9)
            self.SeventeenCritload10 = last_row['Delivery']
            self.CritScala10.set(self.SeventeenCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate17 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate17)

            # save upload onto google classroom
            self.SeventeenGoogCheck = last_row['Google C.']
            self.SeventeenTeachSave = last_row['Teachable']
            self.SeventeenQuizSave = last_row['Quiz Taken']
            self.SeventeenCritSave = last_row['Presentation Check']

            self.SeventeenOfficerSave = last_row['Officer']
            self.officerCheck.set(self.SeventeenOfficerSave)

            self.SeventeenNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.SeventeenNotes)

            # Start by filling in the checkboxes
            if self.SeventeenGoogCheck == 1:
                self.chkGClass.select()
            if self.SeventeenTeachSave == 1:
                self.chkTeachable.select()
            if self.SeventeenQuizSave == 1:
                self.chkQuiz.select()
            if self.SeventeenCritSave == 1:
                self.chkCrit.select()

            if self.SeventeenOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.SeventeenOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.SeventeenOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.SeventeenOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.SeventeenCritload1), int(self.SeventeenCritload2), int(self.SeventeenCritload3), int(self.SeventeenCritload4), int(self.SeventeenCritload5),
                     int(self.SeventeenCritload6), int(self.SeventeenCritload7), int(self.SeventeenCritload8),
                     int(self.SeventeenCritload9), int(self.SeventeenCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 17)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 18:
            level1_rows = df.loc[df['Mission No.'] == 18]
            last_row = level1_rows.iloc[-1]

            self.EighteenCritload1 = last_row['Application']
            self.CritScala1.set(self.EighteenCritload1)
            self.EighteenCritload2 = last_row['Readability']
            self.CritScala2.set(self.EighteenCritload2)
            self.EighteenCritload3 = last_row['Quality']
            self.CritScala3.set(self.EighteenCritload3)
            self.EighteenCritload4 = last_row['Creativity']
            self.CritScala4.set(self.EighteenCritload4)
            self.EighteenCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.EighteenCritload5)
            self.EighteenCritload6 = last_row['Content']
            self.CritScala6.set(self.EighteenCritload6)
            self.EighteenCritload7 = last_row['Originality']
            self.CritScala7.set(self.EighteenCritload7)
            self.EighteenCritload8 = last_row['Body Language']
            self.CritScala8.set(self.EighteenCritload8)
            self.EighteenCritload9 = last_row['Structure']
            self.CritScala9.set(self.EighteenCritload9)
            self.EighteenCritload10 = last_row['Delivery']
            self.CritScala10.set(self.EighteenCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate18 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate18)

            # save upload onto google classroom
            self.EighteenGoogCheck = last_row['Google C.']
            self.EighteenTeachSave = last_row['Teachable']
            self.EighteenQuizSave = last_row['Quiz Taken']
            self.EighteenCritSave = last_row['Presentation Check']

            self.EighteenOfficerSave = last_row['Officer']
            self.officerCheck.set(self.EighteenOfficerSave)

            self.EighteenNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.EighteenNotes)

            # Start by filling in the checkboxes
            if self.EighteenGoogCheck == 1:
                self.chkGClass.select()
            if self.EighteenTeachSave == 1:
                self.chkTeachable.select()
            if self.EighteenQuizSave == 1:
                self.chkQuiz.select()
            if self.EighteenCritSave == 1:
                self.chkCrit.select()

            if self.EighteenOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.EighteenOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.EighteenOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.EighteenOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.EighteenCritload1), int(self.EighteenCritload2), int(self.EighteenCritload3), int(self.EighteenCritload4), int(self.EighteenCritload5),
                     int(self.EighteenCritload6), int(self.EighteenCritload7), int(self.EighteenCritload8),
                     int(self.EighteenCritload9), int(self.EighteenCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 18)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 19:
            level1_rows = df.loc[df['Mission No.'] == 19]
            last_row = level1_rows.iloc[-1]

            self.NineteenCritload1 = last_row['Application']
            self.CritScala1.set(self.NineteenCritload1)
            self.NineteenCritload2 = last_row['Readability']
            self.CritScala2.set(self.NineteenCritload2)
            self.NineteenCritload3 = last_row['Quality']
            self.CritScala3.set(self.NineteenCritload3)
            self.NineteenCritload4 = last_row['Creativity']
            self.CritScala4.set(self.NineteenCritload4)
            self.NineteenCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.NineteenCritload5)
            self.NineteenCritload6 = last_row['Content']
            self.CritScala6.set(self.NineteenCritload6)
            self.NineteenCritload7 = last_row['Originality']
            self.CritScala7.set(self.NineteenCritload7)
            self.NineteenCritload8 = last_row['Body Language']
            self.CritScala8.set(self.NineteenCritload8)
            self.NineteenCritload9 = last_row['Structure']
            self.CritScala9.set(self.NineteenCritload9)
            self.NineteenCritload10 = last_row['Delivery']
            self.CritScala10.set(self.NineteenCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate19 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate19)

            # save upload onto google classroom
            self.NineteenGoogCheck = last_row['Google C.']
            self.NineteenTeachSave = last_row['Teachable']
            self.NineteenQuizSave = last_row['Quiz Taken']
            self.NineteenCritSave = last_row['Presentation Check']

            self.NineteenOfficerSave = last_row['Officer']
            self.officerCheck.set(self.NineteenOfficerSave)

            self.NineteenNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.NineteenNotes)

            # Start by filling in the checkboxes
            if self.NineteenGoogCheck == 1:
                self.chkGClass.select()
            if self.NineteenTeachSave == 1:
                self.chkTeachable.select()
            if self.NineteenQuizSave == 1:
                self.chkQuiz.select()
            if self.NineteenCritSave == 1:
                self.chkCrit.select()

            if self.NineteenOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.NineteenOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.NineteenOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.NineteenOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.NineteenCritload1), int(self.NineteenCritload2), int(self.NineteenCritload3), int(self.NineteenCritload4), int(self.NineteenCritload5),
                     int(self.NineteenCritload6), int(self.NineteenCritload7), int(self.NineteenCritload8),
                     int(self.NineteenCritload9), int(self.NineteenCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 19)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 20:
            level1_rows = df.loc[df['Mission No.'] == 20]
            last_row = level1_rows.iloc[-1]

            self.TwentyCritload1 = last_row['Application']
            self.CritScala1.set(self.TwentyCritload1)
            self.TwentyCritload2 = last_row['Readability']
            self.CritScala2.set(self.TwentyCritload2)
            self.TwentyCritload3 = last_row['Quality']
            self.CritScala3.set(self.TwentyCritload3)
            self.TwentyCritload4 = last_row['Creativity']
            self.CritScala4.set(self.TwentyCritload4)
            self.TwentyCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.TwentyCritload5)
            self.TwentyCritload6 = last_row['Content']
            self.CritScala6.set(self.TwentyCritload6)
            self.TwentyCritload7 = last_row['Originality']
            self.CritScala7.set(self.TwentyCritload7)
            self.TwentyCritload8 = last_row['Body Language']
            self.CritScala8.set(self.TwentyCritload8)
            self.TwentyCritload9 = last_row['Structure']
            self.CritScala9.set(self.TwentyCritload9)
            self.TwentyCritload10 = last_row['Delivery']
            self.CritScala10.set(self.TwentyCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate20 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate20)

            # save upload onto google classroom
            self.TwentyGoogCheck = last_row['Google C.']
            self.TwentyTeachSave = last_row['Teachable']
            self.TwentyQuizSave = last_row['Quiz Taken']
            self.TwentyCritSave = last_row['Presentation Check']

            self.TwentyOfficerSave = last_row['Officer']
            self.officerCheck.set(self.TwentyOfficerSave)

            self.TwentyNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.TwentyNotes)

            # Start by filling in the checkboxes
            if self.TwentyGoogCheck == 1:
                self.chkGClass.select()
            if self.TwentyTeachSave == 1:
                self.chkTeachable.select()
            if self.TwentyQuizSave == 1:
                self.chkQuiz.select()
            if self.TwentyCritSave == 1:
                self.chkCrit.select()

            if self.TwentyOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.TwentyOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.TwentyOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.TwentyOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.TwentyCritload1), int(self.TwentyCritload2), int(self.TwentyCritload3), int(self.TwentyCritload4), int(self.TwentyCritload5),
                     int(self.TwentyCritload6), int(self.TwentyCritload7), int(self.TwentyCritload8),
                     int(self.TwentyCritload9), int(self.TwentyCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 20)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 21:
            level1_rows = df.loc[df['Mission No.'] == 21]
            last_row = level1_rows.iloc[-1]

            self.TwentyOneCritload1 = last_row['Application']
            self.CritScala1.set(self.TwentyOneCritload1)
            self.TwentyOneCritload2 = last_row['Readability']
            self.CritScala2.set(self.TwentyOneCritload2)
            self.TwentyOneCritload3 = last_row['Quality']
            self.CritScala3.set(self.TwentyOneCritload3)
            self.TwentyOneCritload4 = last_row['Creativity']
            self.CritScala4.set(self.TwentyOneCritload4)
            self.TwentyOneCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.TwentyOneCritload5)
            self.TwentyOneCritload6 = last_row['Content']
            self.CritScala6.set(self.TwentyOneCritload6)
            self.TwentyOneCritload7 = last_row['Originality']
            self.CritScala7.set(self.TwentyOneCritload7)
            self.TwentyOneCritload8 = last_row['Body Language']
            self.CritScala8.set(self.TwentyOneCritload8)
            self.TwentyOneCritload9 = last_row['Structure']
            self.CritScala9.set(self.TwentyOneCritload9)
            self.TwentyOneCritload10 = last_row['Delivery']
            self.CritScala10.set(self.TwentyOneCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate21 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate21)

            # save upload onto google classroom
            self.TwentyOneGoogCheck = last_row['Google C.']
            self.TwentyOneTeachSave = last_row['Teachable']
            self.TwentyOneQuizSave = last_row['Quiz Taken']
            self.TwentyOneCritSave = last_row['Presentation Check']

            self.TwentyOneOfficerSave = last_row['Officer']
            self.officerCheck.set(self.TwentyOneOfficerSave)

            self.TwentyOneNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.TwentyOneNotes)

            # Start by filling in the checkboxes
            if self.TwentyOneGoogCheck == 1:
                self.chkGClass.select()
            if self.TwentyOneTeachSave == 1:
                self.chkTeachable.select()
            if self.TwentyOneQuizSave == 1:
                self.chkQuiz.select()
            if self.TwentyOneCritSave == 1:
                self.chkCrit.select()

            if self.TwentyOneOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.TwentyOneOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.TwentyOneOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.TwentyOneOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.TwentyOneCritload1), int(self.TwentyOneCritload2), int(self.TwentyOneCritload3), int(self.TwentyOneCritload4), int(self.TwentyOneCritload5),
                     int(self.TwentyOneCritload6), int(self.TwentyOneCritload7), int(self.TwentyOneCritload8),
                     int(self.TwentyOneCritload9), int(self.TwentyOneCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 21)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 22:
            level1_rows = df.loc[df['Mission No.'] == 22]
            last_row = level1_rows.iloc[-1]

            self.TwentyTwoCritload1 = last_row['Application']
            self.CritScala1.set(self.TwentyTwoCritload1)
            self.TwentyTwoCritload2 = last_row['Readability']
            self.CritScala2.set(self.TwentyTwoCritload2)
            self.TwentyTwoCritload3 = last_row['Quality']
            self.CritScala3.set(self.TwentyTwoCritload3)
            self.TwentyTwoCritload4 = last_row['Creativity']
            self.CritScala4.set(self.TwentyTwoCritload4)
            self.TwentyTwoCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.TwentyTwoCritload5)
            self.TwentyTwoCritload6 = last_row['Content']
            self.CritScala6.set(self.TwentyTwoCritload6)
            self.TwentyTwoCritload7 = last_row['Originality']
            self.CritScala7.set(self.TwentyTwoCritload7)
            self.TwentyTwoCritload8 = last_row['Body Language']
            self.CritScala8.set(self.TwentyTwoCritload8)
            self.TwentyTwoCritload9 = last_row['Structure']
            self.CritScala9.set(self.TwentyTwoCritload9)
            self.TwentyTwoCritload10 = last_row['Delivery']
            self.CritScala10.set(self.TwentyTwoCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate22 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate22)

            # save upload onto google classroom
            self.TwentyTwoGoogCheck = last_row['Google C.']
            self.TwentyTwoTeachSave = last_row['Teachable']
            self.TwentyTwoQuizSave = last_row['Quiz Taken']
            self.TwentyTwoCritSave = last_row['Presentation Check']

            self.TwentyTwoOfficerSave = last_row['Officer']
            self.officerCheck.set(self.TwentyTwoOfficerSave)

            self.TwentyTwoNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.TwentyTwoNotes)

            # Start by filling in the checkboxes
            if self.TwentyTwoGoogCheck == 1:
                self.chkGClass.select()
            if self.TwentyTwoTeachSave == 1:
                self.chkTeachable.select()
            if self.TwentyTwoQuizSave == 1:
                self.chkQuiz.select()
            if self.TwentyTwoCritSave == 1:
                self.chkCrit.select()

            if self.TwentyTwoOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.TwentyTwoOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.TwentyTwoOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.TwentyTwoOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.TwentyTwoCritload1), int(self.TwentyTwoCritload2), int(self.TwentyTwoCritload3), int(self.TwentyTwoCritload4), int(self.TwentyTwoCritload5),
                     int(self.TwentyTwoCritload6), int(self.TwentyTwoCritload7), int(self.TwentyTwoCritload8),
                     int(self.TwentyTwoCritload9), int(self.TwentyTwoCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 22)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 23:
            level1_rows = df.loc[df['Mission No.'] == 23]
            last_row = level1_rows.iloc[-1]

            self.TwentyThreeCritload1 = last_row['Application']
            self.CritScala1.set(self.TwentyThreeCritload1)
            self.TwentyThreeCritload2 = last_row['Readability']
            self.CritScala2.set(self.TwentyThreeCritload2)
            self.TwentyThreeCritload3 = last_row['Quality']
            self.CritScala3.set(self.TwentyThreeCritload3)
            self.TwentyThreeCritload4 = last_row['Creativity']
            self.CritScala4.set(self.TwentyThreeCritload4)
            self.TwentyThreeCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.TwentyThreeCritload5)
            self.TwentyThreeCritload6 = last_row['Content']
            self.CritScala6.set(self.TwentyThreeCritload6)
            self.TwentyThreeCritload7 = last_row['Originality']
            self.CritScala7.set(self.TwentyThreeCritload7)
            self.TwentyThreeCritload8 = last_row['Body Language']
            self.CritScala8.set(self.TwentyThreeCritload8)
            self.TwentyThreeCritload9 = last_row['Structure']
            self.CritScala9.set(self.TwentyThreeCritload9)
            self.TwentyThreeCritload10 = last_row['Delivery']
            self.CritScala10.set(self.TwentyThreeCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate23 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate23)

            # save upload onto google classroom
            self.TwentyThreeGoogCheck = last_row['Google C.']
            self.TwentyThreeTeachSave = last_row['Teachable']
            self.TwentyThreeQuizSave = last_row['Quiz Taken']
            self.TwentyThreeCritSave = last_row['Presentation Check']

            self.TwentyThreeOfficerSave = last_row['Officer']
            self.officerCheck.set(self.TwentyThreeOfficerSave)

            self.TwentyThreeNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.TwentyThreeNotes)

            # Start by filling in the checkboxes
            if self.TwentyThreeGoogCheck == 1:
                self.chkGClass.select()
            if self.TwentyThreeTeachSave == 1:
                self.chkTeachable.select()
            if self.TwentyThreeQuizSave == 1:
                self.chkQuiz.select()
            if self.TwentyThreeCritSave == 1:
                self.chkCrit.select()

            if self.TwentyThreeOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.TwentyThreeOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.TwentyThreeOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.TwentyThreeOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.TwentyThreeCritload1), int(self.TwentyThreeCritload2), int(self.TwentyThreeCritload3), int(self.TwentyThreeCritload4), int(self.TwentyThreeCritload5),
                     int(self.TwentyThreeCritload6), int(self.TwentyThreeCritload7), int(self.TwentyThreeCritload8),
                     int(self.TwentyThreeCritload9), int(self.TwentyThreeCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 23)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)

        elif self.select == 24:
            level1_rows = df.loc[df['Mission No.'] == 24]
            last_row = level1_rows.iloc[-1]

            self.TwentyFourCritload1 = last_row['Application']
            self.CritScala1.set(self.TwentyFourCritload1)
            self.TwentyFourCritload2 = last_row['Readability']
            self.CritScala2.set(self.TwentyFourCritload2)
            self.TwentyFourCritload3 = last_row['Quality']
            self.CritScala3.set(self.TwentyFourCritload3)
            self.TwentyFourCritload4 = last_row['Creativity']
            self.CritScala4.set(self.TwentyFourCritload4)
            self.TwentyFourCritload5 = last_row['Cleanliness']
            self.CritScala5.set(self.TwentyFourCritload5)
            self.TwentyFourCritload6 = last_row['Content']
            self.CritScala6.set(self.TwentyFourCritload6)
            self.TwentyFourCritload7 = last_row['Originality']
            self.CritScala7.set(self.TwentyFourCritload7)
            self.TwentyFourCritload8 = last_row['Body Language']
            self.CritScala8.set(self.TwentyFourCritload8)
            self.TwentyFourCritload9 = last_row['Structure']
            self.CritScala9.set(self.TwentyFourCritload9)
            self.TwentyFourCritload10 = last_row['Delivery']
            self.CritScala10.set(self.TwentyFourCritload10)

            self.subDate = last_row['Date']
            point = self.subDate.find('.')
            self.subDate24 = self.subDate[:point]
            self.lblDateTime.configure(text=self.subDate24)

            # save upload onto google classroom
            self.TwentyFourGoogCheck = last_row['Google C.']
            self.TwentyFourTeachSave = last_row['Teachable']
            self.TwentyFourQuizSave = last_row['Quiz Taken']
            self.TwentyFourCritSave = last_row['Presentation Check']

            self.TwentyFourOfficerSave = last_row['Officer']
            self.officerCheck.set(self.TwentyFourOfficerSave)

            self.TwentyFourNotes = last_row['Notes']
            self.notesEntry1A.insert('1.0', self.TwentyFourNotes)

            # Start by filling in the checkboxes
            if self.TwentyFourGoogCheck == 1:
                self.chkGClass.select()
            if self.TwentyFourTeachSave == 1:
                self.chkTeachable.select()
            if self.TwentyFourQuizSave == 1:
                self.chkQuiz.select()
            if self.TwentyFourCritSave == 1:
                self.chkCrit.select()

            if self.TwentyFourOfficerSave == 'Lannon Khau':
                off1 = 'spaceforce2A'
            elif self.TwentyFourOfficerSave == 'Benny Chiu':
                off1 = 'spaceforce3'
            elif self.TwentyFourOfficerSave == 'Fernando Galvez':
                off1 = 'spaceforce4'
            elif self.TwentyFourOfficerSave == 'Joshua Sanchez':
                off1 = 'spaceforce5'

            self.officer_img1 = ImageTk.PhotoImage(Image.open(f'images/{off1}.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)

            alice = [int(self.TwentyFourCritload1), int(self.TwentyFourCritload2), int(self.TwentyFourCritload3), int(self.TwentyFourCritload4), int(self.TwentyFourCritload5),
                     int(self.TwentyFourCritload6), int(self.TwentyFourCritload7), int(self.TwentyFourCritload8),
                     int(self.TwentyFourCritload9), int(self.TwentyFourCritload10)]

            planet_acquired = df.loc[(df['Mission No.'] == 24)]
            if True in planet_acquired['Planet Acquired'].tolist():
                self.leftMiss.configure(state = NORMAL)


        alice = [alice[0], alice[5], alice[1], alice[6], alice[2], alice[7], alice[3], alice[8], alice[4], alice[9]]
        alice.append(alice[0])
        # Create Spider Plot#######################################
        subjects = ['', '', '', '', '','','','','','']
        angles = np.linspace(0, 2 * np.pi, len(subjects), endpoint=False)
        angles = np.concatenate((angles, [angles[0]]))
        subjects.append(subjects[0])
        self.fig = plt2.figure(figsize=(6, 6), facecolor='black')

        self.ax = self.fig.add_subplot(polar=True)
        self.ax.plot(angles, alice, 'o-', color='g', label='Alice',
                     markerfacecolor='g', markeredgecolor='g')
        self.ax.text(0.09, 0.15, 'Innov.',
                    verticalalignment='bottom', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(0.40, -0.067, 'Struct.',
                    verticalalignment='bottom', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(0.75, -0.08, 'Simpl.',
                    verticalalignment='bottom', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(1.0748, .135, 'Deliv.',
                    verticalalignment='bottom', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(1.18, 0.47, 'Conc.',
                    verticalalignment='top', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(1.09, 0.82, 'Cont.',
                    verticalalignment='top', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(0.80, 1.06, 'Reada.',
                    verticalalignment='top', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(0.355, 1.05, 'Origin.',
                    verticalalignment='top', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(0.09, .86, 'Quala.',
                    verticalalignment='top', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(-0.01,.47, 'Lang.',
                    verticalalignment='top', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')

        self.ax.set_facecolor('black')

        spider = FigureCanvasTkAgg(self.fig, self.planet_canv)
        spider.get_tk_widget().pack(side=LEFT, fill=BOTH)
        # fill plot
        self.ax.fill(angles, alice, alpha=0.25, color='g')
        # Add labels
        self.ax.set_thetagrids(angles * 180 / np.pi, subjects)

        self.planet_tracker += 1
        self.btnLoadOne.configure(state=DISABLED)
        #########################################################

    def SaveRecord1A(self):

        header = [self.student1, 'Mission No.', 'Date','Application', 'Readability', 'Quality',
                  'Creativity', 'Cleanliness', 'Content', 'Originality','Body Language', 'Structure', 'Delivery',
                  'Google C.', 'Teachable', 'Quiz Taken', 'Presentation Check', 'Officer', 'Notes',
                  'Planet Acquired','Planet Name','Planet Type']

        file_exists = os.path.exists('missionRecords4.csv')
        if not file_exists:
            with open('missionRecords4.csv', 'w', newline = '') as f:
                writer = csv.writer(f)
                writer.writerow(header)
            # Open file That saves new record each time
        else:
            pass
            #

        if self.select == 1:
            self.crit1 = self.scale1.get()
            self.crit2 = self.scale2.get()
            self.crit3 = self.scale3.get()
            self.crit4 = self.scale4.get()
            self.crit5 = self.scale5.get()
            self.crit6 = self.scale6.get()
            self.crit7 = self.scale7.get()
            self.crit8 = self.scale8.get()
            self.crit9 = self.scale9.get()
            self.crit10 = self.scale10.get()

            # save upload onto google classroom
            self.googCheck = self.GclassCheck.get()
            self.teachSave = self.teachCheck.get()
            self.quizSave = self.QuizCheck.get()
            self.critSave = self.CritCheck.get()
            self.officerSave = self.CC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)

            # Add up all the points of all the crits
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator() # Should yield both the type of the planet as well as the name
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn2.configure(state = NORMAL)

        elif self.select == 2:
            self.crit1 = self.TwoScale1.get()
            self.crit2 = self.TwoScale2.get()
            self.crit3 = self.TwoScale3.get()
            self.crit4 = self.TwoScale4.get()
            self.crit5 = self.TwoScale5.get()
            self.crit6 = self.TwoScale6.get()
            self.crit7 = self.TwoScale7.get()
            self.crit8 = self.TwoScale8.get()
            self.crit9 = self.TwoScale9.get()
            self.crit10 = self.TwoScale10.get()

            # save upload onto google classroom
            self.googCheck = self.TwoGClassCheck.get()
            self.teachSave = self.TwoTeachCheck.get()
            self.quizSave = self.TwoQuizCheck.get()
            self.critSave = self.TwoCritCheck.get()
            self.officerSave = self.TwoCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)

            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator() # Should yield both the type of the planet as well as the name
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn3.configure(state = NORMAL)

        elif self.select == 3:
            self.crit1 = self.ThreeScale1.get()
            self.crit2 = self.ThreeScale2.get()
            self.crit3 = self.ThreeScale3.get()
            self.crit4 = self.ThreeScale4.get()
            self.crit5 = self.ThreeScale5.get()
            self.crit6 = self.ThreeScale6.get()
            self.crit7 = self.ThreeScale7.get()
            self.crit8 = self.ThreeScale8.get()
            self.crit9 = self.ThreeScale9.get()
            self.crit10 = self.ThreeScale10.get()

            # save upload onto google classroom
            self.googCheck = self.ThreeGClassCheck.get()
            self.teachSave = self.ThreeTeachCheck.get()
            self.quizSave = self.ThreeQuizCheck.get()
            self.critSave = self.ThreeCritCheck.get()
            self.officerSave = self.ThreeCC_Officers.get()
            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)

            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn4.configure(state = NORMAL)

        elif self.select == 4:
            self.crit1 = self.FourScale1.get()
            self.crit2 = self.FourScale2.get()
            self.crit3 = self.FourScale3.get()
            self.crit4 = self.FourScale4.get()
            self.crit5 = self.FourScale5.get()
            self.crit6 = self.FourScale6.get()
            self.crit7 = self.FourScale7.get()
            self.crit8 = self.FourScale8.get()
            self.crit9 = self.FourScale9.get()
            self.crit10 = self.FourScale10.get()

            # save upload onto google classroom
            self.googCheck = self.FourGClassCheck.get()
            self.teachSave = self.FourTeachCheck.get()
            self.quizSave = self.FourQuizCheck.get()
            self.critSave = self.FourCritCheck.get()
            self.officerSave = self.FourCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)

            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn5.configure(state=NORMAL)

        elif self.select == 5:
            self.crit1 = self.FiveScale1.get()
            self.crit2 = self.FiveScale2.get()
            self.crit3 = self.FiveScale3.get()
            self.crit4 = self.FiveScale4.get()
            self.crit5 = self.FiveScale5.get()
            self.crit6 = self.FiveScale6.get()
            self.crit7 = self.FiveScale7.get()
            self.crit8 = self.FiveScale8.get()
            self.crit9 = self.FiveScale9.get()
            self.crit10 = self.FiveScale10.get()

            # save upload onto google classroom
            self.googCheck = self.FiveGClassCheck.get()
            self.teachSave = self.FiveTeachCheck.get()
            self.quizSave = self.FiveQuizCheck.get()
            self.critSave = self.FiveCritCheck.get()
            self.officerSave = self.FiveCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)

            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn6.configure(state=NORMAL)

        elif self.select == 6:
            self.crit1 = self.SixScale1.get()
            self.crit2 = self.SixScale2.get()
            self.crit3 = self.SixScale3.get()
            self.crit4 = self.SixScale4.get()
            self.crit5 = self.SixScale5.get()
            self.crit6 = self.SixScale6.get()
            self.crit7 = self.SixScale7.get()
            self.crit8 = self.SixScale8.get()
            self.crit9 = self.SixScale9.get()
            self.crit10 = self.SixScale10.get()
            # save upload onto google classroom
            self.googCheck = self.SixGClassCheck.get()
            self.teachSave = self.SixTeachCheck.get()
            self.quizSave = self.SixQuizCheck.get()
            self.critSave = self.SixCritCheck.get()
            self.officerSave = self.SixCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)

            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10
            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn7.configure(state=NORMAL)

        elif self.select == 7:
            self.crit1 = self.SevenScale1.get()
            self.crit2 = self.SevenScale2.get()
            self.crit3 = self.SevenScale3.get()
            self.crit4 = self.SevenScale4.get()
            self.crit5 = self.SevenScale5.get()
            self.crit6 = self.SevenScale6.get()
            self.crit7 = self.SevenScale7.get()
            self.crit8 = self.SevenScale8.get()
            self.crit9 = self.SevenScale9.get()
            self.crit10 = self.SevenScale10.get()

            # save upload onto google classroom
            self.googCheck = self.SevenGClassCheck.get()
            self.teachSave = self.SevenTeachCheck.get()
            self.quizSave = self.SevenQuizCheck.get()
            self.critSave = self.SevenCritCheck.get()
            self.officerSave = self.SevenCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10
            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn8.configure(state=NORMAL)

        elif self.select == 8:
            self.crit1 = self.EightScale1.get()
            self.crit2 = self.EightScale2.get()
            self.crit3 = self.EightScale3.get()
            self.crit4 = self.EightScale4.get()
            self.crit5 = self.EightScale5.get()
            self.crit6 = self.EightScale6.get()
            self.crit7 = self.EightScale7.get()
            self.crit8 = self.EightScale8.get()
            self.crit9 = self.EightScale9.get()
            self.crit10 = self.EightScale10.get()

            # save upload onto google classroom
            self.googCheck = self.EightGClassCheck.get()
            self.teachSave = self.EightTeachCheck.get()
            self.quizSave = self.EightQuizCheck.get()
            self.critSave = self.EightCritCheck.get()
            self.officerSave = self.EightCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10
            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn9.configure(state=NORMAL)

        elif self.select == 9:
            self.crit1 = self.NineScale1.get()
            self.crit2 = self.NineScale2.get()
            self.crit3 = self.NineScale3.get()
            self.crit4 = self.NineScale4.get()
            self.crit5 = self.NineScale5.get()
            self.crit6 = self.NineScale6.get()
            self.crit7 = self.NineScale7.get()
            self.crit8 = self.NineScale8.get()
            self.crit9 = self.NineScale9.get()
            self.crit10 = self.NineScale10.get()

            # save upload onto google classroom
            self.googCheck = self.NineGClassCheck.get()
            self.teachSave = self.NineTeachCheck.get()
            self.quizSave = self.NineQuizCheck.get()
            self.critSave = self.NineCritCheck.get()
            self.officerSave = self.NineCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10
            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn10.configure(state=NORMAL)

        elif self.select == 10:
            self.crit1 = self.TenScale1.get()
            self.crit2 = self.TenScale2.get()
            self.crit3 = self.TenScale3.get()
            self.crit4 = self.TenScale4.get()
            self.crit5 = self.TenScale5.get()
            self.crit6 = self.TenScale6.get()
            self.crit7 = self.TenScale7.get()
            self.crit8 = self.TenScale8.get()
            self.crit9 = self.TenScale9.get()
            self.crit10 = self.TenScale10.get()

            # save upload onto google classroom
            self.googCheck = self.TenGClassCheck.get()
            self.teachSave = self.TenTeachCheck.get()
            self.quizSave = self.TenQuizCheck.get()
            self.critSave = self.TenCritCheck.get()
            self.officerSave = self.TenCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10
            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn11.configure(state=NORMAL)

        elif self.select == 11:
            self.crit1 = self.ElevenScale1.get()
            self.crit2 = self.ElevenScale2.get()
            self.crit3 = self.ElevenScale3.get()
            self.crit4 = self.ElevenScale4.get()
            self.crit5 = self.ElevenScale5.get()
            self.crit6 = self.ElevenScale6.get()
            self.crit7 = self.ElevenScale7.get()
            self.crit8 = self.ElevenScale8.get()
            self.crit9 = self.ElevenScale9.get()
            self.crit10 = self.ElevenScale10.get()

            # save upload onto google classroom
            self.googCheck = self.ElevenGClassCheck.get()
            self.teachSave = self.ElevenTeachCheck.get()
            self.quizSave = self.ElevenQuizCheck.get()
            self.critSave = self.ElevenCritCheck.get()
            self.officerSave = self.ElevenCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10
            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn12.configure(state=NORMAL)

        elif self.select == 12:
            self.crit1 = self.TwelveScale1.get()
            self.crit2 = self.TwelveScale2.get()
            self.crit3 = self.TwelveScale3.get()
            self.crit4 = self.TwelveScale4.get()
            self.crit5 = self.TwelveScale5.get()
            self.crit6 = self.TwelveScale6.get()
            self.crit7 = self.TwelveScale7.get()
            self.crit8 = self.TwelveScale8.get()
            self.crit9 = self.TwelveScale9.get()
            self.crit10 = self.TwelveScale10.get()

            # save upload onto google classroom
            self.googCheck = self.TwelveGClassCheck.get()
            self.teachSave = self.TwelveTeachCheck.get()
            self.quizSave = self.TwelveQuizCheck.get()
            self.critSave = self.TwelveCritCheck.get()
            self.officerSave = self.TwelveCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10
            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn13.configure(state=NORMAL)

        elif self.select == 13:
            self.crit1 = self.ThirteenScale1.get()
            self.crit2 = self.ThirteenScale2.get()
            self.crit3 = self.ThirteenScale3.get()
            self.crit4 = self.ThirteenScale4.get()
            self.crit5 = self.ThirteenScale5.get()
            self.crit6 = self.ThirteenScale6.get()
            self.crit7 = self.ThirteenScale7.get()
            self.crit8 = self.ThirteenScale8.get()
            self.crit9 = self.ThirteenScale9.get()
            self.crit10 = self.ThirteenScale10.get()


            # save upload onto google classroom
            self.googCheck = self.ThirteenGClassCheck.get()
            self.teachSave = self.ThirteenTeachCheck.get()
            self.quizSave = self.ThirteenQuizCheck.get()
            self.critSave = self.ThirteenCritCheck.get()
            self.officerSave = self.ThirteenCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)

            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn14.configure(state=NORMAL)

        elif self.select == 14:
            self.crit1 = self.FourteenScale1.get()
            self.crit2 = self.FourteenScale2.get()
            self.crit3 = self.FourteenScale3.get()
            self.crit4 = self.FourteenScale4.get()
            self.crit5 = self.FourteenScale5.get()
            self.crit6 = self.FourteenScale6.get()
            self.crit7 = self.FourteenScale7.get()
            self.crit8 = self.FourteenScale8.get()
            self.crit9 = self.FourteenScale9.get()
            self.crit10 = self.FourteenScale10.get()

            # save upload onto google classroom
            self.googCheck = self.FourteenGClassCheck.get()
            self.teachSave = self.FourteenTeachCheck.get()
            self.quizSave = self.FourteenQuizCheck.get()
            self.critSave = self.FourteenCritCheck.get()
            self.officerSave = self.FourteenCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn15.configure(state=NORMAL)

        elif self.select == 15:
            self.crit1 = self.FifteenScale1.get()
            self.crit2 = self.FifteenScale2.get()
            self.crit3 = self.FifteenScale3.get()
            self.crit4 = self.FifteenScale4.get()
            self.crit5 = self.FifteenScale5.get()
            self.crit6 = self.FifteenScale6.get()
            self.crit7 = self.FifteenScale7.get()
            self.crit8 = self.FifteenScale8.get()
            self.crit9 = self.FifteenScale9.get()
            self.crit10 = self.FifteenScale10.get()

            # save upload onto google classroom
            self.googCheck = self.FifteenGClassCheck.get()
            self.teachSave = self.FifteenTeachCheck.get()
            self.quizSave = self.FifteenQuizCheck.get()
            self.critSave = self.FifteenCritCheck.get()
            self.officerSave = self.FifteenCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn16.configure(state=NORMAL)

        elif self.select == 16:
            self.crit1 = self.SixteenScale1.get()
            self.crit2 = self.SixteenScale2.get()
            self.crit3 = self.SixteenScale3.get()
            self.crit4 = self.SixteenScale4.get()
            self.crit5 = self.SixteenScale5.get()
            self.crit6 = self.SixteenScale6.get()
            self.crit7 = self.SixteenScale7.get()
            self.crit8 = self.SixteenScale8.get()
            self.crit9 = self.SixteenScale9.get()
            self.crit10 = self.SixteenScale10.get()

            # save upload onto google classroom
            self.googCheck = self.SixteenGClassCheck.get()
            self.teachSave = self.SixteenTeachCheck.get()
            self.quizSave = self.SixteenQuizCheck.get()
            self.critSave = self.SixteenCritCheck.get()
            self.officerSave = self.SixteenCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn17.configure(state=NORMAL)

        elif self.select == 17:
            self.crit1 = self.SeventeenScale1.get()
            self.crit2 = self.SeventeenScale2.get()
            self.crit3 = self.SeventeenScale3.get()
            self.crit4 = self.SeventeenScale4.get()
            self.crit5 = self.SeventeenScale5.get()
            self.crit6 = self.SeventeenScale6.get()
            self.crit7 = self.SeventeenScale7.get()
            self.crit8 = self.SeventeenScale8.get()
            self.crit9 = self.SeventeenScale9.get()
            self.crit10 = self.SeventeenScale10.get()

            # save upload onto google classroom
            self.googCheck = self.SeventeenGClassCheck.get()
            self.teachSave = self.SeventeenTeachCheck.get()
            self.quizSave = self.SeventeenQuizCheck.get()
            self.critSave = self.SeventeenCritCheck.get()
            self.officerSave = self.SeventeenCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn18.configure(state=NORMAL)

        elif self.select == 18:
            self.crit1 = self.EighteenScale1.get()
            self.crit2 = self.EighteenScale2.get()
            self.crit3 = self.EighteenScale3.get()
            self.crit4 = self.EighteenScale4.get()
            self.crit5 = self.EighteenScale5.get()
            self.crit6 = self.EighteenScale6.get()
            self.crit7 = self.EighteenScale7.get()
            self.crit8 = self.EighteenScale8.get()
            self.crit9 = self.EighteenScale9.get()
            self.crit10 = self.EighteenScale10.get()

            # save upload onto google classroom
            self.googCheck = self.EighteenGClassCheck.get()
            self.teachSave = self.EighteenTeachCheck.get()
            self.quizSave = self.EighteenQuizCheck.get()
            self.critSave = self.EighteenCritCheck.get()
            self.officerSave = self.EighteenCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn19.configure(state=NORMAL)

        elif self.select == 19:
            self.crit1 = self.NineteenScale1.get()
            self.crit2 = self.NineteenScale2.get()
            self.crit3 = self.NineteenScale3.get()
            self.crit4 = self.NineteenScale4.get()
            self.crit5 = self.NineteenScale5.get()
            self.crit6 = self.NineteenScale6.get()
            self.crit7 = self.NineteenScale7.get()
            self.crit8 = self.NineteenScale8.get()
            self.crit9 = self.NineteenScale9.get()
            self.crit10 = self.NineteenScale10.get()

            # save upload onto google classroom
            self.googCheck = self.NineteenGClassCheck.get()
            self.teachSave = self.NineteenTeachCheck.get()
            self.quizSave = self.NineteenQuizCheck.get()
            self.critSave = self.NineteenCritCheck.get()
            self.officerSave = self.NineteenCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn20.configure(state=NORMAL)

        elif self.select == 20:
            self.crit1 = self.TwentyScale1.get()
            self.crit2 = self.TwentyScale2.get()
            self.crit3 = self.TwentyScale3.get()
            self.crit4 = self.TwentyScale4.get()
            self.crit5 = self.TwentyScale5.get()
            self.crit6 = self.TwentyScale6.get()
            self.crit7 = self.TwentyScale7.get()
            self.crit8 = self.TwentyScale8.get()
            self.crit9 = self.TwentyScale9.get()
            self.crit10 = self.TwentyScale10.get()

            # save upload onto google classroom
            self.googCheck = self.TwentyGClassCheck.get()
            self.teachSave = self.TwentyTeachCheck.get()
            self.quizSave = self.TwentyQuizCheck.get()
            self.critSave = self.TwentyCritCheck.get()
            self.officerSave = self.TwentyCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn21.configure(state=NORMAL)

        elif self.select == 21:
            self.crit1 = self.TwentyOneScale1.get()
            self.crit2 = self.TwentyOneScale2.get()
            self.crit3 = self.TwentyOneScale3.get()
            self.crit4 = self.TwentyOneScale4.get()
            self.crit5 = self.TwentyOneScale5.get()
            self.crit6 = self.TwentyOneScale6.get()
            self.crit7 = self.TwentyOneScale7.get()
            self.crit8 = self.TwentyOneScale8.get()
            self.crit9 = self.TwentyOneScale9.get()
            self.crit10 = self.TwentyOneScale10.get()

            # save upload onto google classroom
            self.googCheck = self.TwentyOneGClassCheck.get()
            self.teachSave = self.TwentyOneTeachCheck.get()
            self.quizSave = self.TwentyOneQuizCheck.get()
            self.critSave = self.TwentyOneCritCheck.get()
            self.officerSave = self.TwentyOneCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn22.configure(state=NORMAL)

        elif self.select == 22:
            self.crit1 = self.TwentyTwoScale1.get()
            self.crit2 = self.TwentyTwoScale2.get()
            self.crit3 = self.TwentyTwoScale3.get()
            self.crit4 = self.TwentyTwoScale4.get()
            self.crit5 = self.TwentyTwoScale5.get()
            self.crit6 = self.TwentyTwoScale6.get()
            self.crit7 = self.TwentyTwoScale7.get()
            self.crit8 = self.TwentyTwoScale8.get()
            self.crit9 = self.TwentyTwoScale9.get()
            self.crit10 = self.TwentyTwoScale10.get()

            # save upload onto google classroom
            self.googCheck = self.TwentyTwoGClassCheck.get()
            self.teachSave = self.TwentyTwoTeachCheck.get()
            self.quizSave = self.TwentyTwoQuizCheck.get()
            self.critSave = self.TwentyTwoCritCheck.get()
            self.officerSave = self.TwentyTwoCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn23.configure(state=NORMAL)

        elif self.select == 23:
            self.crit1 = self.TwentyThreeScale1.get()
            self.crit2 = self.TwentyThreeScale2.get()
            self.crit3 = self.TwentyThreeScale3.get()
            self.crit4 = self.TwentyThreeScale4.get()
            self.crit5 = self.TwentyThreeScale5.get()
            self.crit6 = self.TwentyThreeScale6.get()
            self.crit7 = self.TwentyThreeScale7.get()
            self.crit8 = self.TwentyThreeScale8.get()
            self.crit9 = self.TwentyThreeScale9.get()
            self.crit10 = self.TwentyThreeScale10.get()

            # save upload onto google classroom
            self.googCheck = self.TwentyThreeGClassCheck.get()
            self.teachSave = self.TwentyThreeTeachCheck.get()
            self.quizSave = self.TwentyThreeQuizCheck.get()
            self.critSave = self.TwentyThreeCritCheck.get()
            self.officerSave = self.TwentyThreeCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)

            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

            self.Miss1_RBtn24.configure(state=NORMAL)
        elif self.select == 24:
            self.crit1 = self.TwentyFourScale1.get()
            self.crit2 = self.TwentyFourScale2.get()
            self.crit3 = self.TwentyFourScale3.get()
            self.crit4 = self.TwentyFourScale4.get()
            self.crit5 = self.TwentyFourScale5.get()
            self.crit6 = self.TwentyFourScale6.get()
            self.crit7 = self.TwentyFourScale7.get()
            self.crit8 = self.TwentyFourScale8.get()
            self.crit9 = self.TwentyFourScale9.get()
            self.crit10 = self.TwentyFourScale10.get()

            # save upload onto google classroom
            self.googCheck = self.TwentyFourGClassCheck.get()
            self.teachSave = self.TwentyFourTeachCheck.get()
            self.quizSave = self.TwentyFourQuizCheck.get()
            self.critSave = self.TwentyFourCritCheck.get()
            self.officerSave = self.TwentyFourCC_Officers.get()

            # get the notes
            self.notesSave = self.notesEntry1A.get('1.0', END)
            total = self.crit1 + self.crit2 + self.crit3 + self.crit4 + self.crit5 + \
                    self.crit6 + self.crit7 + self.crit8 + self.crit9 + self.crit10

            if total >= 41:
                self.leftMiss.configure(state=NORMAL)
                self.planet_generator()
                self.MissPlanetAcquired = True
                self.MissPlanetName = self.return_planet
                self.MissPlanetType = self.planet_type
            else:
                self.MissPlanetAcquired = False
                self.MissPlanetName = 'None'
                self.MissPlanetType = 'None'

        data = [str(self.student1), str(self.select), str(self.date), str(self.crit1),
                str(self.crit2), str(self.crit3), str(self.crit4), str(self.crit5),
                str(self.crit6),str(self.crit7),str(self.crit8),str(self.crit9),str(self.crit10),
                str(self.googCheck), str(self.teachSave), str(self.quizSave),
                str(self.critSave), str(self.officerSave), str(self.notesSave),
                str(self.MissPlanetAcquired), str(self.MissPlanetName), str(self.MissPlanetType)]

        # Close all of the records
        with open('missionRecords4.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)

        self.btnSaveOne.configure(state = DISABLED)

    def show_spider(self, a, b, c, d, e, f, g, h, i, j):
        # Create Spider Plot#######################################
        subjects = ['', '', '', '', '', '', '', '', '','']
        alice = [a, b, c, d, e, f, g, h, i, j]
        print(alice)
        angles = np.linspace(0, 2 * np.pi, len(subjects), endpoint=False)
        angles = np.concatenate((angles, [angles[0]]))
        subjects.append(subjects[0])
        alice.append(alice[0])
        self.fig = plt2.figure(figsize=(6, 6), facecolor='black')
        self.ax = self.fig.add_subplot(polar=True)
        self.ax.plot(angles, alice, 'o--', color='g', label='Alice',
                     markerfacecolor='g', markeredgecolor='g')
        self.ax.set_facecolor('black')
        self.ax.text(0.09, 0.15, 'Innov.',
                    verticalalignment='bottom', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(0.40, -0.067, 'Struct.',
                    verticalalignment='bottom', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(0.75, -0.08, 'Simpl.',
                    verticalalignment='bottom', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(1.0748, .135, 'Deliv.',
                    verticalalignment='bottom', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(1.18, 0.47, 'Conc.',
                    verticalalignment='top', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(1.09, 0.82, 'Cont.',
                    verticalalignment='top', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(0.80, 1.06, 'Reada.',
                    verticalalignment='top', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(0.355, 1.05, 'Origin.',
                    verticalalignment='top', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(0.09, .86, 'Quala.',
                    verticalalignment='top', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')
        self.ax.text(-0.01,.47, 'Lang.',
                    verticalalignment='top', horizontalalignment='right',
                    transform= self.ax.transAxes,
                    color = 'white')

        COLOR = 'green'
        spider = FigureCanvasTkAgg(self.fig, self.planet_canv)
        spider.get_tk_widget().pack(side=LEFT, fill=BOTH)
        # fill plot
        self.ax.fill(angles, alice, alpha=0.25, color='g')
        # Add labels
        self.ax.set_thetagrids(angles * 180 / np.pi, subjects)
        #########################################################

    def disp_officer(self, off):
        if off == 'Lannon Khau':
            self.officer_img1 = ImageTk.PhotoImage(Image.open('images/spaceforce2A.png.'))
            self.officerCanv.create_image(-25, 132,
                                          anchor=W,
                                          image=self.officer_img1)
        elif off == 'Benny Chiu':
            self.officer_img1 = ImageTk.PhotoImage(Image.open('images/spaceforce3.png.'))
            self.officerCanv.create_image(-5, 112,
                                          anchor=W,
                                          image=self.officer_img1)
        elif off == 'Fernando Galvez':
            self.officer_img1 = ImageTk.PhotoImage(Image.open('images/spaceforce4.png.'))
            self.officerCanv.create_image(-5, 112,
                                          anchor=W,
                                          image=self.officer_img1)
        elif off == 'Joshua Sanchez':
            self.officer_img1 = ImageTk.PhotoImage(Image.open('images/spaceforce5.png.'))
            self.officerCanv.create_image(-5, 112,
                                          anchor=W,
                                          image=self.officer_img1)
        else:
            self.officer_img1 = ImageTk.PhotoImage(Image.open('images/rank_high_18.png.'))
            self.officerCanv.create_image(100, 112,
                                          anchor=W,
                                          image=self.officer_img1)

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    def open_picfile(self):
        filename = filedialog.askopenfilename()
        print(filename)
        #########################
        self.pic_name = filename.split('/')
        self.pic_name2 = self.pic_name[-1]
        self.pic_split = self.pic_name2.split('.')
        self.pic_name = self.pic_split[0]
        self.pic_file = self.pic_split[1]

        # Save the pic file first
        # creating a image object (main image)
        im1 = Image.open(f"{filename}")

        # save a image using extension
        im1 = im1.save(f"images/{self.pic_name2}")
        #########################
        try:
            print('Selected:', self.pic_name2)

            # reading the csv file
            df = pd.read_csv("studentRegister.csv")

            # updating the column value/data
            df.loc[0, 'Profile pic name'] = self.pic_name2

            # writing into the file
            df.to_csv("studentRegister.csv", index=False)

            print(df)

            img = Image.open(f'images/{self.pic_name2}')
            img2 = img.resize((250, 220))

            self.prof_img = ImageTk.PhotoImage(img2)
            self.profCanv.create_image(0, 95, anchor=W, image=self.prof_img)

            if filename is not None:
                pass
        except:
            pass

    def planet_generator(self):
        random_planet = random.randint(1, 36)
        if 1 <= random_planet <= 15:
            planets = ['common_planet_1','common_planet_2','common_planet_3']
            self.return_planet = random.choice(planets)
            self.planet_type = 'Common Planet'
        elif 16 <= random_planet <= 25:
            planets = ['rare_planet_2','rare_planet_3','rare_planet_4']
            self.return_planet = random.choice(planets)
            self.planet_type = 'Rare Planet'
        elif 26 <= random_planet <= 30:
            planets = ['ultra_rare_planet1','ultra_rare_planet2']
            self.return_planet = random.choice(planets)
            self.planet_type = 'Ultra Rare Planet'
        elif 31 <= random_planet <= 35:
            planets = ['hyper_rare_planet1','hyper_rare_planet2','hyper_rare_planet3']
            self.return_planet = random.choice(planets)
            self.planet_type = 'Hyper Rare Planet'
        else:
            planets = ['god_tier_planet']
            self.return_planet = random.choice(planets)
            self.planet_type = 'God Tier Planet'

        return self.return_planet, self.planet_type

    def letterGrade(self):
        self.get_avail_scores()
        if self.grand_avail_total == 0:
            self.grand_avail_total = 1
        if self.grand_avail_total_present == 0:
            self.grand_avail_total_present = 1

        score = (((0.25 * (self.total_points_earned / self.grand_avail_total)) * 100) + \
                 ((0.25 * (self.total_points_earned_present / self.grand_avail_total_present)) * 100) + \
                 (25) + (25))

        print(score)

        if (score >= 97):
            self.letter_grade = 'A+'
        elif (93 <= score < 97):
            self.letter_grade = 'A'
        elif (90 <= score < 93):
            self.letter_grade = 'A-'
        elif (87 <= score < 90):
            self.letter_grade = 'B+'
        elif (83 <= score < 87):
            self.letter_grade = 'B'
        elif (80 <= score < 83):
            self.letter_grade = 'B-'
        elif (77 <= score < 80):
            self.letter_grade = 'C+'
        elif (73 <= score < 77):
            self.letter_grade = 'C'
        elif (70 <= score < 73):
            self.letter_grade = 'C-'
        elif (67 <= score < 70):
            self.letter_grade = 'D+'
        elif (63 <= score < 67):
            self.letter_grade = 'D'
        elif (60 <= score < 63):
            self.letter_grade = 'D-'
        elif (57 <= score < 60):
            self.letter_grade = 'F+'
        elif (53 <= score < 57):
            self.letter_grade = 'F'
        else:
            self.letter_grade = 'X'

        self.letterPercent = round(score,1)
        print(self.letter_grade, self.letterPercent)
        return self.letter_grade, self.letterPercent

    def refresh(self):
        self.get_avail_scores()
        file_exists = os.path.exists('missionRecords4.csv')
        if not file_exists:
            pass
        else:
            if self.loginBool == True:
                # Opening the .csv file and loading the information
                # onto a pandas dataframe
                #self.rightFrame1A.remove(self.dataCanv)
                self.rightFrame2.remove(self.dataCanv3)
                self.rightFrame2.remove(self.dataCanv4)
                self.dataCanv.pack_forget()
                self.dataCanv2.pack_forget()
                self.dataCanv3.pack_forget()
                self.dataCanv4.pack_forget()
                #self.distCanv.pack_forget()

                load_data = pd.read_csv("missionRecords4.csv")
                df = pd.DataFrame(load_data)
                print(len(df['Mission No.']))
                max_num = max(df['Mission No.'])

                appl = []
                read = []
                qual = []
                create = []
                clean = []
                cont = []
                origin = []
                body = []
                struct = []
                deliv = []

                for x in range(1, max_num + 1):
                    cellA = df.loc[df['Mission No.'] == x]['Application']
                    appl.append(cellA.iloc[-1])
                    cellB = df.loc[df['Mission No.'] == x]['Readability']
                    read.append(cellB.iloc[-1])
                    cellC = df.loc[df['Mission No.'] == x]['Quality']
                    qual.append(cellC.iloc[-1])
                    cellD = df.loc[df['Mission No.'] == x]['Creativity']
                    create.append(cellD.iloc[-1])
                    cellE = df.loc[df['Mission No.'] == x]['Cleanliness']
                    clean.append(cellE.iloc[-1])
                    cellF = df.loc[df['Mission No.'] == x]['Content']
                    cont.append(cellF.iloc[-1])
                    cellG = df.loc[df['Mission No.'] == x]['Originality']
                    origin.append(cellG.iloc[-1])
                    cellH = df.loc[df['Mission No.'] == x]['Body Language']
                    body.append(cellH.iloc[-1])
                    cellI = df.loc[df['Mission No.'] == x]['Structure']
                    struct.append(cellI.iloc[-1])
                    cellJ = df.loc[df['Mission No.'] == x]['Delivery']
                    deliv.append(cellJ.iloc[-1])

                appl = (sum(appl))
                read = (sum(read))
                qual = (sum(qual))
                create = (sum(create))
                clean = (sum(clean))
                cont = (sum(cont))
                origin = (sum(origin))
                body = (sum(body))
                struct = (sum(struct))
                deliv = (sum(deliv))

                print(appl, read, qual, create, clean, cont, origin, body, struct, deliv)

                self.dataCanv = Canvas(self.rightFrame1A, width=50, height=170, bg = '#a9a9a9',
                                       highlightbackground = '#a9a9a9')
                self.dataCanv.pack(side=LEFT)

                self.dataCanv2 = Canvas(self.rightFrame1C, width=200, height=370, bg = '#a9a9a9',
                                        highlightbackground = '#a9a9a9')
                self.dataCanv2.pack(side=RIGHT)

                # self.distCanv = Canvas(self.rightFrame1B, width=200, height=370, bg = '#a9a9a9',
                #                         highlightbackground = '#a9a9a9')
                # self.distCanv.pack(side=RIGHT)

                self.get_avail_scores()

                self.availPointsProjects = self.total_points_earned
                self.totalPointsProjects = self.grand_avail_total
                self.progressProjects['value'] = (self.availPointsProjects / self.totalPointsProjects) * 100
                self.lblPBProjects.configure(text = 'Mission Objectives Score:' + f'{self.availPointsProjects}/{self.totalPointsProjects}')

                self.availPointsProjects = self.total_points_earned_present
                self.totalPointsProjects = self.grand_avail_total_present
                self.progressPart['value'] = (self.availPointsProjects / self.totalPointsProjects) * 100
                self.lblPBPart.configure(text = 'Presentation Score:' + f'{self.availPointsProjects}/{self.totalPointsProjects}')

                self.availPointsTotal = (self.total_points_earned + self.total_points_earned_present)
                self.totalPointsGrand = (self.grand_avail_total + self.grand_avail_total_present)
                self.progressTotalScore['value'] = (self.availPointsTotal / self.totalPointsGrand) * 100
                self.lblPBTotalScore.configure(text='Total Score: ' + f'{self.availPointsTotal}/{self.totalPointsGrand}')

                self.letterGrade()
                self.letterCanv.delete(self.canvText)
                self.letterCanv.delete(self.canvText2)

                self.canvText = self.letterCanv.create_text(67, 47, text=self.letter_grade, font='Helvetica 30 bold')
                self.letterCanv.create_line(28, 75, 106, 75, fill="black", width=5)
                self.canvText2 = self.letterCanv.create_text(67, 105, text=str(self.letterPercent) + '%',
                                                             font='Helvetica 25 bold')

                self.dataCanv3 = Canvas(self.rightFrame2, width=100, height=470, bg='#a9a9a9',
                                        highlightbackground='#a9a9a9')
                self.rightFrame2.add(self.dataCanv3)
                self.rightFrame2.config(opaqueresize=False)

                self.dataCanv4 = Canvas(self.rightFrame2, width=100, height=470, bg='#a9a9a9',
                                        highlightbackground='#a9a9a9')
                self.rightFrame2.add(self.dataCanv4)
                self.rightFrame2.config(opaqueresize=False, sashpad=10, sashrelief=RAISED,
                                               sashwidth=5, showhandle=True)
                self.rightFrame2.sash_place(0,0,0)
                self.root.update()

                self.show_spiderB(appl, read, qual, create, clean, cont, origin, body, struct, deliv)
                #self.show_bar(appl, read, qual, create, clean, cont, origin, body, struct, deliv)
                self.show_bar2()
                self.show_bar3()
                self.show_pie()
                #self.show_dist()
            else:
                pass

    def show_spiderB(self, a, b, c, d, e, f, g, h, i, j):
        # Create Spider Plot#######################################
        subjects = ['App.', 'Reada.', 'Quala.', 'Innov.', 'Simpl.', 'Cont.','Origin.','BodyL.','Struct.','Deliv.']
        alice = [a, b, c, d, e, f, g, h, i, j]
        print(alice)
        angles = np.linspace(0, 2 * np.pi, len(subjects), endpoint=False)
        angles = np.concatenate((angles, [angles[0]]))
        subjects.append(subjects[0])
        alice.append(alice[0])
        self.fig = plt2.figure(figsize=(5, 6), facecolor='darkgrey')
        ax = self.fig.add_subplot(polar=True)
        ax.plot(angles, alice, 'o-', color='white', label='Alice',
                     markerfacecolor='white', markeredgecolor='white')
        ax.set_facecolor('dimgrey')
        #self.dataCanv.update_idletasks()
        spider = FigureCanvasTkAgg(self.fig, self.dataCanv)

        spider.get_tk_widget().pack(side=LEFT)
        # fill plot
        ax.fill(angles, alice, alpha=0.25, color='blue')
        # Add labels
        ax.set_thetagrids(angles * 180 / np.pi, subjects)

    def show_bar(self, a, b, c, d, e, f, g, h, i, j):
        sns.set(style = 'darkgrid')
        # Formatting the data into a dictionary
        # 2 Keys: 2 Values as Lists that contain 5 points.
        data = {"": ['App.', 'Rea.', 'Qua.', 'Inn.', 'Cle.', 'Con.','Ori.','Bod.','Str.','Del.'],
                "Total Points Earned / Criteria": [a, b, c, d, e, f, g, h, i, j]}
        # Dictionary loaded into a DataFrame
        df_dict = pd.DataFrame(data=data)

        self.fig = plt2.figure(facecolor='darkgrey', figsize = (20,4))
        ax = self.fig.add_subplot()

        sns.barplot(x="Total Points Earned / Criteria", y="", data = df_dict,
                    edgecolor = 'white', ax = ax, color = 'white',
                    palette = 'magma_r')
                    #palette = "ch:start=.2,rot=-.3")

        ax.set_facecolor('black')
        #self.dataCanv2.update_idletasks()
        barplot = FigureCanvasTkAgg(self.fig, self.dataCanv2)

        barplot.get_tk_widget().pack()
        # Draw a vertical bar chart where the X values are the criteria names
        # and the Y value is the total points earned scaled to the maximum.

    def get_avail_scores(self):
        load_data = pd.read_csv('missionRecords4.csv')
        df = pd.DataFrame(load_data)

        self.total_points_earned = []
        self.total_points_earned_present = []

        for mission in range(1,24):
            if not (mission in set(df['Mission No.'])):
                a, b, c, d, e, f, g, h, i, j = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            else:
                # This looks for the last row of just that specific mission
                level1_rows = df.loc[df['Mission No.'] == mission]
                last_row = level1_rows.iloc[-1]
                a = last_row['Application']
                b = last_row['Readability']
                c = last_row['Quality']
                d = last_row['Creativity']
                e = last_row['Cleanliness']
                f = last_row['Content']
                g = last_row['Originality']
                h = last_row['Body Language']
                i = last_row['Structure']
                j = last_row['Delivery']

                total_points = [a,b,c,d,e]
                total_points = sum(total_points)
                total_points_present = [f,g,h,i,j]
                total_points_present = sum(total_points_present)
                self.total_points_earned.append(total_points)
                self.total_points_earned_present.append(total_points_present)

        self.grand_avail_total = len(self.total_points_earned) * 25
        self.total_points_earned = sum(self.total_points_earned)

        self.grand_avail_total_present = len(self.total_points_earned_present) * 25
        self.total_points_earned_present = sum(self.total_points_earned_present)

        print(self.total_points_earned, self.grand_avail_total,
              self.total_points_earned_present, self.grand_avail_total_present)
        return self.total_points_earned, self.grand_avail_total, self.total_points_earned_present, self.grand_avail_total_present

    def get_score(self, mission):
        load_data = pd.read_csv('missionRecords4.csv')
        df = pd.DataFrame(load_data)

        if not (mission in set(df['Mission No.'])):
            a, b, c, d, e, = 0, 0, 0, 0, 0
        else:
            level1_rows = df.loc[df['Mission No.'] == mission]
            last_row = level1_rows.iloc[-1]
            a = last_row['Application']
            b = last_row['Readability']
            c = last_row['Quality']
            d = last_row['Creativity']
            e = last_row['Cleanliness']

        tot_points = [a, b, c, d, e]
        return sum(tot_points)

    def show_bar2(self):
        a = self.get_score(1)
        b = self.get_score(2)
        c = self.get_score(3)
        d = self.get_score(4)
        e = self.get_score(5)
        f = self.get_score(6)
        g = self.get_score(7)
        h = self.get_score(8)
        i = self.get_score(9)
        j = self.get_score(10)
        k = self.get_score(11)
        l = self.get_score(12)
        m = self.get_score(13)
        n = self.get_score(14)
        o = self.get_score(15)
        p = self.get_score(16)
        q = self.get_score(17)
        r = self.get_score(18)
        s = self.get_score(19)
        t = self.get_score(20)
        u = self.get_score(21)
        v = self.get_score(22)
        w = self.get_score(23)
        x = self.get_score(24)

        sns.set(style = 'darkgrid')
        # Formatting the data into a dictionary
        # 2 Keys: 2 Values as Lists that contain 5 points.
        data = {"": ['1','2','3','4','5','6','7','8','9','10','11','12',
                             '13','14','15','16','17','18','19','20','21','22','23','24'],
                "Points Per Project": [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x]}
        # Dictionary loaded into a DataFrame
        df_dict = pd.DataFrame(data=data)
        print(df_dict)

        self.fig = plt2.figure(facecolor='darkgrey', figsize = (25,5))
        ax = self.fig.add_subplot()

        sns.barplot(x="", y="Points Per Project", palette = 'magma_r', data = df_dict,
                    edgecolor = 'white', ax = ax)
        ax.set_facecolor('black')
        #self.dataCanv3.update_idletasks()
        barplot = FigureCanvasTkAgg(self.fig, self.dataCanv3)
        barplot.get_tk_widget().pack()

    def get_events(self):
        list_events = []
        with open('events.txt') as file:
            for line in file:
                line = line.rstrip('\n')
                current_event = line.split(',')
                event_date = datetime.strptime(current_event[1], '%m/%d/%y').date()
                current_event[1] = event_date
                list_events.append(current_event)
        return list_events

    def days_between_dates(self, date1, date2):
        time_between = str(date1 - date2)
        number_of_days = time_between.split(' ')
        return number_of_days[0]

    def get_score2(self, mission):
        load_data = pd.read_csv('MissionRecords4.csv')
        df = pd.DataFrame(load_data)

        if not (mission in set(df['Mission No.'])):
            f, g, h, i, j, = 0, 0, 0, 0, 0

        else:
            level1_rows = df.loc[df['Mission No.'] == mission]
            last_row = level1_rows.iloc[-1]
            f = last_row['Content']
            g = last_row['Originality']
            h = last_row['Body Language']
            i = last_row['Structure']
            j = last_row['Delivery']

        tot_points = [f, g, h, i, j]
        return sum(tot_points)

    def show_bar3(self):
        a = self.get_score2(1)
        b = self.get_score2(2)
        c = self.get_score2(3)
        d = self.get_score2(4)
        e = self.get_score2(5)
        f = self.get_score2(6)
        g = self.get_score2(7)
        h = self.get_score2(8)
        i = self.get_score2(9)
        j = self.get_score2(10)
        k = self.get_score2(11)
        l = self.get_score2(12)
        m = self.get_score2(13)
        n = self.get_score2(14)
        o = self.get_score2(15)
        p = self.get_score2(16)
        q = self.get_score2(17)
        r = self.get_score2(18)
        s = self.get_score2(19)
        t = self.get_score2(20)
        u = self.get_score2(21)
        v = self.get_score2(22)
        w = self.get_score2(23)
        x = self.get_score2(24)

        sns.set(style = 'darkgrid')
        # Formatting the data into a dictionary
        # 2 Keys: 2 Values as Lists that contain 5 points.
        data = {"": ['1','2','3','4','5','6','7','8','9','10','11','12',
                             '13','14','15','16','17','18','19','20','21','22','23','24'],
                "Presentation Points / Project": [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x]}
        # Dictionary loaded into a DataFrame
        df_dict = pd.DataFrame(data=data)

        self.fig = plt2.figure(facecolor='darkgrey', figsize = (20,5))
        ax = self.fig.add_subplot()

        sns.barplot(x="", y="Presentation Points / Project", palette = 'magma', data = df_dict,
                    edgecolor = 'white', ax = ax)
        ax.set_facecolor('black')

        barplot = FigureCanvasTkAgg(self.fig, self.dataCanv4)
        barplot.get_tk_widget().pack()

    def register(self):
        reply = messagebox.askyesnocancel('Confirmation', 'Are you sure you want to register?')
        if reply == True:
            try:
                self.registered = True
                self.btnRegister.configure(state = DISABLED)
                messagebox.showinfo('Successful', 'You are now registered with Creative Core!')
                # Take in all the user information details.
                # Just make a new CSV and call it student registration
                studentFirst = self.OneFirst.get()
                studentLast = self.OneLast.get()
                gradeLvl = self.gradeLevel.get()
                studPron = self.studPronoun.get()
                DOB = self.studDOB.get()
                email = self.studEmail.get()
                OS = self.studOS.get()
                GuardName = self.OneGuard.get()
                GuardType = self.OneGuardType.get()
                Phone = self.PGPhone.get()
                PGEm = self.PGEmail.get()
                enroll = self.ClassReg.get()
                username = self.userName.get()
                password = str(self.passWord.get())
                # profile_pic_name = self.pic_name
                # profile_pic_file = self.pic_file

                header = ['Student ID','First Name','Last Name','Grade Level','Pronoun','DOB','Email',
                          'OS','Guardian Name','Guardian Type','Phone','Guardian Email','Enrollment',
                          'Username','Password','Profile pic name', 'Profile pic file']

                data = [random.randint(1,10000), studentFirst, studentLast, gradeLvl, studPron,DOB,
                        email, OS, GuardName, GuardType, Phone, PGEm, enroll, username, password,]
                        #profile_pic_name, profile_pic_file]

                file_exists = os.path.exists('studentRegister.csv')
                if not file_exists:
                    with open('studentRegister.csv', 'w', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(header)
                        writer.writerow(data)
                else:
                    load_data = pd.read_csv("studentRegister.csv")
                    df = pd.DataFrame(load_data)
            except:
                print('Not all the fields have been acquired.')
        else:
            messagebox.showinfo('That\'s Okay!', 'Goodbye, World!')

        # Make up a popup box that Asks "Are You Sure you want to register?"

    def login(self):
        # Just Make another popup box
        self.popup_login = Toplevel(root, bg='#4a4e69', relief = RAISED, bd = 7)
        self.popup_login.geometry("300x400")
        self.popup_login.title("Login")

        logTitleFrame = Frame(self.popup_login, relief = RAISED, width = 300,
                                   height = 50, bd = 5, bg = 'grey25')
        logTitleFrame.propagate(0)
        logTitleFrame.pack(side = TOP)

        self.lblTitle = Label(logTitleFrame, text = 'LOGIN FORM', font = 'consolas 14 bold',
                              fg = 'cornsilk', bg = 'grey25')
        self.lblTitle.pack(pady = (10,10))

        self.userworld = StringVar()
        self.passkey = StringVar()

        self.entUsername = Entry(self.popup_login, width = 15, text = '', font = 'consolas 12',
                                 textvariable = self.userworld)
        self.entUsername.pack(side = TOP, pady = (45,0))

        self.lblUsername = Label(self.popup_login, width = 15, height = 1, text = 'Username',
                                 font = 'consolas 12', bg = '#4a4e69', fg = 'cornsilk')
        self.lblUsername.pack(side = TOP)

        self.entPassword = Entry(self.popup_login, width=15, text='', font='consolas 12',
                                 textvariable = self.passkey, show="*")
        self.entPassword.pack(side=TOP, pady = (25,0))

        self.lblPassword = Label(self.popup_login, width=15, height=1, text='Password',
                                 font='consolas 12', bg = '#4a4e69', fg = 'cornsilk')
        self.lblPassword.pack(side=TOP)

        self.btnLogin = Button(self.popup_login, width = 6, height = 1, text = 'Login',
                               font = 'consolas 12', command = self.btnLog, relief = RAISED,
                               bd = 4)
        self.btnLogin.pack(side = TOP, pady = (40,10))

    def btnLog(self):
        # K that's fine for now. Now we check to see if the Login is the correct Email.
        file_exists = os.path.exists('studentRegister.csv')
        if not file_exists:
            self.lblTitle.configure(text = 'Student Not Registered')
        else:
            load_data = pd.read_csv("studentRegister.csv")
            df = pd.DataFrame(load_data)

            print((df['Password'].item()))

            if (self.userworld.get() in df['Username'].tolist()) and self.passkey.get() == str(df['Password'].item()):
                print('File Found :)')
                self.loginBool = True
                self.SD1_btn.configure(state = NORMAL)
                self.btnLogin1.configure(state=DISABLED)
                self.btnUploadPic.configure(state=NORMAL)
                self.popup_login.destroy()

                try:
                    events = self.get_events()
                    today = date.today()

                    vertical_space = 20
                    events.sort(key=lambda x: x[1])
                    count = 1
                    for event in events:
                        event_name = event[0]
                        days_until = self.days_between_dates(event[1], today)
                        display = f'{count}. {event_name} ➟ {days_until} days'

                        if (int(days_until) <= 3):
                            text_col = 'red'
                        else:
                            text_col = 'black'

                        self.canvTask.create_text(25, vertical_space, anchor='w',
                                                  fill=text_col, font='consolas 12',
                                                  text=display)
                        vertical_space += 18
                        count += 1
                #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                except:
                    self.canvTask.create_text(20, 25, anchor='w',
                                              fill='black', font='consolas 12 bold',
                                              text='Error: Please update events.txt file with future task dates.')


                self.rightFrame2.remove(self.dataCanv4)
                self.rightFrame2.remove(self.dataCanv3)
                self.dataCanv.pack_forget()
                self.dataCanv2.pack_forget()
                self.dataCanv3.pack_forget()
                self.dataCanv4.pack_forget()

                self.show_dist()
                self.show_pie()

                load_data = pd.read_csv("missionRecords4.csv")
                df = pd.DataFrame(load_data)
                print(len(df['Mission No.']))

                if len(df['Mission No.']) > 0:
                    max_num = max(df['Mission No.'])
                    appl = []
                    read = []
                    qual = []
                    create = []
                    clean = []
                    cont = []
                    origin = []
                    body = []
                    struct = []
                    deliv = []

                    for x in range(1, max_num + 1):
                        cellA = df.loc[df['Mission No.'] == x]['Application']
                        appl.append(cellA.iloc[-1])
                        cellB = df.loc[df['Mission No.'] == x]['Readability']
                        read.append(cellB.iloc[-1])
                        cellC = df.loc[df['Mission No.'] == x]['Quality']
                        qual.append(cellC.iloc[-1])
                        cellD = df.loc[df['Mission No.'] == x]['Creativity']
                        create.append(cellD.iloc[-1])
                        cellE = df.loc[df['Mission No.'] == x]['Cleanliness']
                        clean.append(cellE.iloc[-1])
                        cellF = df.loc[df['Mission No.'] == x]['Content']
                        cont.append(cellF.iloc[-1])
                        cellG = df.loc[df['Mission No.'] == x]['Originality']
                        origin.append(cellG.iloc[-1])
                        cellH = df.loc[df['Mission No.'] == x]['Body Language']
                        body.append(cellH.iloc[-1])
                        cellI = df.loc[df['Mission No.'] == x]['Structure']
                        struct.append(cellI.iloc[-1])
                        cellJ = df.loc[df['Mission No.'] == x]['Delivery']
                        deliv.append(cellJ.iloc[-1])

                    appl = (sum(appl))
                    read = (sum(read))
                    qual = (sum(qual))
                    create = (sum(create))
                    clean = (sum(clean))
                    cont = (sum(cont))
                    origin = (sum(origin))
                    body = (sum(body))
                    struct = (sum(struct))
                    deliv = (sum(deliv))

                    print(appl, read, qual, create, clean, cont, origin, body, struct, deliv)

                    self.dataCanv = Canvas(self.rightFrame1A, width=50, height=170, bg='#a9a9a9',
                                           highlightbackground='#a9a9a9')
                    self.dataCanv.pack(side=LEFT)

                    self.dataCanv2 = Canvas(self.rightFrame1C, width=200, height=370, bg='#a9a9a9',
                                            highlightbackground='#a9a9a9')
                    self.dataCanv2.pack(side=RIGHT)

                    self.get_avail_scores()

                    self.availPointsProjects = self.total_points_earned
                    self.totalPointsProjects = self.grand_avail_total
                    self.progressProjects['value'] = (self.availPointsProjects / self.totalPointsProjects) * 100
                    self.lblPBProjects.configure(
                        text='Mission Objectives Score:' + f'{self.availPointsProjects}/{self.totalPointsProjects}')

                    self.availPointsProjects = self.total_points_earned_present
                    self.totalPointsProjects = self.grand_avail_total_present
                    self.progressPart['value'] = (self.availPointsProjects / self.totalPointsProjects) * 100
                    self.lblPBPart.configure(
                        text='Presentation Score:' + f'{self.availPointsProjects}/{self.totalPointsProjects}')

                    self.availPointsTotal = (self.total_points_earned + self.total_points_earned_present)
                    self.totalPointsGrand = (self.grand_avail_total + self.grand_avail_total_present)
                    self.progressTotalScore['value'] = (self.availPointsTotal / self.totalPointsGrand) * 100
                    self.lblPBTotalScore.configure(
                        text='Total Score: ' + f'{self.availPointsTotal}/{self.totalPointsGrand}')

                    self.rightFrame2.propagate(0)
                    self.rightFrame2.pack(side=TOP)

                    self.letterGrade()
                    self.letterCanv.delete(self.canvText)
                    self.letterCanv.delete(self.canvText2)
                    self.canvText = self.letterCanv.create_text(67, 47, text=self.letter_grade, font='Helvetica 30 bold')
                    self.letterCanv.create_line(28, 75, 106, 75, fill="black", width=5)
                    self.canvText2 = self.letterCanv.create_text(67, 105, text=str(self.letterPercent) + '%', font='Helvetica 25 bold')


                    self.dataCanv3 = Canvas(self.rightFrame2, width=100, height=470, bg='#a9a9a9',
                                            highlightbackground='#a9a9a9')
                    self.rightFrame2.add(self.dataCanv3)
                    self.rightFrame2.config(opaqueresize=False)

                    self.dataCanv4 = Canvas(self.rightFrame2, width=100, height=470, bg='#a9a9a9',
                                            highlightbackground='#a9a9a9')
                    self.rightFrame2.add(self.dataCanv4)
                    self.rightFrame2.config(opaqueresize=False, sashpad=10, sashrelief=RAISED,
                                            sashwidth=5, showhandle=True)
                    self.rightFrame2.sash_place(0, 0, 0)
                    self.root.update()

                    self.show_spiderB(appl, read, qual, create, clean, cont, origin, body, struct, deliv)
                    #self.show_bar(appl, read, qual, create, clean, cont, origin, body, struct, deliv)
                    self.show_bar2()
                    self.show_bar3()
                    self.show_pie()

                # Load Everything in the Correct Fields by reading the DF
                load_data = pd.read_csv("studentRegister.csv")
                df = pd.DataFrame(load_data)

                cell1 = df['First Name'].tolist()
                cell2 = df['Last Name'].tolist()
                cell3 = df['Grade Level'].tolist()
                cell4 = df['Pronoun'].tolist()
                cell5 = df['DOB'].tolist()
                cell6 = df['Email'].tolist()
                cell7 = df['OS'].tolist()
                cell8 = df['Guardian Name'].tolist()
                cell9 = df['Guardian Type'].tolist()
                cell10 = df['Phone'].tolist()
                cell11 = df['Guardian Email'].tolist()
                cell12 = df['Enrollment'].tolist()
                cell13 = df['Username'].tolist()
                cell14 = df['Password'].tolist()
                cell15 = df['Profile pic name'].tolist()
                #cell16 = df['Profile pic file'].tolist()

                self.entFName.insert(0, str(cell1[0]))
                self.entLName.insert(0, str(cell2[0]))
                self.cboGradeLevel.set(str(cell3[0]))
                self.cboPronoun.set(str(cell4[0]))
                self.entDOB.insert(0, str(cell5[0]))
                self.entEmail.insert(0, str(cell6[0]))
                self.cboOS.set(str(cell7[0]))
                self.entGuardianName.insert(0, str(cell8[0]))
                self.entGuardianType.insert(0, str(cell9[0]))
                self.entPGPhone.insert(0, str(cell10[0]))
                self.entPGEmail.insert(0, str(cell11[0]))
                self.cboClassReg.set(str(cell12[0]))
                self.entUserName.insert(0, str(cell13[0]))
                self.entPassWord.insert(0, str(cell14[0]))

                self.lblName.configure(text=f'#{cell13[0]}')

                img = Image.open(f'images/{cell15[0]}')
                img2 = img.resize((250, 220))

                self.prof_img = ImageTk.PhotoImage(img2)
                self.profCanv.create_image(0, 95, anchor=W, image=self.prof_img)

            else:
                self.lblTitle.configure(text = 'File Not Found')
                print('File Not Found')

    def show_dist(self):
        # Create Canvas for Distribution
        # When btnLogin is True
        self.distCanv = Canvas(self.rightFrame1B, width = 465, height = 265, bg = '#a9a9a9')
        self.distCanv.propagate(0)
        self.distCanv.pack()

        ###################################################################################################
        # Setting up the dataScores csv file that the program will store from within the Mission Records.csv
        # Now that we've acheived total points. Lets put all these in another dataset called dataScores.csv
        header = ['missionNo', 'Score50']

        file_exists = os.path.exists('dataSores2.csv')
        if not file_exists:
            with open('dataScores2.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
        ###################################################################################################

        data = pd.read_csv("missionRecords4.csv")
        # Now I have to generate a column with only the scores of all
        # the available entries
        score = 0
        df = pd.DataFrame(data)
        max_num = max(df['Mission No.'])
        mission_nums = 0
        # get all the Mission No. first
        with open('dataScores2.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            for mission_no in range(1, max_num + 1, 1):
                load_data = pd.read_csv('missionRecords4.csv')
                df = pd.DataFrame(load_data)

                if not (mission_no in set(df['Mission No.'])):
                    a, b, c, d, e, f, g, h, i, j = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                else:
                    level1_rows = df.loc[df['Mission No.'] == mission_no]
                    last_row = level1_rows.iloc[-1]

                    a = last_row['Application']
                    b = last_row['Readability']
                    c = last_row['Quality']
                    d = last_row['Creativity']
                    e = last_row['Cleanliness']
                    f = last_row['Content']
                    g = last_row['Originality']
                    h = last_row['Body Language']
                    i = last_row['Structure']
                    j = last_row['Delivery']

                    tot_points = sum([a, b, c, d, e, f, g, h, i, j])
                    score_per_proj = tot_points / 50
                    print(tot_points)

                    # Well you're not exactly reading. You're writing line by line :)
                    data = [mission_no, score_per_proj]
                    writer.writerow(data)
        ###########################################################################################
        use_data = pd.read_csv('dataScores2.csv')

        # basically, country finds all the unique countries and puts that into a list. I can do that
        missions = use_data['missionNo'].unique()
        gs = grid_spec.GridSpec(len(missions), 1)

        fig = plt2.figure(figsize=(6, 10), facecolor = '#a9a9a9')

        ridgeplot = FigureCanvasTkAgg(fig, self.distCanv)
        ridgeplot.get_tk_widget().pack()

        i = 0

        ax_objs = []
        for miss in missions:
            miss = missions[i]
            # This line puts all the values country in an array
            # x = np.array(data[data.country == country].score)
            x = np.array(use_data[use_data.missionNo == miss].Score50)
            x_d = np.linspace(0, 20, 1000)

            kde = KernelDensity(bandwidth=0.030, kernel='gaussian')
            kde.fit(x[:, None])

            logprob = kde.score_samples(x_d[:, None])

            # creating new axes object
            ax_objs.append(fig.add_subplot(gs[i:i + 1, 0:]))

            colors = ['#f3e5b6', '#f1d5a7', '#f0c698', '#eeb68b', '#eeb68b', '#e99576',
                      '#e68670', '#e1776f', '#d76871', '#cb5c73', '#bd5276', '#ae4a78',
                      '#a0477c', '#8f3c79', '#803577', '#722f76', '#642974', '#642974',
                      '#4a1e6d', '#3c1b64', '#3c1b64', '#2c1a51', '#120f27', '#120f27']
            # plotting the distribution
            ax_objs[-1].plot(x_d, np.exp(logprob), color="#f0f0f0", lw=1)
            ax_objs[-1].fill_between(x_d, np.exp(logprob), alpha=1, color=colors[-1 - i])

            # setting uniform x and y lims
            ax_objs[-1].set_xlim(0.4, 1.1)
            ax_objs[-1].set_ylim(0, 13.5)

            # make background transparent
            rect = ax_objs[-1].patch
            rect.set_alpha(0)

            # remove borders, axis ticks, and labels
            # plt2.xticks([])
            plt2.yticks([])
            # ax_objs[-1].set_xticklabels([])
            ax_objs[-1].set_yticklabels([])
            # ax_objs[-1].tick_params(length=0)
            #ax_objs[-1].set_ylabel(f'{miss}')

            #ax_objs[-1].set_facecolor("black")

            if i == len(missions) - 1:
                ax_objs[-1].set_xlabel("Total Score Distribution", fontsize=10)
            else:
                ax_objs[-1].set_xticklabels([])

            spines = ["top", "right", "left", "bottom"]
            for s in spines:
                ax_objs[-1].spines[s].set_visible(False)

            # adj_country = miss.replace(" ", "\n")
            # ax_objs[-1].text(-0.02, 0, adj_country, fontweight="bold", fontsize=14, ha="right")

            i += 1

        gs.update(hspace=-0.65)
        #fig.text(0.07, 0.90, "Distribution of Student Scores", fontsize=10)

    def show_pie(self):
        load_data = pd.read_csv("missionRecords4.csv")
        df = pd.DataFrame(load_data)
        print(len(df['Mission No.']))

        if len(df['Mission No.']) > 0:
            max_num = max(df['Mission No.'])
            appl = []
            read = []
            qual = []
            create = []
            clean = []
            cont = []
            origin = []
            body = []
            struct = []
            deliv = []

            for x in range(1, max_num + 1):
                cellA = df.loc[df['Mission No.'] == x]['Application']
                appl.append(cellA.iloc[-1])
                cellB = df.loc[df['Mission No.'] == x]['Readability']
                read.append(cellB.iloc[-1])
                cellC = df.loc[df['Mission No.'] == x]['Quality']
                qual.append(cellC.iloc[-1])
                cellD = df.loc[df['Mission No.'] == x]['Creativity']
                create.append(cellD.iloc[-1])
                cellE = df.loc[df['Mission No.'] == x]['Cleanliness']
                clean.append(cellE.iloc[-1])
                cellF = df.loc[df['Mission No.'] == x]['Content']
                cont.append(cellF.iloc[-1])
                cellG = df.loc[df['Mission No.'] == x]['Originality']
                origin.append(cellG.iloc[-1])
                cellH = df.loc[df['Mission No.'] == x]['Body Language']
                body.append(cellH.iloc[-1])
                cellI = df.loc[df['Mission No.'] == x]['Structure']
                struct.append(cellI.iloc[-1])
                cellJ = df.loc[df['Mission No.'] == x]['Delivery']
                deliv.append(cellJ.iloc[-1])

            appl = (sum(appl))
            read = (sum(read))
            qual = (sum(qual))
            create = (sum(create))
            clean = (sum(clean))
            cont = (sum(cont))
            origin = (sum(origin))
            body = (sum(body))
            struct = (sum(struct))
            deliv = (sum(deliv))

        labels = ['App.', 'Rea.', 'Qua.', 'Inn.', 'Cle.', 'Con.','Ori.','Bod.','Str.','Del.']

        data = [appl, read, qual, create, clean, cont, origin, body, struct, deliv]
        # Dictionary loaded into a DataFrame
        #df_dict = pd.DataFrame(data=data)

        # Interview Question
        # Explode only the largest value in the dataset.
        # 1) Sort the maximum value.
        # 2) make the largest 0.20 explosion rate
        ###########################################
        # 1) create an empty list
        # 2) Look at all the values inside data
        # 3) check to see if its max, then append the explode rate
        # 4) Check to see if its min, then append the explode rate
        # 5) Check to if all else, then append the regular rate (all in that order)
        # 6) Use list comprehension to change everything into a float

        explode = []
        for x in data:
            if x == max(data):
                explode.append('0.30')
            elif x == min(data):
                explode.append('0.30')
            else:
                explode.append('0.05')

        explode = [float(i) for i in explode]
        print(explode)
        colors = sns.color_palette('magma')
        colors = ['#f3e5b6', '#f1d5a7', '#f0c698', '#eeb68b', '#eeb68b', '#e99576',
                  '#e68670', '#e1776f', '#d76871', '#cb5c73', ]
        self.figpie = plt2.figure(facecolor='darkgrey', figsize=(4, 4))
        ax = self.figpie.add_subplot()

        plt2.pie(data,
                labels=labels,
                colors=colors,
                autopct='%0.0f%%',
                explode=explode,
                shadow='False',
                startangle=90,
                textprops={'color': 'black', 'fontsize': 10},
                wedgeprops={'linewidth': 2},
                #frame='true',
                center=(0.1, 0.1),
                #rotatelabels='true',
                radius = 1.10)

        barplot = FigureCanvasTkAgg(self.figpie, self.dataCanv2)
        barplot.get_tk_widget().pack()

    def show_text(self,text):
        self.planet_canv.pack_forget()

        self.lblScreen = Label(self.leftFrameDown1, text='test', bg='black', font='consolas 12 bold',
                               fg='green2')
        self.lblScreen.propagate(0)
        self.lblScreen.pack(fill=BOTH, expand=True)

        if text == '/open_notes.exe':
            if self.txtNotesOn:
                self.txtNotes.pack_forget()
                self.txtNotesOn = False

            if self.rightMissFrames:
                self.titleFrameFor.pack_forget()
                self.dataFrameFor.pack_forget()
                self.dataFrame2B.pack_forget()
                self.dataFrame3.pack_forget()
                self.lbltest.pack_forget()

            if self.lblTestbox == False:
                self.lbltest = Label(self.rightFrameDown, text='', font='consolas 12 bold',
                                     width=50, height=50, bg='cornsilk', justify = LEFT, anchor = NW)
                self.lbltest.pack(side=TOP, fill = BOTH, expand = True)
                self.lblTestbox = True

            self.read_me()

            self.lbltest.configure(justify = LEFT, anchor = NW)
            self.print_general(self.text, 2, 10, 400, 'consolas', 'black', self.lbltest)

        elif text == '/take_notes.exe':
            self.txtNotesOn = True

            if self.rightMissFrames:
                self.titleFrameFor.pack_forget()
                self.dataFrameFor.pack_forget()
                self.dataFrame2B.pack_forget()
                self.dataFrame3.pack_forget()
                self.lbltest.pack_forget()
                self.rightMissFrames = False

            if self.lblTestbox:
                self.lbltest.pack_forget()
                self.lblTestbox = False

            self.txtNotes = Text(self.rightFrameDown, width=300, height=450)
            self.txtNotes.pack(side=TOP)
            self.take_me()

        elif text == '/save_note':

            if self.rightMissFrames:
                self.titleFrameFor.pack_forget()
                self.dataFrameFor.pack_forget()
                self.dataFrame2B.pack_forget()
                self.dataFrame3.pack_forget()
                self.lbltest.pack_forget()
                self.rightMissFrames = False

            if self.lblTestbox:
                self.lbltest.pack_forget()
                self.lblTestbox = False

            # if self.txtNotesOn != True:
            #     pass
            # else:
            self.txtNotesOn = True
            self.save_me()

        elif text == '/open_source.txt':
            if self.txtNotesOn:
                self.txtNotes.pack_forget()
                self.txtNotes = Text(self.rightFrameDown, width=300, height=450)
                self.txtNotes.pack(side=TOP)

            if self.rightMissFrames:
                self.titleFrameFor.pack_forget()
                self.dataFrameFor.pack_forget()
                self.dataFrame2B.pack_forget()
                self.dataFrame3.pack_forget()
                self.lbltest.pack_forget()

            if self.lblTestbox:
                self.lbltest.pack_forget()
                self.lblTestbox = True

            self.open_me()
            self.txtNotes.insert(END, self.text)

            #self.lbltest.configure(justify = LEFT, anchor = NW)
            #self.print_general(self.text, 2, 10, 400, 'consolas', 'black', self.lbltest)

        elif text == '/planet_inv.exe':
            self.print_general('Planetary Observatory', 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            self.planet_inv()

        else:
            self.print_general(self.commands, 2, 12, 325, 'consolas', 'green2', self.lblScreen)

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def popup_rank2(self):
        pass

    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    def animate_planet1(self):
        
        counter = (counter + 1) % len(self.seq_planet1)

        
        self.planet_canv.itemconfig(self.image_planet1, image=self.seq_planet1[counter])
        self.root.after(60, self.animate_planet1)

    def animate_rank1(self, counter):
        self.canvas_rank1B.itemconfig(self.image_rank1, image=self.seq_sd1[counter])
        self.root.after(1000, lambda: self.animate_rank1((counter + 1) % len(self.seq_sd1)))

    def animate_rank2(self, counter):
        self.canvas_rank2B.itemconfig(self.image_rank2, image=self.seq_sd2[counter])
        self.root.after(1000, lambda: self.animate_rank2((counter + 1) % len(self.seq_sd2)))

    def animate_rank3(self, counter):
        self.canvas_rank3B.itemconfig(self.image_rank3, image=self.seq_sd3[counter])
        self.root.after(1000, lambda: self.animate_rank3((counter + 1) % len(self.seq_sd3)))

    def animate_rank4(self, counter):
        self.canvas_rank4B.itemconfig(self.image_rank4, image=self.seq_sd4[counter])
        self.root.after(1000, lambda: self.animate_rank4((counter + 1) % len(self.seq_sd4)))

    def animate_rank5(self, counter):
        self.canvas_rank5B.itemconfig(self.image_rank5, image=self.seq_sd5[counter])
        self.root.after(1000, lambda: self.animate_rank5((counter + 1) % len(self.seq_sd5)))

    def animate_rank6(self, counter):
        self.canvas_rank6B.itemconfig(self.image_rank6, image=self.seq_sd6[counter])
        self.root.after(1000, lambda: self.animate_rank6((counter + 1) % len(self.seq_sd6)))

    def animate_rank7(self, counter):
        self.canvas_rank7B.itemconfig(self.image_rank7, image=self.seq_sd7[counter])
        self.root.after(1000, lambda: self.animate_rank7((counter + 1) % len(self.seq_sd7)))

    def animate_rank8(self, counter):
        self.canvas_rank8B.itemconfig(self.image_rank8, image=self.seq_sd8[counter])
        self.root.after(1000, lambda: self.animate_rank8((counter + 1) % len(self.seq_sd8)))

    def animate_rank9(self, counter):
        self.canvas_rank9B.itemconfig(self.image_rank9, image=self.seq_sd9[counter])
        self.root.after(1000, lambda: self.animate_rank9((counter + 1) % len(self.seq_sd9)))

    def animate_rank10(self, counter):
        self.canvas_rank10B.itemconfig(self.image_rank10, image=self.seq_sd10[counter])
        self.root.after(1000, lambda: self.animate_rank10((counter + 1) % len(self.seq_sd10)))

    def animate_rank11(self, counter):
        self.canvas_rank11B.itemconfig(self.image_rank11, image=self.seq_sd11[counter])
        self.root.after(1000, lambda: self.animate_rank11((counter + 1) % len(self.seq_sd11)))

    def animate_rank12(self, counter):
        self.canvas_rank12B.itemconfig(self.image_rank12, image=self.seq_sd12[counter])
        self.root.after(1000, lambda: self.animate_rank12((counter + 1) % len(self.seq_sd12)))

    def animate_rank13(self, counter):
        self.canvas_rank13B.itemconfig(self.image_rank13, image=self.seq_sd13[counter])
        self.root.after(1000, lambda: self.animate_rank13((counter + 1) % len(self.seq_sd13)))

    def animate_rank14(self, counter):
        self.canvas_rank14B.itemconfig(self.image_rank14, image=self.seq_sd14[counter])
        self.root.after(1000, lambda: self.animate_rank14((counter + 1) % len(self.seq_sd14)))

    def animate_rank15(self, counter):
        self.canvas_rank15B.itemconfig(self.image_rank15, image=self.seq_sd15[counter])
        self.root.after(1000, lambda: self.animate_rank15((counter + 1) % len(self.seq_sd15)))

    def animate_rank16(self, counter):
        self.canvas_rank16B.itemconfig(self.image_rank16, image=self.seq_sd16[counter])
        self.root.after(1000, lambda: self.animate_rank16((counter + 1) % len(self.seq_sd16)))

    ########################################################
    def read_me(self):
        for i in range(1,25,1):
            if self.Miss1.get() == i:
                notepad = f'notes/notes{i}.txt'
        try:
            self.date = dt.datetime.now()
            upload_text = 'Mission One Reference Notes '# + f"{self.date:%A, %B %d, %Y}"
            self.print_general(upload_text, 2, 12, 325, 'consolas', 'green2', self.lblScreen)
            with open(f'{notepad}') as f:
                self.lines = f.readlines()
                self.text = ''
                for char in self.lines:
                    self.text += char
        except:
            self.text = 'File Not Found'

    def save_me(self):
        # Get the lines from the txt notes
        lines = self.txtNotes.get("1.0", END)
        print(lines)

        for i in range(1,25,1):
            if self.Miss1.get() == i:
                notepad = f'notes/notes{i}.txt'
        # lines = ['Readme', 'How to write text files in Python']
        with open(f'{notepad}', 'w', newline = '') as f:
            for line in lines:
                f.write(line)
            #     f.write('\n')

        upload_text = 'Notes Saved Successfully '  # + f"{self.date:%A, %B %d, %Y}"
        self.print_general(upload_text, 2, 12, 325, 'consolas', 'green2', self.lblScreen)

    def take_me(self):
        for i in range(1,25,1):
            if self.Miss1.get() == i:
                notepad = f'notes/notes{i}.txt'

        try:
            with open(f'{notepad}') as f:
                self.lines = f.readlines()
                self.text = ''
                for char in self.lines:
                    self.text += char
        except:
            self.text = f'Mission Objective #{self.Miss1.get()} Notes\n'

        self.txtNotes.insert(END, self.text)

        upload_text = 'Note Taker App '  # + f"{self.date:%A, %B %d, %Y}"
        self.print_general(upload_text, 2, 12, 325, 'consolas', 'green2', self.lblScreen)

        self.date = dt.datetime.now()
        upload_text = f"{self.date:%A, %B %d, %Y}"
        self.txtNotes.insert(END, upload_text)

    def open_me(self):
        for i in range(1,25,1):
            if self.Miss1.get() == i:
                current_code = f'objectives/objective{i}.py'

        try:
            upload_text = 'Mission One Source Code '# + f"{self.date:%A, %B %d, %Y}"
            self.print_general(upload_text, 2, 12, 325, 'consolas', 'green2', self.lblScreen)

            with open(f'{current_code}') as f:
                self.lines = f.readlines()
                self.text = ''
                for char in self.lines:
                    self.text += char

        except:
            self.text = 'file not found'

    ########################################################

    def check_description(self, planet_name):
        # My main goal is to have feed the planet name into this function
        # then it will check to see what planet description that planet name is
        # associated with. Easy!
        all_planets = ['common_planet_1','common_planet_2','common_planet_3',
                       'rare_planet_2','rare_planet_3','rare_planet_4',
                       'ultra_rare_planet1','ultra_rare_planet2',
                       'hyper_rare_planet1','hyper_rare_planet2','hyper_rare_planet3']
        
        all_descs = [self.com_planet1_desc, self.com_planet2_desc, self.com_planet3_desc,
                     self.rar_planet1_desc, self.rar_planet2_desc, self.rar_planet3_desc,
                     self.ult_planet1_desc, self.ult_planet2_desc,
                     self.hyp_planet1_desc, self.hyp_planet2_desc, self.hyp_planet3_desc,
                     self.god_planet1_desc,]

        for index in range(len(all_planets)):
            if planet_name == all_planets[index]:
                self.planet_desc = all_descs[index]

    def planet_inv(self):
        # self.planetFrame = Frame(self.rightFrameDown, borderwidth = 7, bg = 'grey', relief = RAISED, width = 1260,
        #                   height = 735)
        # self.planetFrame.pack_propagate(0)
        # self.planetFrame.pack(side = TOP)
        self.rightFrameDown.configure(relief = RAISED)
        self.frameTwo2 = Frame(self.rightFrameDown, borderwidth=7, background="grey25", relief = RAISED,
                               width=425, height=510, bd = 5)
        self.frameTwo2.pack_propagate(0)
        self.frameTwo2.pack(side = TOP)

        self.canvas1 = Canvas(self.frameTwo2, borderwidth=0, background="grey65", width = 1460, height = 470)
        self.canvas1.propagate(0)

        self.frameTwo = Frame(self.canvas1, background="grey80")

        hsb = Scrollbar(self.frameTwo2, orient="horizontal", command=self.canvas1.xview)
        vsb = Scrollbar(self.frameTwo2, orient = 'vertical', command = self.canvas1.yview)
        self.canvas1.configure(xscrollcommand=hsb.set)
        self.canvas1.configure(yscrollcommand=vsb.set)
        hsb.pack(side="bottom", fill="x")
        vsb.pack(side='right', fill = 'y')
        self.canvas1.pack(side="left")
        self.canvas1.create_window((4, 4), window=self.frameTwo, anchor="nw")
        self.frameTwo.bind("<Configure>", lambda event, canvas1=self.canvas1: self.onFrameConfigure(self.canvas1))

        self.index = 1

        self.cardWidth = 120
        self.cardHeight = 125
        self.cardX = 18
        self.cardY = 100
        self.cardCol = 'black'
        self.cardBD = 7

        self.place_cards()

        for y in range(0,9,2):
            for x in range(0,3):
                planet_det = str(self.index)

                self.lblCard = Button(self.frameTwo, width = 16, height = 1, borderwidth = '5',
                                     bg = 'grey25', relief = RAISED, bd = self.cardBD,
                                     text = planet_det , font = 'consolas 9',
                                     fg = 'cornsilk')
                self.lblCard.grid(row = y, column = x)

                self.index += 1

    def place_cards(self):
        location = "./images/common_planet_1.gif"
        self.card1 = Canvas(self.frameTwo, width=self.cardWidth, height=self.cardHeight, borderwidth="5",
                            bg=self.cardCol, relief=RAISED, bd=self.cardBD)
        self.card1.propagate(0)
        self.card1.grid(row=1, column=0)
        
        self.plan_sd1 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open(location))]
        self.image_plan1 = self.card1.create_image(70, 70, image=self.plan_sd1[0])
        self.animate_plan1(0)

        self.card2 = Canvas(self.frameTwo, width=self.cardWidth, height=self.cardHeight, borderwidth="5",
                            bg=self.cardCol, relief=RAISED, bd=self.cardBD)
        self.card2.propagate(0)
        self.card2.grid(row=1, column=1)

        self.plan_sd2 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open(location))]
        self.image_plan2 = self.card2.create_image(70, 70, image=self.plan_sd2[0])
        self.animate_plan2(0)

        self.card3 = Canvas(self.frameTwo, width=self.cardWidth, height=self.cardHeight, borderwidth="5",
                            bg=self.cardCol, relief=RAISED, bd=self.cardBD)
        self.card3.propagate(0)
        self.card3.grid(row=1, column=2)

        self.plan_sd3 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open(location))]
        self.image_plan3 = self.card3.create_image(70, 70, image=self.plan_sd3[0])
        self.animate_plan3(0)

        self.card4 = Canvas(self.frameTwo, width=self.cardWidth, height=self.cardHeight, borderwidth="5",
                            bg=self.cardCol, relief=RAISED, bd=self.cardBD)
        self.card4.propagate(0)
        self.card4.grid(row=3, column=0)

        self.plan_sd4 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open(location))]
        self.image_plan4 = self.card4.create_image(70, 70, image=self.plan_sd4[0])
        self.animate_plan4(0)

        self.card5 = Canvas(self.frameTwo, width=self.cardWidth, height=self.cardHeight, borderwidth="5",
                            bg=self.cardCol, relief=RAISED, bd=self.cardBD)
        self.card5.propagate(0)
        self.card5.grid(row=3, column=1)

        self.plan_sd5 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open(location))]
        self.image_plan5 = self.card5.create_image(70, 70, image=self.plan_sd5[0])
        self.animate_plan5(0)

        self.card6 = Canvas(self.frameTwo, width=self.cardWidth, height=self.cardHeight, borderwidth="5",
                            bg=self.cardCol, relief=RAISED, bd=self.cardBD)
        self.card6.propagate(0)
        self.card6.grid(row=3, column=2)

        self.plan_sd6 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open(location))]
        self.image_plan6 = self.card6.create_image(70, 70, image=self.plan_sd6[0])
        self.animate_plan6(0)

        self.card7 = Canvas(self.frameTwo, width=self.cardWidth, height=self.cardHeight, borderwidth="5",
                            bg=self.cardCol, relief=RAISED, bd=self.cardBD)
        self.card7.propagate(0)
        self.card7.grid(row=5, column=0)

        self.plan_sd7 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open(location))]
        self.image_plan7 = self.card7.create_image(70, 70, image=self.plan_sd7[0])
        self.animate_plan7(0)

        self.card8 = Canvas(self.frameTwo, width=self.cardWidth, height=self.cardHeight, borderwidth="5",
                            bg=self.cardCol, relief=RAISED, bd=self.cardBD)
        self.card8.propagate(0)
        self.card8.grid(row=5, column=1)

        self.plan_sd8 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open(location))]
        self.image_plan8 = self.card8.create_image(70, 70, image=self.plan_sd8[0])
        self.animate_plan8(0)

        self.card9 = Canvas(self.frameTwo, width=self.cardWidth, height=self.cardHeight, borderwidth="5",
                            bg=self.cardCol, relief=RAISED, bd=self.cardBD)
        self.card9.propagate(0)
        self.card9.grid(row=5, column=2)

        self.plan_sd9 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open(location))]
        self.image_plan9 = self.card9.create_image(70, 70, image=self.plan_sd9[0])
        self.animate_plan9(0)

        self.card10 = Canvas(self.frameTwo, width=self.cardWidth, height=self.cardHeight, borderwidth="5",
                            bg=self.cardCol, relief=RAISED, bd=self.cardBD)
        self.card10.propagate(0)
        self.card10.grid(row=7, column=0)

        self.plan_sd10 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open(location))]
        self.image_plan10 = self.card10.create_image(70, 70, image=self.plan_sd10[0])
        self.animate_plan10(0)

        self.card11 = Canvas(self.frameTwo, width=self.cardWidth, height=self.cardHeight, borderwidth="5",
                             bg=self.cardCol, relief=RAISED, bd=self.cardBD)
        self.card11.propagate(0)
        self.card11.grid(row=7, column=1)

        self.plan_sd11 = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(
                Image.open(location))]
        self.image_plan11 = self.card11.create_image(70, 70, image=self.plan_sd11[0])
        self.animate_plan11(0)

        self.card12 = Canvas(self.frameTwo, width=self.cardWidth, height=self.cardHeight, borderwidth="5",
                            bg=self.cardCol, relief=RAISED, bd=self.cardBD)
        self.card12.propagate(0)
        self.card12.grid(row=7, column=2)

        self.plan_sd12 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open(location))]
        self.image_plan12 = self.card12.create_image(70, 70, image=self.plan_sd12[0])
        self.animate_plan12(0)

        self.card13 = Canvas(self.frameTwo, width=self.cardWidth, height=self.cardHeight, borderwidth="5",
                            bg=self.cardCol, relief=RAISED, bd=self.cardBD)
        self.card13.propagate(0)
        self.card13.grid(row=9, column=0)

        self.plan_sd13 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open(location))]
        self.image_plan13 = self.card13.create_image(70, 70, image=self.plan_sd13[0])
        self.animate_plan13(0)

        self.card14 = Canvas(self.frameTwo, width=self.cardWidth, height=self.cardHeight, borderwidth="5",
                            bg=self.cardCol, relief=RAISED, bd=self.cardBD)
        self.card14.propagate(0)
        self.card14.grid(row=9, column=1)

        self.plan_sd14 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open(location))]
        self.image_plan14 = self.card14.create_image(70, 70, image=self.plan_sd14[0])
        self.animate_plan14(0)

        self.card15 = Canvas(self.frameTwo, width=self.cardWidth, height=self.cardHeight, borderwidth="5",
                            bg=self.cardCol, relief=RAISED, bd=self.cardBD)
        self.card15.propagate(0)
        self.card15.grid(row=9, column=2)

        self.plan_sd15 = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                Image.open(location))]
        self.image_plan15 = self.card15.create_image(70, 70, image=self.plan_sd15[0])
        self.animate_plan15(0)

    def animate_plan1(self, counter):
        self.card1.itemconfig(self.image_plan1, image=self.plan_sd1[counter])
        self.root.after(60, lambda: self.animate_plan1((counter + 1) % len(self.plan_sd1)))

    def animate_plan2(self, counter):
        self.card2.itemconfig(self.image_plan2, image=self.plan_sd2[counter])
        self.root.after(60, lambda: self.animate_plan2((counter + 1) % len(self.plan_sd2)))

    def animate_plan3(self, counter):
        self.card3.itemconfig(self.image_plan3, image=self.plan_sd3[counter])
        self.root.after(60, lambda: self.animate_plan3((counter + 1) % len(self.plan_sd3)))

    def animate_plan4(self, counter):
        self.card4.itemconfig(self.image_plan4, image=self.plan_sd4[counter])
        self.root.after(30, lambda: self.animate_plan4((counter + 1) % len(self.plan_sd4)))

    def animate_plan5(self, counter):
        self.card5.itemconfig(self.image_plan5, image=self.plan_sd5[counter])
        self.root.after(50, lambda: self.animate_plan5((counter + 1) % len(self.plan_sd5)))

    def animate_plan6(self, counter):
        self.card6.itemconfig(self.image_plan6, image=self.plan_sd6[counter])
        self.root.after(60, lambda: self.animate_plan6((counter + 1) % len(self.plan_sd6)))

    def animate_plan7(self, counter):
        self.card7.itemconfig(self.image_plan7, image=self.plan_sd7[counter])
        self.root.after(60, lambda: self.animate_plan7((counter + 1) % len(self.plan_sd7)))

    def animate_plan8(self, counter):
        self.card8.itemconfig(self.image_plan8, image=self.plan_sd8[counter])
        self.root.after(60, lambda: self.animate_plan8((counter + 1) % len(self.plan_sd8)))

    def animate_plan9(self, counter):
        self.card9.itemconfig(self.image_plan9, image=self.plan_sd9[counter])
        self.root.after(60, lambda: self.animate_plan9((counter + 1) % len(self.plan_sd9)))

    def animate_plan10(self, counter):
        self.card10.itemconfig(self.image_plan10, image=self.plan_sd10[counter])
        self.root.after(60, lambda: self.animate_plan10((counter + 1) % len(self.plan_sd10)))

    def animate_plan11(self, counter):
        self.card11.itemconfig(self.image_plan11, image=self.plan_sd11[counter])
        self.root.after(60, lambda: self.animate_plan11((counter + 1) % len(self.plan_sd11)))

    def animate_plan12(self, counter):
        self.card12.itemconfig(self.image_plan12, image=self.plan_sd12[counter])
        self.root.after(60, lambda: self.animate_plan12((counter + 1) % len(self.plan_sd12)))

    def animate_plan13(self, counter):
        self.card13.itemconfig(self.image_plan13, image=self.plan_sd13[counter])
        self.root.after(60, lambda: self.animate_plan13((counter + 1) % len(self.plan_sd13)))

    def animate_plan14(self, counter):
        self.card14.itemconfig(self.image_plan14, image=self.plan_sd14[counter])
        self.root.after(60, lambda: self.animate_plan14((counter + 1) % len(self.plan_sd14)))

    def animate_plan15(self, counter):
        self.card15.itemconfig(self.image_plan15, image=self.plan_sd15[counter])
        self.root.after(60, lambda: self.animate_plan15((counter + 1) % len(self.plan_sd15)))

    def animate_plan16(self, counter):
        self.card16.itemconfig(self.image_plan16, image=self.plan_sd16[counter])
        self.root.after(60, lambda: self.animate_plan16((counter + 1) % len(self.plan_sd16)))

    def animate_plan17(self, counter):
        self.card17.itemconfig(self.image_plan17, image=self.plan_sd17[counter])
        self.root.after(60, lambda: self.animate_plan17((counter + 1) % len(self.plan_sd17)))

    def animate_plan18(self, counter):
        self.card18.itemconfig(self.image_plan18, image=self.plan_sd18[counter])
        self.root.after(60, lambda: self.animate_plan18((counter + 1) % len(self.plan_sd18)))
    

    def onFrameConfigure(self,canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

    def print_general(self, message, duration, size, wraplen, font_n, col, loc):
        string_output = ''
        for char in message:
            string_output += char
            loc.config(text=string_output, font=f'{font_n} {size}',
                       wraplength=wraplen, justify=LEFT, fg=col, pady=2)
            self.waithere(duration)

    def waithere(self, duration):
        var = IntVar()
        root.after(duration, var.set, 1)
        root.wait_variable(var)

if __name__ == '__main__':
    root = Tk()
    application = Planet_Ex(root)
    root.mainloop()
