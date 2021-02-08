from tkinter import*
import sqlite3
from tkinter import messagebox as ms


def detailsform():
    stock_name= stockname.get()
    buy_price=buyprice.get()
    sell_price=sellprice.get()
    quan=quantity.get()



    sqliteConnection = sqlite3.connect('stockdetails.db')
    cursor = sqliteConnection.cursor()
    insert_details_sql = "INSERT INTO  stock (name,buyprice,sellprice,Quantity)values(?,?,?,?);"
    cursor.execute(insert_details_sql,( stock_name,  buy_price,  sell_price, quan))
    sqliteConnection.commit()
    ms.showinfo('yupp','data inserted suceesfully')
    sqliteConnection.close()
    x=int(buy_price)
    y=int(sell_price)
    z=int(quan)
    a=(x*z)
    b=(y*z)
    if(x >= y):
        c=a-b
        ms.showinfo("loss:",c)
       
    else:
        d=b-a
        ms.showinfo("profit:",d)
        
   



#CREATE TABLE stock (name TEXT, buyprice INT,sellprice INT,Quantity INT)
root = Tk()
root.geometry('500x500')
root.title("stock details")

stockname=StringVar()
buyprice= IntVar()
sellprice= IntVar()
quantity= IntVar()

label_0 = Label(root, text="stock detail form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="StockName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

stockname = Entry(root)
stockname.place(x=240,y=130)

label_2 = Label(root, text="buy price",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

buyprice = Entry(root)
buyprice.place(x=240,y=180)

label_4 = Label(root, text="Selling price",width=20,font=("bold", 10))
label_4.place(x=70,y=220)


sellprice = Entry(root)
sellprice.place(x=240,y=220)

label_4 = Label(root, text="Quantity",width=20,font=("bold", 10))
label_4.place(x=70,y=280)


quantity = Entry(root)
quantity.place(x=240,y=280)

Button(root, text='Submit',width=20,bg='brown',fg='white',command = detailsform).place(x=180,y=380)


