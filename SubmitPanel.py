import wx
import os
import sys


class SubmitPanel(wx.Panel):
    def __init__(self, mode, ver, *args, **kwargs):
        super(SubmitPanel, self).__init__(*args, **kwargs)

        self.backgroundColor = (240, 240, 240, 255)
        self.dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.margin = (30, 30)
        self.buttonSize = (180, 40)
        self.InitUI()

    def InitUI(self):
        self.layout = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.layout)
        self.SetBackgroundColour(self.backgroundColor)

        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.SetFont(font)

        previewSizer = wx.BoxSizer(wx.HORIZONTAL)
        previewButton = wx.Button(self, label="PREVIEW ITINERARY", size=self.buttonSize)
        previewSizer.Add(self.margin)
        previewSizer.Add(previewButton)
        
        submitSizer = wx.BoxSizer(wx.HORIZONTAL)
        submitButton = wx.Button(self, label="SAVE && SUBMIT", size=self.buttonSize)
        submitSizer.Add(self.margin)
        submitSizer.Add(submitButton)

        self.layout.Add(self.margin)
        self.layout.Add(previewSizer)
        self.layout.Add(self.margin)
        self.layout.Add(submitSizer)

        self.Update()
        self.Layout()
        self.Refresh()



def main():
    app = wx.App()
    frame = wx.Frame(None, size=(1200, 650))
    SubmitPanel("", "debug", frame)
    frame.Centre()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
