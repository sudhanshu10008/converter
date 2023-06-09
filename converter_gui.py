import json
import tkinter as tk
from tkinter import font
import ttkbootstrap as tb
import customtkinter as ctk
from ttkbootstrap import utility
from ttkbootstrap.constants import *
from tkinter.messagebox import showwarning, showinfo

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


# instantiate the style with another theme_name


class ConverterGui:
    def __init__(self):
        self.root = tb.Window(
            title = "Converter",
            resizable = (False, False),
            iconphoto = "./assets/uniticon.jpg",
        )  # minsize = (720, 480)
        # themename = "litera",
        # self.root.configure(bg = "#cccccc")

        self.frame1 = tk.Frame(self.root, relief = SUNKEN, borderwidth = 1)
        self.frame1.configure(padx = 5, pady = 5)
        self.frame1.pack(side = TOP, pady = 5, padx = 5, fill = X)

        self.frame1.columnconfigure(0, weight = 2)
        self.frame1.columnconfigure(1, weight = 2)

        setting_img = tb.PhotoImage(file = "./assets/settings20.png")

        self.setting_b = tb.Button(
            master = self.frame1,
            image = setting_img,
            padding = (5, 3),
            # relief = GROOVE,
            bootstyle = (OUTLINE, PRIMARY),
            # background = 'black',
            # anchor = CENTER,
            command = self.setting_gui

        )
        self.setting_b.grid(row = 0, column = 0, sticky = W, padx = 10)

        self.label_select = tb.Label(
            self.frame1,
            text = "Select Converter",
            style = "inverse-primary",
            anchor = CENTER
        )
        self.label_select.grid(row = 0, column = 0, sticky = E, padx = 10, pady = 10, ipadx = 10, ipady = 4)

        self.conv_cb_var = tb.StringVar()
        self.conv_cb = tb.Combobox(
            self.frame1,
            state = "readonly",
            values = all_conv_name,
            textvariable = self.conv_cb_var,
            takefocus = True,
            style = PRIMARY
        )

        self.conv_cb.current(newindex = 0)
        self.conv_cb.grid(row = 0, column = 1, sticky = W, pady = 10, ipadx = 10)
        self.conv_cb.bind('<<ComboboxSelected>>', self.conv_select)

        self.cb_sb = tb.Scrollbar(
            command = self.conv_cb.xview,
            # style = ROUND
        )

        self.frame2 = tk.LabelFrame(
            self.root,
            relief = SUNKEN,
            labelanchor = N,
            text = f" {self.conv_cb_var.get()} ",
        )
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

        self.in_label = tb.Label(master = self.in_out_frame, style = DEFAULT, text = "Enter Value:",
                                 anchor = CENTER)
        self.in_label.grid(row = 0, column = 1, padx = (20, 10), pady = (20, 5), sticky = W)

        self.in_value = tb.StringVar()
        self.in_value.trace("w", self.ans2)

        self.entry = tb.Entry(
            master = self.in_out_frame,
            style = PRIMARY,
            validate = "focus",
            textvariable = self.in_value,
            validatecommand = (self.digit_func, '%P'),
        )
        self.entry.grid(row = 0, column = 2, pady = (20, 5), sticky = EW)

        self.conv_button = tb.Button(master = self.in_out_frame, style = "outline-primary", text = "Convert",
                                     command = self.ans)
        self.conv_button.grid(row = 0, column = 0, rowspan = 2, sticky = NSEW, pady = (20, 20))

        self.out_label = tb.Label(master = self.in_out_frame, text = "Output:", style = DEFAULT,
                                  anchor = CENTER)
        self.out_label.grid(row = 1, column = 1, padx = (20, 10), pady = (5, 20), sticky = W)

        self.out_value = tb.StringVar()
        self.out_entry = tb.Entry(
            master = self.in_out_frame,
            style = PRIMARY,
            textvariable = self.out_value,
            state = "readonly")
        self.out_entry.grid(row = 1, column = 2, pady = (5, 20), sticky = EW)

        self.root.mainloop()

    def setting_gui(self):
        self.setting_b.config(state = "disabled")
        Settings()
        print(self.setting_b.cget("state"))
        self.setting_b.configure(state = "normal")

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

    def ans2(self, *args):
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
                if len(inp) > 0:
                    showwarning(title = "Warning", message = "Invalid Input")
                self.out_value.set("")
        else:
            from_value = dic[s].get(from_)
            to_value = dic[s].get(to_)

            try:
                inp = float(inp)
                ans = inp * (from_value / to_value)
                self.out_value.set(ans)
                self.out_entry["state"] = "normal"
            except:
                if len(inp) > 0:
                    showwarning(title = "Warning", message = "Invalid Input")
                self.out_value.set("")

    def validate_number(self, x: str) -> bool:
        """Validates that the input is a number"""
        if x == "":
            return True
        ls = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "."]
        for i in x.strip():
            if i not in ls:
                return False
        return True


