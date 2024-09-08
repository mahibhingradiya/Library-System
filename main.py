from tkinter import*
from tkinter import ttk 
from tkinter import messagebox 
import MySQLdb as db2
from PIL import Image,ImageTk


class Library:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title('Library Management System')

    #Variables
        self.id=StringVar()
        self.title=StringVar()
        self.author=StringVar()
        self.publisher=StringVar()
        self.edition=StringVar()
        self.price=StringVar()
        



    # Title
        lbltitle=Label(self.root,text="Library Managment System",bd=15,relief=RIDGE,bg="white",fg="darkgreen",
                       font=("times new roman",50,"bold") ,padx=2,pady=4)    
        lbltitle.pack(side=TOP,fill=X)
                                                                               
    # mAIN FRAME
        
        Main_frame=Frame(self.root,bd=15,relief=RIDGE,padx=20) #
        Main_frame.place(x=0,y=120,width=1530,height=675)

#-upper left frame-------------------------------------------------------------------------------------------------------------
        
        Upper_left_frame=LabelFrame(Main_frame, bd=10,padx=20,text="Books Information",fg="darkgreen",font=("arial",12,"bold")) 
        Upper_left_frame.place(x=0,y=5,width=900,height=350)

        lb1_space=Label(Upper_left_frame,font=('arial',12,'bold'),text='life is not without book ',fg="black") 
        lb1_space.grid(row=1,column=0,padx=2,pady=10) 

        # Book ID
             
        lb1_id=Label(Upper_left_frame,font=('arial',12,'bold'),text='Book ID: ',fg="black") 
        lb1_id.grid(row=2,column=0,padx=2,pady=10) 
        
        txt_id=ttk.Entry(Upper_left_frame,textvariable=self.id,width=22,font=('arial',11,'bold'))
        txt_id.grid(row=2,column=1,padx=2,pady=7)

        # Book Title
             
        lb1_title=Label(Upper_left_frame,font=('arial',12,'bold'),text='Title: ',fg="black") 
        lb1_title.grid(row=3,column=0,padx=2,pady=10) 
        
        txt_name=ttk.Entry(Upper_left_frame,textvariable=self.title,width=22,font=('arial',11,'bold'))
        txt_name.grid(row=3,column=1,padx=2,pady=7)

        # Author name
             
        lb1_author=Label(Upper_left_frame,font=('arial',12,'bold'),text='Author : ',fg="black") 
        lb1_author.grid(row=4,column=0,padx=2,pady=10)
        
        txt_author=ttk.Entry(Upper_left_frame,textvariable=self.author,width=22,font=('arial',11,'bold'))
        txt_author.grid(row=4,column=1,padx=2,pady=7)

        # Publisher
             
        lb1_publisher=Label(Upper_left_frame,font=('arial',12,'bold'),text='Publisher: ',fg="black") 
        lb1_publisher.grid(row=5,column=0,padx=2,pady=10) 
        
        txt_publisher=ttk.Entry(Upper_left_frame,textvariable=self.publisher,width=22,font=('arial',11,'bold'))
        txt_publisher.grid(row=5,column=1,padx=2,pady=7)

        # Edition
             
        lb1_edition=Label(Upper_left_frame,font=('arial',12,'bold'),text='Edition: ',fg="black") 
        lb1_edition.grid(row=6,column=0,padx=2,pady=10) 
        
        txt_edition=ttk.Entry(Upper_left_frame,textvariable=self.edition,width=22,font=('arial',11,'bold'))
        txt_edition.grid(row=6,column=1,padx=2,pady=7)

        # Price
             
        lb1_price=Label(Upper_left_frame,font=('arial',12,'bold'),text='Price: ',fg="black") 
        lb1_price.grid(row=7,column=0,padx=2,pady=10) 
        
        txt_price=ttk.Entry(Upper_left_frame,textvariable=self.price,width=22,font=('arial',11,'bold'))
        txt_price.grid(row=7,column=1,padx=2,pady=7)


        #BUTTON FRAME
        
        button_frame=Frame(Upper_left_frame, bd=4, relief=RIDGE, bg='darkgreen') 
        button_frame.place(x=550,y=40,width=165, height=220)
        
        btn_add=Button(button_frame,text=" ADD ",font=('arial',15,'bold'),command=self.add_data,width=12,bg="lime",fg="white")  #
        btn_add.grid(row=0,column=0,padx=1,pady=5)
        
        btn_update=Button(button_frame,text="UPDATE",font=('arial',15,'bold'),command=self.update_data,width=12,bg="purple",fg="white") #
        btn_update.grid(row=1,column=0,padx=1,pady=5)
        
        btn_delete=Button(button_frame,text="DELETE",font=('arial',15,'bold'),command=self.delete_data,width=12,bg="red",fg="white") #
        btn_delete.grid(row=2,column=0,padx=1,pady=5)
        
        btn_clear=Button(button_frame,text="CLEAR",font=('arial',15,'bold'),command=self.reset_data,width=12,bg="orange",fg="white") #
        btn_clear.grid(row=3,column=0,padx=1,pady=5)
        

