from Tkinter import *

class Controler():
    pass

class Enclosure():
    pass

class MainWindow(object):
    def __init__(self):
        root = Tk()
        root.title('Main')
        top = Frame(root, width=500, height=400)
        top.grid(column=0, row=0)

        # ----- Start frame
        start_frame = Frame(top)
        lab1 = Label(start_frame, text='IP0', width=30)
        lab1.grid(column=0, row=0)
        ent1 = Entry(start_frame, width=50)
        ent1.grid(column=1, row=0)
        lab2 = Label(start_frame, text='IP1', width=30)
        lab2.grid(column=0, row=1)
        ent2 = Entry(start_frame, width=50)
        ent2.grid(column=1, row=1)
        lab_st1 = Label(start_frame, bg='red', width=5)
        lab_st1.grid(column=2,row=0)
        lab_st2 = Label(start_frame, bg='red', width=5)
        lab_st2.grid(column=2, row=1)
        lab_empty = Label(start_frame)
        lab_empty.grid(column=0, row=2)
        start_frame.grid(column=0, row=0)
        # -----Start frame -----

        # ------Info---------
        info_frame = Frame(top)
        lab3 = Label(info_frame, text='IP0', width=40)
        lab3.grid(column=0,row=0)
        lab4 = Label(info_frame, text='IP1', width=40)
        lab4.grid(column=1, row=0)
        lab5 = Label(info_frame, text='Name', width=40)
        lab5.grid(column=2, row=0)

        lab6 = Label(info_frame, text=self.get_master_ship_IP0(), width=40)
        lab6.grid(column=0, row=1)
        lab7 = Label(info_frame, text=self.get_master_ship_IP1(), width=40)
        lab7.grid(column=1, row=1)
        lab8 = Label(info_frame, text='Mastership', width=40)
        lab8.grid(column=2, row=1)

        lab9 = Label(info_frame, text=self.get_ID_IP0(), width=40)
        lab9.grid(column=0, row=2)
        lab10 = Label(info_frame, text=self.get_ID_IP1(), width=40)
        lab10.grid(column=1, row=2)
        lab11 = Label(info_frame, text='ID', width=40)
        lab11.grid(column=2, row=2)

        lab12 = Label(info_frame, text='v1.000', width=40)
        lab12.grid(column=0, row=3)
        lab13 = Label(info_frame, text='v1.000', width=40)
        lab13.grid(column=1, row=3)
        lab14 = Label(info_frame, text='FW_Version', width=40)
        lab14.grid(column=2, row=3)
        info_frame.grid(column=0, row=2)
        # ----Info------

        but1 = Button(top,text='Load')
        but1.grid(column=0, row=3)

        # ------ Enclosures ------
        enclosure_frame = Frame(top)
        lab15 = Label(enclosure_frame, text=self.get_enclosure(), width=80, height=20, bg='yellow')
        lab15.grid(column=0, row=0, columnspan=2)
        lab16 = Label(enclosure_frame, text='Enclosures', width=40)
        lab16.grid(column=2, row=0)
        enclosure_frame.grid(column=0, row=4)
        #------Enclosure

        but_frame_main = Frame(top)
        but3 = Button(but_frame_main, text='Ping')
        but3.grid(column=0, row=0)
        but4 = Button(but_frame_main, text='GetState')
        but4.grid(column=1, row=0)
        but_frame_main.grid(column=0, row=5)

        but_fr = Frame(top)
        but5 = Button(but_fr, text='HOSTS')
        but5.grid(column=0, row=0)
        but6 = Button(but_fr, text='PDU')
        but6.grid(column=0, row=1)
        but7 = Button(but_fr, text='UNIFIED')
        but7.grid(column=0, row=2)
        but_fr.grid(column=1, row=5)

        root.mainloop()

    def get_master_ship_IP0(self):
        return 'MasterIP0'

    def get_master_ship_IP1(self):
        return 'SlaveIP1'

    def get_ID_IP0(self):
        return ''

    def get_ID_IP1(self):
        return 'Fish'

    def get_enclosure(self):
        return 'Text'

if __name__ == '__main__':
    window = MainWindow()
