#cmf: Summary
#   -timer that has a set "work" time and "break" time. 
#   -Default work time = 30 min (no greater than an hour), break time = no less than 5 min.
#   -Window popup for the duration of the break. 
#   -Makes a system sound? 
#   -Window that allows you to choose times for work and break.

#cmf: Trying to add an edit to the repository from VS

import tkinter
import datetime

m_Today = datetime.datetime.today()

m_MaxWorkTime = datetime.time(1, 0, 0, 0)
m_MinWorkTime = datetime.time(0, 20, 0, 0)

m_MaxBreakTime = datetime.time(0, 30, 0, 0)
m_MinBreakTime = datetime.time(0, 5, 0, 0)

print(str(m_Today.hour) + ":" + str(m_Today.minute))
