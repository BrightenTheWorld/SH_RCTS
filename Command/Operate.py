import tkinter as tk
from tkinter import *
from tkinter import ttk



def Single_RC_test(Cretomain):
    ResonantColumnTest=Toplevel()
    ResonantColumnTest.title("Resonant Column Test")
    ResonantColumnTest.geometry("1280x960+0+10")
    ResonantColumnTest.resizable(True, True)

    ConditionFrame1 = tk.Frame(ResonantColumnTest, width=580, height=450, relief="raised", bd=1)
    ConditionFrame1.place(relx=0.04, rely=0.05)

    TerminalConnection_LB = ttk.Label(ConditionFrame1, text = "1. 다음과 같은 터미널 연결을 확인하시오.", style='10korBlack.TLabel')
    TerminalConnection_LB.place(relx=0.02, rely=0.02)

    TerminalConnection_LB = ttk.Label(ConditionFrame1, text = "가속도계 컨디셔너 출력 연결", style='10korBlack.TLabel')
    TerminalConnection_LB.place(relx=0.046, rely=0.074)

    RCCondition_LB = ttk.Label(ConditionFrame1, text = "2. 공진주 시험조건.", style='10korBlack.TLabel')
    RCCondition_LB.place(relx=0.02, rely=0.15)

    StartInputVoltage_LB = ttk.Label(ConditionFrame1, text = "시작입력전압:", style='10korBlack.TLabel')
    StartInputVoltage_LB.place(relx=0.046, rely=0.204)

    StartInputVoltage = StringVar()
    StartInputVoltage.set(0.05)
    voltage_text = Entry(ConditionFrame1, textvariable=StartInputVoltage, state=DISABLED, width=12, font=10)
    voltage_text.place(relx=0.21, rely=0.204)

    Voltage_LB = ttk.Label(ConditionFrame1, text = "V", style='10korBlack.TLabel')
    Voltage_LB.place(relx=0.4, rely=0.204)

    SweepingFrequencyRange_LB = ttk.Label(ConditionFrame1, text = "Sweeping 주파수 범위:", style='10korBlack.TLabel')
    SweepingFrequencyRange_LB.place(relx=0.046, rely=0.259)
    StartFrequency_text = Entry(ConditionFrame1, width=6, font=10)
    StartFrequency_text.place(relx=0.29, rely=0.259)
    StartFrequency_text.insert(0, 10)
    SweepingFrequency_LB = ttk.Label(ConditionFrame1, text = "Hz 에서", style='10korBlack.TLabel')
    SweepingFrequency_LB.place(relx=0.39, rely=0.259)
    EndFrequency_text = Entry(ConditionFrame1, width=6, font=10)
    EndFrequency_text.place(relx=0.49, rely=0.259)
    EndFrequency_text.insert(0, 130)
    EndFrequency_LB = ttk.Label(ConditionFrame1, text = "Hz 까지", style='10korBlack.TLabel')
    EndFrequency_LB.place(relx=0.59, rely=0.259)

    ProximitorCheckVar1=IntVar()
    c1=Checkbutton(ConditionFrame1,text="Proximitor Target 설치",variable=ProximitorCheckVar1)
    c1.place(relx=0.046, rely=0.319)

    WaitingTime_LB = ttk.Label(ConditionFrame1, text = "각 주파수 단계별 대기 시간: fine sweep", style='10korBlack.TLabel')
    WaitingTime_LB.place(relx=0.046, rely=0.375)

    current_value = StringVar(ConditionFrame1)
    spin_box = Spinbox(
        ConditionFrame1,
        from_=0,
        to=100,
        increment=1,
        textvariable=current_value,
        width=8)
    current_value.set("50")
    spin_box.place(relx=0.46, rely=0.375)

def Single_TS_test(Cretomain):
    pass