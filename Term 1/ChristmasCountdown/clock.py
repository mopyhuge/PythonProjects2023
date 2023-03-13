import datetime

from settings import *

class Application(Frame):
    date = "12/25/2022"

    # font = ("helvetica", 58), width = 20 fg = "green"

    def initUI(self):

        self.event = "?????????"
        self.holiday_index = 0
        self.img_index = 0
        img = PhotoImage(file = path.join(img_folder_list[0],img_lists[self.holiday_index][self.img_index]))
        self.bg = Label(self,image = img)
        self.bg.image = img
        self.bg.configure(image=img)

        self.bg.place(x = 0,y = 0)

        self.event_selector = ttk.Combobox(self,textvariable="")
        self.event_selector["values"]= ("Birthday","4th of July","Christmas","New Years","Halloween","Easter")
        self.event_selector["state"]="readonly"
        self.event_selector.bind("<<ComboboxSelected>>",self.selectDate)
        self.event_selector.place(x=1750,y=975)

        self.monthdefaultVar = IntVar()
        self.monthdefaultVar.set(datetime.datetime.now().month)

        self.moSpinner = Spinbox(self,from_=1,to=12, width = 5, textvariable = self.monthdefaultVar,command = self.setDays)
        self.moSpinner.place(x=1550, y = 975)

        days_in_month = 31
        x = self.moSpinner.get()
        if x in [4,6,9,11]:
            days_in_month = 30
        elif x == 2:
            days_in_month = 28
        else:
            days_in_month = 31

        self.daydefaultVar = IntVar()
        self.daydefaultVar.set(datetime.datetime.now().day)

        self.daySpinner = Spinbox(self, from_=1, to=days_in_month, width=5, textvariable = self.daydefaultVar)
        self.daySpinner.place(x=1610, y=975)

        self.yeardefaultVar = IntVar()
        self.yeardefaultVar.set(datetime.datetime.now().year)

        current_year = datetime.datetime.now().year
        self.yearSpinner = Spinbox(self, from_=current_year, to=current_year+3, width=8,textvariable = self.yeardefaultVar)
        self.yearSpinner.place(x=1670, y=975)

        self.change_img_button = Button(self, text="Change pic?", command=self.change_pic)
        self.change_img_button.place(x=WIDTH / 2, y=HEIGHT / 2)



        self.event_lbl = Label(self,text = "Time until "+self.event, fg = "Black", font=("helvetica", 58))
        self.event_lbl.place(x = 100, y = 100)
        Label(self,text = "Days",fg = "black", font =("helvetica", 58)).place(x=200,y = 200)
        Label(self,text = "Hours",fg = "black", font =("helvetica", 58)).place(x=410,y = 200)
        Label(self,text = "Minutes",fg = "black", font =("helvetica", 58)).place(x=650,y = 200)
        Label(self,text = "Seconds",fg = "black", font =("helvetica", 58)).place(x=950,y = 200)

        self.days_lbl = Label(self,text = "0000", fg = "black", font =("helvetica", 58))
        self.days_lbl.place(x=200,y=300)
        self.hours_lbl = Label(self,text = "00", fg = "black", font =("helvetica", 58))
        self.hours_lbl.place(x=510,y=300)
        self.min_lbl = Label(self,text = "00", fg = "black", font =("helvetica", 58))
        self.min_lbl.place(x=750,y=300)
        self.sec_lbl = Label(self,text = "00", fg = "black", font =("helvetica", 58))
        self.sec_lbl.place(x=1050,y=300)
        self.time = self.time_until(self.setDate())

        self.date = self.setDate()

    def update(self):

        total_seconds = self.time_until(self.date).seconds
        total_minutes = total_seconds//60
        total_hours = total_minutes//60

        cur_sec = total_seconds%60
        cur_min = total_hours%60
        cur_hour = total_hours% 24

        days = StringVar()
        days = self.time_until(self.date).days
        seconds = StringVar()
        min = StringVar()
        hour = StringVar()

        seconds = cur_sec
        min = cur_min
        self.days_lbl.config(text = days)
        self.sec_lbl.config(text = seconds)
        self.min_lbl.config(text = min)
        # self.hours_lbl.config(text = hour)



        self.master.after(1,self.update)

    def setDays(self):
        days_in_month = 31
        x = self.moSpinner.get()
        if x in [4, 6, 9, 11]:
            days_in_month = 30
        elif x == 2:
            days_in_month = 28
        else:
            days_in_month = 31
        self.daySpinner["to"]=days_in_month

    def setDate(self):
        month = self.moSpinner.get()
        day = self.daySpinner.get()
        year = self.yearSpinner.get()
        return str(month)+"/"+str(day)+"/"+str(year)

    def time_until(self, date):
        date = datetime.datetime.strptime(date, "%m/%d/%Y")
        now = datetime.datetime.now()
        if date > now:
            time_until = date - now
            return time_until
        else:
            return now - now

    def change_pic(self):
        ok = self.selectDate(self)

        if ok:
            self.img_index = random.randint(0, len(img_lists[self.holiday_index])-1)
            img = PhotoImage(
                file=path.join(img_folder_list[self.holiday_index], img_lists[self.holiday_index][self.img_index]))
            self.bg.configure(image=img)
            self.bg.image = img

        self.date = self.setDate()

    def selectDate(self,x):
        curMonth = datetime.datetime.now().month
        curDay = datetime.datetime.now().day
        curYear = datetime.datetime.now().year
        curDate = datetime.datetime.now()

        self.x = self.event_selector.get()

        if (self.x == "Christmas"):
            self.holiday_index = 2
            day = 25
            month = 12
            year = curYear
            date = datetime.datetime.strptime(str(month)+"/"+str(day)+"/"+str(year),"%m/%d/%Y")

            if curDate >= date:
                year += 1
            self.daydefaultVar.set(day)
            self.monthdefaultVar.set(month)
            self.yeardefaultVar.set(year)
            return True
        elif self.x == "New Years":
            self.holiday_index = 3
            day = 1
            month = 1
            year = curYear
            date = datetime.datetime.strptime(str(month) + "/" + str(day) + "/" + str(curYear), "%m/%d/%Y")
            if curDate >= date:
                year += 1
            self.daydefaultVar.set(day)
            self.monthdefaultVar.set(month)
            self.yeardefaultVar.set(year)
            return True
        elif self.x == "Easter":
            self.holiday_index = 4
            day = 9
            month = 4
            year = curYear
            date = datetime.datetime.strptime(str(month) + "/" + str(day) + "/" + str(curYear), "%m/%d/%Y")
            if curDate >= date:
                year += 1
            self.daydefaultVar.set(day)
            self.monthdefaultVar.set(month)
            self.yeardefaultVar.set(year)
            return True
        elif self.x == "Halloween":
            self.holiday_index = 5
            day = 31
            month = 10
            year = curYear
            date = datetime.datetime.strptime(str(month) + "/" + str(day) + "/" + str(curYear), "%m/%d/%Y")
            if curDate >= date:
                year += 1
            self.daydefaultVar.set(day)
            self.monthdefaultVar.set(month)
            self.yeardefaultVar.set(year)
            return True
        elif self.x == "Birthday":
            self.holiday_index = 0
            day = 27
            month = 12
            year = curYear
            date = datetime.datetime.strptime(str(month) + "/" + str(day) + "/" + str(curYear), "%m/%d/%Y")
            if curDate >= date:
                year += 1
            self.daydefaultVar.set(day)
            self.monthdefaultVar.set(month)
            self.yeardefaultVar.set(year)
            return True
        elif self.x == "4th of July":
            self.holiday_index = 1
            day = 4
            month = 7
            year = curYear
            date = datetime.datetime.strptime(str(month) + "/" + str(day) + "/" + str(curYear), "%m/%d/%Y")
            if curDate >= date:
                year += 1
            self.daydefaultVar.set(day)
            self.monthdefaultVar.set(month)
            self.yeardefaultVar.set(year)
            return True
        else:
            return False


    def __init__(self,master):
        super(Application, self).__init__(master)

        self.master.title(title)
        self.master.geometry(SCREENSIZE)
        self.master.configure(background = "green")

        self.initUI()

        self.pack(fill=BOTH, expand=1)


