# All works in this code have been curated by ECCC and licensed under the GNU General Public License v3.0. 
# Read more: https://www.gnu.org/licenses/gpl-3.0.en.html

import wx


class MyComboBox(wx.ComboBox):
    def __init__(self, *args, **kwargs):
        super(MyComboBox, self).__init__(*args, **kwargs)
        self.preValue = ""


class DropdownTime(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(DropdownTime, self).__init__(*args, **kwargs)
        self.minutes = self.GenerateMinutes()
        self.hours = self.GenerateHours()
        self.seconds = self.GenerateMinutes()
        self.InitUI()

    def InitUI(self):

        mySizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(mySizer)

        self.hourCmbox = MyComboBox(self, style=wx.CB_DROPDOWN, choices=self.hours)

        self.minuteCmbox = MyComboBox(self, style=wx.CB_DROPDOWN, choices=self.minutes)
        timeText1 = wx.StaticText(self, label=':')

        mySizer.Add(self.hourCmbox, 1, wx.LEFT | wx.TOP, 3)
        mySizer.Add(timeText1, 0, wx.TOP, 3)
        mySizer.Add(self.minuteCmbox, 1, wx.TOP | wx.RIGHT, 3)

        self.hourCmbox.Bind(wx.EVT_KEY_UP, self.OnTimeKeyUp)
        self.minuteCmbox.Bind(wx.EVT_KEY_UP, self.OnTimeKeyUp)


    def GenerateMinutes(self):
        a = list(range(60))
        b = [""]
        for i in a:
            n = str(i)
            if len(n) == 1:
                n = '0' + n
            b.append(n)
        return b

    def GenerateHours(self):
        a = list(range(24))
        b = [""]
        for i in a:
            n = str(i)
            if len(n) == 1:
                n = '0' + n
            b.append(n)
        return b

    def OnTimeKeyUp(self, event):
        keycode = event.GetKeyCode()
        self.NumberControl(event)
        if keycode == ord('R') or keycode == ord('C'):
            self.UpdateTime(keycode)

        event.Skip()

    def UpdateTime(self, keycode):
        if keycode == ord('R'):
            self.Clear()
        elif keycode == ord('C'):
            self.SetToCurrent()

    def Clear(self):
        self.hourCmbox.ChangeValue("")
        self.minuteCmbox.ChangeValue("")
            
    def GetHourVal(self):
        return self.hourCmbox.GetValue()

    def GetHour(self):
        return self.hourCmbox

    def SetHourVal(self, val):
        self.hourCmbox.SetValue(val)

    def ChangeHourVal(self, val):
        self.hourCmbox.ChangeValue(val)

    def GetMinuteVal(self):
        return self.minuteCmbox.GetValue()

    def GetMinute(self):
        return self.minuteCmbox

    def SetMinuteVal(self, val):
        self.minuteCmbox.SetValue(val)

    def ChangeMinuteVal(self, val):
        self.minuteCmbox.ChangeValue(val)

    def GetSecondVal(self):
        return self.secondCmbox.GetValue()

    def GetSecond(self):
        return self.secondCmbox

    def SetSecondVal(self, val):
        self.secondCmbox.SetValue(val)

    def ChangeSecondVal(self, val):
        self.secondCmbox.ChangeValue(val)

    def GetHourCtrl(self):
        return self.hourCmbox

    def GetMinuteCtrl(self):
        return self.minuteCmbox

    def GetSecondCtrl(self):
        return self.secondCmbox

    def GetValue(self):
        return self.GetHourVal() + ":" + self.GetMinuteVal()

    def SetValue(self, val):
        if val is None:
            self.SetSecondVal("")
            self.SetHourVal("")
            self.SetMinuteVal("")
        else:
            hour = val.split(":")[0]
            minute = val.split(":")[1]
            self.SetHourVal(hour)
            self.SetMinuteVal(minute)

    # Check if the time has value for hour, minute and second
    def IsCompleted(self):
        return self.GetHourVal() != '' and self.GetMinuteVal() != ''
    
    def SetBackgroundColour(self, color):
        self.hourCmbox.SetBackgroundColour(color)
        self.minuteCmbox.SetBackgroundColour(color)
        self.hourCmbox.Refresh()
        self.minuteCmbox.Refresh()

    def NumberControl(self, evt):
        ctrl = evt.GetEventObject()
        value = ctrl.GetValue().strip()
        insertPoint = ctrl.GetInsertionPoint()
        digits = len(value) - len(ctrl.preValue)

        try:

            temp = int(value)
            temp = str(temp) if temp > 9 else "0" + str(temp)
            if ((ctrl == self.hourCmbox and temp in self.hours) or 
                (ctrl == self.minuteCmbox and temp in self.minutes)) \
                    and len(value) < 3:

                ctrl.preValue = value
                # ctrl.ChangeValue(value)

            else:
                ctrl.ChangeValue(ctrl.preValue)
                ctrl.SetInsertionPoint(insertPoint - digits)


        except:
            if value == "":
                ctrl.preValue = ""
                ctrl.ChangeValue("")

            else:
                ctrl.ChangeValue(ctrl.preValue)
                ctrl.SetInsertionPoint(insertPoint - digits)

        evt.Skip()