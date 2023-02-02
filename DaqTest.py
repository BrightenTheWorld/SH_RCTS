import nidaqmx
from tkinter import *
from tkinter import ttk

# with nidaqmx.Task() as task:
#     task.ai_channels.add_ai_voltage_chan("PXI1Slot2/ai0")
#     data = task.read()
#     print(data)

# -----------------------------------------------------------------------------------------------------------

root = Tk()

# Create a combobox widget
combo = ttk.Combobox(root)
combo.pack()

# Get a list of channels for the device
channels = nidaqmx.system.System.local().devices[0].ai_physical_channels

# Insert the channels into the combobox
combo['values'] = channels

root.mainloop()