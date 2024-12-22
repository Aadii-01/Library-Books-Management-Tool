import pymysql as sqltor
import csv

# https://fonts.google.com/specimen/JetBrains+Mono
# download above font for proper table size
# pip install https://pypi.python.org/packages/source/P/PrettyTable/prettytable-0.7.2.tar.bz2
from prettytable import PrettyTable
cnx = sqltor.connect(host="localhost", user="", password="")
cur = cnx.cursor()
# if cnx.is_connected():
#         print("Connected")
flag = True
print("HELLO !!")
print("Myself Aaditya Shirke from Class 12th of Atomic Energy Central School No.3, Boisar")
print("I have tried to ease the work of a hostel librarian , hope you like it :)\n\n")

# IMPORTANT TO EDIT THE PATH DURING PROGRAM DISPLAY IN FRONT OF TEACHER
with open("Booksdata.csv", "a", newline="") as file:
    writer = csv.writer(file)
    # Header and popular books data
    header = ["Bookname", "Writer", "Cost", "Total Pages", "InStock"]
    popular_books = [
        ["Ghosts of the Silent Hills", "Anita Krishan", "550", "256", "150"],
        ["Watership Down", "Richard Adams", "650", "748", "320"],
        ["Game of Thrones", "George Martin", "4197", "3473", "10"],
        ["Alchemist", "Paulo Coelho", "387", "224", "242"],
        ["Darkness", "Ratnakar Matkari", "650", "452", "187"],
        ["The Elementals", "Michel McDowell", "680", "765", "135"],
        ["Burnt Offerings", "Robert Marasco", "540", "234", "320"],
        ["Start with Why", "Simon Sinek", "360", "256", "188"],
        ["Indian Polity", "M Laxmikanth", "576", "824", "150"],
        ["You Can", "George Adam", "99", "130", "135"],
        ["Concept of Physics 1", "H.C. Verma", "359", "462", "320"]
    ]
    # Write the header and book data to the file
    writer.writerow(header)
    writer.writerows(popular_books)

