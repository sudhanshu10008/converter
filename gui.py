# import tkinter as tk
import json

import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame

with open("./assets/dictionary.json", "r") as f:
    _ = f.read()
    dic = json.loads(_)

converter_name = dic["converter"]
converter_name.sort()


class Converter_gui:
    def __init__(self) -> None:
        self.root = tb.Window(title = "Converter", iconphoto = "./assets/unit.ico")

        # converter button frame
        self.left_side_frame = ScrolledFrame(master = self.root, padding = 2, name = "all", width = 180,
                                             autohide = True, relief = "sunken")
        self.left_side_frame.pack(fill = BOTH, side = LEFT, padx = 2, pady = 1)

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

    def left_frame(self, container):
        pass

    def right_frame(self, container):
        pass


c = Converter_gui()
