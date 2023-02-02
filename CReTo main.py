import tkinter as tk
from tkinter import *
from tkinter import ttk

from Command.Project import *
from Command.Tools import *
from Command.Operate import *
from Command.help import *
from Command.edit import *

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# Definintion of Global variables-----------------------------------------------------------------------------------------------------------


Project_information = {
'Y/M/D':None, #system의 데이트 정보를 읽어서 초기값으로 설정
'Project ID':None,
'Sample ID':None,
'Operator':None,
'SpecimenDiameter':None,
'SpecimenHeight':None,
'SpecimenMass':None,
'ConfiningPressure':None
}

try:
    with open("Project_information.p", 'rb') as f:
        Project_information = pickle.load(f)
except:
    pass

# print(Project_information)



# -----------------------------------------------------------------------------------------------------------

# creating tkinter window
Cretomain = Tk()
Cretomain.title("C-ReTo 3.0")

# Cretomain.geometry("640x480+300+100")  # 가로 x 세로 + x좌표 + y좌표
Cretomain.geometry("1280x960+0+10")
# x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
Cretomain.resizable(False, False)

# 스타일 -----------------------------------------------------------------------------------------------------------

s1 = ttk.Style(Cretomain)
s1.configure('Red.TLabelframe.Label', font=('Times New Roman', 12, 'bold'), foreground='red')
s2 = ttk.Style(Cretomain)
s2.configure('10Black.TLabel', font=('Times New Roman', 10, 'bold'), foreground='black')
s3 = ttk.Style(Cretomain)
s3.configure('14Black.TLabel', font=('Times New Roman', 14, 'bold'), foreground='black')
s4 = ttk.Style(Cretomain)
s4.configure('10korBlack.TLabel', font=('Arial', 10), foreground='black')

# 메인프레임1-----------------------------------------------------------------------------------------------------------

MainFrame1 = tk.Frame(Cretomain, width=638, height=960, relief="flat")
MainFrame1.place(x=0, y=0)

# -----------------------------------------------------------------------------------------------------------

# with open('info.csv', mode='r') as infile:
#     reader = csv.reader(infile)
#     with open('info_new.csv', mode='w') as outfile:
#         writer = csv.writer(outfile)
#         Recent_Project_information = dict((rows[0],rows[1]) for rows in reader)

# -----------------------------------------------------------------------------------------------------------

ProjectFrame1_title = tk.Frame(MainFrame1, width=580, height=45, relief="solid", bd=2)
ProjectFrame1_title.place(relx=0.04, rely=0.05)

TestCondition_LB = ttk.Label(ProjectFrame1_title, text = "Test Condition", style='14Black.TLabel')
TestCondition_LB.place(relx=0.5, rely=0.5, anchor='center')

ProjectFrame1 = tk.Frame(MainFrame1, width=580, height=190, relief="solid", bd=2)
ProjectFrame1.place(relx=0.04, rely=0.1)

DateTime_LB = ttk.Label(ProjectFrame1, text = "Y/M/D : {}".format(Project_information['Y/M/D']), style='14Black.TLabel')
DateTime_LB.place(relx=0.02, rely=0.105)

Project_ID_LB = ttk.Label(ProjectFrame1, text = "Project ID : {}".format(Project_information['Project ID']), style='14Black.TLabel')
Project_ID_LB.place(relx=0.02, rely=0.305)

Sample_ID_LB = ttk.Label(ProjectFrame1, text = "Sample ID : {}".format(Project_information['Sample ID']), style='14Black.TLabel')
Sample_ID_LB.place(relx=0.02, rely=0.505)

Operator_LB = ttk.Label(ProjectFrame1, text = "Operator : {}".format(Project_information['Operator']), style='14Black.TLabel')
Operator_LB.place(relx=0.02, rely=0.705)

SpecimenDiameter_LB = ttk.Label(ProjectFrame1, text = "Specimen Diameter : {}".format(Project_information['SpecimenDiameter']), style='14Black.TLabel')
SpecimenDiameter_LB.place(relx=0.5, rely=0.105)

SpecimenHeight_LB = ttk.Label(ProjectFrame1, text = "Specimen Height : {}".format(Project_information['SpecimenHeight']), style='14Black.TLabel')
SpecimenHeight_LB.place(relx=0.5, rely=0.305)

SpecimenMass_LB = ttk.Label(ProjectFrame1, text = "Specimen Mass : {}".format(Project_information['SpecimenMass']), style='14Black.TLabel')
SpecimenMass_LB.place(relx=0.5, rely=0.505)

