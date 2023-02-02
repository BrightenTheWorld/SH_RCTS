
# -----------------------------------------------------------------------------------------------------------

#모듈
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from datetime import datetime
import pickle

# -----------------------------------------------------------------------------------------------------------


# 메뉴 함수-----------------------------------------------------------------------------------------------------------

def New_Project(Cretomain, Project_information):                 # New_Project 함수에 매개변수 Cretomain을 입력해서 New_Project 함수를 변수처럼 사용
    ProjectSet = Toplevel()                 # 새 창 만들기는 tkinter의 Toplevel() 함수를 사용해야 함
    ProjectSet.title("프로젝트 정보 입력")
    ProjectSet.geometry("420x500")

    def getinfo(Cretomain):
        Project_information['Y/M/D'] = DateTime_text.get()
        Project_information['Project ID'] = Project_ID_text.get()
        Project_information['Sample ID'] = Sample_ID_text.get()
        Project_information['Operator'] = Operator_text.get()
        Project_information['SpecimenDiameter'] = SpecimenDiameter_text.get()
        Project_information['SpecimenHeight'] = SpecimenHeight_text.get()
        Project_information['SpecimenMass'] = SpecimenMass_text.get()
        Project_information['ConfiningPressure'] = ConfiningPressure_text.get()        

        messagebox.showinfo(
            message=f"설정이 완료되었습니다.",
            title="프로젝트 및 시험 설정"
        )
        ProjectSet.destroy()
