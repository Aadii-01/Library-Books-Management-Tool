import pymysql as sqltor
import csv
#https://fonts.google.com/specimen/JetBrains+Mono
#download above font for proper table size
# pip install https://pypi.python.org/packages/source/P/PrettyTable/prettytable-0.7.2.tar.bz2
from prettytable import PrettyTable
cnx=sqltor.connect(host="localhost", user="", password="")
cur=cnx.cursor()
# if cnx.is_connected():
#         print("Connected")
flag=True
print("HELLO !!")
print("Myself Aaditya Shirke from Class 12th of Atomic Energy Central School No.3, Boisar")
print("I have tried to ease the work of a hostel librarian , hope you like it :)\n\n")
# IMPORTANT TO EDIT THE PATH DURING PROGRAM DISPLAY IN FRONT OF TEACHER
f=open("Booksdata.csv", "a")
wr=csv.writer(f)
# POPULAR BOOKS AMONGST PUBLIC DURING LAST MONTH
h = ["Bookname", "Writer", "Cost", "Total Pages", "InStock"]
Lam = [["Ghosts of the Silent Hills ", "Anita Krishan","550","256","150"],
["Watership down","Richard Adams","650","748","320"],
["Game of Thrones","George Martin","4197","3473","10"],
["Alchemist","Paulo Coelho","387","224","242"],
["Darkness","Ratnakar Matkari","650","452","187"],
["The Elementals","Michel McDowells","680","765","135"],
["Burnt Offerings","Robert Marasco","540","234","320"],
["Start with Why","Simon Sinek","360","256","188"],
["Indian Polity","M Laxmikanth","576","824","150"],
["You Can","George Adam","99","130","135"],
["Concept of Physics 1","H.C.Verma","359","462","320"]]
wr.writerow(h)
for i in Lam:
    wr.writerow(i)
