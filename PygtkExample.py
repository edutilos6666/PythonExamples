import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, Gdk



def example11():
    """Notebook example"""
    class MyWindow(Gtk.Window):
        def __init__(self):
            Gtk.Window.__init__(self, title = "Simple Notebook Example")
            self.set_border_width(3)
            self.notebook = Gtk.Notebook()
            self.add(self.notebook)

            self.page1 = Gtk.Box()
            self.page1.set_border_width(10)
            self.page1.add(Gtk.Label("Default Page!"))
            self.notebook.append_page(self.page1, Gtk.Label("Plain Title"))

            self.page2 = Gtk.Box()
            self.page2.set_border_width(10)
            self.page2.add(Gtk.Label("A page with an image for a Title."))
            self.notebook.append_page(self.page2,
                                      Gtk.Image.new_from_icon_name("help-about", Gtk.IconSize.MENU))

    win = MyWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

def example10():
    """FlowBox example"""
    class FlowBoxWindow(Gtk.Window):
        def __init__(self):
            Gtk.Window.__init__(self, title = "FlowBox Demo")
            self.set_border_width(10)
            self.set_default_size(400, 400)

            header = Gtk.HeaderBar(title = "Flow Box")
            header.set_subtitle("Sample FlowBox app")
            header.props.show_close_button = True

            self.set_titlebar(header)

            scrolled = Gtk.ScrolledWindow()
            scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

            flowbox = Gtk.FlowBox()
            flowbox.set_valign(Gtk.Align.START)
            flowbox.set_valign(Gtk.Align.START)
            flowbox.set_max_children_per_line(30)
            flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

            self.create_flowbox(flowbox)
            scrolled.add(flowbox)

            self.add(scrolled)
            self.show_all()
        def color_swatch_new(self, str_color):
            color = Gdk.color_parse(str_color)
            rgba = Gdk.RGBA.from_color(color)
            button = Gtk.Button()
            area = Gtk.DrawingArea()
            area.set_size_request(24, 24)
            area.override_background_color(0, rgba)
            button.add(area)
            return button

        def create_flowbox(self, flowbox):
            colors = [
                'AliceBlue',
                'AntiqueWhite',
                'AntiqueWhite1',
                'AntiqueWhite2',
                'AntiqueWhite3',
                'AntiqueWhite4',
                'aqua',
                'aquamarine',
                'aquamarine1',
                'aquamarine2',
                'aquamarine3',
                'aquamarine4',
                'azure',
                'azure1',
                'azure2',
                'azure3',
                'azure4',
                'beige',
                'bisque',
                'bisque1',
                'bisque2',
                'bisque3',
                'bisque4',
                'black',
                'BlanchedAlmond',
                'blue',
                'blue1',
                'blue2',
                'blue3',
                'blue4',
                'BlueViolet',
                'brown',
                'brown1',
                'brown2',
                'brown3',
                'brown4',
                'burlywood',
                'burlywood1',
                'burlywood2',
                'burlywood3',
                'burlywood4',
                'CadetBlue',
                'CadetBlue1',
                'CadetBlue2',
                'CadetBlue3',
                'CadetBlue4',
                'chartreuse',
                'chartreuse1',
                'chartreuse2',
                'chartreuse3',
                'chartreuse4',
                'chocolate',
                'chocolate1',
                'chocolate2',
                'chocolate3',
                'chocolate4',
                'coral',
                'coral1',
                'coral2',
                'coral3',
                'coral4'
            ]

            for color in colors:
                button = self.color_swatch_new(color)
                flowbox.add(button)


    win = FlowBoxWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

def example9():
    """HeaderBar example"""
    class HeaderBarWindow(Gtk.Window):
        def __init__(self):
            Gtk.Window.__init__(self, title="HeaderBar Demo")
            self.set_border_width(10)
            self.set_default_size(400, 400)

            hb = Gtk.HeaderBar()
            hb.set_show_close_button(True)
            hb.props.title = "HeaderBar Example"
            self.set_titlebar(hb)

            button = Gtk.Button()
            icon = Gio.ThemedIcon(name="mail-send-receive-symbolic")
            image = Gtk.Image.new_from_gicon(icon , Gtk.IconSize.BUTTON)
            button.add(image)
            hb.pack_end(button)

            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            Gtk.StyleContext.add_class(box.get_style_context(), "linked")

            button = Gtk.Button()
            button.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
            box.add(button)

            button = Gtk.Button()
            button.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
            box.add(button)

            hb.pack_start(box)

            self.add(Gtk.TextView())

    win = HeaderBarWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


