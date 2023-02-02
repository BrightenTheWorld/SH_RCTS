
# -----------------------------------------------------------------------------------------------------------

#모듈
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import nidaqmx

# with nidaqmx.Task() as task:
#     task.ai_channels.add_ai_voltage_chan("PXI1Slot2/ai0")
#     data = task.read()
#     print(data)

# -----------------------------------------------------------------------------------------------------------
class edit():
    test_system_setting = {'acc':None, '가진판':None, 'Target':None, 'Torque':None, 'Topcap':None, '파형발생장치':None}
    AD_board_terminal_setting = {}


    def DeviceSetting(Cretomain):

        SetOption = tk.Toplevel()
        SetOption.title("공진주 / 비틂전단 시험기 설정")
        SetOption.geometry("390x750+0+10")

        # -----------------------------------------------------------------------------------------------------------

        # 스타일 설정
        s1 = ttk.Style()
        s1.configure('Blue.TLabelframe.Label', font=('Times New Roman', 15, 'bold'), foreground='blue')
        s2 = ttk.Style()
        s2.configure('Black.TLabel', font=('Times New Roman', 10, 'bold'), foreground='black')

        # -----------------------------------------------------------------------------------------------------------

        # 프레임 설정
        frame1 = ttk.Labelframe(SetOption, width=370, height=300, relief="solid", text='1. 시험 시스템 설정', style='Blue.TLabelframe')
        frame2 = ttk.Labelframe(SetOption, width=370, height=340, relief="solid", text='2. A/D 보드 터미널 설정', style='Blue.TLabelframe')

        frame1.place(x=10, y=20)
        frame2.place(x=10, y=350)

        # -----------------------------------------------------------------------------------------------------------

        # 라벨, 콤보박스 설정 ---> (라벨_lbl, 콤보박스_combo)

        # 1. 시험시스템 설정, frame1
            # 가속도계
        acc_lbl = ttk.Label(frame1, text = "가속도계", style='Black.TLabel')
        acc_combo = ttk.Combobox(frame1, state="readonly", values=["가속도계 1", "가속도계 2", "가속도계 3", "가속도계 4"], font=10)
        acc_combo.current(0)
        acc_lbl.place(x=20, y=20)
        acc_combo.place(x=170, y=20)
            # 가진판
        가진판_lbl = ttk.Label(frame1, text = "가진판", style='Black.TLabel')
        가진판_combo = ttk.Combobox(frame1, state="readonly", values=["가진판", "..."], font=10)
        가진판_combo.current(0)
        가진판_lbl.place(x=20, y=60)
        가진판_combo.place(x=170, y=60)
            # Target for proximity
        Target_lbl = ttk.Label(frame1, text = "Target for proximity", style='Black.TLabel')
        Target_combo = ttk.Combobox(frame1, state="readonly", values=["#1", "#2", "#3", "#4"], font=10)
        Target_combo.current(0)
        Target_lbl.place(x=20, y=100)
        Target_combo.place(x=170, y=100)
            # Torque system ID
        Torque_lbl = ttk.Label(frame1, text = "Torque system ID", style='Black.TLabel')
        Torque_combo = ttk.Combobox(frame1, state="readonly", values=["sys#1", "sys#2", "sys#3"], font=10)
        Torque_combo.current(0)
        Torque_lbl.place(x=20, y=140)
        Torque_combo.place(x=170, y=140)
            # Topcap
        Topcap_lbl = ttk.Label(frame1, text = "Topcap", style='Black.TLabel')
        Topcap_combo = ttk.Combobox(frame1, state="readonly", values=["50mm", "100mm"], font=10)
        Topcap_combo.current(0)
        Topcap_lbl.place(x=20, y=180)
        Topcap_combo.place(x=170, y=180)
            # 파형발생장치
        파형발생장치_lbl = ttk.Label(frame1, text = "파형발생장치", style='Black.TLabel')
        # DAQboard = 
        파형발생장치_combo = ttk.Combobox(frame1, state="readonly", values=["DAQ보드1", "DAQ보드2", "DAQ보드3"], font=10)
        파형발생장치_combo.current(0)
        파형발생장치_lbl.place(x=20, y=220)
        파형발생장치_combo.place(x=170, y=220)


        
        # -----------------------------------------------------------------------------------------------------------

        # 2. A/D 보드 터미널 설정, frame2
            # 신호획득측
        신호획득측_lbl = ttk.Label(frame2, text = "신호획득측", style='Black.TLabel')
        ttk.Separator(frame2).place(x=95, y=10, width=260)
        신호획득측_lbl.place(x=20, y=0)
            # 가속도계 컨디셔너 출력
        acc_conditioner_lbl = ttk.Label(frame2, text = "가속도계 컨디셔너 출력", style='Black.TLabel')
        acc_conditioner_combo = ttk.Combobox(frame2, state="readonly", values=["Dev1/ai1","Dev2/ai1","..."], font=10)
        acc_conditioner_combo.current(0)
        acc_conditioner_lbl.place(x=20, y=30)
        acc_conditioner_combo.place(x=170, y=30)
            # NEC 9B02의 A채널
        NEC_9B02_Ch1_lbl = ttk.Label(frame2, text = "NEC 9B02의 A채널", style='Black.TLabel')
        NEC_9B02_Ch1_combo = ttk.Combobox(frame2, state="readonly", values=["Dev1/ai2","Dev2/ai2","..."], font=10)
        NEC_9B02_Ch1_combo.current(0)
        NEC_9B02_Ch1_lbl.place(x=20, y=70)
        NEC_9B02_Ch1_combo.place(x=170, y=70)
            # NEC 9B02의 B채널
        NEC_9B02_Ch2_lbl = ttk.Label(frame2, text = "NEC 9B02의 B채널", style='Black.TLabel')
        NEC_9B02_Ch2_combo = ttk.Combobox(frame2, state="readonly", values=["Dev1/ai3","Dev2/ai3","..."], font=10)
        NEC_9B02_Ch2_combo.current(0)
        NEC_9B02_Ch2_lbl.place(x=20, y=110)
        NEC_9B02_Ch2_combo.place(x=170, y=110)
            # 함수발생기 SYNC
        SYNC_lbl = ttk.Label(frame2, text = "함수 발생기 SYNC", style='Black.TLabel')
        SYNC_combo = ttk.Combobox(frame2, state="readonly", values=["Dev1/ai4","Dev2/ai4","..."], font=10)
        SYNC_combo.current(0)
        SYNC_lbl.place(x=20, y=150)
        SYNC_combo.place(x=170, y=150)
            # 파형발생측
        파형발생측_lbl = ttk.Label(frame2, text = "파형발생측", style='Black.TLabel')
        ttk.Separator(frame2).place(x=95, y=210, width=260)
        파형발생측_lbl.place(x=20, y=200)
            # 출력채널
        output_Ch_lbl = ttk.Label(frame2, text = "출력 채널", style='Black.TLabel')
        output_Ch_combo = ttk.Combobox(frame2, state="readonly", values=["Dev1/ao0","Dev2/ao0","..."], font=10)
        output_Ch_combo.current(0)
        output_Ch_lbl.place(x=20, y=230)
        output_Ch_combo.place(x=170, y=230)
            # 분해능
        resolution_lbl = ttk.Label(frame2, text = "분해능", style='Black.TLabel')
        resolution_text = ttk.Entry(frame2, width=10)
        resolution_text.insert(0, "500")
        sampleNum_lbl = ttk.Label(frame2, text=":1 파장 내 샘플 수", style='Black.TLabel')
        resolution_lbl.place(x=20, y=270)
        resolution_text.place(x=170, y=270)
        sampleNum_lbl.place(x=250, y=270)


        # -----------------------------------------------------------------------------------------------------------
        def __init__(self):
            edit.test_system_setting['acc'] = acc_combo.get()
            edit.test_system_setting['가진판'] = 가진판_combo.get()
            edit.test_system_setting['Target'] = Target_combo.get()
            edit.test_system_setting['Torque'] = Torque_combo.get()
            edit.test_system_setting['Topcap'] = Topcap_combo.get()
            edit.test_system_setting['파형발생장치'] = 파형발생장치_combo.get()
        


        def get_value():
            print([acc_combo.get(), 가진판_combo.get(), Target_combo.get(), Torque_combo.get(), Topcap_combo.get(), 파형발생장치_combo.get()])
            print([acc_conditioner_combo.get(), NEC_9B02_Ch1_combo.get(), NEC_9B02_Ch2_combo.get(), SYNC_combo.get(), output_Ch_combo.get(), resolution_text.get()])
            messagebox.showinfo(
                message=f"설정이 완료되었습니다.",
                title="시험기 설정"
            )


        button = ttk.Button(SetOption, text="설정", command=get_value)
        button.place(x=280, y=700)

# -----------------------------------------------------------------------------------------------------------


