from tkinter import *
from madhu1 import backend
from tkinter import font
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


class calamity:

    def __init__(self):
        self.root=Tk()
        self.top_panel()
        self.admin_login()
        self.exit_button()
        
        # self.page_2_param()
        self.ob=backend()
    
    def admin_login(self):
        self.canvas.destroy()
        self.top_panel()

        self.txt7=self.canvas.create_text(680,60,text="Natural Calamity Monitoring and Management System",font=('Comic Sans MS',38),fill="white")
        self.txt2=self.canvas.create_text(550,200,text="Username:",font=('Comic Sans MS',25),fill="white")
        self.e3=Entry(self.canvas)

        self.canvas.create_window(700,200,window=self.e3)
        self.txt3=self.canvas.create_text(550,250,text="Password:",font=('Comic Sans MS',25),fill="white")
        self.e4=Entry(self.canvas,show="*")
        self.canvas.create_window(700,250,window=self.e4)
        
        self.button3=Button(self.root,text="Login",anchor='center',width=8,font=('Comic Sans MS',15),command=self.login_db)
        self.button3_window=self.canvas.create_window(500,350,anchor='center',window=self.button3)

        self.button3=Button(self.root,text="Update Password",anchor='center',width=15,font=('Comic Sans MS',15),command=self.update_doc_password)
        self.button3_window=self.canvas.create_window(750,350,anchor='center',window=self.button3)

    def top_panel(self):
        self.canvas=Canvas(self.root,width=1920,height=1080)
        self.my_image=PhotoImage(file='C:\\1.data\\Madhuraank\\dbms-project\\imgs\\stone.gif')
        self.canvas.create_image(0,0,anchor=NW,image=self.my_image)
        self.canvas.grid()
        self.root.title("Natural Calamity Monitoring and Management System")

    def exit_button(self):
        self.menuBar=Menu(self.root)
        self.root.config(menu=self.menuBar)
        self.fileMenu=Menu(self.menuBar,tearoff=0)
        self.menuBar.add_command(label="Exit",command=self.exit)
    
    def login_db(self):
        username=self.e3.get()
        password=self.e4.get()
        self.login(username,password)
        self.txt4=self.canvas.create_text(500,300,text="",font=("arial",15),fill="white")

    def login(self,username,password):
        i=0
        j=0
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select name from users where name=%s",(username))
        for row in cursor:
            i=i+1
            if(i==1):
                cursor.execute("select password from users where password=%s and name=%s",(password,username))
                for row in cursor:
                    j=j+1
                    if(j==1):
                        self.canvas.destroy()
                        self.top_panel()
                        self.page_2_param()
                        self.exit_button()
        if(i==0):
            self.admin_login()
            self.txt4=self.canvas.create_text(700,300,text="User Doesn't Exist!!!!!!",font=("cooper std",20),fill="cyan")
        elif(i==1 and j==0):
            self.admin_login()
            self.txt4=self.canvas.create_text(700,300,text="You Have Entered Worng Password",font=("cooper std",18),fill="Red")
        conn.commit()
        self.ob.close(cursor,conn)