def example8():
    """ stack example"""
    class StackWindow(Gtk.Window):
        def __init__(self):
            Gtk.Window.__init__(self, title="Stack Demo")
            self.set_border_width(10)

            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 6)
            self.add(vbox)

            stack = Gtk.Stack()
            stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
            stack.set_transition_duration(1000)
            checkbutton = Gtk.CheckButton("Click me!")
            stack.add_titled(checkbutton, "check", "Check Button")

            label = Gtk.Label()
            label.set_markup("<big>A fancy label</big>")
            stack.add_titled(label, "label", "A label")

            stack_switcher = Gtk.StackSwitcher()
            stack_switcher.set_stack(stack)
            vbox.pack_start(stack_switcher, True, True, 10)
            vbox.pack_start(stack , True, True, 0)


    win = StackWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

def example7():
    """Grid example"""
    class MyWindow(Gtk.Window):
        def __init__(self):
            Gtk.Window.__init__(self, title="Grid Example")
            self.set_border_width(10)
            # self.set_size_request(500, 500)
            self.grid = Gtk.Grid()
            self.add(self.grid)
            self.add_components()
            self.register_events()

        def add_components(self):
            # title
            self.lblTitle = Gtk.Label("Simple Grid Example")
            # grid.attach(col, row, col_span , row_span)
            self.grid.attach(self.lblTitle, 0, 0, 1, 1)

            # id
            self.lblId = Gtk.Label("Id: ")
            self.entryId = Gtk.Entry()
            self.grid.attach(self.lblId , 0, 1 , 1, 1)
            self.grid.attach(self.entryId, 1, 1, 1, 1)

            # name
            self.lblName = Gtk.Label("Name: ")
            self.entryName = Gtk.Entry()
            self.grid.attach(self.lblName, 0 , 2 , 1, 1)
            self.grid.attach(self.entryName, 1, 2, 1, 1)

            # age
            self.lblAge = Gtk.Label("Age: ")
            self.entryAge = Gtk.Entry()
            self.grid.attach(self.lblAge , 0, 3, 1, 1)
            self.grid.attach(self.entryAge, 1, 3, 1, 1)

            # wage
            self.lblWage = Gtk.Label("Wage: ")
            self.entryWage = Gtk.Entry()
            self.grid.attach(self.lblWage, 0, 4, 1, 1)
            self.grid.attach(self.entryWage, 1, 4, 1, 1)

            # active
            self.lblActive = Gtk.Label("Active: ")
            self.entryActive = Gtk.Entry()
            self.grid.attach(self.lblActive, 0, 5, 1, 1)
            self.grid.attach(self.entryActive, 1, 5, 1, 1)

            # buttons
            self.btnOk = Gtk.Button("Ok")
            self.btnClear = Gtk.Button("Clear")
            self.grid.attach(self.btnOk , 0 , 6, 1, 1)
            self.grid.attach(self.btnClear , 1, 6, 1, 1)




        def onBtnOkClicked(self, widget):
            try:
                id = int(self.entryId.get_text())
                name = self.entryName.get_text()
                age = int(self.entryAge.get_text())
                wage = float(self.entryWage.get_text())
                temp = self.entryActive.get_text().lower()
                active = True if(temp == "true") else False
                msg = """id = {0}
name = {1}
age = {2}
wage = {3}
active = {4}""".format(id, name, age, wage, active)
                title = "<<INFO: onOkBtnClicked>>"
                msgDialog = Gtk.MessageDialog(self, 0 , Gtk.MessageType.INFO, Gtk.ButtonsType.OK, title)
                msgDialog.format_secondary_text(msg)
                response = msgDialog.run()
                msgDialog.destroy()
            except:
                msg = "Something went wrong."
                title = "<<ERROR: onOkBtnClicked>>"
                msgDialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.CANCEL, title)
                msgDialog.format_secondary_text(msg)
                response = msgDialog.run()
                msgDialog.destroy()


        def onBtnClearClicked(self, widget):
            self.entryId.set_text("")
            self.entryName.set_text("")
            self.entryAge.set_text("")
            self.entryWage.set_text("")
            self.entryActive.set_text("")

        def register_events(self):
            self.btnOk.connect("clicked", self.onBtnOkClicked)
            self.btnClear.connect("clicked", self.onBtnClearClicked)

    win = MyWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