ConfiningPressure_LB = ttk.Label(ProjectFrame1, text = "Confining Pressure : {}".format(Project_information['ConfiningPressure']), style='14Black.TLabel')
ConfiningPressure_LB.place(relx=0.5, rely=0.705)

# -----------------------------------------------------------------------------------------------------------

ProjectFrame2_title = tk.Frame(MainFrame1, width=580, height=45, relief="solid", bd=2)
ProjectFrame2_title.place(relx=0.04, rely=0.35)

Daq_LB = ttk.Label(ProjectFrame2_title, text = "DAQ", style='14Black.TLabel')
Daq_LB.place(relx=0.5, rely=0.5, anchor='center')

ProjectFrame2= tk.Frame(MainFrame1, width=580, height=190, relief="solid", bd=2)
ProjectFrame2.place(relx=0.04, rely=0.4)\

# -----------------------------------------------------------------------------------------------------------

ProjectFrame3_title = tk.Frame(MainFrame1, width=580, height=45, relief="solid", bd=2)
ProjectFrame3_title.place(relx=0.04, rely=0.65)

TestConditions_LB = ttk.Label(ProjectFrame3_title, text = "Device Setting", style='14Black.TLabel')
TestConditions_LB.place(relx=0.5, rely=0.5, anchor='center')

ProjectFrame3= tk.Frame(MainFrame1, width=580, height=190, relief="solid", bd=2)
ProjectFrame3.place(relx=0.04, rely=0.7)

tabControl = ttk.Notebook(ProjectFrame3)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='1. Test system setting')
tabControl.add(tab2, text='2. A/D board terminal setting')
tabControl.place(relx=0, rely=0, width=576, height=186)

    # 가속도계
acc_lbl = ttk.Label(tab1, text = "가속도계", style='10Black.TLabel')
acc_combo = ttk.Combobox(tab1, state="readonly", values=["가속도계 1", "가속도계 2", "가속도계 3", "가속도계 4"], font=10) # 가속도계 설정은 treading를 이용해야 할듯함
acc_combo.current(0)
acc_lbl = acc_lbl.place(relx=0.03, rely=0.1)
acc_combo = acc_combo.place(relx=0.26, rely=0.1, width=120)
    # 가진판
가진판_lbl = ttk.Label(tab1, text = "가진판", style='10Black.TLabel')
가진판_combo = ttk.Combobox(tab1, state="readonly", values=["가진판", "..."], font=10)
가진판_combo.current(0)
가진판_lbl = 가진판_lbl.place(relx=0.03, rely=0.3)
가진판_combo = 가진판_combo.place(relx=0.26, rely=0.3, width=120)
    # Target for proximity
Target_lbl = ttk.Label(tab1, text = "Target for proximity", style='10Black.TLabel')
Target_combo = ttk.Combobox(tab1, state="readonly", values=["#1", "#2", "#3", "#4"], font=10)
Target_combo.current(0)
Target_lbl = Target_lbl.place(relx=0.03, rely=0.5)
Target_combo = Target_combo.place(relx=0.26, rely=0.5, width=120)
    # Torque system ID
Torque_lbl = ttk.Label(tab1, text = "Torque system ID", style='10Black.TLabel')
Torque_combo = ttk.Combobox(tab1, state="readonly", values=["sys#1", "sys#2", "sys#3"], font=10)
Torque_combo.current(0)
Torque_lbl = Torque_lbl.place(relx=0.5, rely=0.1)
Torque_combo = Torque_combo.place(relx=0.73, rely=0.1, width=120)
    # Topcap
Topcap_lbl = ttk.Label(tab1, text = "Topcap", style='10Black.TLabel')
Topcap_combo = ttk.Combobox(tab1, state="readonly", values=["50mm", "100mm"], font=10)
Topcap_combo.current(0)
Topcap_lbl = Topcap_lbl.place(relx=0.5, rely=0.3)
Topcap_combo = Topcap_combo.place(relx=0.73, rely=0.3, width=120)
    # 파형발생장치
파형발생장치_lbl = ttk.Label(tab1, text = "파형발생장치", style='10Black.TLabel')
DAQboard = ["DAQ보드1", "DAQ보드2", "DAQ보드3"]
파형발생장치_combo = ttk.Combobox(tab1, state="readonly", values=DAQboard, font=10)
파형발생장치_combo.current(0)
파형발생장치_lbl = 파형발생장치_lbl.place(relx=0.5, rely=0.5)
파형발생장치_combo = 파형발생장치_combo.place(relx=0.73, rely=0.5, width=120)

