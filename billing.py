from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib

#create bills folder
if not os.path.exists('bills'):
    os.mkdir('bills')

#clear bill
    
def clear():
    bath_soap_entry.delete(0,END)
    face_cream_entry.delete(0,END)
    face_wash_entry.delete(0,END)
    body_lotion_entry.delete(0,END)
    hair_gel_entry.delete(0,END)
    hair_spray_entry.delete(0,END)
    wheat_entry.delete(0,END)
    sugar_entry.delete(0,END)
    salt_entry.delete(0,END)
    rice_entry.delete(0,END)
    tea_entry.delete(0,END)
    oil_entry.delete(0,END)
    maaza_entry.delete(0,END)
    sprite_entry.delete(0,END)
    cocacola_entry.delete(0,END)
    frooti_entry.delete(0,END)
    dew_entry.delete(0,END)
    pepsi_entry.delete(0,END)

    bath_soap_entry.insert(0,0)
    face_cream_entry.insert(0,0)
    face_wash_entry.insert(0,0)
    body_lotion_entry.insert(0,0)
    hair_gel_entry.insert(0,0)
    hair_spray_entry.insert(0,0)
    wheat_entry.insert(0,0)
    sugar_entry.insert(0,0)
    salt_entry.insert(0,0)
    rice_entry.insert(0,0)
    tea_entry.insert(0,0)
    oil_entry.insert(0,0)
    maaza_entry.insert(0,0)
    sprite_entry.insert(0,0)
    cocacola_entry.insert(0,0)
    frooti_entry.insert(0,0)
    dew_entry.insert(0,0)
    pepsi_entry.insert(0,0)

    cosmetic_price_entry.delete(0,END)
    grocery_price_entry.delete(0,END)
    cold_drinks_price_entry.delete(0,END)

    cosmetic_tax_entry.delete(0,END)
    grocery_tax_entry.delete(0,END)
    cold_drinks_tax_entry.delete(0,END)

    name_entry.delete(0,END)
    phone_entry.delete(0,END)
    bill_entry.delete(0,END)
    bill_text_area.delete(1.0,END)




