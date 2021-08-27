import wx
import os
import sys


class AccommodationPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(AccommodationPanel, self).__init__(*args, **kwargs)

        self.backgroundColor = (240, 240, 240, 255)
        self.dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.margin = (20, 20)

        self.InitUI()

    def InitUI(self):
        self.layout = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.layout)
        self.SetBackgroundColour(self.backgroundColor)

        font = wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.SetFont(font)
        
        generalSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        categorySizer = wx.BoxSizer(wx.VERTICAL)
        categoryPanel = wx.Panel(self, style=wx.SIMPLE_BORDER)
        categoryPanel.SetBackgroundColour(wx.WHITE)
        categoryPanel.SetSizer(categorySizer)
        
        categoryLabel = wx.StaticText(categoryPanel, label="  Accommodations  ", size=(115, -1))
        categorySizer.Add((-1, 5))
        categorySizer.Add(categoryLabel)
        categorySizer.Add((-1, 5))

        self.removeButton = wx.Button(self, label="-", size=(28, 28))

        generalSizer.Add(categoryPanel)
        generalSizer.Add(self.removeButton)
        
        selectSizer = wx.BoxSizer(wx.VERTICAL)
        selectPanel = wx.Panel(self, style=wx.SIMPLE_BORDER)
        selectPanel.SetSizer(selectSizer)
        
        selectHeader = wx.StaticText(selectPanel, label="  ACCOMMODATIONS")
        selectEntrySizer = wx.BoxSizer(wx.HORIZONTAL)
        selectEntry = wx.ComboBox(selectPanel, size=(240, -1))
        selectEntrySizer.Add((10, -1))
        selectEntrySizer.Add(selectEntry)
        selectEntrySizer.Add((10, -1))
        
        selectSizer.Add(selectHeader)
        selectSizer.Add((-1, 5))
        selectSizer.Add(selectEntrySizer)
        selectSizer.Add((-1, 5))
        
        self.layout.Add(generalSizer)
        self.layout.Add((-1, 10))
        self.layout.Add(selectPanel)
        self.layout.Add(self.margin)

        
        self.Refresh()
        

def main():
    app = wx.App()
    frame = wx.Frame(None, size=(1200, 650))
    AccommodationPanel("", "debug", frame)
    frame.Centre()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