def example6():
    """Box example"""
    class MyWindow(Gtk.Window):
        def __init__(self):
            Gtk.Window.__init__(self, title="Simple Form Example")
            self.set_border_width(10)
            self.set_size_request(500, 500)

            mainBox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 0)
            self.add(mainBox)

            # title
            hbox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
            lblTitle = Gtk.Label("Simple Form Example", xalign = 0)
            hbox.pack_start(lblTitle, True, True, 0)
            mainBox.pack_start(hbox, True, True, 0)

            # id
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL , spacing = 5)
            lblId = Gtk.Label("Id: ", xalign = 0)
            entryId = Gtk.Entry()
            hbox.pack_start(lblId , True, True, 0)
            hbox.pack_start(entryId , True, True, 0)
            mainBox.pack_start(hbox, True, True, 0)

            # name
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
            lblName = Gtk.Label("Name: ", xalign=0)
            entryName = Gtk.Entry()
            hbox.pack_start(lblName, True, True, 0)
            hbox.pack_start(entryName, True, True, 0)
            mainBox.pack_start(hbox, True, True, 0)

            # age
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
            lblAge = Gtk.Label("Age: ", xalign=0)
            entryAge = Gtk.Entry()
            hbox.pack_start(lblAge, True, True, 0)
            hbox.pack_start(entryAge, True, True, 0)
            mainBox.pack_start(hbox, True, True, 0)

            # wage
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
            lblWage = Gtk.Label("Wage: ", xalign=0)
            entryWage = Gtk.Entry()
            hbox.pack_start(lblWage, True, True, 0)
            hbox.pack_start(entryWage, True, True, 0)
            mainBox.pack_start(hbox, True, True, 0)

            # active
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
            lblActive = Gtk.Label("Active: ", xalign=0)
            entryActive = Gtk.Entry()
            hbox.pack_start(lblActive, True, True, 0)
            hbox.pack_start(entryActive, True, True, 0)
            mainBox.pack_start(hbox, True, True, 0)


            # buttons
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
            btnOk  = Gtk.Button(label="Hello")
            btnClear = Gtk.Button(label = "Clear")
            hbox.pack_start(btnOk, True, True, 0)
            hbox.pack_start(btnClear, True, True, 0)
            mainBox.pack_start(hbox, True, True, 0)


            def btnOkClicked(widget):
                try:
                    id = int(entryId.get_text())
                    name = entryName.get_text()
                    age = int(entryAge.get_text())
                    wage = float(entryWage.get_text())
                    temp = entryActive.get_text().lower()
                    active = True if(temp == "true") else False

                    msg = """id = {0}
name = {1}
age = {2}
wage = {3}
active = {4}""".format(id, name, age, wage, active)

                    dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                               Gtk.ButtonsType.OK, "<<Info btnOkClicked>>")
                    dialog.format_secondary_text(msg)
                    dialog.run()
                    dialog.destroy()
                except:
                    msg = "Something went wrong."
                    dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                                               Gtk.ButtonsType.CANCEL, "<<Error btnOkClicked>>")
                    dialog.format_secondary_text(msg)
                    response = dialog.run()
                    dialog.destroy()



            def btnClearClicked(widget):
                entryId.set_text("")
                entryName.set_text("")
                entryAge.set_text("")
                entryWage.set_text("")
                entryActive.set_text("")


            btnOk.connect("clicked", btnOkClicked)
            btnClear.connect("clicked", btnClearClicked)








    win = MyWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()



