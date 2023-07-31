from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class crime:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("CRIME MANAGEMENT SYSTEM")

        #variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_criminal_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrestdate=StringVar()
        self.var_dateofcrime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_crimetype=StringVar()
        self.var_policestation=StringVar()
        self.var_evidence=StringVar()
        self.var_fathername=StringVar()
        self.var_birthmark=StringVar()
        self.var_gender=StringVar()

        lbl_title=Label(self.root,text="CRIME MANAGEMENT SYSTEM",font=('times new roman',40,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1530,height=70)


        #logo 
        img_logo=Image.open("images\LOGO.jpg")
        img_logo=img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=100,y=5,width=60,height=60)

        # Image Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1530,height=130)

        img1=Image.open("images\image1.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)
        self.img_1=Label(self.root,image=self.photo1)
        self.img_1.place(x=0,y=70,width=500,height=130)

        img2=Image.open("images\image2.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)
        self.img_2=Label(self.root,image=self.photo2)
        self.img_2.place(x=500,y=70,width=530,height=130)

        img3=Image.open("images\image3.jpg")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)
        self.img_3=Label(self.root,image=self.photo3)
        self.img_3.place(x=1050,y=70,width=500,height=130)


        #MainFrame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=200,width=1500,height=560)

        #UpperFrame 
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text="CRIMINAL INFORMATION",font=('times new roman',15,'bold'),fg='blue')
        upper_frame.place(x=10,y=10,width=1480,height=260)
        
        #Labels

        #Case ID:
        caseid=Label(upper_frame,text="Criminal Registration ID:",font=('arial',11,'bold'))
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        #Criminal Number:
        lbl_criminal_no=Label(upper_frame,text="Criminal Number:",font=('arial',11,'bold'))
        lbl_criminal_no.grid(row=0,column=2,sticky=W,padx=2,pady=7)
        txt_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=('arial',11,'bold'))
        txt_criminal_no.grid(row=0,column=3,padx=2,pady=7,sticky=W)

        #Criminal Name:
        lbl_name=Label(upper_frame,text="Criminal Name:",font=('arial',11,'bold'))
        lbl_name.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        txt_name=ttk.Entry(upper_frame,textvariable=self.var_criminal_name,width=22,font=('arial',11,'bold'))
        txt_name.grid(row=1,column=1,padx=2,pady=7,sticky=W)

        #Criminal NickName:
        lbl_nickname=Label(upper_frame,text="Criminal's NickName:",font=('arial',11,'bold'))
        lbl_nickname.grid(row=1,column=2,sticky=W,padx=2,pady=7)
        txt_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=('arial',11,'bold'))
        txt_nickname.grid(row=1,column=3,padx=3,pady=7,sticky=W)

        #Arrest Date:
        lbl_arrestDate=Label(upper_frame,text="Criminal's ArrestDate:",font=('arial',11,'bold'))
        lbl_arrestDate.grid(row=2,column=0,sticky=W,padx=2,pady=7)
        txt_arrestDate=ttk.Entry(upper_frame,textvariable=self.var_arrestdate,width=22,font=('arial',11,'bold'))
        txt_arrestDate.grid(row=2,column=1,padx=3,pady=7,sticky=W)

        #Crime Commiting Date:
        lbl_crimeDate=Label(upper_frame,text="Crime Commiting Date:",font=('arial',11,'bold'))
        lbl_crimeDate.grid(row=2,column=2,sticky=W,padx=2,pady=7)
        txt_crimeDate=ttk.Entry(upper_frame,width=22,textvariable=self.var_dateofcrime,font=('arial',11,'bold'))
        txt_crimeDate.grid(row=2,column=3,padx=3,pady=7,sticky=W)

        #Address
        lbl_Address=Label(upper_frame,text="Address:",font=('arial',11,'bold'))
        lbl_Address.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        txt_Address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        txt_Address.grid(row=3,column=1,padx=3,pady=7,sticky=W)

        #Age
        lbl_Age=Label(upper_frame,text="Age:",font=('arial',11,'bold'))
        lbl_Age.grid(row=3,column=2,sticky=W,padx=2,pady=7)
        txt_Age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('arial',11,'bold'))
        txt_Age.grid(row=3,column=3,padx=3,pady=7,sticky=W) 

        #Crime Type
        lbl_crimetype=Label(upper_frame,text="Crime Type:",font=('arial',11,'bold'))
        lbl_crimetype.grid(row=4,column=0,sticky=W,padx=2,pady=7)
        txt_crimetype=ttk.Entry(upper_frame,textvariable=self.var_crimetype,width=22,font=('arial',11,'bold'))
        txt_crimetype.grid(row=4,column=1,padx=3,pady=7,sticky=W)

        #Police_Station Name
        lbl_Police_Station=Label(upper_frame,text="Police_Station Name:",font=('arial',11,'bold'))
        lbl_Police_Station.grid(row=4,column=2,sticky=W,padx=2,pady=7)
        txt_Police_Station=ttk.Entry(upper_frame,textvariable=self.var_policestation,width=22,font=('arial',11,'bold'))
        txt_Police_Station.grid(row=4,column=3,padx=3,pady=7,sticky=W)

        #BirthMark
        lbl_BirthMark=Label(upper_frame,text="BirthMark :",font=('arial',11,'bold'))
        lbl_BirthMark.grid(row=2,column=4,sticky=W,padx=2,pady=7)
        txt_BirthMark=ttk.Entry(upper_frame,textvariable=self.var_birthmark,width=22,font=('arial',11,'bold'))
        txt_BirthMark.grid(row=2,column=5,padx=3,pady=7,sticky=W)

        #Gender
        lbl_Gender=Label(upper_frame,text="Gender:",font=('arial',11,'bold'))
        lbl_Gender.grid(row=3,column=4,sticky=W,padx=2,pady=7)
        txt_Gender=ttk.Entry(upper_frame,textvariable=self.var_gender,width=22,font=('arial',11,'bold'))
        txt_Gender.grid(row=3,column=5,padx=3,pady=7,sticky=W)

        #Evidence
        lbl_Evidence=Label(upper_frame,text="Evidence:",font=('arial',11,'bold'))
        lbl_Evidence.grid(row=0,column=4,sticky=W,padx=2,pady=7)
        txt_Evidence=ttk.Entry(upper_frame,width=22,textvariable=self.var_evidence,font=('arial',11,'bold'))
        txt_Evidence.grid(row=0,column=5,padx=3,pady=7,sticky=W)

        #Father's name
        lbl_Fathers_name=Label(upper_frame,text="Father's name:",font=('arial',11,'bold'))
        lbl_Fathers_name.grid(row=1,column=4,sticky=W,padx=2,pady=7)
        txt_Fathers_name=ttk.Entry(upper_frame,textvariable=self.var_fathername,width=22,font=('arial',11,'bold'))
        txt_Fathers_name.grid(row=1,column=5,padx=3,pady=7,sticky=W)

        #Buttons
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=190,width=620,height=40)

        #Buttonadd
        btn_add=Button(button_frame,command=self.add_data,text='Save Details',font=('arial',13,'bold'),width=14,bg='aqua')
        btn_add.grid(row=0,column=0,padx=3,pady=3)

        #ButtonUpdate
        btn_update=Button(button_frame,command=self.update_data,text='Update Details',font=('arial',13,'bold'),width=14,bg='aqua')
        btn_update.grid(row=0,column=1,padx=3,pady=3)

        #Buttonadd
        btn_delete=Button(button_frame,command=self.delete_data,text='Delete Details',font=('arial',13,'bold'),width=14,bg='aqua')
        btn_delete.grid(row=0,column=2,padx=3,pady=3)

        #Buttonadd
        btn_clear=Button(button_frame,command=self.clear_data,text='Clear Details',font=('arial',13,'bold'),width=14,bg='aqua')
        btn_clear.grid(row=0,column=3,padx=3,pady=3)

        #picture
        img_crime=Image.open("images\image4.jpg")
        img_crime=img_crime.resize((470,230),Image.ANTIALIAS)
        self.photocrime=ImageTk.PhotoImage(img_crime)
        self.img_crime=Label(self.root,image=self.photocrime)
        self.img_crime.place(x=1070,y=230,width=430,height=230)



        #LowerFrame
        lower_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text="CRIMINAL INFORMATION DATASET",font=('times new roman',15,'bold'),fg='blue')
        lower_frame.place(x=10,y=280,width=1480,height=260)

        #SearchFrame 
        search_frame=LabelFrame(lower_frame,bd=2,relief=RIDGE,text="Search Criminal Records",font=('times new roman',12,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1480,height=60)

        search_by=Label(search_frame,font=('arial',11,'bold'),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)
        combo_search_box=ttk.Combobox(search_frame,font=('arial',11,"bold"),width=18)
        combo_search_box["value"]=('Select option','Case_Id','Criminal_no')
        combo_search_box.set(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)
        search_txt=ttk.Entry(search_frame,width=22,font=('arial',11,'bold'))
        search_txt.grid(row=0,column=2,padx=3,pady=5,sticky=W)

        btn_search=Button(search_frame,text='Search :',font=('arial',13,'bold'),width=14,bg='aqua')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        btn_all=Button(search_frame,text='Show All :',font=('arial',13,'bold'),width=14,bg='aqua')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,text="DELHI POLICE SERVICE (DPCR)",font=('arial',30,'bold'),fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=50,pady=0)

        table_frame=Frame(lower_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,columns=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)
        self.criminal_table.heading('1',text='Registration Id')
        self.criminal_table.heading('2',text='Criminal Number')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='Nickname')
        self.criminal_table.heading('5',text='Arrestdate')
        self.criminal_table.heading('6',text='Dateofcrime')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='CrimeType')
        self.criminal_table.heading('10',text='Police Station')
        self.criminal_table.heading('11',text='Evidence')
        self.criminal_table.heading('12',text='Father Name')
        self.criminal_table.heading('13',text='Birthmark')
        self.criminal_table.heading('14',text='Gender')
        self.criminal_table['show']='headings'
        self.criminal_table.pack(fill=BOTH,expand=1)
        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()  

    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                con=mysql.connector.connect(host='localhost',username='root',password='yash',database='management')
                my_cursor=con.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                            self.var_case_id.get(),
                                                                                                            self.var_criminal_no.get(),
                                                                                                            self.var_criminal_name.get(),
                                                                                                            self.var_nickname.get(),
                                                                                                            self.var_arrestdate.get(),
                                                                                                            self.var_dateofcrime.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_age.get(),
                                                                                                            self.var_crimetype.get(),
                                                                                                            self.var_policestation.get(),
                                                                                                            self.var_evidence.get(),
                                                                                                            self.var_fathername.get(),
                                                                                                            self.var_birthmark.get(),
                                                                                                            self.var_gender.get()

                ))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo('Success','Data is added')
            except Exception as es:
                messagebox.showerror('Error',f'Due to {str(es)}')

        #fetch data
    def fetch_data(self):
        con=mysql.connector.connect(host='localhost',username='root',password='yash',database='management')
        my_cursor=con.cursor()
        my_cursor.execute('select * from criminal')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            con.commit()
        con.close()

    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']
        self.var_case_id.set(data[0]),
        self.var_criminal_no.set(data[1]),
        self.var_criminal_name.set(data[2]),
        self.var_nickname.set(data[3]),
        self.var_arrestdate.set(data[4]),
        self.var_dateofcrime.set(data[5]),
        self.var_address.set(data[6]),
        self.var_age.set(data[7]),
        self.var_crimetype.set(data[8]),
        self.var_policestation.set(data[9]),
        self.var_evidence.set(data[10]),
        self.var_fathername.set(data[11]),
        self.var_birthmark.set(data[12]),
        self.var_gender.set(data[13])
    
    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                update=messagebox.askyesno("Update Details","Do you want to update the records")
                if update>0:
                    con=mysql.connector.connect(host='localhost',username='root',password='yash',database='management')
                    my_cursor=con.cursor()
                    my_cursor.execute("update criminal set criminal_no=%s,criminal_name=%s,Nickname=%s,Arrestdate=%s,Dateofcrime=%s,Address=%s,Age=%s,CrimeType=%s,Police_Station=%s,Evidence=%s,Father_Name=%s,Birthmark=%s,Gender=%s where Registration_id=%s",(                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                self.var_criminal_no.get(),
                                                                                                                                                                                                                                                                self.var_criminal_name.get(),
                                                                                                                                                                                                                                                                self.var_nickname.get(),
                                                                                                                                                                                                                                                                self.var_arrestdate.get(),
                                                                                                                                                                                                                                                                self.var_dateofcrime.get(),
                                                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                                                self.var_age.get(),
                                                                                                                                                                                                                                                                self.var_crimetype.get(),
                                                                                                                                                                                                                                                                self.var_policestation.get(),
                                                                                                                                                                                                                                                                self.var_evidence.get(),
                                                                                                                                                                                                                                                                self.var_fathername.get(),
                                                                                                                                                                                                                                                                self.var_birthmark.get(),
                                                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                                                self.var_case_id.get()
                    
                                                                                                                                                                                                                                                            ))
                else:
                    if not update:
                        return
                con.commit()
                self.fetch_data()
                self.clear_data()
                con.close()
                messagebox.showinfo('Success','Data is added')
            except Exception as es:
                messagebox.showerror('Error',f'Due to {str(es)}')

    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want delete the records")
                if delete>0:
                    con=mysql.connector.connect(host='localhost',username='root',password='yash',database='management')
                    my_cursor=con.cursor()
                    sql='delete from criminal where registration_id=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                con.commit()
                self.fetch_data()
                self.clear_data()
                con.close()
                messagebox.showinfo('Success','Data is Deleted')
            except Exception as es:
                messagebox.showerror('Error',f'Due to {str(es)}')
    
    def clear_data(self):
        self.var_case_id.set(""),
        self.var_criminal_no.set(""),
        self.var_criminal_name.set(""),
        self.var_nickname.set(""),
        self.var_arrestdate.set(""),
        self.var_dateofcrime.set(""),
        self.var_address.set(""),
        self.var_age.set(""),
        self.var_crimetype.set(""),
        self.var_policestation.set(""),
        self.var_evidence.set(""),
        self.var_fathername.set(""),
        self.var_birthmark.set(""),
        self.var_gender.set("")

    
        
        





        





if __name__=="__main__":
    root=Tk()
    obj=crime(root)
    root.mainloop()