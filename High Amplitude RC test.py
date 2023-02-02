from tkinter import *

# creating tkinter window
RC = Tk()
RC.title("High Amplitude RC test")

# RC.geometry("640x480+300+100")  # 가로 x 세로 + x좌표 + y좌표
RC.geometry("1280x960+0+10")
# x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
RC.resizable(True, True)  

# 메뉴바 만들기
menubar = Menu(RC)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = RC.destroy)
  
# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)
  
# Adding Operate Menu
Operate = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Operate', menu = Operate)
Operate.add_command(label ='Tk Help', command = None)
Operate.add_command(label ='Demo', command = None)
Operate.add_separator()
Operate.add_command(label ='About Tk', command = None)
 
# Adding Projects Menu
Projects = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Projects', menu = Projects)
Projects.add_command(label ='Tk Help', command = None)
Projects.add_command(label ='Demo', command = None)
Projects.add_separator()
Projects.add_command(label ='About Tk', command = None)
 
# Adding Windows Menu
Windows = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Windows', menu = Windows)
Windows.add_command(label ='Tk Help', command = None)
Windows.add_command(label ='Demo', command = None)
Windows.add_separator()
Windows.add_command(label ='About Tk', command = None)
 
# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)

# display Menu
RC.config(menu = menubar)
RC.mainloop()