def example5():
    """list box example"""
    class ListBoxRowWithData(Gtk.ListBoxRow):
        def __init__(self, data):
            super(Gtk.ListBoxRow, self).__init__()
            self.data = data
            self.add(Gtk.Label(data))

    class ListBoxWindow(Gtk.Window):
        def __init__(self):
            Gtk.Window.__init__(self, title = "ListBox Demo")
            self.set_border_width(10)

            box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            self.add(box_outer)

            listbox = Gtk.ListBox()
            listbox.set_selection_mode(Gtk.SelectionMode.NONE)
            box_outer.pack_start(listbox, True, True, 0)


            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
            row.add(hbox)
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            hbox.pack_start(vbox, True, True, 0)

            label1 = Gtk.Label("Automatic Date & Time", xalign=0)
            label2 = Gtk.Label("Requires internet access", xalign=0)
            vbox.pack_start(label1, True, True, 0)
            vbox.pack_start(label2, True, True, 0)

            switch = Gtk.Switch()
            switch.props.valign = Gtk.Align.CENTER
            hbox.pack_start(switch , False, True, 0)

            listbox.add(row)
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
            row.add(hbox)
            label = Gtk.Label("Enable Automatic Update", xalign=0)
            check = Gtk.CheckButton()
            hbox.pack_start(label, True, True, 0)
            hbox.pack_start(check, False, True, 0)
            listbox.add(row)

            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
            row.add(hbox)
            label = Gtk.Label("Date Format", xalign=0)
            combo = Gtk.ComboBoxText()
            combo.insert(0, "0", "24-hour")
            combo.insert(1, "1", "AM/PM")
            hbox.pack_start(label, True, True, 0)
            hbox.pack_start(combo, False, True, 0)
            listbox.add(row)

            listbox_2 = Gtk.ListBox()
            items = "This is a sorted ListBox Fail".split()
            for item in items:
                listbox_2.add(ListBoxRowWithData(item))

            def sort_func(row_1, row_2, data, notify_destroy):
                return row_1.data.lower() > row_2.data.lower()

            def filter_func(row, data, notify_destroy):
                return False if row.data == "Fail" else True

            listbox_2.set_sort_func(sort_func , None , False)
            listbox_2.set_filter_func(filter_func, None , False)
            listbox.connect("row-activated", lambda widget, row:print(row.data))
            box_outer.pack_start(listbox_2, True, True, 0)
            listbox_2.show_all()

    win = ListBoxWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

def example4():
    """box example"""
    class MyWindow(Gtk.Window):
        def __init__(self):
            Gtk.Window.__init__(self, title = "Space Example")
            self.box = Gtk.Box(spacing=6)
            self.add(self.box)

            self.button1 = Gtk.Button(label="Hello")
            self.button1.connect("clicked", self.on_button1_clicked)
            self.box.pack_start(self.button1, True, True, 0)

            self.button2 = Gtk.Button(label="Goodbye")
            self.button2.connect("clicked", self.on_button2_clicked)
            self.box.pack_start(self.button2, True, True, 0)

        def on_button1_clicked(self, widget):
            print("Hello")

        def on_button2_clicked(self, widget):
            print("Goodbye")

    win = MyWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


def example3():
    class GridWindow(Gtk.Window):
        def __init__(self):
            Gtk.Window.__init__(self, title= "Grid Example")

            grid = Gtk.Grid()
            self.add(grid)

            button1 = Gtk.Button(label="Button 1")
            button2 = Gtk.Button(label = "Button 2")
            button3 = Gtk.Button(label = "Button 3")
            button4 = Gtk.Button(label = "Button 4")
            button5 = Gtk.Button(label = "Button 5")
            button6 = Gtk.Button(label = "Button 6")

            grid.add(button1)
            grid.attach(button2, 1, 0, 2, 1)
            grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
            grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
            grid.attach(button5, 1, 2, 1, 1)
            grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)

    win = GridWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

def example2():
    class MyWindow(Gtk.Window):
        def __init__(self):
            Gtk.Window.__init__(self, title = "Hello World")
            self.button = Gtk.Button(label = "Click Here")
            self.button.connect("clicked", self.on_button_clicked)
            self.add(self.button)

        def on_button_clicked(self, widget):
            print("Hello World")

    win = MyWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

def example1():
    win = Gtk.Window()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

