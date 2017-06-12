#cmf: Summary
#   -timer that has a set "work" time and "break" time. 
#   -Default work time = 30 min (no greater than an hour), break time = no less than 5 min.
#   -Window popup for the duration of the break. 
#   -Makes a system sound? 
#   -Window that allows you to choose times for work and break.

#cmf: Trying to add an edit to the repository from VS

from tkinter import *
import datetime

m_Today = datetime.datetime.today()

m_MaxWorkTime = datetime.time(1, 0, 0, 0)
m_MinWorkTime = datetime.time(0, 20, 0, 0)

m_MaxBreakTime = datetime.time(0, 30, 0, 0)
m_MinBreakTime = datetime.time(0, 5, 0, 0)

m_CurrentHrMin = str(m_Today.hour) + ":" + str(m_Today.minute)

global errorMessage

#print(str(m_Today.hour) + ":" + str(m_Today.minute))

#cmf: the properties that must belong to the main window
class MainWindow:
    def __init__(self, wintitle, name, dimensionx, dimensiony):
        self.wintitle = wintitle
        self.name = name
        self.dimensionx = dimensionx
        self.dimensiony = dimensiony

def CreateLabel(wn, n, t, h, w, r, c , cs):
    if(cs == 0):
        n = Label(wn, text = t, height = h, width = w, borderwidth = 2, relief = GROOVE).grid(row = r, column = c)
    else:
        n = Label(wn, text = t, height = h, width = w, borderwidth = 2, relief = GROOVE).grid(row = r, column = c, columnspan = cs)

def MakeTimeNiceFormat(variable):
    if(len(str(variable.minute)) > 1): 
        return(str(variable.hour) + ":" + str(variable.minute))
    else:
        return(str(variable.hour) + ":" + "0" + str(variable.minute))

#cmf: contents of the main window. 
def WindowContents(windowName):
    errorMessage = StringVar()
    errorMessage.set("")
    
    default01 = StringVar()
    default02 = StringVar() 
    default03 = StringVar()
    default04 = StringVar() 

    def CreateEntry(entryname, svname, defaultText, entrywidth, entryrow, entrycolumn, entrysticky):
        svname.set(defaultText)
        #print(str(svname))

        entryname = Entry(windowName, textvariable = svname, width = entrywidth).grid(row = entryrow, column = entrycolumn, sticky = entrysticky)


    CreateLabel(windowName, "contentTitle", "Break Timer Settings", 2, 20, 0, 0,4)
    CreateLabel(windowName, "contentSubtitle", "select a work and break duration, then click 'GO!' to begin your schedule", 2,80, 1,0,4)
    CreateLabel(windowName, "workDurLabel", "Work Duration:", 2, 20, 2, 0, 0)
    CreateEntry("entry01", default01, "00", 5, 2, 1, E)
    CreateLabel(windowName, "colonLabel01", ":", 2,1,2,2,0)
    CreateEntry("entry02", default02, "00", 5, 2 , 3, W)
    CreateLabel(windowName, "breakDurLabel", "Break Duration:", 2, 20, 3, 0, 0)
    CreateEntry("entry03", default03, "00", 5, 3 , 1, E)
    CreateLabel(windowName, "colonLabel02", ":", 2,1, 3,2,0)
    CreateEntry("entry04", default04, "00", 5, 3 , 3, W)
    
    #cmf: a place to show error messages
    CreateLabel(windowName, "errorLabel", errorMessage.get(), 2, 50, 4, 0, 4)

    #lambda : CheckEntryContents((str(default01.get()) + ":" + str(default02.get())),(str(default03.get()) + ":" + str(default04.get())))
    startButton = Button(windowName, text = "GO!", command = lambda: CheckEntryContents(windowName, default01.get(), default02.get(), default03.get(), default04.get(), errorMessage), height = 2, width = 20).grid(row = 5, column = 0, columnspan = 4)

def StartTimer(workTime, breakTime):
    print("Starting Timer")
    print("Work Duration: " + MakeTimeNiceFormat(workTime))
    print("Work Duration: " + MakeTimeNiceFormat(breakTime))

    #cmf: Plan:
    #1. 


def CheckEntryContents(winname, workHr, workMin, breakHr, breakMin, emessage):
    #print(workHr + ":" + workMin, breakHr + ":" + breakMin)
    
    startTimerCheck = 0
    
    inputs = [workHr, workMin, breakHr, breakMin]

    #cmf: if there are too many numbers in the entry boxes. 
    for x in range(0, 4):
        if(len(inputs[x]) > 2 or len(inputs[x]) < 2):
            emessage.set("Error: Bad time length. Enter two digits in each field")
            break
        else:
            startTimerCheck +=1 
            print("Good Time Length")
    
    #checking to see if there are any characters other than digits in the user input
    if(startTimerCheck == 4 and (workHr + workMin + breakHr + breakMin).isdigit()):
        print("All inputs are digits")
        startTimerCheck +=1 
    elif(startTimerCheck == 4):
        emessage.set("Error: Input should only be numerical")
    
    workDateTime = datetime.time()
    breakDateTime = datetime.time()

    #cmf: translating the user input into datetime format.
    if(startTimerCheck == 5):
        workDateTime = datetime.time(int(workHr), int(workMin), 0, 0)
        breakDateTime = datetime.time(int(breakHr), int(breakMin), 0, 0)
        
        #cmf: checking to see if the work and time durations are within the limits set above.
        if(workDateTime <= m_MaxWorkTime and workDateTime >= m_MinWorkTime):
            startTimerCheck += 1
            print("Good work time duration")
        else:
            emessage.set("Error: Work duration must be between " + MakeTimeNiceFormat(m_MinWorkTime) + " and " + MakeTimeNiceFormat(m_MaxWorkTime))
        if(breakDateTime <= m_MaxBreakTime and breakDateTime >= m_MinBreakTime):
            startTimerCheck += 1
            print("Good break time duration")
        else:
            emessage.set("Error: Break duration must be between " + MakeTimeNiceFormat(m_MinBreakTime) + " and " + MakeTimeNiceFormat(m_MaxBreakTime))

    #cmf: if all the parameters are correct, start the actual timer 
    if(startTimerCheck == 7):
        emessage.set("")
        StartTimer(workDateTime, breakDateTime)
        
        successMessage = StringVar()
        successMessage.set("Your workday has begun. Your work duration is: " + MakeTimeNiceFormat(workDateTime) + " and your break duration is: " + MakeTimeNiceFormat(breakDateTime) + "\nYou may now minimize this window.")        

        Label(winname, textvariable = successMessage, height = 5, width = 80, borderwidth = 2, relief = GROOVE).grid(row = 2, column = 0, columnspan = 4, rowspan = 2)
        cancelButton = Button(winname, text = "Close Program", command = sys.exit, height = 2, width = 20).grid(row = 5, column = 0, columnspan = 4)
 
    print(startTimerCheck)
    CreateLabel(winname, "errorLabel", emessage.get(), 2, 50, 4, 0, 4)


#cmf: a function that creates any window of type MainWindow
def CreateWindow(w):
    w.name = Tk()
    w.name.title(w.wintitle)
    w.name.geometry(str(w.dimensionx) + "x" + str(w.dimensiony))

    WindowContents(w.name)

    w.name.mainloop()
        

#cmf: defining the main window
MainWindow01 = MainWindow("Break Timer", "BreakTimerWindow", 565, 230)


#cmf: showing the main window on screen
CreateWindow(MainWindow01)

