import wx
import wx.grid


def example6():
    """using wx.GridSizer """
    class MyFrame(wx.Frame):
        def __init__(self, parent, id, title):
            wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition , wx.Size(400, 400))
            gs = wx.GridSizer(7, 2, 3, 3)
            panelMain = wx.Panel(self)

            # title
            lblTitle = wx.StaticText(panelMain, -1, style = wx.ALIGN_CENTER)
            lblTitle.SetLabel("GridSizer Example")
            lblEmpty = wx.StaticText(panelMain, -1)
            lblEmpty.SetLabel("")
            # id
            lblId = wx.StaticText(panelMain , -1, style = wx.ALIGN_RIGHT)
            lblId.SetLabel("Id: ")
            fieldId = wx.TextCtrl(panelMain)
            # name
            lblName = wx.StaticText(panelMain , -1)
            lblName.SetLabel("Name: ")
            fieldName = wx.TextCtrl(panelMain)

            # age
            lblAge = wx.StaticText(panelMain, -1)
            lblAge.SetLabel("Age: ")
            fieldAge = wx.TextCtrl(panelMain)

            # wage
            lblWage = wx.StaticText(panelMain, -1)
            lblWage.SetLabel("Wage: ")
            fieldWage = wx.TextCtrl(panelMain)

            # active
            lblActive = wx.StaticText(panelMain, -1)
            lblActive.SetLabel("Active: ")
            fieldActive = wx.TextCtrl(panelMain)

            #buttons
            btnOk = wx.Button(panelMain, -1, "Ok")
            btnCancel = wx.Button(panelMain, -1, "Cancel")


            gs.Add(lblTitle)
            gs.Add(lblEmpty)
            gs.Add(lblId)
            gs.Add(fieldId)
            gs.Add(lblName)
            gs.Add(fieldName)
            gs.Add(lblAge)
            gs.Add(fieldAge)
            gs.Add(lblWage)
            gs.Add(fieldWage)
            gs.Add(lblActive)
            gs.Add(fieldActive)
            gs.Add(btnOk)
            gs.Add(btnCancel)

            panelMain.SetSizer(gs)
            self.Centre()

    class MyApp(wx.App):
        def OnInit(self):
            frame = MyFrame(None, -1, "GridSizer layout")
            frame.Show(True)
            return True


    app = MyApp(None)
    app.MainLoop()



def example5():
    """using layout manager: wx.BoxSizer """
    class MyFrame(wx.Frame):
        def __init__(self, parent, id, title):
            wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition , wx.Size(400, 400))
            panel = wx.Panel(self,-1)
            box = wx.BoxSizer(wx.HORIZONTAL)
            box.Add(wx.Button(panel, -1, "Button1"), 1)
            box.Add(wx.Button(panel, -1, "Button2"), 1)
            box.Add(wx.Button(panel, -1, "Button3"), 1)
            panel.SetSizer(box)
            self.Centre()

    class MyApp(wx.App):
        def OnInit(self):
            frame = MyFrame(None, -1, "BoxSizer layout")
            frame.Show(True)
            return True

    app = MyApp(None)
    app.MainLoop()


def example4():
    class MyMenu(wx.Frame):
        def __init__(self, parent, id, title):
            wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(200,150))

            menubar = wx.MenuBar()
            file = wx.Menu()
            edit = wx.Menu()
            help = wx.Menu()
            file.Append(101, "&Open", "Open a new document")
            file.Append(102, "&Save", "Save the document")
            file.AppendSeparator()
            quit = wx.MenuItem(file, 105, "&Quit\tCtrl+Q", "Quit the Application")
            # quit.SetBitmap(wx.Image("stock_exit-16.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap())
            file.AppendItem(quit)

            # Deprecated
            menubar.Append(file, "&File")
            menubar.Append(edit, "&Edit")
            menubar.Append(help, "&Help")


            self.SetMenuBar(menubar)
            self.CreateStatusBar()

    class MyApp(wx.App):
        def OnInit(self):
            frame = MyMenu(None,-1, "Menubar Example")
            frame.Show(True)
            return True

    app = MyApp(None)
    app.MainLoop()


def example3():
    app = wx.App()
    frame = wx.Frame(None, -1, "Hello World")
    frame.SetToolTip(wx.ToolTip("This is a frame"))
    frame.SetCursor(wx.Cursor(wx.CURSOR_MAGNIFIER))
    frame.SetPosition(wx.Point(0, 0))
    frame.SetSize(wx.Size(300, 300))
    frame.SetTitle("Hello World 2")
    frame.Show()

    app.MainLoop()

def example2():
    app = wx.App()
    frame = wx.Frame(None , -1, "Hello World")
    frame.Show()
    app.MainLoop()


def example1():
    class TestGrid(wx.grid.Grid):
        def __init__(self, *args, **kw):
            wx.grid.Grid.__init__(self, *args, **kw)
            self.CreateGrid(25, 25)

            # Show some simple cell formatting
            self.SetColSize(3, 200)
            self.SetRowSize(4, 45)
            self.SetCellValue(0, 0, "First cell")
            self.SetCellValue(1, 1, "Another cell")
            self.SetCellValue(2, 2, "Yet another cell")
            self.SetCellValue(3, 3, "This cell is read-only")
            self.SetCellFont(0, 0, wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL))
            self.SetCellTextColour(1, 1, wx.RED)
            self.SetCellBackgroundColour(2, 2, wx.CYAN)
            self.SetReadOnly(3, 3, True)

            self.SetCellEditor(5, 0, wx.grid.GridCellNumberEditor(1, 1000))
            self.SetCellValue(5, 0, "123")
            self.SetCellEditor(6, 0, wx.grid.GridCellFloatEditor())
            self.SetCellValue(6, 0, "123.34")
            self.SetCellEditor(7, 0, wx.grid.GridCellNumberEditor())

            # Attribute objects let you keep a set of formatting values
            # in one spot, and reuse them if needed
            attr = wx.grid.GridCellAttr()
            attr.SetTextColour(wx.BLACK)
            attr.SetBackgroundColour('pink')
            attr.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

            # you can set cell attributes for the whole row (or column)
            self.SetRowAttr(5, attr)

            self.SetColLabelValue(0, "Custom")
            self.SetColLabelValue(1, "column")
            self.SetColLabelValue(2, "labels")

            self.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_BOTTOM)

            # overflow cells
            self.SetCellValue(9, 1,
                              "This default cell will overflow into empty neighboring cells, but not if you turn overflow off.");
            self.SetCellSize(11, 1, 3, 3);
            self.SetCellAlignment(11, 1, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE);
            self.SetCellValue(11, 1, "This cell is set to span 3 rows and 3 columns");

            editor = wx.grid.GridCellTextEditor()
            editor.SetParameters('10')
            self.SetCellEditor(0, 4, editor)
            self.SetCellValue(0, 4, "Limited text")

            renderer = wx.grid.GridCellAutoWrapStringRenderer()
            self.SetCellRenderer(15, 0, renderer)
            self.SetCellValue(15, 0, "The text in this cell will be rendered with word-wrapping")
            self.SetRowSize(15, 40)

    class TestFrame(wx.Frame):
        def __init__(self, *args, **kw):
            wx.Frame.__init__(self, *args, **kw)
            self.grid = TestGrid(self)

    app = wx.App()
    frm = TestFrame(None, title="Simple Test Grid", size=(700, 500))
    frm.Show()
    app.MainLoop()