# -----------------------------------------------------------------------------------------------------------
        
        # info.csv로 저장
        """
        w = csv.writer(open("info.csv", "w"))
        for key, val in Project_information.items():
            w.writerow([key, val]) # 서버 중단시 recall시 이용, RC.set
            """
        with open('Project_information.p', 'wb') as f:
            pickle.dump(Project_information, f)


        # -----------------------------------------------------------------------------------------------------------


        MainFrame1 = tk.Frame(Cretomain, width=640, height=960, relief="flat")
        MainFrame1.place(x=0, y=0)

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


        ProjectFrame2_title = tk.Frame(MainFrame1, width=580, height=45, relief="solid", bd=2)
        ProjectFrame2_title.place(relx=0.04, rely=0.35)

        Daq_LB = ttk.Label(ProjectFrame2_title, text = "DAQ", style='14Black.TLabel')
        Daq_LB.place(relx=0.5, rely=0.5, anchor='center')

        ProjectFrame2= tk.Frame(MainFrame1, width=580, height=190, relief="solid", bd=2)
        ProjectFrame2.place(relx=0.04, rely=0.4)\

        # -----------------------------------------------------------------------------------------------------------

        ProjectFrame3_title = tk.Frame(MainFrame1, width=580, height=45, relief="solid", bd=2)
        ProjectFrame3_title.place(relx=0.04, rely=0.65)

        TestConditions_LB = ttk.Label(ProjectFrame3_title, text = "Test Conditions", style='14Black.TLabel')
        TestConditions_LB.place(relx=0.5, rely=0.5, anchor='center')

        ProjectFrame3= tk.Frame(MainFrame1, width=580, height=190, relief="solid", bd=2)
        ProjectFrame3.place(relx=0.04, rely=0.7)


    # -----------------------------------------------------------------------------------------------------------

    # 확인 버튼
    button = ttk.Button(ProjectSet, text="확인", command = lambda : getinfo(Cretomain))
    button.place(x=280, y=450)

    # -----------------------------------------------------------------------------------------------------------

    # 라벨, 콤보박스 설정 ---> (라벨_lbl, 콤보박스_text)
        # 프로젝트 정보, 시간설정
    Project_info_lbl = ttk.Label(ProjectSet, text = "프로젝트 정보", style='Black.TLabel')
    Date_lbl = ttk.Label(ProjectSet, text = "날짜 : ", style='Black.TLabel')
    DateTime = datetime.today().strftime("%Y/%m/%d")
    DateTime_text = Entry(ProjectSet, width=12, font=10)
    Project_info_lbl = Project_info_lbl.place(x=20, y=20)
    Date_lbl = Date_lbl.place(x=200, y=20)
    DateTime_text.insert(0, DateTime)
    DateTime_text.place(x=240, y=20)

    # -----------------------------------------------------------------------------------------------------------

    # 1. 시험 관련 정보, frame1
    frame1 = ttk.Labelframe(ProjectSet, width=370, height=160, relief="solid", text='1. 시험 관련 정보', style='Red.TLabelframe', takefocus=TRUE)
    frame1.place(x=10, y=50)
        # Project ID
    Project_ID_lbl = ttk.Label(frame1, text = "Project ID", style='Black.TLabel')
    Project_ID_text = Entry(frame1, width=22, font=10)
    Project_ID_lbl.place(x=20, y=20)
    Project_ID_text.place(x=170, y=20)
        # Sample_Hight
    Sample_ID_lbl = ttk.Label(frame1, text = "Sample ID", style='Black.TLabel')
    Sample_ID_text = Entry(frame1, width=22, font=10)
    Sample_ID_lbl.place(x=20, y=60)
    Sample_ID_text.place(x=170, y=60)
        # 시험자
    Operator_lbl = ttk.Label(frame1, text = "시험자", style='Black.TLabel')
    Operator_text = Entry(frame1, width=22, font=10)
    Operator_lbl.place(x=20, y=100)
    Operator_text.place(x=170, y=100)

    # -----------------------------------------------------------------------------------------------------------

    # 2. 시료조건 및 시험조건, frame2
    frame2 = ttk.Labelframe(ProjectSet, width=370, height=210, relief="solid", text='2. 시료조건 및 시험조건', style='Red.TLabelframe', takefocus=TRUE)
    frame2.place(x=10, y=220)
        # 시료 직경
    SpecimenDiameter_lbl = ttk.Label(frame2, text = "시료 직경", style='Black.TLabel')
    SpecimenDiameter_text = Entry(frame2, width=15, font=10)
    mm_lbl = ttk.Label(frame2, text = "mm", style='Black.TLabel')

    SpecimenDiameter_lbl.place(x=20, y=20)
    SpecimenDiameter_text.place(x=170, y=20)
    mm_lbl.place(x=320, y=20)

        # 시료 높이
    SpecimenHeight_lbl = ttk.Label(frame2, text = "시료 높이", style='Black.TLabel')
    SpecimenHeight_text = Entry(frame2, width=15, font=10)
    mm_lbl = ttk.Label(frame2, text = "mm", style='Black.TLabel')

    SpecimenHeight_lbl.place(x=20, y=60)
    SpecimenHeight_text.place(x=170, y=60)
    mm_lbl.place(x=320, y=60)
        # 시료 질량
    SpecimenMass_lbl = ttk.Label(frame2, text = "시료 질량", style='Black.TLabel')
    SpecimenMass_text = Entry(frame2, width=15, font=10)
    mass_lbl = ttk.Label(frame2, text = "g", style='Black.TLabel')
    SpecimenMass_lbl.place(x=20, y=100)
    SpecimenMass_text.place(x=170, y=100)
    mass_lbl.place(x=320, y=100)
        # 구속응력
    ConfiningPressure_lbl = ttk.Label(frame2, text = "구속응력", style='Black.TLabel')
    ConfiningPressure_text = Entry(frame2, width=15, font=10)
    StressUnit_lbl = ttk.Label(frame2, text = "kPa", style='Black.TLabel')
    ConfiningPressure_lbl.place(x=20, y=140)
    ConfiningPressure_text.place(x=170, y=140)
    StressUnit_lbl.place(x=320, y=140)

# def Exit():
    '''Project.py파일의 Exit()함수를 참조하는 것이 아니라는 CreTo main.py 파일에 존재한다.
     Project.add_command(label ='Exit', command = Cretomain.destroy)'''