button = ttk.Button(tab1, text="설정", command=None)
button.place(relx=0.8, rely=0.7)


    # 신호획득측
신호획득측_lbl = ttk.Label(tab2, text = "신호획득측", style='10Black.TLabel')
ttk.Separator(tab2).place(relx=0.15, rely=0.1, width=200)
신호획득측_lbl.place(relx=0.03, rely=0.05)
    # 가속도계 컨디셔너 출력
acc_conditioner_lbl = ttk.Label(tab2, text = "가속도계 컨디셔너 출력", style='10Black.TLabel')
acc_conditioner_combo = ttk.Combobox(tab2, state="readonly", values=["Dev1/ai1","Dev2/ai1","..."], font=10)
acc_conditioner_combo.current(0)
acc_conditioner_lbl.place(relx=0.03, rely=0.2)
acc_conditioner_combo.place(relx=0.3, rely=0.2, width=120)
    # NEC 9B02의 A채널
NEC_9B02_Ch1_lbl = ttk.Label(tab2, text = "NEC 9B02의 A채널", style='10Black.TLabel')
NEC_9B02_Ch1_combo = ttk.Combobox(tab2, state="readonly", values=["Dev1/ai2","Dev2/ai2","..."], font=10)
NEC_9B02_Ch1_combo.current(0)
NEC_9B02_Ch1_lbl.place(relx=0.03, rely=0.4)
NEC_9B02_Ch1_combo.place(relx=0.3, rely=0.4, width=120)
    # NEC 9B02의 B채널
NEC_9B02_Ch2_lbl = ttk.Label(tab2, text = "NEC 9B02의 B채널", style='10Black.TLabel')
NEC_9B02_Ch2_combo = ttk.Combobox(tab2, state="readonly", values=["Dev1/ai3","Dev2/ai3","..."], font=10)
NEC_9B02_Ch2_combo.current(0)
NEC_9B02_Ch2_lbl.place(relx=0.03, rely=0.6)
NEC_9B02_Ch2_combo.place(relx=0.3, rely=0.6, width=120)
    # 함수발생기 SYNC
SYNC_lbl = ttk.Label(tab2, text = "함수 발생기 SYNC", style='10Black.TLabel')
SYNC_combo = ttk.Combobox(tab2, state="readonly", values=["Dev1/ai4","Dev2/ai4","..."], font=10)
SYNC_combo.current(0)
SYNC_lbl.place(relx=0.03, rely=0.8)
SYNC_combo.place(relx=0.3, rely=0.8, width=120)
    # 파형발생측
파형발생측_lbl = ttk.Label(tab2, text = "파형발생측", style='10Black.TLabel')
ttk.Separator(tab2).place(relx=0.65, rely=0.1, width=200)
파형발생측_lbl.place(relx=0.53, rely=0.05)
    # 출력채널
output_Ch_lbl = ttk.Label(tab2, text = "출력 채널", style='10Black.TLabel')
output_Ch_combo = ttk.Combobox(tab2, state="readonly", values=["Dev1/ao0","Dev2/ao0","..."], font=10)
output_Ch_combo.current(0)
output_Ch_lbl.place(relx=0.53, rely=0.2)
output_Ch_combo.place(relx=0.73, rely=0.2, width=120)
    # 분해능
resolution_lbl = ttk.Label(tab2, text = "분해능", style='10Black.TLabel')
resolution_text = ttk.Entry(tab2, width=7)
resolution_text.insert(0, "500")
sampleNum_lbl = ttk.Label(tab2, text=":1 파장 내 샘플 수", style='10Black.TLabel')
resolution_lbl.place(relx=0.53, rely=0.4)
resolution_text.place(relx=0.63, rely=0.4)
sampleNum_lbl.place(relx=0.73, rely=0.4)

button = ttk.Button(tab2, text="설정", command=None)
button.place(relx=0.8, rely=0.7)

a = edit()
print(a.test_system_setting['acc'])

# 메인 프레임2 -----------------------------------------------------------------------------------------------------------

MainFrame2 = tk.Frame(Cretomain, width=640, height=960, relief="flat")
MainFrame2.place(relx=0.5, rely=0)

# -----------------------------------------------------------------------------------------------------------

ProjectFrame4_title = tk.Frame(MainFrame2, width=580, height=45, relief="solid", bd=2)
ProjectFrame4_title.place(relx=0.04, rely=0.05)

