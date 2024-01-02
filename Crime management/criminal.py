
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Criminal:
    def __init__(  self,root):
        self.root=root
        self.root.geometry('1366x720+0+0')
        self.root.title('Criminal Management System')
        
        
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthmark= StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()



        labl_title=Label(  self.root,text='Criminal Management System Software',font=('times new roman',36,'bold'),bg='black',fg='gold')
        labl_title.place(x=0,y=0,width=1366,height=60)
        
        
        #logo
        img_logo=Image.open('images/logo.png')
        img_logo=img_logo.resize((60,50),Image.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        
        self.logo=Label(   self.root,image=   self.photo_logo)
        self.logo.place(x=70,y=5,width=60,height=50)
        
        
        #image frame
        
        img_frame=Frame(   self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=60,width=1366,height=130)
        
        img1=Image.open('images/img1.jpg')
        img1=img1.resize(( 455,170),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)
        
        self.img_1=Label(img_frame,image=  self.photo1)
        self.img_1.place(x=0,y=0,width=455,height=170)
        
        img2=Image.open('images/img2.jpg')
        img2=img2.resize(( 455,170),Image.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)
        
        self.img_2=Label(img_frame,image=  self.photo2)
        self.img_2.place(x=455,y=0,width=455,height=170)
        
        img3=Image.open('images/img3.jpeg')
        img3=img3.resize(( 455,170),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)
        
        self.img_3=Label(img_frame,image=  self.photo3)
        self.img_3.place(x=910,y=0,width=455,height=170)

        
        main_frame=Frame(  self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=200,width=1300,height=500)
        
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Criminal Information',font=('times new roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1280,height=250)
        
        #lables
        
        caseid=Label(upper_frame,text='Case ID:', font=('arial', 11, 'bold'), bg='white') 
        caseid.grid(row=0,column=0,padx=2, sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=  self.var_case_id, width=22, font=('arial', 11, 'bold'))
        caseentry.grid(row=0,column=1,padx=2, sticky=W)
        
        
        lbl_criminal=Label(upper_frame,text='Criminal No.:', font=('arial', 11, 'bold'), bg='white') 
        lbl_criminal.grid(row=0,column=2,padx=2, sticky=W,pady=7)

        txt_c_no=ttk.Entry(upper_frame,textvariable=   self.var_criminal_no, width=22, font=('arial', 11, 'bold'))
        txt_c_no.grid(row=0,column=3,padx=2, pady=7 ,sticky=W)
        
        
        lbl_name=Label(upper_frame,text='Criminal Name:', font=('arial', 11, 'bold'), bg='white') 
        lbl_name.grid(row=1,column=0,padx=2, sticky=W,pady=7)

        txt_name=ttk.Entry(upper_frame, textvariable=  self.var_name,width=22, font=('arial', 11, 'bold'))
        txt_name.grid(row=1,column=1,padx=2, sticky=W,pady=7)
        
        
        
        lbl_Nick=Label(upper_frame,text='Nickname:', font=('arial', 11, 'bold'), bg='white') 
        lbl_Nick.grid(row=1,column=2,padx=2, sticky=W,pady=7)

        txt_nick=ttk.Entry(upper_frame,textvariable=   self.var_nickname, width=22, font=('arial', 11, 'bold'))
        txt_nick.grid(row=1,column=3,padx=2,pady=7, sticky=W)

        
        
        lbl_arrest=Label(upper_frame,text='Arrest Date:', font=('arial', 11, 'bold'), bg='white') 
        lbl_arrest.grid(row=2,column=0,padx=2, sticky=W,pady=7)

        txt_arrest=ttk.Entry(upper_frame,textvariable= self.var_arrest_date, width=22, font=('arial', 11, 'bold'))
        txt_arrest.grid(row=2,column=1,padx=2, sticky=W,pady=7)
        
        
        lbl_doc=Label(upper_frame,text='Date of Crime:', font=('arial', 11, 'bold'), bg='white') 
        lbl_doc.grid(row=2,column=2,padx=2, sticky=W,pady=7)

        txt_doc=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime, width=22, font=('arial', 11, 'bold'))
        txt_doc.grid(row=2,column=3,padx=2, sticky=W,pady=7)
        
        
        lbl_address=Label(upper_frame,text='Address:', font=('arial', 11, 'bold'), bg='white') 
        lbl_address.grid(row=3,column=0,padx=2, sticky=W,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address, width=22, font=('arial', 11, 'bold'))
        txt_address.grid(row=3,column=1,padx=2, sticky=W,pady=7)
    
        
        
        lbl_age=Label(upper_frame,text='Age:', font=('arial', 11, 'bold'), bg='white') 
        lbl_age.grid(row=3,column=2,padx=2, sticky=W,pady=7)

        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age, width=22, font=('arial', 11, 'bold'))
        txt_age.grid(row=3,column=3,padx=2, sticky=W,pady=7)
        
        
        lbl_occ=Label(upper_frame,text='Occupation:', font=('arial', 11, 'bold'), bg='white') 
        lbl_occ.grid(row=4,column=0,padx=2, sticky=W,pady=7)

        txt_occ=ttk.Entry(upper_frame,textvariable=self.var_occupation, width=22, font=('arial', 11, 'bold'))
        txt_occ.grid(row=4,column=1,padx=2, sticky=W,pady=7)
        
        
        lbl_bm=Label(upper_frame,text='Birth Mark:', font=('arial', 11, 'bold'), bg='white') 
        lbl_bm.grid(row=4,column=2,padx=2, sticky=W,pady=7)

        txt_bm=ttk.Entry(upper_frame,textvariable= self.var_birthmark, width=22, font=('arial', 11, 'bold'))
        txt_bm.grid(row=4,column=3,padx=2, sticky=W,pady=7)
        
        
        lbl_ct=Label(upper_frame,text='Crime Type:', font=('arial', 11, 'bold'), bg='white') 
        lbl_ct.grid(row=0,column=4,padx=2, sticky=W,pady=7)

        txt_ct=ttk.Entry(upper_frame,textvariable= self.var_crime_type, width=22, font=('arial', 11, 'bold'))
        txt_ct.grid(row=0,column=5,padx=2, sticky=W,pady=7)
        
        lbl_fn=Label(upper_frame,text='Father Name:', font=('arial', 11, 'bold'), bg='white') 
        lbl_fn.grid(row=1,column=4,padx=2, sticky=W,pady=7)

        txt_fn=ttk.Entry(upper_frame,textvariable= self.var_father_name, width=22, font=('arial', 11, 'bold'))
        txt_fn.grid(row=1,column=5,padx=2, sticky=W,pady=7)
        
        
        lbl_gender=Label(upper_frame,text='Gender:', font=('arial', 11, 'bold'), bg='white') 
        lbl_gender.grid(row=2,column=4,padx=2, sticky=W,pady=7)

        #txt_address=ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'))
        #txt_address.grid(row=3,column=1,padx=2, sticky=W,pady=7)
        
        
        
        lbl_mw=Label(upper_frame,text='Most Wanted:', font=('arial', 11, 'bold'), bg='white') 
        lbl_mw.grid(row=3,column=4,padx=2, sticky=W,pady=7)

       # txt_address=ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'))
        #txt_address.grid(row=3,column=1,padx=2, sticky=W,pady=7)
        
        
        #radio button
        
        radio_frame_g=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_g.place(x=710,y=81,width=170,height=30)
        
        male=Radiobutton(radio_frame_g,text='Male',variable=   self.var_gender,value='male',font=('arial', 9, 'bold'),bg='white')
        male.grid(row=0,column=0,pady=0,padx=5,sticky=W)
        self.var_gender.set('male')
        female=Radiobutton(radio_frame_g,text='Female',variable=   self.var_gender,value='Female',font=('arial', 9, 'bold'),bg='white')
        female.grid(row=0,column=1,pady=0,padx=5,sticky=W)
        
        
        
        radio_frame_w=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_w.place(x=710,y=121,width=170,height=30)
        
        yes=Radiobutton(radio_frame_w,text='Yes',variable= self.var_wanted,value='yes',font=('arial', 9, 'bold'),bg='white')
        yes.grid(row=0,column=0,pady=0,padx=5,sticky=W)
        self.var_wanted.set('yes')
        no=Radiobutton(radio_frame_w,text='No',variable=   self.var_wanted,value='no',font=('arial', 9, 'bold'),bg='white')
        no.grid(row=0,column=1,pady=0,padx=5,sticky=W)
        
        
        
        
        #button
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=190,width=573,height=38)
        
        
        btn_add=Button(button_frame,command=self.add_data,text='Record Save',font=('arial', 11, 'bold'),width=14,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=1)
        
        
        btn_up=Button(button_frame,command=self.update_data,text='Update',font=('arial', 11, 'bold'),width=14,bg='blue',fg='white')
        btn_up.grid(row=0,column=1,padx=3,pady=1)
        
        btn_del=Button(button_frame,command=self.delete_data,text='Delete',font=('arial', 11, 'bold'),width=14,bg='blue',fg='white')
        btn_del.grid(row=0,column=2,padx=3,pady=1)
        
        btn_clr=Button(button_frame,command=self.clear_data,text='Clear',font=('arial', 11, 'bold'),width=14,bg='blue',fg='white')
        btn_clr.grid(row=0,column=3,padx=3,pady=1)
        
        
        #bg side image
        
        
        img4=Image.open('images/img3.jpeg')
        img4=img4.resize(( 370,230),Image.LANCZOS)
        self.photo4=ImageTk.PhotoImage(img4)
        
        self.img_4=Label(upper_frame,image=self.photo3)
        self.img_4.place(x=900,y=0,width=370,height=230)
        
        
        #lower frame
        
        lower_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Criminal Information Table',font=('times new roman',11,'bold'),fg='red')
        lower_frame.place(x=10,y=260,width=1280,height=220)
        
        
        
        search_frame=LabelFrame(lower_frame,bd=2,relief=RIDGE,text='Search Criminal Record',font=('times new roman',11,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1000,height=50)
        
        lbl_sb=Label(search_frame,text='Search Bar:', font=('arial', 8, 'bold'), bg='Red',fg='white') 
        lbl_sb.grid(row=0,column=0,padx=2, sticky=W)
        
        self.var_com_search=StringVar()
        combo_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial', 8, 'bold'),width=18)
        combo_box['value']=('Select Option','Case_id','Criminal_no')
        combo_box.current(0)
        combo_box.grid(row=0,column=1,padx=2, sticky=W)
        
        self.var_search=StringVar()
        txt_se=ttk.Entry(search_frame,textvariable=self.var_search, width=18, font=('arial', 8, 'bold'))
        txt_se.grid(row=0,column=2,padx=2, sticky=W)
        
        btn_search=Button(search_frame,command=self.serch_data,text='Search',font=('arial', 8, 'bold'),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3)
        
        btn_all=Button(search_frame,command=self.fetch_data,text='Show All',font=('arial', 8, 'bold'),width=14,bg='blue',fg='white')
        btn_all.grid(row=0,column=4)
        
        lbl_ca=Label(search_frame,text='NATIONAL CRIME AGENCY', font=('arial', 14, 'bold'), bg='white',fg='crimson') 
        lbl_ca.grid(row=0,column=5,padx=50, sticky=W,)

        table_frame=Frame(lower_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1275,height=130)
        
        
        #Scroll bar
        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.criminal_table=ttk.Treeview(table_frame,column=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        
        Scroll_x.config(command=   self.criminal_table.xview)
        Scroll_y.config(command=   self.criminal_table.yview)
        
        
        self.criminal_table.heading('1',text='CaseID')
        self.criminal_table.heading("2", text="CrimeNo")
        self.criminal_table.heading("3",text="Criminal Name")
        self.criminal_table.heading("4", text="NickName") 
        self.criminal_table.heading("5", text="ArrestDate")
        self.criminal_table.heading("6", text="CrimeOfDate")
        self.criminal_table.heading("7", text="Address")
        self.criminal_table.heading("8", text="Age")
        self.criminal_table.heading("9", text="Occupation")
        self.criminal_table.heading("10", text="Birth Mark")
        self.criminal_table.heading("11", text="Crime Type")
        self.criminal_table.heading("12", text="Father Name")
        self.criminal_table.heading("13", text="Gender")
        self.criminal_table.heading("14", text="Wanted")
        
        self.criminal_table['show']='headings'
        self.criminal_table.column('1',width=100)
        self.criminal_table.column('2',width=100)
        self.criminal_table.column('3',width=100)
        self.criminal_table.column('4',width=100)
        self.criminal_table.column('5',width=100)
        self.criminal_table.column('6',width=100)
        self.criminal_table.column('7',width=100)
        self.criminal_table.column('8',width=100)
        self.criminal_table.column('9',width=100)
        self.criminal_table.column('10',width=100)
        self.criminal_table.column('11',width=100)
        self.criminal_table.column('12',width=100)
        self.criminal_table.column('13',width=100)
        self.criminal_table.column('14',width=100)
        
        self.criminal_table.pack(fill=BOTH,expand=1)
        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
    
        self.fetch_data()
        
        
        #Add fucntion
        
    def add_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='123456', database='cm')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                    self.var_case_id.get(),
                    self.var_criminal_no.get(),
                    self.var_name.get(),
                    self.var_nickname.get(),
                    self.var_arrest_date.get(),
                    self.var_date_of_crime.get(),
                    self.var_address.get(),
                    self.var_age.get(),
                    self.var_occupation.get(),
                    self.var_birthmark.get(),
                    self.var_crime_type.get(),
                    self.var_father_name.get(),
                    self.var_gender.get(),
                    self.var_wanted.get()
            ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success', 'Criminal record has been added')
            except Exception as es:
                messagebox.showerror('Error', f'Due To {str(es)}')

    #FETCH DATA
    
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='123456', database='cm')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from criminal')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('', END, values=i)
            conn.commit()
        conn.close()        
                
    def get_cursor(self,event=""):
        cursur_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursur_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthmark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])           
    #update
    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are equired')
            
        else:
            try:
                update=messagebox.askyesno('update','Are you sure update this criminal')
                if update>0:
                    conn=mysql.connector.connect(host='localhost', username='root', password='123456', database='cm')
                    my_cursor = conn.cursor()   
                    my_cursor.execute('update criminal set Criminal_no=%s, Criminal_name=%s , Nick_name=%s , Arrest_date=%s , DateofCrime=%s , address=%s , age=%s , occupation=%s, birthmark=%s , crimetype=%s , fathername=%s , gender=%s , wanted=%s where Case_id=%s',(
                    self.var_criminal_no.get(),
                    self.var_name.get(),
                    self.var_nickname.get(),
                    self.var_arrest_date.get(),
                    self.var_date_of_crime.get(),
                    self.var_address.get(),
                    self.var_age.get(),
                    self.var_occupation.get(),
                    self.var_birthmark.get(),
                    self.var_crime_type.get(),
                    self.var_father_name.get(),
                    self.var_gender.get(),
                    self.var_wanted.get(),
                    self.var_case_id.get()
                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success', 'Criminal record has been added')
            except Exception as es:
                messagebox.showerror('Error', f'Due To {str(es)}')        
                
                
    # delete
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete', 'Are you sure Delete this criminal')
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost', username='root', password='123456', database='cm')
                    my_cursor = conn.cursor()
                    sql='delete from criminal where Case_id=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success', 'Criminal record has been Deleted')
            except Exception as es:
                messagebox.showerror('Error', f'Due To {str(es)}')
    
    
    #Clear
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthmark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")
        
        
    #searcg
    
    def serch_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:

                conn=mysql.connector.connect(host='localhost', username='root', password='123456', database='cm')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from criminal where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('', END, values=i)
                conn.commit()
                conn.close()  
            except Exception as es:
                messagebox.showerror('Error', f'Due To {str(es)}')    
        

if __name__ =="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()

