import tkinter as tk
from tkinter import font
import ttkbootstrap as ttk
from ttkbootstrap import utility
from ttkbootstrap.constants import *
from ttkbootstrap.localization import MessageCatalog


class FontDialog:
    """A dialog that displays a variety of options for choosing a font.

    This dialog constructs and returns a `Font` object based on the
    options selected by the user. The initial font is based on OS
    settings and will vary.

    The font object is returned when the **Ok** button is pressed and
    can be passed to any widget that accepts a _font_ configuration
    option.

    ![](../../assets/dialogs/querybox-get-font.png)
    """

    def __init__(self, title="Font Selector", parent=None):
        title = MessageCatalog.translate(title)
        self._style = ttk.Style()
        self._default = font.nametofont("TkDefaultFont")
        self._actual = self._default.actual()
        self._size = ttk.Variable(value = self._actual["size"])
        self._family = ttk.Variable(value = self._actual["family"])
        self._slant = ttk.Variable(value = self._actual["slant"])
        self._weight = ttk.Variable(value = self._actual["weight"])
        self._overstrike = ttk.Variable(value = self._actual["overstrike"])
        self._underline = ttk.Variable(value = self._actual["underline"])
        self._preview_font = font.Font()
        self._slant.trace_add("write", self._update_font_preview)
        self._weight.trace_add("write", self._update_font_preview)
        self._overstrike.trace_add("write", self._update_font_preview)
        self._underline.trace_add("write", self._update_font_preview)

        _headingfont = font.nametofont("TkHeadingFont")
        _headingfont.configure(weight = "bold")

        self._update_font_preview()
        self._families = {self._family.get()}
        for f in font.families():
            if all([f, not f.startswith("@"), "emoji" not in f.lower()]):
                self._families.add(f)

        self._toplevel = ttk.Toplevel(title = title)
        self.create_body(master = self._toplevel)
        self.create_buttonbox(master = self._toplevel)

    def create_body(self, master):
        width = utility.scale_size(master, 600)
        height = utility.scale_size(master, 500)
        self._toplevel.geometry(f"{width}x{height}")

        family_size_frame = ttk.Frame(master, padding = 10)
        family_size_frame.pack(fill = X, anchor = N)
        self._initial_focus = self._font_families_selector(family_size_frame)
        self._font_size_selector(family_size_frame)
        self._font_options_selectors(master, padding = 10)
        self._font_preview(master, padding = 10)

    def create_buttonbox(self, master):
        container = ttk.Frame(master, padding = (5, 10))
        container.pack(fill = X)

        ok_btn = ttk.Button(
            master = container,
            bootstyle = "primary",
            text = MessageCatalog.translate("OK"),
            command = self._on_submit,
        )
        ok_btn.pack(side = RIGHT, padx = 5)
        ok_btn.bind("<Return>", lambda _: ok_btn.invoke())

        cancel_btn = ttk.Button(
            master = container,
            bootstyle = "secondary",
            text = MessageCatalog.translate("Cancel"),
            command = self._on_cancel,
        )
        cancel_btn.pack(side = RIGHT, padx = 5)
        cancel_btn.bind("<Return>", lambda _: cancel_btn.invoke())

    def _font_families_selector(self, master):
        container = ttk.Frame(master)
        container.pack(fill = BOTH, expand = YES, side = LEFT)

        header = ttk.Label(
            container,
            text = MessageCatalog.translate("Family"),
            font = "TkHeadingFont",
        )
        header.pack(fill = X, pady = (0, 2), anchor = N)

        listbox = ttk.Treeview(
            master = container,
            height = 5,
            show = "",
            columns = [0],
        )
        listbox.column(0, width = utility.scale_size(listbox, 250))
        listbox.pack(side = LEFT, fill = BOTH, expand = YES)

        listbox_vbar = ttk.Scrollbar(
            container,
            command = listbox.yview,
            orient = VERTICAL,
            bootstyle = "rounded",
        )
        listbox_vbar.pack(side = RIGHT, fill = Y)
        listbox.configure(yscrollcommand = listbox_vbar.set)

        for f in self._families:
            listbox.insert("", iid = f, index = END, tags = [f], values = [f])
            listbox.tag_configure(f, font = (f, self._size.get()))

        iid = self._family.get()
        listbox.selection_set(iid)  # select default value
        listbox.see(iid)  # ensure default is visible
        listbox.bind(
            "<<TreeviewSelect>>", lambda e: self._on_select_font_family(e)
        )
        return listbox

    def _font_size_selector(self, master):
        container = ttk.Frame(master)
        container.pack(side = LEFT, fill = Y, padx = (10, 0))

        header = ttk.Label(
            container,
            text = MessageCatalog.translate("Size"),
            font = "TkHeadingFont",
        )
        header.pack(fill = X, pady = (0, 2), anchor = N)

        sizes_listbox = ttk.Treeview(container, height = 7, columns = [0], show = "")
        sizes_listbox.column(0, width = utility.scale_size(sizes_listbox, 24))

        sizes = [*range(8, 13), *range(13, 30, 2), 36, 48, 72]
        for s in sizes:
            sizes_listbox.insert("", iid = s, index = END, values = [s])

        iid = self._size.get()
        sizes_listbox.selection_set(iid)
        sizes_listbox.see(iid)
        sizes_listbox.bind(
            "<<TreeviewSelect>>", lambda e: self._on_select_font_size(e)
        )

        sizes_listbox_vbar = ttk.Scrollbar(
            master = container,
            orient = VERTICAL,
            command = sizes_listbox.yview,
            bootstyle = "round",
        )
        sizes_listbox.configure(yscrollcommand = sizes_listbox_vbar.set)
        sizes_listbox.pack(side = LEFT, fill = Y, expand = YES, anchor = N)
        sizes_listbox_vbar.pack(side = LEFT, fill = Y, expand = YES)

    def _font_options_selectors(self, master, padding: int):
        container = ttk.Frame(master, padding = padding)
        container.pack(fill = X, padx = 2, pady = 2, anchor = N)

        weight_lframe = ttk.Labelframe(
            container, text = MessageCatalog.translate("Weight"), padding = 5
        )
        weight_lframe.pack(side = LEFT, fill = X, expand = YES)
        opt_normal = ttk.Radiobutton(
            master = weight_lframe,
            text = MessageCatalog.translate("normal"),
            value = "normal",
            variable = self._weight,
        )
        opt_normal.invoke()
        opt_normal.pack(side = LEFT, padx = 5, pady = 5)
        opt_bold = ttk.Radiobutton(
            master = weight_lframe,
            text = MessageCatalog.translate("bold"),
            value = "bold",
            variable = self._weight,
        )
        opt_bold.pack(side = LEFT, padx = 5, pady = 5)

        slant_lframe = ttk.Labelframe(
            container, text = MessageCatalog.translate("Slant"), padding = 5
        )
        slant_lframe.pack(side = LEFT, fill = X, padx = 10, expand = YES)
        opt_roman = ttk.Radiobutton(
            master = slant_lframe,
            text = MessageCatalog.translate("roman"),
            value = "roman",
            variable = self._slant,
        )
        opt_roman.invoke()
        opt_roman.pack(side = LEFT, padx = 5, pady = 5)
        opt_italic = ttk.Radiobutton(
            master = slant_lframe,
            text = MessageCatalog.translate("italic"),
            value = "italic",
            variable = self._slant,
        )
        opt_italic.pack(side = LEFT, padx = 5, pady = 5)

        effects_lframe = ttk.Labelframe(
            container, text = MessageCatalog.translate("Effects"), padding = 5
        )
        effects_lframe.pack(side = LEFT, padx = (2, 0), fill = X, expand = YES)
        opt_underline = ttk.Checkbutton(
            master = effects_lframe,
            text = MessageCatalog.translate("underline"),
            variable = self._underline,
        )
        opt_underline.pack(side = LEFT, padx = 5, pady = 5)
        opt_overstrike = ttk.Checkbutton(
            master = effects_lframe,
            text = MessageCatalog.translate("overstrike"),
            variable = self._overstrike,
        )
        opt_overstrike.pack(side = LEFT, padx = 5, pady = 5)

    def _font_preview(self, master, padding: int):
        container = ttk.Frame(master, padding = padding)
        container.pack(fill = BOTH, expand = YES, anchor = N)

        header = ttk.Label(
            container,
            text = MessageCatalog.translate("Preview"),
            font = "TkHeadingFont",
        )
        header.pack(fill = X, pady = 2, anchor = N)

        content = MessageCatalog.translate(
            "The quick brown fox jumps over the lazy dog."
        )
        self._preview_text = ttk.Text(
            master = container,
            height = 3,
            font = self._preview_font,
            highlightbackground = self._style.colors.primary,
        )
        self._preview_text.insert(END, content)
        self._preview_text.pack(fill = BOTH, expand = YES)
        container.pack_propagate(False)

    def _on_select_font_family(self, e):
        tree: ttk.Treeview = self._toplevel.nametowidget(e.widget)
        fontfamily = tree.selection()[0]
        self._family.set(value = fontfamily)
        self._update_font_preview()

    def _on_select_font_size(self, e):
        tree: ttk.Treeview = self._toplevel.nametowidget(e.widget)
        fontsize = tree.selection()[0]
        self._size.set(value = fontsize)
        self._update_font_preview()

    def _on_submit(self) -> font.Font:
        self._toplevel.destroy()
        return self._result

    def _on_cancel(self):
        self._toplevel.destroy()

    def _update_font_preview(self, *_):
        family = self._family.get()
        size = self._size.get()
        slant = self._slant.get()
        overstrike = self._overstrike.get()
        underline = self._underline.get()

        self._preview_font.config(
            family = family,
            size = size,
            slant = slant,
            overstrike = overstrike,
            underline = underline,
        )
        try:
            self._preview_text.configure(font = self._preview_font)
        except:
            pass
        self._result = self._preview_font

    def __str__(self):
        family = self._family.get()
        size = self._size.get()
        slant = self._slant.get()
        overstrike = self._overstrike.get()
        underline = self._underline.get()
        return f"{family}, {size}, {slant}, {overstrike}, {underline}"


def dialogs_box():
    font1 = font.Font()
    f = FontDialog(title = "font dialogs")
    print(f)
    # f_ = str(f)
    # button.configure(font = d)
    # text.configure(font = f)


# create the root window
root = tk.Tk()
root.geometry("500x500")

button = ttk.Button(root, text = "button", command = dialogs_box)
button.pack()

text = ttk.Text(
    master = root,
)
text.pack()
text.insert('1.0', 'This is a Text widget demo')
# d = dialogs.Dialog(title = "dialogs")

root.mainloop()