f.close()
while True:
    op=int(input("\nWhat Do you want to do?"
    "\n1.Update your original data"
    "\n2. Customer's page "
    "\nEnter your choice no.--->"))
    if op==1:
        while flag:
            opt=int(input("\n ----------------------"
            "\n| 1.Create database |"
            "\n ----------------------"
            "\n| 2.Create sections |"
            "\n ----------------------"
            "\n| 3.Perform operations |"
            "\n ----------------------"
            "\n| 4.Quit |"
            "\n ----------------------"
            "\nEnter choice no. ----> "))
            if opt==1:
                print("\n\n\nFILL UP THE FOLLOWING DETAIL TO CREATE NEW DATABASE IN YOUR LIBRARY")
                db=input("** Enter new database name--->")
                cur.execute("Create database"+' '+db)
                print("=> Database created successfully !!")
            elif opt==2:
                print("\nFILL UP THE FOLLOWING DETAILS TO CREATE NEW SECTION IN YOUR LIBRARY")
                db=input("** Enter database name--->")
                cur.execute("use "+db)
                m=input("** Enter section name--->")
                cur.execute("create table "+m+" (Bookname varchar(50),writer varchar(50),cost int,TotPages int,InStock int)")
                print("Section "+m+" created successfully !!")
            elif opt==3:
                print("\nFILL UP THE FOLLOWING DETAILS TO PERFORM OPERATIONS ON YOUR DESIRED SECTION")
                db = input("** Enter database name--->")
                cur.execute("use " + db)
                cur.execute("show tables")
                data = cur.fetchall()
                po=[]
                print("Tables in " + db)
                for i in data:
                    po.append(i)
                    print(str(i))
                if po==[]:
                    print("This database has no sections , go back and create one !!")
                else:
                    tb = input("** Enter table name to be operated ---> ")
                    x=input("Do you want to add Dummy Data to ur table? (y/n) ---> ")
                    if x=="y" or x=="Y":
                        for i in Lam:
                            qry = "insert into {} values (%s,%s,%s,%s,%s)".format(tb)
                            val = tuple(i)
                            cur.execute(qry, val)
                            cnx.commit()
                    elif x=="n" or x=="N":
                        pass
                    while True:
                        z=input("\n\nContinue with operations ?? (y/n) ----> ")
                        if z=="y":
                            opr=int(input("** What operation do you want to perform ?"
                            "\n ____________________"
                            "\n| 1.Insert values |"
                            "\n --------------------"
                            "\n| 2.Display data |"
                            "\n --------------------"
                            "\n| 3.Drop table |"
                            "\n -------------------"
                            "\n| 4.Update table |"
                            "\n -------------------"
                            "\n| 5.Delete records |"
                            "\n -------------------"
                            "\n| 6.Display prt data |"
                            "\n -------------------"
                            "\n| 7. Quit |"
                            "\n -------------------"
                            "\nEnter choice no. --->"))
                            if opr==1:
                                x=int(input("How many values do you wanna insert into the section? ---> "))
                                R=[]
                                for i in range(x):
                                    a1=input("\n* Enter Bookname ---> ")
                                    a2=input("* Enter Writer name ---> ")
                                    a3=int(input("* Enter Cost of the book---> "))
                                    a4=int(input("* Enter Total Pages of the book---> "))
                                    a5=int(input("* Enter Total Books in Stock ---> "))
                                    qry="insert into {} values (%s, %s, %s, %s, %s)".format(tb)
                                    val=(a1,a2,a3,a4,a5)
                                    cur.execute(qry, val)
                                    cnx.commit()
                                    print("=> Values have been inserted succesfully !!")
                                    R.append(list(val))
                                f = open("Datum.csv", "w")
                                wrtr = csv.writer(f)
                                h = ["Bookname", "Writer", "Cost", "Total Pages", "InStock"]
                                L=[]
                                wrtr.writerow(h)
                                for i in R:
                                    wrtr.writerow(i)
                                f.close()   
                            elif opr==2:
                                cur.execute("select * from " + tb)
                                data = cur.fetchall()
                                count = cur.rowcount
                                print("Total No. of Records: ", count)
                                x=PrettyTable()
                                x.field_names=["Bookname","Writer's name","Cost","Total Pages","In Stock"]
                                for i in data:
                                    x.add_row(i)
                                print(x)
                            elif opr==3:
                                cur.execute("drop table "+tb)
                                print("Section has been deleted successfully !!")
                            elif opr==4:
                                en=int(input("\n ------------------"
                                "\n| 1.Bookname |"
                                "\n ------------------"
                                "\n| 2.Writer |"
                                "\n ------------------"
                                "\n| 3.Cost |"
                                "\n ------------------"
                                "\n| 4.Total Pages |"
                                "\n ------------------"
                                "\n| 5.InStock |"
                                "\n ------------------"
                                "\nEnter section no. to be updated---> "))
                                if en==1:
                                    fn=input("\n* Enter new Bookname---> ")
                                    wr=input("* Enter where condition (for eg. cost)---> ")
                                    cs=input("* Enter the value of condition (for eg. 275)--->")
                                    qry = "update {} set Bookname=%s where {}={}".format(tb,wr, cs)
                                    val = (fn,)
                                    cur.execute(qry, val)
                                    cnx.commit()
                                    print("Bookname has been successfully changed to "+fn)
                                elif en==2:
                                    fn=input("\n* Enter new Writer name---> ")
                                    wr=input("* Enter where condition (for eg. cost)---> ")
                                    cs = input("* Enter the value of condition (for eg. 275)--->")
                                    qry="update {} set writer=%s where {}={}".format(tb,wr, cs)
                                    val=(fn,)
                                    cur.execute(qry,val)
                                    cnx.commit()
                                    print("Writer's name has been successfully changed to "+fn)
                                elif en==3:
                                    fn=input("\n* Enter new cost---> ")
                                    wr=input("* Enter where condition (for eg. TotPages)---> ")
                                    cs = input("* Enter the value of condition (for eg. 275)--->")
                                    qry = "update {} set cost=%s where {}={}".format(tb, wr, cs)
                                    val = (fn,)
                                    cur.execute(qry,val)
                                    cnx.commit()
                                    print("Cost has been successfully changed to "+fn)
                                elif en==4:
                                    fn=input("\n* Enter new Total pages---> ")
                                    wr=input("* Enter where condition (for eg. cost)---> ")
                                    cs = input("* Enter the value of condition (for eg. 275)--->")
                                    qry = "update {} set TotPages=%s where {}={}".format(tb, wr, cs)
                                    val = (fn,)
                                    cur.execute(qry,val)
                                    cnx.commit()
                                    print("Cost has been successfully changed to "+fn)
                                elif en==5:
                                    fn=input("\n* Enter total no. of books in stock---> ")
                                    wr=input("* Enter where condition (for eg. cost)---> ")
                                    cs = input("* Enter the value of condition (for eg. 275)--->")
                                    qry = "update {} set InStock=%s where {}={}".format(tb, wr, cs)
                                    val = (fn,)
                                    cur.execute(qry,val)
                                    cnx.commit()
                                    print("Total no. of books in stock has been perfectly changed to "+fn)
                            elif opr==5:
                                wr1=input("\n* Enter Column name for reference to delete data (for eg.Bookname,writer,cost,TotPages,InStock) ---> ")
                                cs=input("* Enter the value of column name (for eg. 275) ---> ")
                                qry = "delete from {} where {}={}".format(tb, wr1,cs)
                                val = (wr1,cs,)
                                cur.execute(qry)
                                cnx.commit()
                                print("Values have been successfully deleted !!")
                                print("Have a look!!\n")
                                cur.execute("select * from " + tb)
                                data = cur.fetchall()
                                x = PrettyTable()
                                x.field_names = ["Bookname", "Writer's name", "Cost", "Total Pages", "In Stock"]
                                for i in data:
                                    x.add_row(i)
                                print(x)
                    #cost alag var value alag var and %s style----|
                    #<^>
                            elif opr==6:
                                wr2=input("\n* Enter the where condition to display particular data (for eg. cost)--->")
                                cs = input("* Enter the value of condition (for eg. 275)--->")
                                qry = "select * from {} where {}={}".format(tb, wr2, cs)
                                val = (wr2, cs,)
                                cur.execute(qry)
                                data=cur.fetchall()
                                x = PrettyTable()
                                x.field_names = ["Bookname", "Writer's name", "Cost", "Total Pages", "In Stock"]
                                for i in data:
                                    x.add_row(i)
                                print(x)
                                cnx.close()
                            elif opr==7:
                                print("Heading back to initial stage --> \n\n")
                                break
                        elif z=="n":
                            break
            elif opt==4:
                print("Thank You !!")
                break