while True:
    process = int(input("\nWhat Do you want to do?"
                        "\n1.Update your original data"
                        "\n2. Land on the customer's page "
                        "\nEnter your choice no.--->"))
    if process == 1:
        while flag:
            opt = int(input("\n ----------------------"
                            "\n| 1.Create database |"
                            "\n ----------------------"
                            "\n| 2.Create sections |"
                            "\n ----------------------"
                            "\n| 3.Perform operations |"
                            "\n ----------------------"
                            "\n| 4.Quit |"
                            "\n ----------------------"
                            "\nEnter choice no. ----> "))
            match opt:
                case 1:
                    print("\n\n\nFILL UP THE FOLLOWING DETAIL TO CREATE NEW DATABASE IN YOUR LIBRARY")
                    database_name = input("** Enter new database name--->")
                    cur.execute(f"Create database {database_name}")
                    print("=> Database created successfully !!")
                case 2:
                    print("\nFILL UP THE FOLLOWING DETAILS TO CREATE NEW SECTION IN YOUR LIBRARY")
                    database_name = input("** Enter database name--->")
                    cur.execute(f"use {database_name}")
                    section_name = input("** Enter section name--->")
                    cur.execute(f"create table {section_name} (Bookname varchar(50),writer varchar(50),cost int,TotPages int,InStock int)")
                    print(f"Section {section_name} created successfully !!")
                case 3:
                    print("\nFILL UP THE FOLLOWING DETAILS TO PERFORM OPERATIONS ON YOUR DESIRED SECTION")
                    database_name = input("** Enter database name--->")
                    cur.execute(f"use {database_name}")
                    cur.execute("show tables")
                    data = cur.fetchall()
                    list_of_sections = []
                    print(f"Tables in {database_name}")
                    for i in data:
                        list_of_sections.append(i)
                        print(str(i))
                    if not list_of_sections: print("This database has no sections , go back and create one !!")
                    else:
                        table_name = input("** Enter table name to be operated ---> ")
                        x = input("Do you want to add Dummy Data to ur table? (y/n) ---> ")
                        if x.lower() == "y":
                            for i in popular_books:
                                query = "insert into {} values (%s,%s,%s,%s,%s)".format(table_name)
                                value = tuple(i)
                                cur.execute(query, value)
                                cnx.commit()
                        elif x.lower() == "n": pass
                        while True:
                            status = input("\n\nContinue with operations ?? (y/n) ----> ").lower()
                            if status == "y":
                                opr = int(input("** What operation do you want to perform ?"
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
                                if opr == 1:
                                    x = int(input("How many values do you wanna insert into the section? ---> "))
                                    R = []
                                    for i in range(x):
                                        book_name = input("\n* Enter Bookname ---> ")
                                        writer_name = input("* Enter Writer name ---> ")
                                        cost_of_book = int(input("* Enter Cost of the book---> "))
                                        total_pages = int(input("* Enter Total Pages of the book---> "))
                                        books_in_stock = int(input("* Enter Total Books in Stock ---> "))
                                        query = "insert into {} values (%s, %s, %s, %s, %s)".format(table_name)
                                        values = (book_name, writer_name, cost_of_book, total_pages, books_in_stock)
                                        cur.execute(query, values)
                                        cnx.commit()
                                        print("=> Values have been inserted succesfully !!")
                                        R.append(list(values))
                                    with open("Datum.csv", "w") as datum_file:
                                        wrtr = csv.writer(datum_file)
                                        heading = ["Bookname", "Writer", "Cost", "Total Pages", "InStock"]
                                        wrtr.writerow(heading)
                                        for i in R : wrtr.writerow(i)
                                elif opr == 2:
                                    cur.execute(f"select * from {table_name}")
                                    data = cur.fetchall()
                                    count = cur.rowcount
                                    print("Total No. of Records: ", count)
                                    x = PrettyTable()
                                    x.field_names = ["Bookname", "Writer's name", "Cost", "Total Pages", "In Stock"]
                                    for i in data:
                                        x.add_row(i)
                                    print(x)
                                elif opr == 3:
                                    cur.execute(f"drop table {table_name}")
                                    print("Section is deleted successfully !!")
                                elif opr == 4:
                                    choice_no = int(input("\n ------------------"
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
                                                          "\nEnter choice no. to be updated---> "))
                                    match choice_no:
                                        case 1:
                                            new_book_name = input("\n* Enter new Bookname---> ")
                                            condition = input("* Enter where condition (for eg. cost)---> ")
                                            condition_value = input("* Enter the value of condition (for eg. 275)--->")
                                            qry = "update {} set Bookname=%s where {}={}".format(table_name, condition, condition_value)
                                            val = (new_book_name,)
                                            cur.execute(qry, val)
                                            cnx.commit()
                                            print(f"Bookname has been successfully changed to {new_book_name}")
                                        case 2:
                                            new_writer_name = input("\n* Enter new Writer name---> ")
                                            condition = input("* Enter where condition (for eg. cost)---> ")
                                            condition_value = input("* Enter the value of condition (for eg. 275)--->")
                                            qry = "update {} set writer=%s where {}={}".format(table_name, condition,condition_value)
                                            val = (new_writer_name,)
                                            cur.execute(qry, val)
                                            cnx.commit()
                                            print(f"Writer's name has been successfully changed to {new_writer_name}")
                                        case 3:
                                            new_cost = input("\n* Enter new cost---> ")
                                            condition = input("* Enter where condition (for eg. TotPages)---> ")
                                            condition_value = input("* Enter the value of condition (for eg. 275)--->")
                                            qry = "update {} set cost=%s where {}={}".format(table_name, condition,condition_value)
                                            val = (new_cost,)
                                            cur.execute(qry, val)
                                            cnx.commit()
                                            print(f"Cost has been successfully changed to {new_cost}")
                                        case 4:
                                            new_pages = input("\n* Enter new Total pages---> ")
                                            condition = input("* Enter where condition (for eg. cost)---> ")
                                            condition_value = input("* Enter the value of condition (for eg. 275)--->")
                                            qry = "update {} set TotPages=%s where {}={}".format(table_name, condition,condition_value)
                                            val = (new_pages,)
                                            cur.execute(qry, val)
                                            cnx.commit()
                                            print(f"Cost has been successfully changed to {new_pages}")
                                        case 5:
                                            books_in_stock = input("\n* Enter total no. of books in stock---> ")
                                            condition = input("* Enter where condition (for eg. cost)---> ")
                                            condition_value = input("* Enter the value of condition (for eg. 275)--->")
                                            qry = "update {} set InStock=%s where {}={}".format(table_name, condition,condition_value)
                                            val = (books_in_stock,)
                                            cur.execute(qry, val)
                                            cnx.commit()
                                            print(f"Total no. of books in stock has been perfectly changed to {books_in_stock}")

                                elif opr == 5:
                                    col_name = input(
                                        "\n* Enter Column name for reference to delete data (for eg.Bookname,writer,cost,TotPages,InStock) ---> ")
                                    col_value = input("* Enter the value of column name (for eg. 275) ---> ")
                                    qry = "delete from {} where {}={}".format(table_name, col_name, col_value)
                                    val = (col_name, col_value,)
                                    cur.execute(qry)
                                    cnx.commit()
                                    print("Values have been successfully deleted !!")
                                    print("Have a look!!\n")
                                    cur.execute(f"select * from {table_name}")
                                    data = cur.fetchall()
                                    x = PrettyTable()
                                    x.field_names = ["Bookname", "Writer's name", "Cost", "Total Pages", "In Stock"]
                                    for i in data: x.add_row(i)
                                    print(x)

                                elif opr == 6:
                                    col_where = input(
                                        "\n* Enter the where condition to display particular data (for eg. cost)--->")
                                    col_where_val = input("* Enter the value of condition (for eg. 275)--->")
                                    qry = "select * from {} where {}={}".format(table_name, col_where, col_where_val)
                                    val = (col_where, col_where_val,)
                                    cur.execute(qry)
                                    data = cur.fetchall()
                                    x = PrettyTable()
                                    x.field_names = ["Bookname", "Writer's name", "Cost", "Total Pages", "In Stock"]
                                    for i in data: x.add_row(i)
                                    print(x)
                                    cnx.close()

                                elif opr == 7:
                                    print("Heading back to the initial stage --> \n\n")
                                    break

                            elif status == "n":
                                break
                case 4:
                    print("Thank You !!")
                    break


    # CUSTOMERS SECTION
    elif process == 2:
        print("\n-------------------------------------------------")
        print("**---------------------------------------------**")
        print("Welcome to the Hostel's Library !!")
        print("Here we have multiple types of categories of Books ")
        print("Here is the list of books we have right now")

        #Function to display books in prettytable format
        def display_books(category, books):
            table = PrettyTable()
            table.field_names = ["BOOK NAME", "AUTHOR'S NAME"]
            for book in books:
                table.add_row(book)
            print(f"\n{category}")
            print(table)

        #Various categorised books
        categories_books = {
            "I} BOOKS ON DRAMA" : [
                  ["I'm Your Huckleberry ", "Val Kilmer"],
                  ["Walking With Ghosts", "Gabriel Byrne"],
                  ["Forever Young", "Hayley Mills"],
                  ["Will, AKA Where There's a Way", "Will Smith"],
                  ["Things I Should Have Said ", "Jamie Lynn Spears"],
                  ["The Great Peace", "Mena Suvari"],
            ],
            "II} BOOKS ON LITERATURE" : [
                      ["Istanbul: Memories and the City", "Orhan Pamuk"],
                      ["A Writer's Life ", "Gay Talese"],
                      ["More About Boy ", "Roald Dahl"],
                      ["Jacky Daydream & My Secret Diary", "Jacqueline Wilson"],
                      ["Once in a House on Fire", "Andrea Ashworth"],
                      ["Turning Point in My Life", "Paul Kipchumb"],
            ],
            "III} GREAT HITS OF THEIR TIME" : [
                ["The Golden Notebook", "Doris Lessing"],
                      ["The Catcher in the Rye", "J. D. Salinger"],
                      ["Red Harvest", "Dashiell Hammett"],
                      ["What We Talk About When We Talk About Love", "Raymond Carver"],
                      ["Dubliners", "James Joyce "],
                      ["Cane", "Jean Toomer"],
            ],
            "IV} POPULAR HARRY POTTER SERIES BY J.K.ROWLING" : [
                      ["Harry Potter and the Sorcerer’s Stone (I)", "J.K.ROWLING"],
                      ["Harry Potter and the Chamber of Secrets (II)", "J.K.ROWLING"],
                      ["Harry Potter and the Prisoner of Azkaban (III)", "J.K.ROWLING"],
                      ["Harry Potter and the Goblet of Fire (IV)", "J.K.ROWLING"],
                      ["Harry Potter and the Order of the Phoenix (V)", "J.K.ROWLING"],
                      ["Harry Potter and the Half-Blood Prince (VI)", "J.K.ROWLING"],
                      ["Harry Potter and the Deathly Hallows (VII)", "J.K.ROWLING"],
                      ["Harry Potter and the Cursed Child (VIII)", "J.K.ROWLING"],
            ],
            "V} BEST BOOKS FOR COLLEGE STUDENTS" : [
                ["How To Win At College", "Cal Newport"],
                      ["10 Steps To Earning Awesome Grades", "Thomas Frank"],
                      ["How To Win Friends And Influence People", "Dale Carnegie"],
                      ["Deep Work", "Cal Newport"],
                      ["To Kill a Mocking Bird", "Harper Lee"],
                      ["Atomic Habits", "James Clear"],
                      ["The 7 Habits of Highly Effective People", "Stephen.R.Covey"],
                      ["The Monk Who Sold His Ferrari", "Robin Sharma"],
                      ["The Power of Now", "Eckhart Tolle"],
            ],
            "VI} POPULAR INDIAN BOOKS" : [
                      ["White Tiger", "Arvind Adiga"],
                      ["The Great Indian Novel", "Shashi Tharoor"],
                      ["Train to Pakistan", "Khushwant Singh"],
                      ["Malgudi Days", "R.K Narayan"],
                      ["Chanakya's Chant", "Ashwin Sanghi"],
                      ["Sacred Games", "Vikram Chandra"],
                      ["Byomkesh Bakshi(series)", "Sharadindu Bandopadhyay"],
                      ["The Devourers", "Indra Das"],
                      ["Alice in Deadland", "Mainak Dhar"],
                      ["Wings Of Fire", "A.P.J. Abdul Kalam"],
                      ["The Accidental PM", "Sanjaya Baru"],
                      ["Habit of winning", "Prakash Iyer"],
            ]
        }
        for category, books in categories_books.items():
            display_books(category, books)

        print("\n\nOk before issuing books, confirm me your name , your room number and your year of college going on !!")
        issuer_name = input("** So,let me know your name---> ")
        issuer_room_no = input("** What was your room number ?---> ")
        issuer_college_year = input("** Your college year ?---> ")
        print("Ok, u can proceed now :)")
        print("\nWhat do you want to do ?")

        #Function to display the names of the books issued
        def display_issued_books(book_category, index):
            print(categories_books[book_category][index - 1][0])

        optional_query = 1
        if optional_query == 1:
            no_of_books_to_issue = int(input("How many books do you want to issue ?---> "))
            issued_books = []
            for no in range(no_of_books_to_issue):
                category_no = input("For easy purpose not to enter much jus write the category number (I,II,III,IV,V,VI)--->")
                book_no = input("Enter the Book no. you want to issue --->")
                issued_books.append([category_no.upper(), book_no])
            print("\n=> Here are the books you have issued :- ")

            for books in issued_books:
                match books[0]:
                    case "I": display_issued_books("I} BOOKS ON DRAMA", int(books[1]))
                    case "II": display_issued_books("II} BOOKS ON LITERATURE", int(books[1]))
                    case "III": display_issued_books("III} GREAT HITS OF THEIR TIME", int(books[1]))
                    case "IV": display_issued_books("IV} POPULAR HARRY POTTER SERIES BY J.K.ROWLING", int(books[1]))
                    case "V": display_issued_books("V} BEST BOOKS FOR COLLEGE STUDENTS", int(books[1]))
                    case "VI": display_issued_books("VI} POPULAR INDIAN BOOKS", int(books[1]))

            issuer_data = [issuer_name, issuer_room_no, issuer_college_year, issued_books]
            issuance_data = open("ISSUANCEDATA.csv", "a")
            wr1 = csv.writer(issuance_data)
            wr1.writerow(issuer_data)
            issuance_data.close()
            print("\nDo read wisely !!")
            days_to_return_books = str(len(issued_books) * 7)
            print(f"And do return back the books by {days_to_return_books} days else you will be penalised !!")
            print("Thank You and keep coming !")

        elif optional_query == 2 : pass