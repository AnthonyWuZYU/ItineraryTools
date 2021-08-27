import wx
import os
import sys
from DropdownTime import *


class TravelPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(TravelPanel, self).__init__(*args, **kwargs)

        self.backgroundColor = (240, 240, 240, 255)
        self.dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.margin = (20, 20)
        self.rowSize = (150, 24)

        self.rowSizer = []
        self.removeList = []
        self.departEntry = []
        self.arrivalEntry = []
        self.vehicleEntry = []
        self.infoEntry = []
        self.companyEntry = []

        self.InitUI()

    def InitUI(self):
        self.layout = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.layout)
        self.SetBackgroundColour(self.backgroundColor)

        font = wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL)
        entryFont = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.SetFont(font)

        generalSizer = wx.BoxSizer(wx.HORIZONTAL)

        categorySizer = wx.BoxSizer(wx.VERTICAL)
        categoryPanel = wx.Panel(self, style=wx.SIMPLE_BORDER)
        categoryPanel.SetBackgroundColour(wx.WHITE)
        categoryPanel.SetSizer(categorySizer)

        categoryLabel = wx.StaticText(categoryPanel, label="             Travel", size=(115, -1))
        categorySizer.Add((-1, 5))
        categorySizer.Add(categoryLabel)
        categorySizer.Add((-1, 5))

        self.removeButton = wx.Button(self, label="-", size=(28, 28))

        generalSizer.Add(categoryPanel)
        generalSizer.Add(self.removeButton)

        # Start time
        startSizer = wx.BoxSizer(wx.VERTICAL)
        startPanel = wx.Panel(self, style=wx.SIMPLE_BORDER)
        startPanel.SetSizer(startSizer)

        startHeader = wx.StaticText(startPanel, label="  START TIME")
        startEntrySizer = wx.BoxSizer(wx.HORIZONTAL)
        startEntry = DropdownTime(startPanel, size=(160, -1))
        startEntry.SetFont(entryFont)
        startEntrySizer.Add((5, -1))
        startEntrySizer.Add(startEntry)
        startEntrySizer.Add((5, -1))

        startSizer.Add(startHeader)
        startSizer.Add((-1, 5))
        startSizer.Add(startEntrySizer)
        startSizer.Add((-1, 10))

        # Content
        contentSizer = wx.BoxSizer(wx.VERTICAL)
        self.contentPanel = wx.Panel(self, style=wx.SIMPLE_BORDER)
        self.contentPanel.SetSizer(contentSizer)
        self.contentPanel.SetFont(entryFont)

        labelSizer = wx.BoxSizer(wx.HORIZONTAL)

        buttonPanel = wx.Panel(self.contentPanel, style=wx.SIMPLE_BORDER, size=(24, 24))

        departSizer = wx.BoxSizer(wx.HORIZONTAL)
        departPanel = wx.Panel(self.contentPanel, style=wx.SIMPLE_BORDER, size=self.rowSize)
        departPanel.SetSizer(departSizer)
        departHeader = wx.StaticText(departPanel, label=" Departure Location")
        departSizer.Add(departHeader)

        arrivalSizer = wx.BoxSizer(wx.HORIZONTAL)
        arrivalPanel = wx.Panel(self.contentPanel, style=wx.SIMPLE_BORDER, size=self.rowSize)
        arrivalPanel.SetSizer(arrivalSizer)
        arrivalHeader = wx.StaticText(arrivalPanel, label=" Arrival Location")
        arrivalSizer.Add(arrivalHeader)

        vehicleSizer = wx.BoxSizer(wx.HORIZONTAL)
        vehiclePanel = wx.Panel(self.contentPanel, style=wx.SIMPLE_BORDER, size=self.rowSize)
        vehiclePanel.SetSizer(vehicleSizer)
        vehicleHeader = wx.StaticText(vehiclePanel, label=" Vehicle")
        vehicleSizer.Add(vehicleHeader)

        infoSizer = wx.BoxSizer(wx.HORIZONTAL)
        infoPanel = wx.Panel(self.contentPanel, style=wx.SIMPLE_BORDER, size=self.rowSize)
        infoPanel.SetSizer(infoSizer)
        infoHeader = wx.StaticText(infoPanel, label=" Vehicle Info")
        infoSizer.Add(infoHeader)

        companySizer = wx.BoxSizer(wx.HORIZONTAL)
        companyPanel = wx.Panel(self.contentPanel, style=wx.SIMPLE_BORDER, size=self.rowSize)
        companyPanel.SetSizer(companySizer)
        companyHeader = wx.StaticText(companyPanel, label=" Air Charter Company")
        companySizer.Add(companyHeader)

        labelSizer.Add(buttonPanel)
        labelSizer.Add(departPanel)
        labelSizer.Add(arrivalPanel)
        labelSizer.Add(vehiclePanel)
        labelSizer.Add(infoPanel)
        labelSizer.Add(companyPanel)

        self.tableSizer = wx.BoxSizer(wx.VERTICAL)

        addSizer = wx.BoxSizer(wx.HORIZONTAL)
        addButton = wx.Button(self.contentPanel, label="+", size=(24, 24))
        addButton.Bind(wx.EVT_BUTTON, self.addRow)
        addSizer.Add(addButton)

        contentSizer.Add(labelSizer)
        contentSizer.Add(self.tableSizer)
        contentSizer.Add(addSizer)

        # End time
        endSizer = wx.BoxSizer(wx.VERTICAL)
        endPanel = wx.Panel(self, style=wx.SIMPLE_BORDER)
        endPanel.SetSizer(endSizer)

        endHeader = wx.StaticText(endPanel, label="  END TIME")
        endEntrySizer = wx.BoxSizer(wx.HORIZONTAL)
        endEntry = DropdownTime(endPanel, size=(160, -1))
        endEntry.SetFont(entryFont)
        endEntrySizer.Add((10, -1))
        endEntrySizer.Add(endEntry)
        endEntrySizer.Add((10, -1))

        endSizer.Add(endHeader)
        endSizer.Add((-1, 5))
        endSizer.Add(endEntrySizer)
        endSizer.Add((-1, 10))

        self.layout.Add(generalSizer)
        self.layout.Add((-1, 10))
        self.layout.Add(startPanel)
        self.layout.Add((-1, 10))
        self.layout.Add(self.contentPanel)
        self.layout.Add((-1, 10))
        self.layout.Add(endPanel)

        self.addRow(None)

        self.layout.Add(self.margin)

        self.Refresh()

    def addRow(self, event):
        self.rowSizer.append(wx.BoxSizer(wx.HORIZONTAL))
        self.removeList.append(wx.Button(self.contentPanel, label="-", size=(24, 24)))
        self.removeList[-1].Bind(wx.EVT_BUTTON, self.removeRow)
        self.departEntry.append(wx.ComboBox(self.contentPanel, size=self.rowSize))
        self.arrivalEntry.append(wx.ComboBox(self.contentPanel, size=self.rowSize))
        self.vehicleEntry.append(wx.ComboBox(self.contentPanel, size=self.rowSize))
        self.infoEntry.append(wx.ComboBox(self.contentPanel, size=self.rowSize))
        self.companyEntry.append(wx.ComboBox(self.contentPanel, size=self.rowSize))

        self.rowSizer[-1].Add(self.removeList[-1])
        self.rowSizer[-1].Add(self.departEntry[-1])
        self.rowSizer[-1].Add(self.arrivalEntry[-1])
        self.rowSizer[-1].Add(self.vehicleEntry[-1])
        self.rowSizer[-1].Add(self.infoEntry[-1])
        self.rowSizer[-1].Add(self.companyEntry[-1])

        self.tableSizer.Add(self.rowSizer[-1])
        self.GetParent().Layout()

    def removeRow(self, event):
        id = self.removeList.index(event.GetEventObject())

        self.removeList[id].Destroy()
        self.departEntry[id].Destroy()
        self.arrivalEntry[id].Destroy()
        self.vehicleEntry[id].Destroy()
        self.infoEntry[id].Destroy()
        self.companyEntry[id].Destroy()

        del self.rowSizer[id]
        del self.removeList[id]
        del self.departEntry[id]
        del self.arrivalEntry[id]
        del self.vehicleEntry[id]
        del self.infoEntry[id]
        del self.companyEntry[id]

        self.GetParent().Layout()

def main():
    app = wx.App()
    frame = wx.Frame(None, size=(1200, 650))
    TravelPanel("", "debug", frame)
    frame.Centre()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
