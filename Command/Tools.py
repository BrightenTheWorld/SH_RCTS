import tkinter as tk
from tkinter import *
from tkinter import ttk

def Option(Cretomain):
    User_Interface_Event_Handler=Toplevel()
    User_Interface_Event_Handler.title("User Interface Event Handler")
    User_Interface_Event_Handler.geometry("500x680+300+100")
    User_Interface_Event_Handler.resizable(True, True)
    
    # -----------------------------------------------------------------------------------------------------------

    # 스타일 설정
    s4 = ttk.Style(User_Interface_Event_Handler)
    s4.configure('Black.TLabelframe.Label', font=('Times New Roman', 10, 'bold'), foreground='black')

    # -----------------------------------------------------------------------------------------------------------

    frame1 = ttk.Labelframe(User_Interface_Event_Handler, width=480, height=580, relief="solid", text='공진주 시험 설정', style='Black.TLabelframe')
    frame1.place(relx=0.02, rely=0.05)
    
    ACC_frame = ttk.Labelframe(frame1, text = "가속도계", style='Black.TLabel')
    ACC_frame.place(relx=0.02, rely=0.03)
    
    scrollbar1=tk.Scrollbar(ACC_frame, orient='vertical')
    scrollbar1.pack(side='right', fill='y')

    treeview1=ttk.Treeview(ACC_frame, height=3, columns=["#1", "#2"], displaycolumns=["#1", "#2"], yscrollcommand = scrollbar1.set)
    treeview1.pack(side='left')

    scrollbar1["command"]=treeview1.yview


    treeview1.column("#0", width=145, anchor="center")
    treeview1.heading("#0", text="Part ID", anchor="center")

    treeview1.column("#1", width=145, anchor="center")
    treeview1.heading("#1", text="Censitivity, V/g", anchor="center")

    treeview1.column("#2", width=145, anchor="center")
    treeview1.heading("#2", text="Gain", anchor="center")

    treelist1=["0.49", 1]
    treeview1.insert('', 'end', text="가속도계1", values=treelist1)

    # -----------------------------------------------------------------------------------------------------------

    DrivePlate_frame = ttk.Labelframe(frame1, text = "가진판", style='Black.TLabel')
    DrivePlate_frame.place(relx=0.02, rely=0.25)
    
    scrollbar2=tk.Scrollbar(DrivePlate_frame, orient='vertical')
    scrollbar2.pack(side='right', fill='y')

    treeview2=ttk.Treeview(DrivePlate_frame, height=3, columns=["#1", "#2"], displaycolumns=["#1", "#2"], yscrollcommand = scrollbar2.set)
    treeview2.pack(side='left')

    scrollbar2["command"]=treeview2.yview


    treeview2.column("#0", width=145, anchor="center")
    treeview2.heading("#0", text="Part ID", anchor="center")

    treeview2.column("#1", width=145, anchor="center")
    treeview2.heading("#1", text="I_O, 10^6 g-mm2", anchor="center")

    treeview2.column("#2", width=145, anchor="center")
    treeview2.heading("#2", text="R_acc, mm", anchor="center")


    treelist2=["2.996", 53]
    treeview2.insert('', 'end', text="가진판", values=treelist2)

    # -----------------------------------------------------------------------------------------------------------
    
    TopCap_frame = ttk.Labelframe(frame1, text = "Top Cap", style='Black.TLabel')
    TopCap_frame.place(relx=0.02, rely=0.47)
    
    scrollbar3=tk.Scrollbar(TopCap_frame, orient='vertical')
    scrollbar3.pack(side='right', fill='y')

    treeview3=ttk.Treeview(TopCap_frame, height=3, columns=["#1"], displaycolumns=["#1"], yscrollcommand = scrollbar3.set)
    treeview3.pack(side='left')

    scrollbar3["command"]=treeview3.yview


    treeview3.column("#0", width=80, anchor="center")
    treeview3.heading("#0", text="Part ID", anchor="center")

    treeview3.column("#1", width=120, anchor="center")
    treeview3.heading("#1", text="I_tc, 10^3 g-mm2", anchor="center")

    treelist3=["61.98"]
    treeview3.insert('', 'end', text="50mm", values=treelist3)
    
    # -----------------------------------------------------------------------------------------------------------
    
    target_frame = ttk.Labelframe(frame1, text = "간극측정기 타겟", style='Black.TLabel')
    target_frame.place(relx=0.52, rely=0.47)
    
    scrollbar4=tk.Scrollbar(target_frame, orient='vertical')
    scrollbar4.pack(side='right', fill='y')

    treeview4=ttk.Treeview(target_frame, height=3, columns=["#1"], displaycolumns=["#1"], yscrollcommand = scrollbar4.set)
    treeview4.pack(side='left')

    scrollbar4["command"]=treeview4.yview


    treeview4.column("#0", width=80, anchor="center")
    treeview4.heading("#0", text="Part ID", anchor="center")

    treeview4.column("#1", width=120, anchor="center")
    treeview4.heading("#1", text="I_tg, 10^3 g-mm2", anchor="center")

    treelist4=["18.42"]
    treeview4.insert('', 'end', text="#1", values=treelist4)

    # -----------------------------------------------------------------------------------------------------------

    TS_frame = ttk.Labelframe(frame1, text = "비틂전단시험 설정", style='Black.TLabel')
    TS_frame.place(relx=0.02, rely=0.69)
    
    scrollbar5=tk.Scrollbar(TS_frame, orient='vertical')
    scrollbar5.pack(side='right', fill='y')

    treeview5=ttk.Treeview(TS_frame, height=3, columns=["#1", "#2", "3", "4"], displaycolumns=["#1", "#2", "3", "4"], yscrollcommand = scrollbar5.set)
    treeview5.pack(side='left')

    scrollbar5["command"]=treeview5.yview


    treeview5.column("#0", width=70, anchor="center")
    treeview5.heading("#0", text="Part ID", anchor="center")

    treeview5.column("#1", width=115, anchor="center")
    treeview5.heading("#1", text="Angle, 10-3 rad/V", anchor="center")

    treeview5.column("#2", width=105, anchor="center")
    treeview5.heading("#2", text="Torque, Nm/V", anchor="center")

    treeview5.column("#3", width=75, anchor="center")
    treeview5.heading("#3", text="Filter A", anchor="center")
    
    treeview5.column("#4", width=75, anchor="center")
    treeview5.heading("#4", text="Filter B", anchor="center")

    treelist5=[2.67, 0.1645, 2.8981, 0.9913]
    treeview5.insert('', 'end', text="sys#1", values=treelist5)