TestResults_LB = ttk.Label(ProjectFrame4_title, text = "Test Results", style='14Black.TLabel')
TestResults_LB.place(relx=0.5, rely=0.5, anchor='center')

ProjectFrame4 = tk.Frame(MainFrame2, width=580, height=765, relief="solid", bd=2)
ProjectFrame4.place(relx=0.04, rely=0.1)

#-------------------------------------------------------------

GraphFrame_title = tk.Frame(ProjectFrame4, width=190, height=45, relief="solid", bd=2)
GraphFrame_title.place(relx=0.015, rely=0.02)

Graph_LB = ttk.Label(GraphFrame_title, text = "Graph", style='14Black.TLabel')
Graph_LB.place(relx=0.5, rely=0.5, anchor='center')

GraphFrame = tk.Frame(ProjectFrame4, width=560, height=300, relief="solid", bd=2)
GraphFrame.place(relx=0.015, rely=0.082)

tabControl = ttk.Notebook(GraphFrame)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Test Graph 1')
tabControl.add(tab2, text='Test Graph 2')
tabControl.pack(expand = 1, fill ="both")

def create_plot():    
    x=np.arange(1, 10, 1)
    y=2*x**2
    fig = Figure(figsize=(5.5, 3), dpi=100)  #그리프 그릴 창 생성
    fig.add_subplot(1,1,1).plot(x, y) #창에 그래프 하나 추가
    canvas = FigureCanvasTkAgg(fig, master=tab1)
    canvas.draw()
    canvas.get_tk_widget().pack()


def create_sinewave():
    time = np.arange(0, 10, 0.1)
    amplitude = np.sin(time)
    plt.plot(time, amplitude)
    plt.title('Sine wave')
    plt.xlabel('Time')
    plt.ylabel('Amplitude = sin(time)') 
    fig = Figure(figsize=(5.5, 3), dpi=100)  #그리프 그릴 창 생성
    fig.add_subplot(1,1,1).plot(time, amplitude) #창에 그래프 하나 추가
    canvas = FigureCanvasTkAgg(fig, master=tab2)
    canvas.draw()
    canvas.get_tk_widget().pack()

create_plot()
create_sinewave()


# -----------------------------------------------------------------------------------------------------------

TestFrame_title = tk.Frame(ProjectFrame4, width=190, height=45, relief="solid", bd=2)
TestFrame_title.place(relx=0.015, rely=0.54)

Test_LB = ttk.Label(TestFrame_title, text = "Test Conditions", style='14Black.TLabel')
Test_LB.place(relx=0.5, rely=0.5, anchor='center')

TestFrame = tk.Frame(ProjectFrame4, width=560, height=300, relief="solid", bd=2)
TestFrame.place(relx=0.015, rely=0.602)

# -----------------------------------------------------------------------------------------------------------


# About------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------


# 메뉴바------------------------------------------------------------------------------------------------------
menubar = Menu(Cretomain)

# Adding File Menu and commands
Project = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Project', menu = Project)
Project.add_command(label ='New Project', command = lambda : New_Project(Cretomain, Project_information))
Project.add_separator()
Project.add_command(label ='Exit', command = Cretomain.destroy)


# Adding Edit Menu and commands
edit_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit_)
edit_.add_command(label ='DAQ setting', command = None)
edit_.add_command(label ='Device setting', command = lambda : edit.DeviceSetting(Cretomain))
edit_.add_command(label ='Testing information', command = None)
  
# Adding Operate Menu
Operate = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Operate', menu = Operate)
Operate.add_command(label ='Multiple Staged RC tests', command = None)
Operate.add_separator()
Operate.add_command(label ='Single RC test', command = lambda : Single_RC_test(Cretomain))
Operate.add_command(label ='Signle TS test', command = None)
 
# Adding Projects Menu
Tools = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Tools', menu = Tools)
Tools.add_command(label ='Options', command = lambda : Option(Cretomain))

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='About C-ReTo', command = lambda : about(Cretomain))

# display Menu
Cretomain.config(menu = menubar)

# -----------------------------------------------------------------------------------------------------------

# vertical separator
ttk.Separator(
    master=Cretomain,
    orient=VERTICAL,
    style='TSeparator',
    class_= ttk.Separator,
    takefocus= 1,
    cursor='man'
).pack(fill=Y, pady=10, expand=True)

# -----------------------------------------------------------------------------------------------------------
Cretomain.mainloop()

