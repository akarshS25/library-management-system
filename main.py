from tkinter import*
from tkinter import ttk
import mysql.connector

class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x785+0+0")


        lbltitle = Label(self.root,text="Library Management System",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)


        frame = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue") 
        frame.place(x=0,y=130,width=1530,height=400)
      
        #=============================DataFrameLeft========================
        DataFrameLeft=LabelFrame(frame,text="Library Memebership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",20,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,sticky=W)

        comMember= ttk.Combobox(DataFrameLeft, font=("times new roman",15,"bold"), width=27,state="readonly")
        comMember["values"] = ("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)  # Use row and column options directly on the widget

        lblPRn_No=Label(DataFrameLeft,font=("arial",12,"bold"),text="PRN No",padx=2,bg="powder blue")
        lblPRn_No.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID No",padx=2,pady=4,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtTitle.grid(row=2,column=1)

        lblName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Name",padx=2,pady=6,bg="powder blue")
        lblName.grid(row=3,column=0,sticky=W)
        txtName=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtName.grid(row=3,column=1)

        lblAddress=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address",padx=2,pady=6,bg="powder blue")
        lblAddress.grid(row=4,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtAddress.grid(row=4,column=1)

        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile No.",padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=5,column=1)

        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Id",padx=2,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtBookId.grid(row=0,column=3)

        lblBoookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title",padx=2,pady=6,bg="powder blue")
        lblBoookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,font=("arial",12,"bold"),text="Author",padx=2,pady=6,bg="powder blue")
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed",padx=2,pady=6,bg="powder blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Due Date",padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)

        lblDateReturn=Label(DataFrameLeft,font=("arial",12,"bold"),text="Return Date",padx=2,pady=6,bg="powder blue")
        lblDateReturn.grid(row=5,column=2,sticky=W)
        txtDateReturn=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtDateReturn.grid(row=5,column=3)


        #=================================Dtat frame right============================

        DataFrameRight=LabelFrame(frame,text="Books Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",20,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight, font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column =1,sticky="ns")

        Listbooks=["The Great Gatsby","To Kill a Mockingbird","1984","Pride and Prejudice","The Catcher in the Rye","The Lord of the Rings","The Hobbit","Harry Potter and the Sorcerer's Stone"]

        listbox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listbox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listbox.yview)
        for item in Listbooks:
            listbox.insert(END,item)
        
        

        #================================Button Frame=========================
        framebutton = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue") 
        framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(framebutton,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(framebutton,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(framebutton,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(framebutton,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(framebutton,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(framebutton,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

        btnAddData=Button(framebutton,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=6)







        #===========================================================================

        frameDetails = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue") 
        frameDetails.place(x=0,y=600,width=1530,height=195)

        Table_Frame=LabelFrame(frameDetails,bd=6,relief=RIDGE,bg="powder blue") 
        Table_Frame.place(x=0,y=2,width=1460,height=190)

        self.library_table=ttk.Treeview(Table_Frame,column=("member type","prno.","title","name","address","mobile","bookid","booktitle","author"))

        self.library_table.heading("member type",text="Member Type")
        self.library_table.heading("prno.",text="Pr no.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("name",text="Name")
        self.library_table.heading("address",text="Address")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="book id")
        self.library_table.heading("booktitle",text="book title")
        self.library_table.heading("author",text="author")
        
        

        self.library_table["show"]="heading"
        self.library_table.pack(fill=BOTH,expand=1)




if __name__=="__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