# to update password

    def update_doc_password(self):
        
        paramBtnFont=font.Font(family='Comic Sans MS', size=15)
            
        self.canvas.destroy()
        self.top_panel()
    
        self.txt2=self.canvas.create_text(520,150,text="Enter user name  :",font=paramBtnFont,fill="white")
        self.txt2=self.canvas.create_text(500,200,text="Enter old password  :",font=paramBtnFont,fill="white")
        self.txt3=self.canvas.create_text(500,250,text="Enter new password :",font=paramBtnFont,fill="white")
        self.b1=Entry(self.canvas)
        self.canvas.create_window(730,150,window=self.b1)
        self.b2=Entry(self.canvas)
        self.canvas.create_window(730,200,window=self.b2)
        self.b3=Entry(self.canvas)
        self.canvas.create_window(730,250,window=self.b3)
        
        self.button3=Button(self.root,text="Back",anchor='center',font=paramBtnFont,width=20,height=1,command=self.back4)
        self.button3_window=self.canvas.create_window(300,310,anchor='nw',window=self.button3)
        
        self.button2=Button(self.root,text="Submit",anchor='center',font=paramBtnFont,width=20,height=1,command=self.update_doc_password_db)
        self.button2_window=self.canvas.create_window(680,310,anchor='nw',window=self.button2)      
    
    def update_doc_password_db(self):
        usr=self.b1.get()
        old_password=self.b2.get()
        new_password=self.b3.get()
        self.ob.update_doc_password(usr,new_password,old_password)
    
    def back4(self):
        self.canvas.destroy()
        self.top_panel()
        self.admin_login()

    # page 2 : calamity, parameter and alert

    def page_2_param(self):
        self.canvas.destroy()
        self.top_panel()

        self.txt=self.canvas.create_text(680,30,text="Natural Calamity Monitoring and Management System",font=('Comic Sans MS',30),fill="white")
        
        mainBtnFont=font.Font(family='Comic Sans MS', size=15, weight='bold')
        paramBtnFont=font.Font(family='Comic Sans MS', size=10)

        # earthquake buttons

        self.earthquakePic=PhotoImage(file='C:\\1.data\\Madhuraank\\dbms-project\\imgs\\earthquake-1.gif')
        self.button=Button(self.root,image=self.earthquakePic,width=260,height=140)
        self.button_window=self.canvas.create_window(20,75,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Earthquake",bg="green yellow",anchor='center',width=12,height=2,font=mainBtnFont,command=self.earthquake)
        self.button_window=self.canvas.create_window(340,110,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Seismic Wave",bg="yellow",anchor='center',width=12,height=2,font=paramBtnFont,command=self.seismic_wave)
        self.button_window=self.canvas.create_window(540,125,anchor='nw',window=self.button)

        self.button=Button(self.root,text="P Wave",bg="yellow",anchor='center',width=12,height=2,font=paramBtnFont,command=self.p_wave)
        self.button_window=self.canvas.create_window(680,125,anchor='nw',window=self.button)

        self.button=Button(self.root,text="S Wave",bg="yellow",anchor='center',width=12,height=2,font=paramBtnFont,command=self.s_wave)
        self.button_window=self.canvas.create_window(820,125,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Ground Motion",bg="yellow",anchor='center',width=12,height=2,font=paramBtnFont,command=self.ground_motion)
        self.button_window=self.canvas.create_window(960,125,anchor='nw',window=self.button)
        
        # flood buttons

        self.floodPic=PhotoImage(file='C:\\1.data\\Madhuraank\\dbms-project\\imgs\\flood-1.gif')
        self.button=Button(self.root,image=self.floodPic,width=260,height=140)
        self.button_window=self.canvas.create_window(20,225,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Floods",bg="green yellow",anchor='center',width=12,height=2,font=mainBtnFont,command=self.floods)
        self.button_window=self.canvas.create_window(340,260,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Water Surface Elevation",bg="yellow",wraplength=80,anchor='center',width=12,height=2,font=paramBtnFont,command=self.water_surface_elevation)
        self.button_window=self.canvas.create_window(540,275,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Water Level Measurement",bg="yellow",wraplength=80,anchor='center',width=12,height=2,font=paramBtnFont,command=self.water_level_measurement)
        self.button_window=self.canvas.create_window(680,275,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Soil Moisture Content",bg="yellow",wraplength=80,anchor='center',width=12,height=2,font=paramBtnFont,command=self.soil_moisture_content)
        self.button_window=self.canvas.create_window(820,275,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Rainfall Measurement",bg="yellow",wraplength=80,anchor='center',width=12,height=2,font=paramBtnFont,command=self.rainfall_measurement)
        self.button_window=self.canvas.create_window(960,275,anchor='nw',window=self.button)

        # wildfire buttons

        self.wildfirePic=PhotoImage(file='C:\\1.data\\Madhuraank\\dbms-project\\imgs\\wildfire-1.gif')
        self.button=Button(self.root,image=self.wildfirePic,width=260,height=140)
        self.button_window=self.canvas.create_window(20,375,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Wildfire",bg="green yellow",anchor='center',width=12,height=2,font=mainBtnFont,command=self.wildfire)
        self.button_window=self.canvas.create_window(340,410,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Temperature",bg="yellow",anchor='center',width=12,height=2,font=paramBtnFont,command=self.temperature)
        self.button_window=self.canvas.create_window(540,425,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Humidity",bg="yellow",anchor='center',width=12,height=2,font=paramBtnFont,command=self.humidity)
        self.button_window=self.canvas.create_window(680,425,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Smoke Density",bg="yellow",anchor='center',width=12,height=2,font=paramBtnFont,command=self.smoke_density)
        self.button_window=self.canvas.create_window(820,425,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Light Intensity",bg="yellow",anchor='center',width=12,height=2,font=paramBtnFont,command=self.light_intensity)
        self.button_window=self.canvas.create_window(960,425,anchor='nw',window=self.button)

        # storm buttons

        self.stormPic=PhotoImage(file='C:\\1.data\\Madhuraank\\dbms-project\\imgs\\storm-1.gif')
        self.button=Button(self.root,image=self.stormPic,width=260,height=140)
        self.button_window=self.canvas.create_window(20,525,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Storms",bg="green yellow",anchor='center',width=12,height=2,font=mainBtnFont,command=self.storms)
        self.button_window=self.canvas.create_window(340,560,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Equilibrium Level",bg="yellow",wraplength=80,anchor='center',width=12,height=2,font=paramBtnFont,command=self.equilibrium_level)
        self.button_window=self.canvas.create_window(540,575,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Lapse Rate",bg="yellow",anchor='center',width=12,height=2,font=paramBtnFont,command=self.lapse_rate)
        self.button_window=self.canvas.create_window(680,575,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Convective Inhibition",bg="yellow",wraplength=80,anchor='center',width=12,height=2,font=paramBtnFont,command=self.convective_inhibition)
        self.button_window=self.canvas.create_window(820,575,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Storm Relative Helicity",bg="yellow",wraplength=80,anchor='center',width=12,height=2,font=paramBtnFont,command=self.storm_relative_helicity)
        self.button_window=self.canvas.create_window(960,575,anchor='nw',window=self.button)

        # alert buttons
        
        self.button=Button(self.root,text="Alerts",bg="salmon",anchor='center',width=12,height=2,font=mainBtnFont,command=self.view_delete_alert)
        self.button_window=self.canvas.create_window(1150,300,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Back",bg="salmon",anchor='center',width=12,height=2,font=mainBtnFont,command=self.admin_login)
        self.button_window=self.canvas.create_window(1150,400,anchor='nw',window=self.button)

    # pg2 design ends here

    # back button for param page

    def back_button_param(self):
        self.canvas.destroy()
        self.top_panel()
        self.page_2_param()    

    # earthquake button functionality

    def earthquake(self):
        self.canvas.destroy()
        self.top_panel()

        mainBtnFont=font.Font(family='Comic Sans MS', size=15, weight='bold')
        paramBtnFont=font.Font(family='Comic Sans MS', size=10)

        self.txt=self.canvas.create_text(600,50,text="Earthquake",font=("Comic Sans MS",55),fill="OliveDrab1")

        self.button=Button(self.root,text="Insert Data",anchor='center',bg="dark orange",width=12,height=2,font=mainBtnFont,command=self.insert_earthquake)
        self.button_window=self.canvas.create_window(1180,150,anchor='nw',window=self.button)

        self.button=Button(self.root,text="View Data",anchor='center',bg="dark orange",width=12,height=2,font=mainBtnFont,command=self.display_earthquake)
        self.button_window=self.canvas.create_window(1180,250,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Graph",anchor='center',bg="dark orange",width=12,height=2,font=mainBtnFont,command=self.graph_earthquake)
        self.button_window=self.canvas.create_window(1180,350,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Back",anchor='center',bg="dark orange",width=12,height=2,font=mainBtnFont,command=self.back_button_param)
        self.button_window=self.canvas.create_window(1180,450,anchor='nw',window=self.button)

        self.txt=self.canvas.create_text(520,390,font=("Comic Sans MS",16),fill="wheat1",text="An earthquake (also known as a quake, tremor or temblor) is the shaking \n of the surface of the Earth, resulting from the sudden release of energy \n in the Earth's lithosphere that creates seismic waves. Earthquakes can \n range in size from those that are so weak that they cannot be felt to those \n violent enough to toss people around and destroy whole cities. The seismicity, \n or seismic activity, of an area is the frequency, type and size of earthquakes \n experienced over a period of time. The word tremor is also used for non-earthquake \n seismic rumbling. At the Earth's surface, earthquakes manifest themselves by \n shaking and displacing or disrupting the ground. When the epicenter of a \n large earthquake is located offshore, the seabed may be displaced sufficiently \n to cause a tsunami. Earthquakes can also trigger landslides, and occasionally \n volcanic activity. In its most general sense, the word earthquake is used to \n describe any seismic event — whether natural or caused by humans — that generates \n seismic waves. Earthquakes are caused mostly by rupture of geological faults, \n but also by other events such as volcanic activity, landslides, mine blasts, \n and nuclear tests. An earthquake's point of initial rupture is called its \n focus or hypocenter. The epicenter is the point at ground level directly above the hypocenter.")

    # insert data to earthquake table

    def insert_earthquake(self):
        self.canvas.destroy()
        self.top_panel()

        mainBtnFont=font.Font(family='Comic Sans MS', size=15, weight='bold')

        self.txt=self.canvas.create_text(200,150,text="E Id:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.e_id_insert=Entry(self.canvas)
        self.canvas.create_window(350,150,width=200,height=30,window=self.e_id_insert)
        
        self.txt=self.canvas.create_text(125,250,text="Seismic Wave:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.seismic_wave_insert=Entry(self.canvas)
        self.canvas.create_window(350,250,width=200,height=30,window=self.seismic_wave_insert)
        
        self.txt=self.canvas.create_text(180,350,text="P Wave:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.p_wave_insert=Entry(self.canvas)
        self.canvas.create_window(350,350,width=200,height=30,window=self.p_wave_insert)
        
        self.txt=self.canvas.create_text(180,450,text="S Wave:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.s_wave_insert=Entry(self.canvas)
        self.canvas.create_window(350,450,width=200,height=30,window=self.s_wave_insert)
        
        self.txt=self.canvas.create_text(125,550,text="Ground Motion:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.ground_motion_insert=Entry(self.canvas)
        self.canvas.create_window(350,550,width=200,height=30,window=self.ground_motion_insert)
        
        self.button=Button(self.root,text="Submit",anchor='center',width=10,height=1,font=mainBtnFont,command=self.submit_earthquake)
        self.button_window=self.canvas.create_window(600,580,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Back",anchor='center',width=10,height=1,font=mainBtnFont,command=self.back_button_earthquake)
        self.button_window=self.canvas.create_window(800,580,anchor='nw',window=self.button)
        
    def submit_earthquake(self):
        
        # check if fields are blank

        if len(self.e_id_insert.get()) and len(self.seismic_wave_insert.get()) and len(self.p_wave_insert.get()) and len(self.s_wave_insert.get()) and len(self.ground_motion_insert.get()) == 0:
            tk.messagebox.showerror('Please fill fields')

        # store float values

        e_id=float(self.e_id_insert.get())
        seismic_wave=float(self.seismic_wave_insert.get())
        p_wave=float(self.p_wave_insert.get())
        s_wave=float(self.s_wave_insert.get())
        ground_motion=float(self.ground_motion_insert.get())
    
        # insert to earthquake table in the DB

        self.ob.add_earthquake(e_id,seismic_wave,p_wave,s_wave,ground_motion)
        tk.messagebox._show('Submitted')

        # insert to alert table if value is greater that 9

        cn='earthquake'
        pn1='seismic_wave'
        pn2='p_wave'
        pn3='s_wave'
        pn4='ground_motion'

        if seismic_wave>9:
            self.ob.add_alert(seismic_wave,cn,pn1)
        if p_wave>9:
            self.ob.add_alert(p_wave,cn,pn2)
        if s_wave>9:
            self.ob.add_alert(s_wave,cn,pn3)
        if ground_motion>9:
            self.ob.add_alert(ground_motion,cn,pn4)

        # clear the fields, once submitted

        self.e_id_insert.delete(0, 'end')
        self.seismic_wave_insert.delete(0, 'end')
        self.p_wave_insert.delete(0, 'end')
        self.s_wave_insert.delete(0, 'end')
        self.ground_motion_insert.delete(0, 'end')

    def back_button_earthquake(self):
        self.canvas.destroy()
        self.top_panel()
        self.earthquake()    

# display data from earthquake table

    def display_earthquake(self):
        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1", "2","3","4","5")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')
        tv.column("2", width=100, anchor='c')
        tv.column("3", width=100, anchor='c')
        tv.column("4", width=100, anchor='c')
        tv.column("5", width=100, anchor='c')
        
        tv.heading("1", text="e_id")
        tv.heading("2", text="seismic_wave")
        tv.heading("3", text="p_wave")
        tv.heading("4", text="s_wave")
        tv.heading("5", text="ground_motion")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select * from earthquake")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0],row[1],row[2],row[3],row[4]))
            cpt += 1
        self.ob.close(cursor,conn)

# graph for earthquake data

    def graph_earthquake(self):
        self.canvas.destroy()
        self.page_2_param()

    # floods button functionality

    def floods(self):
        self.canvas.destroy()
        self.top_panel()

        mainBtnFont=font.Font(family='Comic Sans MS', size=15, weight='bold')
        paramBtnFont=font.Font(family='Comic Sans MS', size=10)

        self.txt=self.canvas.create_text(600,50,text="Floods",font=("Comic Sans MS",55),fill="OliveDrab1")

        self.button=Button(self.root,text="Insert Data",anchor='center',bg="dark orange",width=12,height=2,font=mainBtnFont,command=self.insert_floods)
        self.button_window=self.canvas.create_window(1180,150,anchor='nw',window=self.button)

        self.button=Button(self.root,text="View Data",anchor='center',bg="dark orange",width=12,height=2,font=mainBtnFont,command=self.display_floods)
        self.button_window=self.canvas.create_window(1180,250,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Graph",anchor='center',bg="dark orange",width=12,height=2,font=mainBtnFont,command=self.graph_floods)
        self.button_window=self.canvas.create_window(1180,350,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Back",anchor='center',bg="dark orange",width=12,height=2,font=mainBtnFont,command=self.back_button_param)
        self.button_window=self.canvas.create_window(1180,450,anchor='nw',window=self.button)

        self.txt=self.canvas.create_text(520,390,font=("Comic Sans MS",16),fill="wheat1",text="A flood is an overflow of water that submerges land that is usually dry. \n The European Union (EU) Floods Directive defines a flood as a covering by \n water of land not normally covered by water.[2] In the sense of 'flowing water', \n the word may also be applied to the inflow of the tide. Floods are an area \n of study of the discipline hydrology and are of significant concern in agriculture, \n civil engineering and public health. Flooding may occur as an overflow of water from water bodies, \n such as a river, lake, or ocean, in which the water overtops or breaks levees, \n resulting in some of that water escaping its usual boundaries,[3] or it may \n occur due to an accumulation of rainwater on saturated ground in an areal \n flood. While the size of a lake or other body of water will vary with \n seasonal changes in precipitation and snow melt, these changes in size are \n unlikely to be considered significant unless they flood property or drown \n domestic animals. Floods can also occur in rivers when the flow rate exceeds the capacity \n of the river channel, particularly at bends or meanders in the waterway. Floods \n often cause damage to homes and businesses if they are in the natural flood \n plains of rivers. While riverine flood damage can be eliminated by moving away \n from rivers and other bodies of water, people have traditionally lived and \n worked by rivers because the land is usually flat and fertile and because \n rivers provide easy travel and access to commerce and industry.")

    # insert data to floods table

    def insert_floods(self):
        self.canvas.destroy()
        self.top_panel()

        mainBtnFont=font.Font(family='Comic Sans MS', size=15, weight='bold')

        self.txt=self.canvas.create_text(380,150,text="F Id:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.f_id_insert=Entry(self.canvas)
        self.canvas.create_window(550,150,width=200,height=30,window=self.f_id_insert)
        
        self.txt=self.canvas.create_text(225,250,text="Water Surface Elevation:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.water_surface_elevation_insert=Entry(self.canvas)
        self.canvas.create_window(550,250,width=200,height=30,window=self.water_surface_elevation_insert)
        
        self.txt=self.canvas.create_text(225,350,text="Water Level Measurement:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.water_level_measurement_insert=Entry(self.canvas)
        self.canvas.create_window(550,350,width=200,height=30,window=self.water_level_measurement_insert)
        
        self.txt=self.canvas.create_text(250,450,text="Soil Moisture Content:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.soil_moisture_content_insert=Entry(self.canvas)
        self.canvas.create_window(550,450,width=200,height=30,window=self.soil_moisture_content_insert)
        
        self.txt=self.canvas.create_text(260,550,text="Rainfall Measurement:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.rainfall_measurement_insert=Entry(self.canvas)
        self.canvas.create_window(550,550,width=200,height=30,window=self.rainfall_measurement_insert)
        
        self.button=Button(self.root,text="Submit",anchor='center',width=10,height=1,font=mainBtnFont,command=self.submit_floods)
        self.button_window=self.canvas.create_window(800,580,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Back",anchor='center',width=10,height=1,font=mainBtnFont,command=self.back_button_floods)
        self.button_window=self.canvas.create_window(1000,580,anchor='nw',window=self.button)
        
    def submit_floods(self):
        
         # check if fields are blank

        if len(self.f_id_insert.get()) and len(self.water_surface_elevation_insert.get()) and len(self.soil_moisture_content_insert.get()) and len(self.rainfall_measurement_insert.get()) == 0:
            tk.messagebox.showerror('Please fill fields')

        # store float values

        f_id=float(self.f_id_insert.get())
        water_surface_elevation=float(self.water_surface_elevation_insert.get())
        water_level_measurement=float(self.water_level_measurement_insert.get())
        soil_moisture_content=float(self.soil_moisture_content_insert.get())
        rainfall_measurement=float(self.rainfall_measurement_insert.get())
        
        # insert to flood table in the DB
        
        self.ob.add_floods(f_id,water_surface_elevation,water_level_measurement,soil_moisture_content,rainfall_measurement)
        tk.messagebox._show('Submitted')

        # insert to alert table if value is greater that 9

        cn='floods'
        pn1='water_surface_elevation'
        pn2='water_level_measurement'
        pn3='soil_moisture_content'
        pn4='rainfall_measurement'

        if water_surface_elevation>9:
            self.ob.add_alert(water_surface_elevation,cn,pn1)
        if water_level_measurement>9:
            self.ob.add_alert(water_level_measurement,cn,pn2)
        if soil_moisture_content>9:
            self.ob.add_alert(soil_moisture_content,cn,pn3)
        if rainfall_measurement>9:
            self.ob.add_alert(rainfall_measurement,cn,pn4)

        # clear the fields, once submitted

        self.f_id_insert.delete(0, 'end')
        self.water_surface_elevation_insert.delete(0, 'end')
        self.water_level_measurement_insert.delete(0, 'end')
        self.soil_moisture_content_insert.delete(0, 'end')
        self.rainfall_measurement_insert.delete(0, 'end')

    def back_button_floods(self):
        self.canvas.destroy()
        self.top_panel()
        self.floods()    

# display data from floods table

    def display_floods(self):
        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1", "2","3","4","5")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')
        tv.column("2", width=100, anchor='c')
        tv.column("3", width=100, anchor='c')
        tv.column("4", width=100, anchor='c')
        tv.column("5", width=100, anchor='c')
        
        tv.heading("1", text="f_id")
        tv.heading("2", text="water_surface_elevation")
        tv.heading("3", text="water_level_measurement")
        tv.heading("4", text="soil_moisture_content")
        tv.heading("5", text="rainfall_measurement")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select * from flood")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0],row[1],row[2],row[3],row[4]))
            cpt += 1
        self.ob.close(cursor,conn)

    # graph for floods data

    def graph_floods(self):
        self.canvas.destroy()
        self.page_2_param()

    # wildfire button functionality

    def wildfire(self):
        self.canvas.destroy()
        self.top_panel()

        mainBtnFont=font.Font(family='Comic Sans MS', size=15, weight='bold')
        paramBtnFont=font.Font(family='Comic Sans MS', size=10)

        self.txt=self.canvas.create_text(600,50,text="Wildfire",font=("Comic Sans MS",55),fill="OliveDrab1")

        self.button=Button(self.root,text="Insert Data",anchor='center',bg="dark orange",width=12,height=2,font=mainBtnFont,command=self.insert_wildfire)
        self.button_window=self.canvas.create_window(1180,150,anchor='nw',window=self.button)

        self.button=Button(self.root,text="View Data",anchor='center',bg="dark orange",width=12,height=2,font=mainBtnFont,command=self.display_wildfire)
        self.button_window=self.canvas.create_window(1180,250,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Graph",anchor='center',bg="dark orange",width=12,height=2,font=mainBtnFont,command=self.graph_wildfire)
        self.button_window=self.canvas.create_window(1180,350,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Back",anchor='center',bg="dark orange",width=12,height=2,font=mainBtnFont,command=self.back_button_param)
        self.button_window=self.canvas.create_window(1180,450,anchor='nw',window=self.button)

        self.txt=self.canvas.create_text(520,390,font=("Comic Sans MS",16),fill="wheat1",text="A wildfire or wildland fire is a fire in an area of combustible vegetation \n occurring in rural areas.[1] Depending on the type of vegetation present, \n a wildfire can also be classified more specifically as a brush fire, bushfire, \n desert fire, forest fire, grass fire, hill fire, peat fire, vegetation fire, \n and veld fire. Fossil charcoal indicates that wildfires began soon after \n the appearance of terrestrial plants 420 million years ago.[3] Wildfire's \n occurrence throughout the history of terrestrial life invites conjecture that \n fire must have had pronounced evolutionary effects on most ecosystems' flora \n and fauna.[4] Earth is an intrinsically flammable planet owing to its cover \n of carbon-rich vegetation, seasonally dry climates, atmospheric oxygen, and \n widespread lightning and volcanic ignitions. Wildfires can be characterized \n in terms of the cause of ignition, their physical properties, the combustible \n material present, and the effect of weather on the fire.[5] Wildfires can \n cause damage to property and human life, though naturally occurring wildfires \n may have beneficial effects on native vegetation, animals, and ecosystems that \n have evolved with fire.")

    # insert data to wildfire table

    def insert_wildfire(self):
        self.canvas.destroy()
        self.top_panel()

        mainBtnFont=font.Font(family='Comic Sans MS', size=15, weight='bold')

        self.txt=self.canvas.create_text(380,150,text="W Id:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.w_id_insert=Entry(self.canvas)
        self.canvas.create_window(550,150,width=200,height=30,window=self.w_id_insert)
        
        self.txt=self.canvas.create_text(325,250,text="Temperature:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.temperature_insert=Entry(self.canvas)
        self.canvas.create_window(550,250,width=200,height=30,window=self.temperature_insert)
        
        self.txt=self.canvas.create_text(360,350,text="Humidity:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.humidity_insert=Entry(self.canvas)
        self.canvas.create_window(550,350,width=200,height=30,window=self.humidity_insert)
        
        self.txt=self.canvas.create_text(310,450,text="Smoke Density:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.smoke_density_insert=Entry(self.canvas)
        self.canvas.create_window(550,450,width=200,height=30,window=self.smoke_density_insert)
        
        self.txt=self.canvas.create_text(320,550,text="Light Intensity:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.light_intensity_insert=Entry(self.canvas)
        self.canvas.create_window(550,550,width=200,height=30,window=self.light_intensity_insert)
        
        self.button=Button(self.root,text="Submit",anchor='center',width=10,height=1,font=mainBtnFont,command=self.submit_wildfire)
        self.button_window=self.canvas.create_window(800,580,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Back",anchor='center',width=10,height=1,font=mainBtnFont,command=self.back_button_wildfire)
        self.button_window=self.canvas.create_window(1000,580,anchor='nw',window=self.button)
        
    def submit_wildfire(self):
        
        # check if fields are blank

        if len(self.w_id_insert.get()) and len(self.temperature_insert.get()) and len(self.humidity_insert.get()) and len(self.smoke_density_insert.get()) and len(self.light_intensity_insert.get()) == 0:
            tk.messagebox.showerror('Please fill fields')
        
        # store float values

        w_id=float(self.w_id_insert.get())
        temperature=float(self.temperature_insert.get())
        humidity=float(self.humidity_insert.get())
        smoke_density=float(self.smoke_density_insert.get())
        light_intensity=float(self.light_intensity_insert.get())
        
        # insert to wildfire table in the DB
        
        self.ob.add_wildfire(w_id,temperature,humidity,smoke_density,light_intensity)
        tk.messagebox._show('Submitted')

        # insert to alert table if value is greater that 9

        cn='wildfire'
        pn1='temperature'
        pn2='humidity'
        pn3='smoke_density'
        pn4='light_intensity'

        if temperature>9:
            self.ob.add_alert(temperature,cn,pn1)
        if humidity>9:
            self.ob.add_alert(humidity,cn,pn2)
        if smoke_density>9:
            self.ob.add_alert(smoke_density,cn,pn3)
        if light_intensity>9:
            self.ob.add_alert(light_intensity,cn,pn4)

        # clear the fields, once submitted

        self.w_id_insert.delete(0, 'end')
        self.temperature_insert.delete(0, 'end')
        self.humidity_insert.delete(0, 'end')
        self.smoke_density_insert.delete(0, 'end')
        self.light_intensity_insert.delete(0, 'end')

    def back_button_wildfire(self):
        self.canvas.destroy()
        self.top_panel()
        self.wildfire()    

# display data from wildfire table

    def display_wildfire(self):
        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1", "2","3","4","5")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')
        tv.column("2", width=100, anchor='c')
        tv.column("3", width=100, anchor='c')
        tv.column("4", width=100, anchor='c')
        tv.column("5", width=100, anchor='c')
        
        tv.heading("1", text="w_id")
        tv.heading("2", text="temperature")
        tv.heading("3", text="humidity")
        tv.heading("4", text="smoke_density")
        tv.heading("5", text="light_intensity")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select * from wildfire")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0],row[1],row[2],row[3],row[4]))
            cpt += 1
        self.ob.close(cursor,conn)

# graph for wildfire data

    def graph_wildfire(self):
        self.canvas.destroy()
        self.page_2_param()

    # storms button functionality

    def storms(self):
        self.canvas.destroy()
        self.top_panel()

        mainBtnFont=font.Font(family='Comic Sans MS', size=15, weight='bold')
        paramBtnFont=font.Font(family='Comic Sans MS', size=10)

        self.txt=self.canvas.create_text(600,50,text="Storms",font=("Comic Sans MS",55),fill="OliveDrab1")

        self.button=Button(self.root,text="Insert Data",anchor='center',bg="dark orange",width=12,height=2,font=mainBtnFont,command=self.insert_storms)
        self.button_window=self.canvas.create_window(1180,150,anchor='nw',window=self.button)

        self.button=Button(self.root,text="View Data",anchor='center',bg="dark orange",width=12,height=2,font=mainBtnFont,command=self.display_storms)
        self.button_window=self.canvas.create_window(1180,250,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Graph",anchor='center',bg="dark orange",width=12,height=2,font=mainBtnFont,command=self.graph_storms)
        self.button_window=self.canvas.create_window(1180,350,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Back",anchor='center',bg="dark orange",width=12,height=2,font=mainBtnFont,command=self.back_button_param)
        self.button_window=self.canvas.create_window(1180,450,anchor='nw',window=self.button)

        self.txt=self.canvas.create_text(520,390,font=("Comic Sans MS",16),fill="wheat1",text="A storm is any disturbed state of an environment or in an astronomical body's \n atmosphere especially affecting its surface, and strongly implying severe \n weather. It may be marked by significant disruptions to normal conditions such \n as strong wind, tornadoes, hail, thunder and lightning (a thunderstorm), \n heavy precipitation (snowstorm, rainstorm), heavy freezing rain (ice storm), \n strong winds (tropical cyclone, windstorm), or wind transporting some \n substance through the atmosphere as in a dust storm, blizzard, sandstorm, etc. \n Storms have the potential to harm lives and property via storm surge, heavy \n rain or snow causing flooding or road impassibility, lightning, wildfires, \n and vertical wind shear. Systems with significant rainfall and duration help \n alleviate drought in places they move through. Heavy snowfall can allow special \n recreational activities to take place which would not be possible otherwise, \n such as skiing and snowmobiling")

    # insert data to storms table

    def insert_storms(self):
        self.canvas.destroy()
        self.top_panel()

        mainBtnFont=font.Font(family='Comic Sans MS', size=15, weight='bold')

        self.txt=self.canvas.create_text(380,150,text="S Id:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.s_id_insert=Entry(self.canvas)
        self.canvas.create_window(550,150,width=200,height=30,window=self.s_id_insert)
        
        self.txt=self.canvas.create_text(300,250,text="Equilibrium Level:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.equilibrium_level_insert=Entry(self.canvas)
        self.canvas.create_window(550,250,width=200,height=30,window=self.equilibrium_level_insert)
        
        self.txt=self.canvas.create_text(345,350,text="Lapse Rate:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.lapse_rate_insert=Entry(self.canvas)
        self.canvas.create_window(550,350,width=200,height=30,window=self.lapse_rate_insert)
        
        self.txt=self.canvas.create_text(270,450,text="Convective Inhibition:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.convective_inhibition_insert=Entry(self.canvas)
        self.canvas.create_window(550,450,width=200,height=30,window=self.convective_inhibition_insert)
        
        self.txt=self.canvas.create_text(250,550,text="Storm Relative Helicity:",font=("Comic Sans MS",25),fill="OliveDrab1")
        self.storm_relative_helicity_insert=Entry(self.canvas)
        self.canvas.create_window(550,550,width=200,height=30,window=self.storm_relative_helicity_insert)
        
        self.button=Button(self.root,text="Submit",anchor='center',width=10,height=1,font=mainBtnFont,command=self.submit_storms)
        self.button_window=self.canvas.create_window(800,580,anchor='nw',window=self.button)

        self.button=Button(self.root,text="Back",anchor='center',width=10,height=1,font=mainBtnFont,command=self.back_button_storms)
        self.button_window=self.canvas.create_window(1000,580,anchor='nw',window=self.button)
        
    def submit_storms(self):
        
        # check if fields are blank

        if len(self.s_id_insert.get()) and len(self.equilibrium_level_insert.get()) and len(self.lapse_rate_insert.get()) and len(self.convective_inhibition_insert.get()) and len(self.storm_relative_helicity_insert.get()) == 0:
            tk.messagebox.showerror('Please fill fields')

        # store float values

        s_id=float(self.s_id_insert.get())
        equilibrium_level=float(self.equilibrium_level_insert.get())
        lapse_rate=float(self.lapse_rate_insert.get())
        convective_inhibition=float(self.convective_inhibition_insert.get())
        storm_relative_helicity=float(self.storm_relative_helicity_insert.get())
        
        # insert to earthquake table in the DB
        
        self.ob.add_storms(s_id,equilibrium_level,lapse_rate,convective_inhibition,storm_relative_helicity)
        tk.messagebox._show('Submitted')

        # insert to alert table if value is greater that 9

        cn='storms'
        pn1='equilibrium_level'
        pn2='lapse_rate'
        pn3='convective_inhibition'
        pn4='storm_relative_helicity'

        if equilibrium_level>9:
            self.ob.add_alert(equilibrium_level,cn,pn1)
        if lapse_rate>9:
            self.ob.add_alert(lapse_rate,cn,pn2)
        if convective_inhibition>9:
            self.ob.add_alert(convective_inhibition,cn,pn3)
        if storm_relative_helicity>9:
            self.ob.add_alert(storm_relative_helicity,cn,pn4)

        # clear the fields, once submitted

        self.s_id_insert.delete(0, 'end')
        self.equilibrium_level_insert.delete(0, 'end')
        self.lapse_rate_insert.delete(0, 'end')
        self.convective_inhibition_insert.delete(0, 'end')
        self.storm_relative_helicity_insert.delete(0, 'end')

    def back_button_storms(self):
        self.canvas.destroy()
        self.top_panel()
        self.storms()    

# display data from storms table

    def display_storms(self):
        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1", "2","3","4","5")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')
        tv.column("2", width=100, anchor='c')
        tv.column("3", width=100, anchor='c')
        tv.column("4", width=100, anchor='c')
        tv.column("5", width=100, anchor='c')
        
        tv.heading("1", text="s_id")
        tv.heading("2", text="equilibrium_level")
        tv.heading("3", text="lapse_rate")
        tv.heading("4", text="convective_inhibition")
        tv.heading("5", text="storm_relative_helicity")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select * from storm")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0],row[1],row[2],row[3],row[4]))
            cpt += 1
        self.ob.close(cursor,conn)

# graph for storms data

    def graph_storms(self):
        self.canvas.destroy()
        self.page_2_param()

# display data from storms table

    def view_alert(self):
        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1", "2","3","4")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')
        tv.column("2", width=100, anchor='c')
        tv.column("3", width=100, anchor='c')
        tv.column("4", width=100, anchor='c')
        
        
        tv.heading("1", text="a_id")
        tv.heading("2", text="value")
        tv.heading("3", text="calamity_name")
        tv.heading("4", text="parameter_name")
        
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select * from alert")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0],row[1],row[2],row[3]))
            cpt += 1
        self.ob.close(cursor,conn)

    def view_deleted_alert(self):
        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1", "2","3","4")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')
        tv.column("2", width=100, anchor='c')
        tv.column("3", width=100, anchor='c')
        tv.column("4", width=100, anchor='c')
        
        
        tv.heading("1", text="a_id")
        tv.heading("2", text="value")
        tv.heading("3", text="calamity_name")
        tv.heading("4", text="parameter_name")
        
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select * from alert_dlt")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0],row[1],row[2],row[3]))
            cpt += 1
        self.ob.close(cursor,conn)


    # parameter functions : to be edited if needed

    # earthquake params

    def seismic_wave(self):
        
        self.canvas.destroy()
        self.page_2_param()

        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')        
        tv.heading("1", text="seismic_wave")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select seismic_wave from earthquake")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0]))
            cpt += 1
        self.ob.close(cursor,conn)

    def p_wave(self):
        
        self.canvas.destroy()
        self.page_2_param()

        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')        
        tv.heading("1", text="p_wave")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select p_wave from earthquake")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0]))
            cpt += 1
        self.ob.close(cursor,conn)

    def s_wave(self):

        self.canvas.destroy()
        self.page_2_param()

        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')        
        tv.heading("1", text="s_wave")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select s_wave from earthquake")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0]))
            cpt += 1
        self.ob.close(cursor,conn)

    def ground_motion(self):

        self.canvas.destroy()
        self.page_2_param()

        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')        
        tv.heading("1", text="ground_motion")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select ground_motion from earthquake")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0]))
            cpt += 1
        self.ob.close(cursor,conn)

    # flood params
    
    def water_surface_elevation(self):
        
        self.canvas.destroy()
        self.page_2_param()

        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')        
        tv.heading("1", text="water_surface_elevation")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select water_surface_elevation from flood")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0]))
            cpt += 1
        self.ob.close(cursor,conn)

    def water_level_measurement(self):

        self.canvas.destroy()
        self.page_2_param()

        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')        
        tv.heading("1", text="water_level_measurement")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select water_level_measurement from flood")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0]))
            cpt += 1
        self.ob.close(cursor,conn)

    def soil_moisture_content(self):

        self.canvas.destroy()
        self.page_2_param()

        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')        
        tv.heading("1", text="soil_moisture_content")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select soil_moisture_content from flood")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0]))
            cpt += 1
        self.ob.close(cursor,conn)

    def rainfall_measurement(self):

        self.canvas.destroy()
        self.page_2_param()

        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')        
        tv.heading("1", text="rainfall_measurement")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select rainfall_measurement from flood")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0]))
            cpt += 1
        self.ob.close(cursor,conn)

    # wildfire params

    def temperature(self):

        self.canvas.destroy()
        self.page_2_param()

        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')        
        tv.heading("1", text="temperature")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select temperature from wildfire")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0]))
            cpt += 1
        self.ob.close(cursor,conn)

    def humidity(self):

        self.canvas.destroy()
        self.page_2_param()

        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')        
        tv.heading("1", text="humidity")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select humidity from wildfire")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0]))
            cpt += 1
        self.ob.close(cursor,conn)

    def smoke_density(self):

        self.canvas.destroy()
        self.page_2_param()

        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')        
        tv.heading("1", text="smoke_density")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select smoke_density from wildfire")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0]))
            cpt += 1
        self.ob.close(cursor,conn)

    def light_intensity(self):

        self.canvas.destroy()
        self.page_2_param()

        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')        
        tv.heading("1", text="light_intensity")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select light_intensity from wildfire")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0]))
            cpt += 1
        self.ob.close(cursor,conn)

    # storms params

    def equilibrium_level(self):

        self.canvas.destroy()
        self.page_2_param()

        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')        
        tv.heading("1", text="equilibrium_level")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select equilibrium_level from storm")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0]))
            cpt += 1
        self.ob.close(cursor,conn)

    def lapse_rate(self):

        self.canvas.destroy()
        self.page_2_param()

        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')        
        tv.heading("1", text="lapse_rate")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select lapse_rate from storm")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0]))
            cpt += 1
        self.ob.close(cursor,conn)

    def convective_inhibition(self):

        self.canvas.destroy()
        self.page_2_param()

        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')        
        tv.heading("1", text="convective_inhibition")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select convective_inhibition from storm")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0]))
            cpt += 1
        self.ob.close(cursor,conn)

    def storm_relative_helicity(self):

        self.canvas.destroy()
        self.page_2_param()

        win = Tk()
        win.resizable(width=0,height=0)
        tv = ttk.Treeview(win, selectmode='browse')
        vsb = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
        vsb.place(x=1322, height=200+20)
        tv.configure(yscrollcommand=vsb.set)
        tv["columns"] = ("1")
        tv['show'] = 'headings'
        tv.column("1", width=100, anchor='c')        
        tv.heading("1", text="storm_relative_helicity")
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        cursor.execute("select storm_relative_helicity from storm")
        cpt=0;
        for row in cursor:
            tv.insert('','end',text=str(cpt),values=(row[0]))
            cpt += 1
        self.ob.close(cursor,conn)


    def alert(self):
        self.canvas.destroy()
        self.page_2_param()
            
    def logout(self):
        self.canvas.destroy()
        self.top_panel()
        self.page_2_param()
    def back(self):
        self.canvas.destroy()
        self.top_panel()
        # self.afterlogin()
    def exit(self):
        self.canvas.destroy()
        self.root.quit()
        self.root.destroy()
        exit()




    # view and delete from alert table
        
    def view_delete_alert(self):
        
        mainBtnFont=font.Font(family='Comic Sans MS', size=15, weight='bold')
        mainBtnFont_1=font.Font(family='Comic Sans MS', size=10, weight='bold')
        paramBtnFont=font.Font(family='Comic Sans MS', size=10)

        self.canvas.destroy()
        self.top_panel()
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)

        self.button=Button(self.root,text="View alerts",bg="salmon",anchor='center',width=12,height=2,font=mainBtnFont,command=self.view_alert)
        self.button_window=self.canvas.create_window(600,80,anchor='nw',window=self.button)

        self.txt7=self.canvas.create_text(630,250,text="To Delete Alerts",font=('Comic Sans MS',50),fill="white")

        self.txt7=self.canvas.create_text(630,320,text="Please select alert id",font=('Comic Sans MS',30),fill="white")

        self.txt3=self.canvas.create_text(580,400,text="a_id   :",font=('Comic Sans MS',25),fill="white") 
                
        cursor.execute("SELECT a_id FROM alert")
        result=cursor.fetchall()
        final4=[list(i) for i in result] #fr drop table
        number4=StringVar()

        self.numberchose1n=ttk.Combobox(self.canvas,width=20,textvariable=number4)#fr values in dropdown
        self.numberchose1n['values']=final4
        self.canvas.create_window(760,400,width=126,window=self.numberchose1n)

        self.button5=Button(self.root,text="Back",bg="salmon",anchor='center',width=12,height=2,font=mainBtnFont,command=self.page_2_param)
        self.button5_window=self.canvas.create_window(150,500,anchor='nw',window=self.button5)

        self.button4=Button(self.root,text="Delete",bg="salmon",anchor='center',width=12,height=2,font=mainBtnFont,command=self.delete_alert_1)
        self.button4_window=self.canvas.create_window(550,500,anchor='nw',window=self.button4)        

        self.button4=Button(self.root,text="View deleted \n alert values",bg="salmon",anchor='center',width=12,height=2,font=mainBtnFont,command=self.view_deleted_alert)
        self.button4_window=self.canvas.create_window(950,500,anchor='nw',window=self.button4)        

    def delete_alert_1(self):
        a_id=self.numberchose1n.get()
        conn,cursor=self.ob.connect()
        self.ob.usedb(cursor)
        #fst gets inserted to a table and then deletes it
        
        cursor.execute("insert into alert_dlt (a_id,value,calamity_name,parameter_name) select a_id,value,calamity_name,parameter_name from alert where a_id=%s",(a_id))
        cursor.execute("delete FROM alert where a_id=%s",(a_id))
        conn.commit()
        self.ob.close(cursor,conn)
        tk.messagebox._show('Deleted')
        self.numberchose1n.delete(0, 'end')
        

objec=calamity()
