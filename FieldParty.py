import wx
import os
import sys

class FieldParty(wx.Panel):
    def __init__(self, mode, ver, *args, **kwargs):
        super(FieldParty, self).__init__(*args, **kwargs)

        self.backgroundColor = (240, 240, 240, 255)
        self.dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.margin = (30, 30)
        
        self.InitUI()

    def InitUI(self):
        self.layout = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self.layout)
        self.SetBackgroundColour(self.backgroundColor)
        
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        boldFont = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.SetFont(font)
        
        # Field information
        fieldSizer = wx.BoxSizer(wx.VERTICAL)
        
        memberSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.memberPanel = wx.Panel(self, style=wx.SIMPLE_BORDER, size=(620, -1))
        self.memberPanel.SetSizer(memberSizer)
        
        partySizer = wx.BoxSizer(wx.VERTICAL)
        partyHeader = wx.StaticText(self.memberPanel, label="  FIELD PARTY")
        
        flSizer = wx.BoxSizer(wx.HORIZONTAL)
        flLabel = wx.StaticText(self.memberPanel, label=" FL", size = (30 , -1))
        flEntry = wx.ComboBox(self.memberPanel, style=wx.TE_READONLY, size=(260, -1))
        flSizer.Add(flLabel)
        flSizer.Add(flEntry)
        
        self.faGroupSizer = wx.BoxSizer(wx.VERTICAL)
        
        self.faSizerList = []
        self.faLabelList = []
        self.faEntryList = []
        self.faIndent = []
        
        legend = wx.StaticText(self.memberPanel, label="     FL = Field Leader; FA = Field Assistant")
        
        partySizer.Add(partyHeader)
        partySizer.Add((-1, 10))
        partySizer.Add(flSizer)
        partySizer.Add(self.faGroupSizer)
        partySizer.Add((-1, 27))
        partySizer.Add(legend)

        # Phone
        phoneSizer = wx.BoxSizer(wx.VERTICAL)
        phoneHeader = wx.StaticText(self.memberPanel, label="  SAT PHONE")

        flPhoneSizer = wx.BoxSizer(wx.HORIZONTAL)
        flPhoneEntry = wx.ComboBox(self.memberPanel, size=(260, -1))
        flPhoneSizer.Add(flPhoneEntry)
        
        self.phoneGroupSizer = wx.BoxSizer(wx.VERTICAL)
        
        self.phoneSizerList = []
        self.phoneEntryList = []
        self.phoneRemoveList = []
        self.phoneIndent = []

        addPartySizer = wx.BoxSizer(wx.HORIZONTAL)
        addPartybutton = wx.Button(self.memberPanel, label="Add FA", size=(60, -1))
        addPartybutton.Bind(wx.EVT_BUTTON, self.addPartyRow)
        addPartySizer.Add((220, -1))
        addPartySizer.Add(addPartybutton)

        # initially having one row
        self.addPartyRow(None)

        phoneSizer.Add(phoneHeader)
        phoneSizer.Add((-1, 10))
        phoneSizer.Add(flPhoneSizer)
        phoneSizer.Add(self.phoneGroupSizer)
        phoneSizer.Add((-1, 10))
        phoneSizer.Add(addPartySizer)
        
        memberSizer.Add(partySizer, wx.EXPAND)
        memberSizer.Add((20, -1))
        memberSizer.Add(phoneSizer, wx.EXPAND)
        
        generalSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Supervisor
        supervisorSizer = wx.BoxSizer(wx.VERTICAL)
        self.supervisorPanel = wx.Panel(self, style=wx.SIMPLE_BORDER, size=(300, -1))
        self.supervisorPanel.SetSizer(supervisorSizer)
        
        supervisorHeader = wx.StaticText(self.supervisorPanel, label="  SUPERVISOR")

        # Add or remove rows with entries for Supervisors
        self.supervisorGroup = wx.BoxSizer(wx.VERTICAL)

        self.supervisorSizers = []
        self.supervisorEntrys = []
        self.supervisorRemoves = []
        self.supervisorIndents = []

        # Initially having one row
        self.addSupervisorRow(None)

        addSupervisorSizer = wx.BoxSizer(wx.HORIZONTAL)
        addSupervisorbutton = wx.Button(self.supervisorPanel, label="Add Supervisor", size=(100, -1))
        addSupervisorbutton.Bind(wx.EVT_BUTTON, self.addSupervisorRow)
        addSupervisorSizer.Add((185, -1))
        addSupervisorSizer.Add(addSupervisorbutton)
        addSupervisorSizer.Add((10, -1))
        
        supervisorSizer.Add(supervisorHeader)
        supervisorSizer.Add(self.supervisorGroup)
        supervisorSizer.Add((-1, 10))
        supervisorSizer.Add(addSupervisorSizer)
        supervisorSizer.Add((-1, 10))
        
        # Office Info
        officeSizer = wx.BoxSizer(wx.VERTICAL)
        officePanel = wx.Panel(self, style=wx.SIMPLE_BORDER, size=(290, -1))
        officePanel.SetSizer(officeSizer)
        officeHeader = wx.StaticText(officePanel, label="  OFFICE")
        
        locationSizer = wx.BoxSizer(wx.HORIZONTAL)
        locationBox = wx.ComboBox(officePanel, style=wx.TE_READONLY, size=(270, -1))
        locationSizer.Add((10, -1))
        locationSizer.Add(locationBox)
        locationSizer.Add((10, -1))
        
        # Street Address
        streetSizer = wx.BoxSizer(wx.HORIZONTAL)
        streetHeader = wx.StaticText(officePanel, label=" Street Address", size=(100, -1))
        streetEntry = wx.TextCtrl(officePanel, size=(178, -1))
        streetSizer.Add(streetHeader)
        streetSizer.Add(streetEntry)

        # City, Province
        citySizer = wx.BoxSizer(wx.HORIZONTAL)
        cityHeader = wx.StaticText(officePanel, label=" City, Province", size=(90, -1))
        cityEntry = wx.TextCtrl(officePanel, size=(188, -1))
        citySizer.Add(cityHeader)
        citySizer.Add(cityEntry)
        
        # Postal Code
        postalSizer = wx.BoxSizer(wx.HORIZONTAL)
        postalHeader = wx.StaticText(officePanel, label=" Postal Code", size=(80, -1))
        postalEntry = wx.TextCtrl(officePanel, size=(198, -1))
        postalSizer.Add(postalHeader)
        postalSizer.Add(postalEntry)
        
        officeSizer.Add(officeHeader)
        officeSizer.Add((-1, 10))
        officeSizer.Add(locationSizer)
        officeSizer.Add((-1, 10))
        officeSizer.Add(streetSizer)
        officeSizer.Add((-1, 10))
        officeSizer.Add(citySizer)
        officeSizer.Add((-1, 10))
        officeSizer.Add(postalSizer)
        officeSizer.Add((-1, 20))
        
        generalSizer.Add(self.supervisorPanel)
        generalSizer.Add(self.margin)
        generalSizer.Add(officePanel)
        
        
        fieldSizer.Add(self.margin)
        fieldSizer.Add(self.memberPanel)
        fieldSizer.Add(self.margin)
        fieldSizer.Add(generalSizer)
        
        # Organization, directory, link, comments
        otherInfoSizer = wx.BoxSizer(wx.VERTICAL)
        
        orgSizer = wx.BoxSizer(wx.HORIZONTAL)

        organizationSizer = wx.BoxSizer(wx.VERTICAL)
        organizationPanel = wx.Panel(self, style = wx.SIMPLE_BORDER, size = (140, 70))
        organizationPanel.SetSizer(organizationSizer)
        
        orgHeader = wx.StaticText(organizationPanel, label="  ORGANIZATION")
        orgEntrySizer = wx.BoxSizer(wx.HORIZONTAL)
        orgEntry = wx.TextCtrl(organizationPanel, size=(110, -1))
        orgEntrySizer.Add((-1, -1), wx.EXPAND)
        orgEntrySizer.Add(orgEntry, wx.EXPAND)
        orgEntrySizer.Add((-1, -1), wx.EXPAND)
        organizationSizer.Add(orgHeader)
        organizationSizer.Add((-1, 10))
        organizationSizer.Add(orgEntrySizer)

        # Itinerary Report Directory
        directorySizer = wx.BoxSizer(wx.VERTICAL)
        directoryPanel = wx.Panel(self, style=wx.SIMPLE_BORDER, size=(300, 70))
        directoryPanel.SetSizer(directorySizer)

        dirHeader = wx.StaticText(directoryPanel, label="  ITINERARY REPORT DIRECTORY")
        dirEntrySizer = wx.BoxSizer(wx.HORIZONTAL)
        dirEntry = wx.TextCtrl(directoryPanel, size=(270, -1))
        dirEntrySizer.Add((-1, -1), wx.EXPAND)
        dirEntrySizer.Add(dirEntry, wx.EXPAND)
        dirEntrySizer.Add((-1, -1), wx.EXPAND)
        directorySizer.Add(dirHeader)
        directorySizer.Add((-1, 10))
        directorySizer.Add(dirEntrySizer)

        orgSizer.Add(organizationPanel)
        orgSizer.Add(self.margin)
        orgSizer.Add(directoryPanel)
        
        # InReach Link
        linkSizer = wx.BoxSizer(wx.VERTICAL)
        linkPanel = wx.Panel(self, style=wx.SIMPLE_BORDER, size=(470, -1))
        linkPanel.SetSizer(linkSizer)
        
        linkHeader = wx.StaticText(linkPanel, label="  INREACH LINK")
        linkEntrySizer = wx.BoxSizer(wx.HORIZONTAL)
        linkEntry = wx.TextCtrl(linkPanel, size=(450, -1))
        linkEntrySizer.Add((10, -1))
        linkEntrySizer.Add(linkEntry)
        linkSizer.Add(linkHeader)
        linkSizer.Add((-1, 10))
        linkSizer.Add(linkEntrySizer)
        linkSizer.Add((-1, 20))

        # Comment section
        commentSizer = wx.BoxSizer(wx.VERTICAL)
        commentPanel = wx.Panel(self, style=wx.SIMPLE_BORDER, size=(470, -1))
        commentPanel.SetSizer(commentSizer)

        commentHeader = wx.StaticText(commentPanel, label="  ITINERARY COMMENTS")
        commentEntrySizer = wx.BoxSizer(wx.HORIZONTAL)
        commentEntry = wx.TextCtrl(commentPanel, style=wx.TE_MULTILINE, size=(450, 180))
        commentEntrySizer.Add((10, -1))
        commentEntrySizer.Add(commentEntry)
        commentSizer.Add(commentHeader)
        commentSizer.Add((-1, 10))
        commentSizer.Add(commentEntrySizer)
        commentSizer.Add((-1, 20))
        
        # Load Itinerary Form Button
        loadSizer = wx.BoxSizer(wx.HORIZONTAL)
        loadButton = wx.Button(self, label="LOAD ITINERARY", size=(150, 40))
        loadButton.SetFont(boldFont)
        loadSizer.Add((-1, -1), wx.EXPAND)
        loadSizer.Add(loadButton, wx.EXPAND)
        loadSizer.Add((-1, -1), wx.EXPAND)

        # Going back to main page of the Itinerary tool
        backSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.backButton = wx.Button(self, label="Back to Main", style=wx.NO_BORDER, size=(100, 30))
        self.backButton.SetFont(boldFont)
        self.backButton.SetBackgroundColour(self.backgroundColor)
        backSizer.Add((400, -1))
        backSizer.Add(self.backButton)
        
        otherInfoSizer.Add(self.margin)
        otherInfoSizer.Add(orgSizer)
        otherInfoSizer.Add(self.margin)
        otherInfoSizer.Add(linkPanel)
        otherInfoSizer.Add(self.margin)
        otherInfoSizer.Add(commentPanel)
        otherInfoSizer.Add(self.margin)
        otherInfoSizer.Add(loadSizer)
        otherInfoSizer.Add(backSizer)
        
        
        self.layout.Add((self.margin))
        self.layout.Add(fieldSizer)
        self.layout.Add((self.margin))
        self.layout.Add(otherInfoSizer)
        self.layout.Add((self.margin))

        self.SetDoubleBuffered(True)
        self.Update()
        self.Layout()
        self.Refresh()
        
    def addPartyRow(self, event):
        self.faSizerList.append(wx.BoxSizer(wx.HORIZONTAL))
        self.faLabelList.append(wx.StaticText(self.memberPanel, label=" FA", size=(30, -1)))
        self.faEntryList.append(wx.ComboBox(self.memberPanel, style=wx.TE_READONLY, size=(260, -1)))
        self.faSizerList[-1].Add(self.faLabelList[-1])
        self.faSizerList[-1].Add(self.faEntryList[-1])
        self.faIndent.append(wx.StaticText(self.memberPanel, size = (-1, 10)))
        self.faGroupSizer.Add(self.faIndent[-1])
        self.faGroupSizer.Add(self.faSizerList[-1])

        self.phoneSizerList.append(wx.BoxSizer(wx.HORIZONTAL))
        self.phoneEntryList.append(wx.ComboBox(self.memberPanel, size=(260, -1)))
        self.phoneRemoveList.append(wx.Button(self.memberPanel, label="-", size=(25, 24)))
        self.phoneRemoveList[-1].Bind(wx.EVT_BUTTON, self.removePartyRow)
        self.phoneSizerList[-1].Add(self.phoneEntryList[-1])
        self.phoneSizerList[-1].Add(self.phoneRemoveList[-1])

        self.phoneIndent.append(wx.StaticText(self.memberPanel, size = (-1, 10)))
        self.phoneGroupSizer.Add(self.phoneIndent[-1])
        self.phoneGroupSizer.Add(self.phoneSizerList[-1])
        
        self.Layout()

    def removePartyRow(self, event):
        id = self.phoneRemoveList.index(event.GetEventObject())

        self.faLabelList[id].Destroy()
        self.faEntryList[id].Destroy()
        self.faIndent[id].Destroy()
        self.phoneEntryList[id].Destroy()
        self.phoneRemoveList[id].Destroy()
        self.phoneIndent[id].Destroy()
        
        del self.faSizerList[id]
        del self.phoneSizerList[id]
        del self.faLabelList[id]
        del self.faEntryList[id]
        del self.phoneEntryList[id]
        del self.phoneRemoveList[id]
        del self.faIndent[id]
        del self.phoneIndent[id]

        self.Layout()
        
    def addSupervisorRow(self, event):
        self.supervisorSizers.append(wx.BoxSizer(wx.HORIZONTAL))
        self.supervisorEntrys.append(wx.ComboBox(self.supervisorPanel, style=wx.TE_READONLY, size=(250, -1)))
        self.supervisorRemoves.append(wx.Button(self.supervisorPanel, label="-", size=(25, 24)))
        self.supervisorRemoves[-1].Bind(wx.EVT_BUTTON, self.removeSupervisorRow)
        self.supervisorSizers[-1].Add((10, -1))
        self.supervisorSizers[-1].Add(self.supervisorEntrys[-1])
        self.supervisorSizers[-1].Add(self.supervisorRemoves[-1])
        self.supervisorSizers[-1].Add((10, -1))

        self.supervisorIndents.append(wx.StaticText(self.supervisorPanel, size=(-1, 10)))
        self.supervisorGroup.Add(self.supervisorIndents[-1])
        self.supervisorGroup.Add(self.supervisorSizers[-1])
        
        self.Layout()

    def removeSupervisorRow(self, event):
        id = self.supervisorRemoves.index(event.GetEventObject())

        self.supervisorEntrys[id].Destroy()
        self.supervisorRemoves[id].Destroy()
        self.supervisorIndents[id].Destroy()

        del self.supervisorSizers[id]
        del self.supervisorEntrys[id]
        del self.supervisorRemoves[id]
        del self.supervisorIndents[id]

        self.Layout()

def main():
    app = wx.App()
    frame = wx.Frame(None, size=(1200, 650))
    FieldParty("", "debug", frame)
    frame.Centre()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