#send bill
def send_bill():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderentry.get(),passwordentry.get())
            message=email_text_area.get(1.0,END)
            ob.sendmail(senderentry.get(),recieverentry.get(),message)
            ob.quit()
            messagebox.showinfo('Success','Bill sent successfully',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong, Please try again',parent=root1)

    if bill_text_area.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('send gmail')
        root1.config(bg='gray20')
        root1.resizable(0,0)

        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderlabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
        senderlabel.grid(row=0,column=0,padx=10,pady=8)
        senderentry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderentry.grid(row=0,column=1,padx=10,pady=8)

        passwordlabel=Label(senderFrame,text="Password",font=('arial',14,'bold'),bg='gray20',fg='white')
        passwordlabel.grid(row=1,column=0,padx=10,pady=8)
        passwordentry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        passwordentry.grid(row=1,column=1,padx=10,pady=8)

        recipientFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        recipientFrame.grid(row=1,column=0,padx=40,pady=20)

        recieverlabel=Label(recipientFrame,text="Email Address",font=('arial',14,'bold'),bg='gray20',fg='white')
        recieverlabel.grid(row=0,column=0,padx=10,pady=8)
        recieverentry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        recieverentry.grid(row=0,column=1,padx=10,pady=8)

        messagelabel=Label(recipientFrame,text="Message",font=('arial',14,'bold'),bg='gray20',fg='white')
        messagelabel.grid(row=1,column=0,padx=10,pady=8)

        email_text_area=Text(recipientFrame,font=('arial',16,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_text_area.grid(row=2,column=0,columnspan=2)
        email_text_area.delete(1.0,END)
        email_text_area.insert(END,bill_text_area.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendButton=Button(root1,text='SEND',font=('arial',14,'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)

        root1.mainloop()



#print bill
def print_bill():
    if bill_text_area.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(bill_text_area.get(1.0,END))
        os.startfile(file,'print')


#search bill
def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==bill_entry.get():
            f=open(f'bills/{i}','r')
            bill_text_area.delete(1.0,END)
            for data in f:
                bill_text_area.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')

#Save Bill
def save_bill():
    global billNumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=bill_text_area.get(1.0,END)
        file=open(f'bills/{billNumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill Number:{billNumber} is saved successfully')
        billNumber=random.randint(500,1000)

billNumber=random.randint(500,1000)

#Bill Area
def bill_area():
    if name_entry.get()=='' or phone_entry.get()=='':
        messagebox.showerror('Error','Cusomer Details Are Required')
    elif cosmetic_price_entry.get()=='' and grocery_price_entry.get()=='' and cold_drinks_price_entry.get()=='':
        messagebox.showerror('Error','No Products Are Selected')
    elif cosmetic_price_entry.get()=='0 Rs' and grocery_price_entry.get()=='0 Rs' and cold_drinks_price_entry.get()=='0 Rs':
        messagebox.showerror('Error','Cusomer Details Are Required')
    else:
        bill_text_area.delete(1.0,END)
        bill_text_area.insert(END,'\t\t**Welcome Customer**\n')
        bill_text_area.insert(END,f'\nBill Number:{billNumber}\n')
        bill_text_area.insert(END,f'\nCustomer Name:{name_entry.get()}\n')
        bill_text_area.insert(END,f'\nPhone Number:{phone_entry.get()}\n')
        bill_text_area.insert(END,'=======================================================')
        bill_text_area.insert(END,'\nProduct\t\t\tQuantity\t\t\tPrice\n')
        bill_text_area.insert(END,'=======================================================')

        if bath_soap_entry.get()!='0':
            bill_text_area.insert(END,f'\nBath Soap\t\t\t{bath_soap_entry.get()}\t\t\t{soapprice} Rs')
        if face_cream_entry.get()!='0':
            bill_text_area.insert(END,f'\nFace Cream\t\t\t{face_cream_entry.get()}\t\t\t{facecreamprice} Rs')
        if face_wash_entry.get()!='0':
            bill_text_area.insert(END,f'\nFace Wash\t\t\t{face_wash_entry.get()}\t\t\t{facewashprice} Rs')
        if hair_spray_entry.get()!='0':
            bill_text_area.insert(END,f'\nHair Spray\t\t\t{hair_spray_entry.get()}\t\t\t{hairsprayprice} Rs')
        if hair_gel_entry.get()!='0':
            bill_text_area.insert(END,f'\nHair Gel\t\t\t{hair_gel_entry.get()}\t\t\t{hairgelprice} Rs')
        if body_lotion_entry.get()!='0':
            bill_text_area.insert(END,f'\nBody Lotion\t\t\t{body_lotion_entry.get()}\t\t\t{bodylotionprice} Rs')

        if wheat_entry.get()!='0':
            bill_text_area.insert(END,f'\nWheat\t\t\t{wheat_entry.get()}\t\t\t{wheatprice} Rs')
        if sugar_entry.get()!='0':
            bill_text_area.insert(END,f'\nSugar\t\t\t{sugar_entry.get()}\t\t\t{sugarprice} Rs')
        if salt_entry.get()!='0':
            bill_text_area.insert(END,f'\nSalt\t\t\t{salt_entry.get()}\t\t\t{saltprice} Rs')
        if oil_entry.get()!='0':
            bill_text_area.insert(END,f'\nOil\t\t\t{oil_entry.get()}\t\t\t{oilprice} Rs')
        if tea_entry.get()!='0':
            bill_text_area.insert(END,f'\nTea\t\t\t{tea_entry.get()}\t\t\t{teaprice} Rs')
        if rice_entry.get()!='0':
            bill_text_area.insert(END,f'\nRice\t\t\t{rice_entry.get()}\t\t\t{riceprice} Rs')
        
        if maaza_entry.get()!='0':
            bill_text_area.insert(END,f'\nMaza\t\t\t{maaza_entry.get()}\t\t\t{mazaprice} Rs')
        if pepsi_entry.get()!='0':
            bill_text_area.insert(END,f'\nPepsi\t\t\t{pepsi_entry.get()}\t\t\t{pepsiprice} Rs')
        if sprite_entry.get()!='0':
            bill_text_area.insert(END,f'\nSprite\t\t\t{sprite_entry.get()}\t\t\t{spriteprice} Rs')
        if dew_entry.get()!='0':
            bill_text_area.insert(END,f'\nDew\t\t\t{dew_entry.get()}\t\t\t{dewprice} Rs')
        if frooti_entry.get()!='0':
            bill_text_area.insert(END,f'\nFrooti\t\t\t{frooti_entry.get()}\t\t\t{frootiprice} Rs')
        if cocacola_entry.get()!='0':
            bill_text_area.insert(END,f'\nCoca Cola\t\t\t{cocacola_entry.get()}\t\t\t{cocacolaprice} Rs')

            
        bill_text_area.insert(END,'\n-------------------------------------------------------')

        if cosmetic_tax_entry.get()!= '0.0 Rs':
            bill_text_area.insert(END,f'\nCosmetic Tax:\t\t\t\t{cosmetic_tax_entry.get()} Rs')
        if grocery_tax_entry.get()!= '0.0 Rs':
            bill_text_area.insert(END,f'\nGrocery Tax:\t\t\t\t{grocery_tax_entry.get()} Rs')
        if cold_drinks_tax_entry.get()!= '0.0 Rs':
            bill_text_area.insert(END,f'\nCold Drinks Tax:\t\t\t\t{cold_drinks_tax_entry.get()} Rs')
        
        bill_text_area.insert(END,f'\n\nTotal Bill:\t\t\t\t{totalBill} Rs')

        bill_text_area.insert(END,'\n-------------------------------------------------------')
        save_bill()





#funcionality part

def total():
    #cosmetic
    global soapprice,facecreamprice,facewashprice,hairsprayprice,bodylotionprice,hairgelprice
    global wheatprice,sugarprice,saltprice,oilprice,teaprice,riceprice
    global mazaprice,pepsiprice,spriteprice,dewprice,frootiprice,cocacolaprice
    global totalBill


    soapprice=int(bath_soap_entry.get())*20
    facecreamprice=int(face_cream_entry.get())*30
    facewashprice=int(face_wash_entry.get())*20
    hairsprayprice=int(hair_spray_entry.get())*30
    hairgelprice=int(hair_gel_entry.get())*30
    bodylotionprice=int(body_lotion_entry.get())*30

    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmetic_price_entry.delete(0,END)
    cosmetic_price_entry.insert(0,f'{totalcosmeticprice} Rs')
    cosmetictax=totalcosmeticprice*0.12
    cosmetic_tax_entry.delete(0,END)
    cosmetic_tax_entry.insert(0, '{:.2f} Rs'.format(cosmetictax))

    #grocery
    wheatprice=int(wheat_entry.get())*50
    sugarprice=int(sugar_entry.get())*50
    saltprice=int(salt_entry.get())*50
    oilprice=int(oil_entry.get())*50
    teaprice=int(tea_entry.get())*50
    riceprice=int(rice_entry.get())*50

    totlagroceryprice=wheatprice+sugarprice+saltprice+oilprice+teaprice+riceprice
    grocery_price_entry.delete(0,END)
    grocery_price_entry.insert(0,f'{totlagroceryprice} Rs')
    grocerytax=totlagroceryprice*0.12
    grocery_tax_entry.delete(0,END)
    grocery_tax_entry.insert(0, '{:.2f} Rs'.format(grocerytax))

    #cold drinks
    mazaprice=int(maaza_entry.get())*50
    pepsiprice=int(pepsi_entry.get())*50
    spriteprice=int(sprite_entry.get())*50
    dewprice=int(dew_entry.get())*50
    frootiprice=int(frooti_entry.get())*50
    cocacolaprice=int(cocacola_entry.get())*50

    totalcolddrinksprice=mazaprice+pepsiprice+spriteprice+dewprice+frootiprice+cocacolaprice
    cold_drinks_price_entry.delete(0,END)
    cold_drinks_price_entry.insert(0,f'{totalcolddrinksprice} Rs')
    colddrinkstax=totalcolddrinksprice*0.12
    cold_drinks_tax_entry.delete(0,END)
    cold_drinks_tax_entry.insert(0, '{:.2f} Rs'.format(colddrinkstax))

    totalBill=totalcosmeticprice+totlagroceryprice+totalcolddrinksprice+cosmetictax+grocerytax+colddrinkstax
    

#GUI Part
root = Tk()
root.title("Retail Billing System")
root.geometry("1270x685")
root.iconbitmap('icon.ico')

heading_label = Label(root, text="Retail Billing System", font=("Times New Roman", 30, "bold"), fg="gold", bg="gray20",bd=12,relief=GROOVE)
heading_label.pack(fill=X)

customer_details_frame = LabelFrame(root, text="Customer Details", font=("Times New Roman", 15, "bold"), fg="gold", bg="gray20", bd=8, relief=GROOVE)
customer_details_frame.pack(fill=X)

name_label = Label(customer_details_frame, text="Name", font=("Times New Roman", 15, "bold"), fg="white", bg="gray20")
name_label.grid(row=0, column=0, padx=10, pady=2)

name_entry = Entry(customer_details_frame, font=("Arial", 15), bd=7)
name_entry.grid(row=0, column=1, padx=10)

phone_label = Label(customer_details_frame, text="Phone Number", font=("Times New Roman", 15, "bold"), fg="white", bg="gray20")
phone_label.grid(row=0, column=2, padx=10, pady=2)

phone_entry = Entry(customer_details_frame, font=("Arial", 15), bd=7)
phone_entry.grid(row=0, column=3, padx=10)

bill_label = Label(customer_details_frame, text="Bill Number", font=("Times New Roman", 15, "bold"), fg="white", bg="gray20")
bill_label.grid(row=0, column=4, padx=10, pady=2)

bill_entry = Entry(customer_details_frame, font=("Arial", 15), bd=7)
bill_entry.grid(row=0, column=5, padx=10)

search_button = Button(customer_details_frame, text="Search", font=("Times New Roman", 15, "bold"), fg="white", bg="gray20", bd=7, relief=GROOVE,command=search_bill)
search_button.grid(row=0, column=6, padx=10,pady=8)
####
products_frame = Frame(root)
products_frame.pack(fill=X)
########
cosmetics_frame = LabelFrame(products_frame, text="Cosmetics", font=("Times New Roman", 15, "bold"), fg="gold", bg="gray20", bd=8, relief=GROOVE)
cosmetics_frame.grid(row=0, column=0)

face_cream_label = Label(cosmetics_frame, text="Face Cream", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20")
face_cream_label.grid(row=0, column=0, padx=20, pady=13)
face_cream_entry = Entry(cosmetics_frame, font=("Times New Roman", 12), width=10, bd=5)
face_cream_entry.grid(row=0, column=1, padx=20)
face_cream_entry.insert(0,0)

face_wash_label = Label(cosmetics_frame, text="Face Wash", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20")
face_wash_label.grid(row=1, column=0, padx=20, pady=13)
face_wash_entry = Entry(cosmetics_frame, font=("Times New Roman", 12), width=10, bd=5)
face_wash_entry.grid(row=1, column=1, padx=20)
face_wash_entry.insert(0,0)

hair_spray_label = Label(cosmetics_frame, text="Hair Spray", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20")
hair_spray_label.grid(row=2, column=0, padx=20, pady=13)
hair_spray_entry = Entry(cosmetics_frame, font=("Times New Roman", 12), width=10, bd=5)
hair_spray_entry.grid(row=2, column=1, padx=20)
hair_spray_entry.insert(0,0)


hair_gel_label =Label(cosmetics_frame, text="Hair Gel", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20").grid(row=3, column=0, padx=20, pady=13)
hair_gel_entry = Entry(cosmetics_frame, font=("Times New Roman", 12), width=10, bd=5)
hair_gel_entry.grid(row=3, column=1, padx=20)
hair_gel_entry.insert(0,0)


body_lotion_label = Label(cosmetics_frame, text="Body Lotion", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20")
body_lotion_label.grid(row=4, column=0, padx=20, pady=13)
body_lotion_entry = Entry(cosmetics_frame, font=("Times New Roman", 12), width=10, bd=5)
body_lotion_entry.grid(row=4, column=1, padx=20)
body_lotion_entry.insert(0,0)


bath_soap_label = Label(cosmetics_frame, text="Bath Soap", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20")
bath_soap_label.grid(row=5, column=0, padx=20, pady=13)
bath_soap_entry = Entry(cosmetics_frame, font=("Times New Roman", 12), width=10, bd=5)
bath_soap_entry.grid(row=5, column=1, padx=20)
bath_soap_entry.insert(0,0)

######
grocery_frame = LabelFrame(products_frame, text="Grocery", font=("Times New Roman", 15, "bold"), fg="gold", bg="gray20", bd=8, relief=GROOVE)
grocery_frame.grid(row=0, column=1)


wheat_label = Label(grocery_frame, text="Wheat", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20")
wheat_label.grid(row=0, column=0, padx=20, pady=13, sticky="w")
wheat_entry = Entry(grocery_frame, font=("Times New Roman", 12), width=10, bd=5)
wheat_entry.grid(row=0, column=1, padx=20)
wheat_entry.insert(0,0)


sugar_label = Label(grocery_frame, text="Sugar", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20")
sugar_label.grid(row=1, column=0, padx=20, pady=13, sticky="w")
sugar_entry = Entry(grocery_frame, font=("Times New Roman", 12), width=10, bd=5)
sugar_entry.grid(row=1, column=1, padx=20)
sugar_entry.insert(0,0)

salt_label = Label(grocery_frame, text="Salt", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20")
salt_label.grid(row=2, column=0, padx=20, pady=13, sticky="w")
salt_entry = Entry(grocery_frame, font=("Times New Roman", 12), width=10, bd=5)
salt_entry.grid(row=2, column=1, padx=20)
salt_entry.insert(0,0)

oil_label = Label(grocery_frame, text="Oil", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20")
oil_label.grid(row=3, column=0, padx=20, pady=13, sticky="w")
oil_entry = Entry(grocery_frame, font=("Times New Roman", 12), width=10, bd=5)
oil_entry.grid(row=3, column=1, padx=20)
oil_entry.insert(0,0)

tea_label = Label(grocery_frame, text="Tea", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20")
tea_label.grid(row=4, column=0, padx=20, pady=13, sticky="w")
tea_entry = Entry(grocery_frame, font=("Times New Roman", 12), width=10, bd=5)
tea_entry.grid(row=4, column=1, padx=20)
tea_entry.insert(0,0)


rice_label = Label(grocery_frame, text="Rice", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20")
rice_label.grid(row=5, column=0, padx=20, pady=13, sticky="w")
rice_entry = Entry(grocery_frame, font=("Times New Roman", 12), width=10, bd=5)
rice_entry.grid(row=5, column=1, padx=20)
rice_entry.insert(0,0)

#######


cold_drinks_frame = LabelFrame(products_frame, text="Cold Drinks", font=("Times New Roman", 15, "bold"), fg="gold", bg="gray20", bd=8, relief=GROOVE)
cold_drinks_frame.grid(row=0, column=2)

maaza_label = Label(cold_drinks_frame, text="Maaza", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20")
maaza_label.grid(row=0, column=0, padx=20, pady=13)
maaza_entry = Entry(cold_drinks_frame, font=("Times New Roman", 12), width=10, bd=5)
maaza_entry.grid(row=0, column=1, padx=20)
maaza_entry.insert(0,0)

pepsi_label = Label(cold_drinks_frame, text="Pepsi", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20")
pepsi_label.grid(row=1, column=0, padx=20, pady=13)
pepsi_entry = Entry(cold_drinks_frame, font=("Times New Roman", 12), width=10, bd=5)
pepsi_entry.grid(row=1, column=1, padx=20)
pepsi_entry.insert(0,0)

sprite_label = Label(cold_drinks_frame, text="Sprite", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20")
sprite_label.grid(row=2, column=0, padx=20, pady=13)
sprite_entry = Entry(cold_drinks_frame, font=("Times New Roman", 12), width=10, bd=5)
sprite_entry.grid(row=2, column=1, padx=20)
sprite_entry.insert(0,0)

dew_label =Label(cold_drinks_frame, text="Dew", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20").grid(row=3, column=0, padx=20, pady=13)
dew_entry = Entry(cold_drinks_frame, font=("Times New Roman", 12), width=10, bd=5)
dew_entry.grid(row=3, column=1, padx=20)
dew_entry.insert(0,0)

frooti_label = Label(cold_drinks_frame, text="Frooti", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20")
frooti_label.grid(row=4, column=0, padx=20, pady=13)
frooti_entry = Entry(cold_drinks_frame, font=("Times New Roman", 12), width=10, bd=5)
frooti_entry.grid(row=4, column=1, padx=20)
frooti_entry.insert(0,0)

cocacola_label = Label(cold_drinks_frame, text="Coca Cola", font=("Times New Roman", 12, "bold"), fg="gold", bg="gray20")
cocacola_label.grid(row=5, column=0, padx=20, pady=13)
cocacola_entry = Entry(cold_drinks_frame, font=("Times New Roman", 12), width=10, bd=5)
cocacola_entry.grid(row=5, column=1, padx=20)
cocacola_entry.insert(0,0)

#########


bill_frame = Frame(products_frame,bd=8,relief=GROOVE)
bill_frame.grid(row=0, column=3,padx=10)

bill_area_label=Label(bill_frame,text="Bill Area",font=('times new Roman',15,'bold'),bd=8,relief=GROOVE)
bill_area_label.pack(fill=X)

scrollbar=Scrollbar(bill_frame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
bill_text_area = Text(bill_frame,height=18,width=55,yscrollcommand=scrollbar.set)
bill_text_area.pack()
scrollbar.config(command=bill_text_area.yview)

###########

bill_menu_frame = LabelFrame(root, text="Bill Menu", font=("Times New Roman", 15, "bold"), fg="gold", bg="gray20", bd=8, relief=GROOVE)
bill_menu_frame.pack(fill=X)

cosmetic_price_label = Label(bill_menu_frame, text="Cosmetic Price", font=("Times New Roman", 14, "bold"), fg="gold", bg="gray20")
cosmetic_price_label.grid(row=0, column=0, padx=10, pady=6)
cosmetic_price_entry = Entry(bill_menu_frame, font=("Arial", 12), bg="white", bd=3)
cosmetic_price_entry.grid(row=0, column=1)

grocery_price_label = Label(bill_menu_frame, text="Grocery Price", font=("Times New Roman", 14, "bold"), fg="gold", bg="gray20")
grocery_price_label.grid(row=1, column=0, padx=10, pady=6)
grocery_price_entry = Entry(bill_menu_frame, font=("Arial", 12), bg="white", bd=3)
grocery_price_entry.grid(row=1, column=1)

cold_drinks_price_label = Label(bill_menu_frame, text="Cold Drinks Price", font=("Times New Roman", 14, "bold"), fg="gold", bg="gray20")
cold_drinks_price_label.grid(row=2, column=0, padx=10, pady=6)
cold_drinks_price_entry = Entry(bill_menu_frame, font=("Arial", 12), bg="white", bd=3)
cold_drinks_price_entry.grid(row=2, column=1)


cosmetic_tax_label = Label(bill_menu_frame, text="Cosmetic Tax", font=("Times New Roman", 14, "bold"), fg="gold", bg="gray20")
cosmetic_tax_label.grid(row=0, column=2, padx=10, pady=6)
cosmetic_tax_entry = Entry(bill_menu_frame, font=("Arial", 12), bg="white", bd=3)
cosmetic_tax_entry.grid(row=0, column=3)

grocery_tax_label = Label(bill_menu_frame, text="Grocery Tax", font=("Times New Roman", 14, "bold"), fg="gold", bg="gray20")
grocery_tax_label.grid(row=1, column=2, padx=10, pady=6)
grocery_tax_entry = Entry(bill_menu_frame, font=("Arial", 12), bg="white", bd=3)
grocery_tax_entry.grid(row=1, column=3)

cold_drinks_tax_label = Label(bill_menu_frame, text="Cold Drinks Tax", font=("Times New Roman", 14, "bold"), fg="gold", bg="gray20")
cold_drinks_tax_label.grid(row=2, column=2, padx=10, pady=6)
cold_drinks_tax_entry = Entry(bill_menu_frame, font=("Arial", 12), bg="white", bd=3)
cold_drinks_tax_entry.grid(row=2, column=3)

button_frame=Frame(bill_menu_frame,bd=8,relief=GROOVE)
button_frame.grid(row=0,column=4,rowspan=3,padx=10)

total_button=Button(button_frame,text='Total',font=('arial',14,'bold'),bg='gray20',fg='white',bd=5,width=6,pady=10,command=total)
total_button.grid(row=0,column=0,pady=15,padx=5)

bill_button=Button(button_frame,text='Bill',font=('arial',14,'bold'),bg='gray20',fg='white',bd=5,width=6,pady=10,command=bill_area)
bill_button.grid(row=0,column=1,pady=15,padx=5)

email_button=Button(button_frame,text='Email',font=('arial',14,'bold'),bg='gray20',fg='white',bd=5,width=6,pady=10,command=send_bill)
email_button.grid(row=0,column=2,pady=15,padx=5)

print_button=Button(button_frame,text='Print',font=('arial',14,'bold'),bg='gray20',fg='white',bd=5,width=6,pady=10,command=print_bill)
print_button.grid(row=0,column=3,pady=15,padx=5)

clear_button=Button(button_frame,text='Clear',font=('arial',14,'bold'),bg='gray20',fg='white',bd=5,width=6,pady=10,command=clear)
clear_button.grid(row=0,column=4,pady=15,padx=5)


root.mainloop()