class Settings(tb.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Settings")
        self.geometry()
        # self.resizable(False, False)

        self._default = font.nametofont("TkDefaultFont")
        self._actual = self._default.actual()
        self.size = tb.IntVar(value = self._actual["size"])
        # self._family = tb.Variable(value = self._actual["family"])
        self._slant = tb.Variable(value = self._actual["slant"])
        # print(type(self._actual["size"]))
        # print(self._actual["size"])
        self._weight = tb.Variable(value = self._actual["weight"])
        self._overstrike = tb.Variable(value = self._actual["overstrike"])
        self._underline = tb.Variable(value = self._actual["underline"])
        self._font = font.Font()

        f_names = list(font.families())
        f_names.sort()
        self.default_index = f_names.index(self._actual["family"])
        self._family = tk.Variable(value = f_names)

        self.padding = {'padx': 10, 'pady': 5}

        with open("./assets/config.json") as f:
            self.config_dic = json.loads(f.read())

        self.mode_value = self.config_dic.get("appearance mode")
        self.mode_var = tb.StringVar(value = self.mode_value[0])

        self.theme_value = self.config_dic["light theme"]
        self.theme_var = tb.StringVar(value = self.theme_value[0])

        self.mode_var.trace("w", self.mode_func)
        self.theme_var.trace("w", self.theme_change)
        self._slant.trace_add("write", self._update_font_preview)
        self.size.trace_add("write", self._update_font_preview)
        self._weight.trace_add("write", self._update_font_preview)
        self._overstrike.trace_add("write", self._update_font_preview)
        self._underline.trace_add("write", self._update_font_preview)

        self.theme_settings()
        self.font_setting()
        self.buttonbox(self)

        # width = utility.scale_size(self, 500)
        # height = utility.scale_size(self, 600)
        # self.geometry(f"{width}x{height}")

    def theme_settings(self):
        theme_frame = tb.LabelFrame(
            master = self,
            text = " Appearance ",
            labelanchor = "nw",
            padding = (5, 10)
        )
        theme_frame.pack(side = TOP, **self.padding, fill = X)

        mode = tb.Label(
            master = theme_frame,
            text = "Appearance Mode:",
            style = DEFAULT,
            padding = (5, 0)
        )
        mode.grid(row = 0, column = 0, **self.padding, sticky = "nsew", )

        mode_opt = tb.Combobox(
            master = theme_frame,
            state = "readonly",
            textvariable = self.mode_var,
            values = self.mode_value,
        )
        mode_opt.grid(row = 0, column = 1, **self.padding, sticky = "nsew")

        theme_label = tb.Label(
            master = theme_frame,
            text = "Theme:",
            style = DEFAULT,
            padding = (5, 0)
        )
        theme_label.grid(row = 1, column = 0, **self.padding, sticky = "nsew", )

        global theme_opt
        theme_opt = tb.Combobox(
            master = theme_frame,
            state = "readonly",
            textvariable = self.theme_var,
            values = self.config_dic.get("light theme"),
        )
        theme_opt.grid(row = 1, column = 1, **self.padding, sticky = "nsew")

    def font_setting(self):
        font_frame = tb.LabelFrame(
            master = self,
            text = " Font Settings ",
        )
        font_frame.pack(**self.padding, fill = BOTH, expand = True)

        font_frame.columnconfigure(0, weight = 1)
        font_frame.rowconfigure(0, weight = 1)

        font_family = self.font_family_frame(master = font_frame)
        font_family.grid(row = 0, rowspan = 4, column = 0, sticky = "nsew", **self.padding)

        font_size = self.font_size_frame(master = font_frame)
        font_size.grid(row = 0, column = 1, sticky = "nsew", **self.padding)

        font_weight = self.font_weight_frame(master = font_frame)
        font_weight.grid(row = 1, column = 1, sticky = "nsew", **self.padding)

        font_slant = self.font_slant_frame(master = font_frame)
        font_slant.grid(row = 2, column = 1, sticky = "nsew", **self.padding)

        font_effect = self.font_effect_frame(master = font_frame)
        font_effect.grid(row = 3, column = 1, sticky = "nsew", **self.padding)

        font_preview = self.font_preview_frame(master = font_frame, padding = 5)
        font_preview.grid(row = 4, column = 0, columnspan = 2, sticky = "nsew")

    def font_family_frame(self, master):

        global font_family_lb
        font_family_lb = tk.Listbox(
            master = master,
            relief = SOLID,
            borderwidth = 1,
            selectmode = SINGLE,
            listvariable = self._family,
        )
        font_family_lb.selection_clear(0)

        font_family_lb.selection_set(self.default_index)
        font_family_lb.see(self.default_index)

        font_family_lb.bind("<<ListboxSelect>>", self._update_font_preview)

        font_family_lb_sb = tb.Scrollbar(
            master = font_family_lb,
            orient = tk.VERTICAL,
            style = ROUND,
            command = font_family_lb.yview,
        )
        font_family_lb_sb.pack(side = RIGHT, fill = Y)
        font_family_lb["yscrollcommand"] = font_family_lb_sb.set
        return font_family_lb

    def font_size_frame(self, master):
        size_frame = tb.Frame(
            master = master,
        )
        # size_frame.grid(row = 0, column = 1, sticky = "n", **self.padding)

        size_lbl = tb.Label(
            master = size_frame,
            text = "Size:",
            font = "TkHeadingFont",
        )
        size_lbl.grid(row = 0, column = 0, sticky = "sw")

        size_sb = tb.Spinbox(
            master = size_frame,
            from_ = 7,
            to = 30,
            increment = 1,
            textvariable = self.size,
        )
        size_sb.grid(row = 1, column = 0, sticky = NW)
        return size_frame

    def font_weight_frame(self, master):
        font_weight_lf = tb.LabelFrame(
            master = master,
            text = " Weight ",
        )
        # font_weight_lf.grid(row = 1, column = 1, sticky = "ew", **self.padding)
        opt_normal = tb.Radiobutton(
            master = font_weight_lf,
            text = "normal",
            value = "normal",
            variable = self._weight,
        )
        opt_normal.invoke()
        opt_normal.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "ew")

        opt_bold = tb.Radiobutton(
            master = font_weight_lf,
            text = "bold",
            value = "bold",
            variable = self._weight,
        )
        opt_bold.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "ew")

        return font_weight_lf

    def font_slant_frame(self, master):
        slant_lframe = tb.Labelframe(
            master, text = "Slant", padding = 5
        )
        # slant_lframe.pack(side = LEFT, fill = X, padx = 10, expand = YES)
        opt_roman = tb.Radiobutton(
            master = slant_lframe,
            text = "roman",
            value = "roman",
            variable = self._slant,
        )
        opt_roman.invoke()
        opt_roman.pack(side = LEFT, padx = 5, pady = 5)
        opt_italic = tb.Radiobutton(
            master = slant_lframe,
            text = "italic",
            value = "italic",
            variable = self._slant,
        )
        opt_italic.pack(side = LEFT, padx = 5, pady = 5)
        return slant_lframe

    def font_effect_frame(self, master):
        effects_lframe = tb.Labelframe(
            master, text = "Effects", padding = 5
        )
        # effects_lframe.pack(side = LEFT, padx = (2, 0), fill = X, expand = YES)
        opt_underline = tb.Checkbutton(
            master = effects_lframe,
            text = "underline",
            variable = self._underline,
        )
        opt_underline.pack(side = LEFT, padx = 5, pady = 5)
        opt_overstrike = tb.Checkbutton(
            master = effects_lframe,
            text = "overstrike",
            variable = self._overstrike,
        )
        opt_overstrike.pack(side = LEFT, padx = 5, pady = 5)
        return effects_lframe

    def font_preview_frame(self, master, padding: int):
        container = tb.Frame(master, padding = padding)
        # container.pack(fill = BOTH, expand = YES, anchor = N)

        header = tb.Label(
            container,
            text = "Preview",
            font = "TkHeadingFont",
        )
        header.pack(fill = X, pady = 2, anchor = N)

        content = "The quick brown fox jumps over the lazy dog."

        self.preview_text = tb.Text(
            master = container,
            height = 2,
            # font = self._font,
        )
        # self.preview_text.configure(height = utility.scale_size(self.preview_text, 3))
        # self.preview_text.configure(width = utility.scale_size(self.preview_text, 20))
        self.preview_text.insert(END, content)
        self.preview_text.pack(fill = BOTH, expand = YES)
        # container.pack_propagate(False)

        return container

    def buttonbox(self, master):
        container = tb.Frame(master, padding = (5, 10))
        container.pack(fill = X, side = BOTTOM, )

        ok_btn = tb.Button(
            master = container,
            bootstyle = "primary",
            text = "OK",
            # command = self._on_submit,
        )
        ok_btn.pack(side = RIGHT, padx = 5)
        # ok_btn.bind("<Return>", lambda _: ok_btn.invoke())

        cancel_btn = tb.Button(
            master = container,
            bootstyle = "secondary",
            text = "Cancel",
            command = self.destroy,
        )
        cancel_btn.pack(side = RIGHT, padx = 5)
        # cancel_btn.bind("<Return>", lambda _: cancel_btn.invoke())

    def _update_font_preview(self, *_):
        _ = font_family_lb.curselection()
        family = font_family_lb.get(_)
        size = self.size.get()
        slant = self._slant.get()
        overstrike = self._overstrike.get()
        underline = self._underline.get()

        self._font.config(
            family = family,
            size = size,
            slant = slant,
            overstrike = overstrike,
            underline = underline,
        )
        try:
            self.preview_text.configure(font = self._font)
        except:
            pass
        self._result = self._font

    def mode_func(self, *_):
        mode = self.mode_var.get()
        if mode == "Light":
            theme_opt.configure(values = self.config_dic.get("light theme"))
            theme_opt.set(value = self.config_dic.get("light theme")[0])
        else:
            theme_opt.configure(values = self.config_dic.get("dark theme"))
            theme_opt.set(value = self.config_dic.get("dark theme")[0])

    def theme_change(self, *_):
        theme_name = self.theme_var.get()
        style = tb.Style()
        style.theme_use(theme_name)

    # def font_change(self, event):
    #     print(self.font_family_names.get())


ConverterGui()
