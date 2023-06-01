import json

import ttkbootstrap as tb

from ttkbootstrap.constants import *

from tkinter.messagebox import showwarning

# from ttkbootstrap.scrolled import ScrolledFrame

TemperatureConverter = {
    ("Celsius", "Celsius"): lambda x: x,
    ("Celsius", "Kelvin"): lambda x: x + 273.15,
    ("Celsius", "Fahrenheit"): lambda x: (x * 9 / 5) + 32,

    ("Kelvin", "Celsius"): lambda x: x - 273.15,
    ("Kelvin", "Kelvin"): lambda x: x,
    ("Kelvin", "Fahrenheit"): lambda x: round((x - 273.15) * 9 / 5 + 32, 2),

    ("Fahrenheit", "Celsius"): lambda x: round((x - 32) * 5 / 9, 2),
    ("Fahrenheit", "Kelvin"): lambda x: round((x - 32) * 5 / 9 + 273.15, 2),
    ("Fahrenheit", "Fahrenheit"): lambda x: x,
}

with open("./assets/dicforgui.json", "r") as f:
    _ = f.read()
    dic = json.loads(_)

    all_conv_name: list = dic["converter"]
    all_conv_name.sort()


class Converter_gui:
    def __init__(self):
        self.theme = "superhero"

        self.root = tb.Window(title = "Converter",
                              themename = self.theme,
                              iconphoto = "./assets/uniticon.jpg",
                              resizable = (False, False)
                              )  # minsize = (720, 480)

        self.frame1 = tb.Frame(self.root, relief = "solid", borderwidth = 1)
        self.frame1['padding'] = 5
        self.frame1.pack(side = TOP, pady = 5, padx = 5, fill = X)

        self.frame1.columnconfigure(0, weight = 2)
        self.frame1.columnconfigure(1, weight = 2)

        self.label_select = tb.Label(self.frame1,
                                     text = "Select Converter",
                                     style = "inverse-primary",
                                     anchor = CENTER)
        self.label_select.grid(row = 0, column = 0, sticky = E, padx = 10, pady = 10, ipadx = 10, ipady = 4)

        self.conv_cb_var = tb.StringVar()
        self.conv_cb = tb.Combobox(self.frame1,
                                   state = "readonly",
                                   values = all_conv_name,
                                   textvariable = self.conv_cb_var,
                                   takefocus = True, style = PRIMARY)

        self.conv_cb.current(newindex = 0)
        self.conv_cb.grid(row = 0, column = 1, sticky = W, pady = 10, ipadx = 10)
        self.conv_cb.bind('<<ComboboxSelected>>', self.conv_select)

        self.frame2 = tb.LabelFrame(self.root, labelanchor = N, text = self.conv_cb_var.get())
        self.frame2.pack(side = TOP, padx = (5, 5), pady = (10, 5), )

        self.frame3 = tb.Label(self.frame2)
        self.frame3.grid(row = 0, column = 0, padx = (5, 5), ipadx = 5)

        self.unit_name = list(dic[self.conv_cb_var.get()].keys())

        self.label_from = tb.Label(self.frame3, text = "From", style = "inverse-primary", anchor = CENTER)
        self.label_from.pack(side = LEFT, padx = (10, 10), pady = 10, ipadx = 10, ipady = 4)

        self.combobox_from = tb.Combobox(self.frame3, values = self.unit_name, style = PRIMARY, state = "readonly")
        self.combobox_from.current(newindex = 0)
        self.combobox_from.pack(side = LEFT, pady = 10, ipadx = 10)

        self.label_to = tb.Label(self.frame3, text = "To", style = "inverse-primary",
                                 anchor = CENTER)
        self.label_to.pack(side = LEFT, padx = 10, pady = 10, ipadx = 10, ipady = 4)

        self.combobox_to = tb.Combobox(self.frame3, values = self.unit_name, style = PRIMARY, state = "readonly")
        self.combobox_to.current(newindex = 0)
        self.combobox_to.pack(side = LEFT, pady = 10, ipadx = 10)

        self.in_out_frame = tb.Frame(self.frame2)
        self.in_out_frame.grid(row = 1, column = 0, padx = (15, 15), sticky = EW)

        self.in_out_frame.columnconfigure(2, weight = 3)

        # register the validation callbackself.
        self.digit_func = self.root.register(self.validate_number)

        self.in_label = tb.Label(master = self.in_out_frame, style = "inverse-primary", text = "Enter Value",
                                 anchor = CENTER)
        self.in_label.grid(row = 0, column = 1, padx = 10, pady = (20, 5), ipadx = 10, ipady = 4, sticky = EW)

        self.in_value = tb.StringVar()
        self.entry = tb.Entry(master = self.in_out_frame,
                              style = PRIMARY,
                              validate = "focus",
                              textvariable = self.in_value,
                              validatecommand = (self.digit_func, '%P'))
        self.entry.grid(row = 0, column = 2, pady = (20, 5), sticky = EW)

        self.conv_button = tb.Button(master = self.in_out_frame, style = "outline-primary", text = "Convert",
                                     command = self.ans)
        self.conv_button.grid(row = 0, column = 0, rowspan = 2, sticky = NS, pady = (20, 20))

        self.out_label = tb.Label(master = self.in_out_frame, text = "Output", style = "inverse-primary",
                                  anchor = CENTER)
        self.out_label.grid(row = 1, column = 1, padx = 10, pady = (5, 20), ipadx = 10, ipady = 4, sticky = EW)

        self.out_value = tb.StringVar()
        self.out_entry = tb.Entry(master = self.in_out_frame, style = PRIMARY, textvariable = self.out_value,
                                  state = "disable")
        self.out_entry.grid(row = 1, column = 2, pady = (5, 20), sticky = EW)

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

    def ans(self):
        s = self.conv_cb_var.get()
        inp = self.in_value.get()

        from_ = self.combobox_from.get()
        to_ = self.combobox_to.get()

        if s == "Temperature Converter":
            try:
                inp = float(inp)
                ans = TemperatureConverter.get((from_, to_))(inp)
                self.out_value.set(ans)
                self.out_entry["state"] = "normal"
            except:
                showwarning(title = "Warning", message = "Invalid Input")
        else:
            from_value = dic[s].get(from_)
            to_value = dic[s].get(to_)

            try:
                inp = float(inp)
                ans = inp * (from_value / to_value)
                self.out_value.set(ans)
                self.out_entry["state"] = "normal"
            except:
                showwarning(title = "Warning", message = "Invalid Input")

    def validate_number(self, x) -> bool:
        """Validates that the input is a number"""
        if x == "":
            return True
        ls = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "."]
        for i in x.strip():
            if i not in ls:
                return False
        else:
            return True


Converter_gui()
