import json

import ttkbootstrap as tb

from ttkbootstrap.constants import *

# from ttkbootstrap.scrolled import ScrolledFrame

with open("./assets/dicforgui.json", "r") as f:
    _ = f.read()
    dic = json.loads(_)

    all_conv_name: list = dic["converter"]
    all_conv_name.sort()


class Converter_gui:
    def __init__(self):
        self.theme = "litera"

        self.root = tb.Window(title = "Converter",
                              themename = self.theme,
                              iconphoto = "./assets/uniticon.jpg",
                              )  # minsize = (720, 480)

        self.frame1 = tb.Frame(self.root)
        self.frame1.pack(side = TOP, pady = 5)

        self.label_select = tb.Label(self.frame1,
                                     text = "Select Converter",
                                     style = "inverse-primary",
                                     anchor = CENTER)
        self.label_select.pack(anchor = N, side = LEFT, padx = 10, pady = 10, ipadx = 10, ipady = 4)

        self.conv_cb_var = tb.StringVar()
        self.conv_cb = tb.Combobox(self.frame1,
                                   state = "readonly",
                                   values = all_conv_name,
                                   textvariable = self.conv_cb_var,
                                   takefocus = True, style = PRIMARY)
        self.conv_cb.current(newindex = 0)
        self.conv_cb.pack(anchor = N, side = LEFT, pady = 10, ipadx = 10)
        self.conv_cb.bind('<<ComboboxSelected>>', self.conv_select)

        self.frame2 = tb.LabelFrame(self.root,
                                    labelanchor = N,
                                    text = self.conv_cb_var.get())
        self.frame2.pack(side = TOP, padx = (5, 5), ipadx = 5)

        self.unit_name = list(dic[self.conv_cb_var.get()].keys())
        # print(self.unit_name)

        self.label_from = tb.Label(self.frame2, text = "From", style = "inverse-primary", anchor = CENTER)
        self.label_from.pack(anchor = CENTER, side = LEFT, padx = (10, 10), pady = 10, ipadx = 10, ipady = 4)

        self.combobox_from = tb.Combobox(self.frame2, values = self.unit_name, style = PRIMARY, state = "readonly")
        self.combobox_from.current(newindex = 0)
        self.combobox_from.pack(anchor = CENTER, side = LEFT, pady = 10, ipadx = 10)

        self.label_to = tb.Label(self.frame2, text = "To", style = "inverse-primary",
                                 anchor = CENTER)
        self.label_to.pack(anchor = CENTER, side = LEFT, padx = 10, pady = 10, ipadx = 10, ipady = 4)

        self.combobox_to = tb.Combobox(self.frame2, values = self.unit_name, style = PRIMARY, state = "readonly")
        self.combobox_to.current(newindex = 0)
        self.combobox_to.pack(anchor = CENTER, side = LEFT, pady = 10, ipadx = 10)

        self.root.mainloop()

    def conv_select(self, event):
        s = self.conv_cb_var.get()
        self.frame2["text"] = s

        if s == "Temperature Converter":
            unit_name = list(dic[s])
        else:
            unit_name = list(dic[s].keys())

        self.combobox_from.config(values = unit_name)
        self.combobox_to.config(values = unit_name)

        self.combobox_from.current(newindex = 0)
        self.combobox_to.current(newindex = 0)


c = Converter_gui()