###########################################################
#####################################
#CUSTOMERS SECTION
    elif op==2:
        print("\n-------------------------------------------------")
        print("**---------------------------------------------**")
        print("Welcome to the Hostel's Library !!")
        print("Here we have multiple types of categories of Books ")
        print("Here is the list of books we have right now")
        print("\nI} BOOKS ON DRAMA:--> ")
        y=PrettyTable()
        y.field_names = ["BOOK NAME", "AUTHOR'S NAME"]
        A=[["I'm Your Huckleberry ","Val Kilmer"],
        ["Walking With Ghosts","Gabriel Byrne"],
        ["Forever Young","Hayley Mills"],
        ["Will, AKA Where There's a Way","Will Smith"],
        ["Things I Should Have Said ","Jamie Lynn Spears"],
        ["The Great Peace","Mena Suvari"]]
        for i in A:
            y.add_row(i)
        print(y)
        print("\n\nII} BOOKS ON LITERATURE")
        y=PrettyTable()
        y.field_names = ["BOOK NAME", "AUTHOR'S NAME"]
        B=[["Istanbul: Memories and the City","Orhan Pamuk"],
        ["A Writer's Life ","Gay Talese"],
        ["More About Boy ","Roald Dahl"],
        ["Jacky Daydream & My Secret Diary","Jacqueline Wilson"],
        ["Once in a House on Fire","Andrea Ashworth"],
        ["Turning Point in My Life","Paul Kipchumb"]]
        for i in B:
            y.add_row(i)
        print(y)
        print("\n\nIII} GREAT HITS OF THEIR TIME")
        y = PrettyTable()
        y.field_names = ["BOOK NAME", "AUTHOR'S NAME"]
        C=[["The Golden Notebook","Doris Lessing"],
        ["The Catcher in the Rye","J. D. Salinger"],
        ["Red Harvest","Dashiell Hammett"],
        ["What We Talk About When We Talk About Love","Raymond Carver"],
        ["Dubliners","James Joyce "],
        ["Cane","Jean Toomer"]]
        for i in C:
            y.add_row(i)
        print(y)
        print("\n\nIV} POPULAR HARRY POTTER SERIES BY J.K.ROWLING")
        y = PrettyTable()
        y.field_names = ["BOOK NAME", "AUTHOR'S NAME"]
        D=[["Harry Potter and the Sorcerer’s Stone (I)","|"],
        ["Harry Potter and the Chamber of Secrets (II)","|"],
        ["Harry Potter and the Prisoner of Azkaban (III)","|"],
        ["Harry Potter and the Goblet of Fire (IV)","} J.K.ROWLING"],
        ["Harry Potter and the Order of the Phoenix (V)","|"],
        ["Harry Potter and the Half-Blood Prince (VI)","|"],
        ["Harry Potter and the Deathly Hallows (VII)","|"],
        ["Harry Potter and the Cursed Child (VIII)","|"]]
        for i in D:
            y.add_row(i)
        print(y)
        print("\n\nV} BEST BOOKS FOR COLLEGE STUDENTS")
        y = PrettyTable()
        y.field_names = ["BOOK NAME", "AUTHOR'S NAME"]
        E=[["How To Win At College","Cal Newport"],
        ["10 Steps To Earning Awesome Grades","Thomas Frank"],
        ["How To Win Friends And Influence People","Dale Carnegie"],
        ["Deep Work","Cal Newport"],
        ["To Kill a Mocking Bird","Harper Lee"],
        ["Atomic Habits","James Clear"],
        ["The 7 Habits of Highly Effective People","Stephen.R.Covey"],
        ["The Monk Who Sold His Ferrari","Robin Sharma"],
        ["The Power of Now","Eckhart Tolle"]]
        for i in E:
            y.add_row(i)
        print(y)
        print("\n\nVI} POPULAR INDIAN BOOKS")
        y = PrettyTable()
        y.field_names = ["BOOK NAME", "AUTHOR'S NAME"]
        F=[["White Tiger","Arvind Adiga"],
        [ "The Great Indian Novel","Shashi Tharoor"],
        ["Train to Pakistan","Khushwant Singh"],
        ["Malgudi Days","R.K Narayan"],
        ["Chanakya's Chant","Ashwin Sanghi"],
        ["Sacred Games","Vikram Chandra"],
        ["Byomkesh Bakshi(series)","Sharadindu Bandopadhyay"],
        ["The Devourers","Indra Das"],
        ["Alice in Deadland","Mainak Dhar"],
        ["Wings Of Fire","A.P.J. Abdul Kalam"],
        ["The Accidental PM","Sanjaya Baru"],
        ["Habit of winning","Prakash Iyer"]]
        for i in F:
            y.add_row(i)
        print(y)
        print("\n\nOhk before issuing books, confirm me your name , your room number and your year of college going on !!")
        nm = input("** So,let me know your name---> ")
        rn = input("** What was your room number ?---> ")
        cy = input("** Your college year ?---> ")
        p=[]
        print("Ohk, u can proceed now :)")
        print("\nWhat do you want to do ?")
        oq = 1
        if oq==1:
            l=int(input("How many books do you want to issue ?---> "))
            s=[]
            t=[]
            for i in range(l):
                cat=input("For easy purpose not to enter much jus write the category number (I,II,III,IV,V,VI)--->")
                bno=input("Enter the Book no. you want to issue --->")
                s=[cat,bno]
                t.append(s)
                s=[]
            print("\n=> Here are the books you have issued :- ")
            for j in t:
                if j[0]=="I" or j[0]=="i":
                    if j[1]=="1":
                        print("I'm Your Huckleberry ")
                    elif j[1]=="2":
                        print("Walking With Ghosts")
                    elif j[1]=="3":
                        print("Forever Young")
                    elif j[1]=="4":
                        print("Will, AKA Where There's a Way")
                    elif j[1]=="5":
                        print("Things I Should Have Said")
                    elif j[1]=="6":
                        print("The Great Peace")
                elif j[0]=="II" or j[0]=="ii":
                    if j[1]=="1":
                        print("Istanbul: Memories and the City")
                    elif j[1]=="2":
                        print("A Writer's Life ")
                    elif j[1]=="3":
                        print("More About Boy ")
                    elif j[1]=="4":
                        print("Jacky Daydream & My Secret Diary")
                    elif j[1]=="5":
                        print("Once in a House on Fire")
                    elif j[1]=="6":
                        print("Turning Point in My Life")
                elif j[0]=="III" or j[0]=="iii":
                    if j[1]=="1":
                        print("The Golden Notebook-")
                    elif j[1]=="2":
                        print("The Catcher in the Rye")
                    elif j[1]=="3":
                        print("Red Harvest")
                    elif j[1]=="4":
                        print("What We Talk About When We Talk About Love")
                    elif j[1]=="5":
                        print("Dubliners")
                    elif j[1]=="6":
                        print("Cane")
                elif j[0]=="IV" or j[0]=="iv":
                    if j[1]=="1":
                        print("Harry Potter and the Sorcerer’s Stone (I)")
                    elif j[1]=="2":
                        print("Harry Potter and the Chamber of Secrets (II)")
                    elif j[1]=="3":
                        print("Harry Potter and the Prisoner of Azkaban (III)")
                    elif j[1]=="4":
                        print("Harry Potter and the Goblet of Fire (IV)")
                    elif j[1]=="5":
                        print("Harry Potter and the Order of the Phoenix (V)")
                    elif j[1]=="6":
                        print("Harry Potter and the Half-Blood Prince (VI)")
                    elif j[1]=="7":
                        print("Harry Potter and the Deathly Hallows (VII)")
                    elif j[1]=="8":
                        print("Harry Potter and the Cursed Child (VIII)")
                elif j[0]=="V" or j[0]=="v":
                    if j[1]=="1":
                        print(".How To Win At College")
                    elif j[1]=="2":
                        print("10 Steps To Earning Awesome Grades")
                    elif j[1]=="3":
                        print("How To Win Friends And Influence People")
                    elif j[1]=="4":
                        print("Deep Work")
                    elif j[1]=="5":
                        print("To Kill A Mockingbird")
                    elif j[1]=="6":
                        print("Atomic Habits")
                    elif j[1]=="7":
                        print("The 7 Habits of Highly Effective People")
                    elif j[1]=="8":
                        print("The Monk Who Sold His Ferrari")
                    elif j[1]=="9":
                        print("The Power of Now")
                elif j[0]=="VI" or j[0]=="vi":
                    if j[1]=="1":
                        print("White Tiger")
                    elif j[1]=="2":
                        print("The Great Indian Novel")
                    elif j[1]=="3":
                        print("Train to Pakistan")
                    elif j[1]=="4":
                        print("Malgudi Days")
                    elif j[1]=="5":
                        print("Chanakya's Chant")
                    elif j[1]=="6":
                        print("Sacred Games")
                    elif j[1]=="7":
                        print("Byomkesh Bakshi(series)")
                    elif j[1]=="8":
                        print("The Devourers")
                    elif j[1]=="9":
                        print("Alice in Deadland")
                    elif j[1]=="10":
                        print("Wings Of Fire")
                    elif j[1]=="11":
                        print("The Accidental PM")
                    elif j[1]=="12":
                        print("Habit of winning")
            eq = [nm, rn, cy, t]
            # order => name, room no. , college year , list(t) containing category number and book no.
            f1 = open("ISSUANCEDATA.csv", "a")
            wr1 = csv.writer(f1)
            wr1.writerow(eq)
            f1.close()
            print("\nDo read wisely !!")
            le = len(t)
            dy = str(le * 7)
            print("And do return back the books by " + dy + " days else you will be penalised !!")
            print("Thank You and keep coming :")
        elif oq==2:
            pass