#-upper right frame------------------------------------------------------------------------------------------------------------
        
        Upper_right_frame=Label(Main_frame, bd=10,relief=RIDGE,padx=20,fg="darkgreen",font=("arial",12,"bold")) 
        Upper_right_frame.place(x=915,y=5,width=550,height=350)  

        #image
        
        
        img1=Image.open('abdul kalam.png')
        self.photo1=ImageTk.PhotoImage(img1)
           
        self.img_1=Label(Upper_right_frame,image=self.photo1)
        self.img_1.place(x=160,y=0)   

        lblhome=Label(Upper_right_frame,font=("arial",12,"bold"),text="- Dr A.P.J.Abdul Kalam",
                      fg="black")
        lblhome.place(x=145,y=175)


        quote =""" \"One best book is equal to hundred good friends,
        one good friend is equal to a library.\""""
        lblhome=Label(Upper_right_frame,font=("arial",15,"bold"),text=quote,fg="black")
        lblhome.place(x=20,y=230)

    



#-Down frame-------------------------------------------------------------------------------------------------------------------
        
        down_frame=Label(Main_frame, bd=10, relief=RIDGE,font=('ariel',12,'bold'),fg='darkgreen') 
        down_frame.place(x=0,y=360,width=1465, height=275)
        
        img2=Image.open('simple.png')
        self.photo2=ImageTk.PhotoImage(img2)
           
        self.img_2=Label(down_frame,image=self.photo2)
        self.img_2.place(x=0,y=5)
    

#  ***************FUNCTIONS***********************
        
    # ADD data----------------------------------------------------------------
        
    def add_data(self):
        if self.id.get()=="" or self.price.get()=="" or self.title.get()=="":
                messagebox.showerror('Error','All Fields are required')
        else:
            try:
                db1 = db2.connect(host="Localhost",user="root",password="",db="LMS")
                cursor=db1.cursor() #cursor object to interact with the database.
                cursor.execute('insert into Library values(%s,%s,%s,%s,%s,%s)',(
                        
                                                                                                               self.id.get(),
                                                                                                               self.title.get(),
                                                                                                               self.author.get(),
                                                                                                               self.publisher.get(),
                                                                                                               self.edition.get(),
                                                                                                               self.price.get()
                                                                                                            
                        
                                                                                                            ))
                db1.commit()
                db1.close()
                messagebox.showinfo('Success','Book has been added!',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)


        
    #-update------------------------------------------------- 
           
    def update_data(self):
        if self.id.get()=="" or self.price.get()=="":
                messagebox.showerror('Error','All Fields are required')
        else:
           try:
                update=messagebox.askyesno('update','Are you sure update this BOOK data')
                if update>0:
                    db1 = db2.connect(host="Localhost",user="root",password="",db="LMS")
                    cursor=db1.cursor()

                    # Check if the provided id exists in the database
                    cursor.execute('SELECT * FROM Library WHERE id = %s', (self.id.get()))
                    book = cursor.fetchone()  # Fetch one row

                    if book is None:
                        messagebox.showerror('Error', 'Book ID does not exist')
                        db1.close()
                        return

                    cursor.execute('update Library set title=%s,author=%s,publisher=%s,edition=%s,price=%s where id=%s',(
                        
                                                                                                                    self.title.get(),
                                                                                                                    self.author.get(),
                                                                                                                    self.publisher.get(),
                                                                                                                    self.edition.get(),
                                                                                                                    self.price.get(),
                                                                                                                    self.id.get(),

                                                                                                         
                                                                                                                   ))
                else:
                    if not update:
                        return
                db1.commit()
                db1.close()
                messagebox.showinfo('success','Library Successfully updated',parent=self.root)
                      
           except Exception as es:
               messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)




    #-Delete---------------------------------------------------------  
     
     
    def delete_data(self):
        if self.id.get()=="":
            messagebox.showerror('Error',"All Fields are required")
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure delete this BOOK',parent=self.root)
                if Delete>0:
                    db1 = db2.connect(host="Localhost",user="root",password="",db="LMS")
                    cursor=db1.cursor()

                    # id exist 
                    cursor.execute('SELECT * FROM Library WHERE id = %s', (self.id.get(),))
                    book = cursor.fetchone() 

                    if book is None:
                        messagebox.showerror('Error', 'Book ID does not exist')
                        db1.close()
                        return

                    sql='delete from Library where id=%s'
                    value=(self.id.get())
                    cursor.execute(sql,value)
                    
                else:
                    if not Delete:
                        return
                db1.commit()
                db1.close()
                messagebox.showinfo('Delete','BOOK Successfully Deleted',parent=self.root)
                      
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root) 



    #-reset-----------------------------------------------------
    
    def reset_data(self):
        self.id.set("")
        self.title.set("")       
        self.author.set("")
        self.publisher.set("")
        self.edition.set("")
        self.price.set("")


























            

# object        

if __name__=="__main__":
    root=Tk()
    obj=Library(root)
    root.mainloop()