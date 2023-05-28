# import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from assets.converter_dict import dictionary as dic
from ttkbootstrap.scrolled import ScrolledFrame

# converter= [
#         'Area Converter',
#         "Angle Converter",
#         'Length Converter',
#         'Time Converter',
#         "Volume Converter",
#         'Weight Converter',
#         "Speed Converter",
#         "Storage Converter",
#         "Energy Converter",
#         'Temperature Converter',
#     ]
converter_name = dic["converter"]
converter_name.sort()


class Converter_gui:
    def __init__(self) -> None:
        self.root = tb.Window(title = "Converter", iconphoto="./assets/unit.ico")

        # converter button frame
        self.left_side_frame = ScrolledFrame(master = self.root, padding = 2, name = "all", width = 180,
                                             autohide = True)
        self.left_side_frame.pack(fill = BOTH, side = LEFT, padx = 1, pady = 2)

        # main converter frame
        self.right_side_frame = tb.Frame(master = self.root, padding = 2, width = 180)
        self.right_side_frame.pack(fill = BOTH, side = LEFT)

        # main converter ui
        self.con_to_frame = ScrolledFrame(master = self.right_side_frame, padding = 2, width = 180, autohide = True)
        self.con_to_frame.pack(fill = BOTH, side = LEFT, padx = 1, pady = 2)

        for i in dic["converter"]:
            pass

        self.con_in_frame = ScrolledFrame(master = self.right_side_frame, padding = 2, width = 180, autohide = True)
        self.con_in_frame.pack(fill = BOTH, side = RIGHT, padx = 1, pady = 2)

        # all converter buttons
        for i in converter_name:
            name = i.split()[0]
            self.name = tb.Button(master = self.left_side_frame, text = name, width = 15)
            self.name.pack(side = TOP, pady = 5)

        self.root.mainloop()


c = Converter_gui()
