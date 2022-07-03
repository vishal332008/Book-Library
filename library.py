import json

# pylint: disable-all

class Library():
    '''Just a Library'''
    def __init__(self) -> None:
        print("Menu")
        print("1. Lend Book")
        print("2. Return Book")
        print("3. Search Book")
        print("4. Add Book")
        print("5. Register Student")
        a = False

        while(not a):
            try:
                choice = int(input("Enter your choice : "))
            except:
                choice = 0
                
            if choice == 1:
                a = True
                self.ask_student_info()
                self.lend_book()
                break
            elif choice == 2:
                a = True
                self.ask_student_info()
                self.return_book()
                break
            elif choice == 3:
                self.search_book()
                a = True
                break
            elif choice == 4:
                self.add_book()
                a = True
                break
            elif choice == 5:
                self.register_student()
                a = True
                break
            else:
                print("Enter a correct value")


    def ask_student_info(self) -> None:
        self.student_name = input("Enter your Name : ")


    def lend_book(self) -> None:
        with open("books_data.json","r") as f:
            data = json.load(f)
            book_name = input("Enter the Name of the book : ")
            count = 0
            with open("students_data.json","r") as i:
                s_data = json.load(i)
                count1 = 0
                for z in s_data:
                    if self.student_name == s_data[z]["name"]:
                        count1 = count1 + 1
                        for index,i in enumerate(data):
                            if data[i]["name"].lower() == book_name.lower():
                                count = count + 1
                                if data[i]["available"] == "yes":
                                    data["book"+str(index+1)]["available"] = "no"
                                    data["book"+str(index+1)]["taken_by"] = self.student_name
                                    
                                    with open("books_data.json","w") as j:
                                        json.dump(data,j,indent = 2)
                                        j.close()
                                    with open("students_data.json","w") as j:
                                        s_data[z]["books_taken"].append(book_name)
                                        json.dump(s_data,j,indent = 2)
                                        j.close()

                                    print("Book has been lended.")
                                    break
                                else:
                                    print("The Book is not Available Right Now.")
                                    break
                        break
            f.close()

            if count1 == 0:
                print(f"No Student is Registered with the Name \"{self.student_name}\"")
            elif count == 0:
                print(f"No Book Found With the Name \"{book_name}\".")


    def return_book(self) -> None:
        with open("books_data.json","r") as f:
            data = json.load(f)
            book_name = input("Enter the Name of the book : ")
            count = 0
            with open("students_data.json","r") as i:
                s_data = json.load(i)
                count1 = 0
                for z in s_data:
                    if self.student_name == s_data[z]["name"]:
                        count1 = count1 + 1
                        for index,i in enumerate(data):
                            if data[i]["name"].lower() == book_name.lower():
                                count = count + 1
                                if data[i]["available"] == "no":
                                    if data[i]["taken_by"] == self.student_name:       
                                        data["book"+str(index+1)]["available"] = "yes"
                                        data["book"+str(index+1)]["taken_by"] = "None"

                                        with open("books_data.json","w") as j:
                                            json.dump(data,j,indent = 2)
                                            j.close()

                                        with open("students_data.json","w") as j:
                                            s_data[z]["books_taken"].remove(book_name)
                                            json.dump(s_data,j,indent = 2)
                                            j.close()

                                        print("Book has been Returned.")
                                        break
                                    else:
                                        print("Your name is not matching with the person who lent the book.")
                                        break
                                else:
                                    print("You can't return a book that hasn't been lend to anyone.")
                                    break
                        break
                f.close()

            if count1 == 0:
                print(f"No Student is Registered with the Name \"{self.student_name}\"")
            elif count == 0:
                print(f"No Book Found With the Name \"{book_name}\".")


    def search_book(self) -> None:
        book_name = input("Search for a Book : ")
        with open("books_data.json") as f:
            data = json.load(f)
            print("Related Books : ")
            count = 0
            for i in data:
                if book_name.lower() in data[i]["name"].lower():
                    print(data[i]["name"])
                    count = count + 1
            if count == 0:
                print("None")
            f.close()


    def add_book(self) -> None:
        book_name  = input("Enter the Book Name : ")
        book_pages = input("Enter the Number of Pages : ")
        book_author = input("Enter the Author of the Book : ")
        with open("books_data.json") as f:
            data = json.load(f)
            no_of_books = len(data)
            data["book"+str(no_of_books+1)] = {}
            data["book"+str(no_of_books+1)]["name"] = book_name
            data["book"+str(no_of_books+1)]["pages"] = book_pages
            data["book"+str(no_of_books+1)]["author"] = book_author
            data["book"+str(no_of_books+1)]["available"] = "yes"
            data["book"+str(no_of_books+1)]["taken_by"] = "None"
            with open("books_data.json","w") as j:
                json.dump(data,j,indent = 2)
                j.close()
            f.close()

            print(f"Added New Book : \"{book_name}\".")


    def register_student(self):
        student_name  = input("Enter the Student Name : ")
        student_email = input("Enter the Student Email : ")
        with open("students_data.json") as f:
            data = json.load(f)
            no_of_students = len(data)
            check = 0
            for i in data:
                if data[i]["name"] == student_name:
                    print("This name already Exists.")
                    check = 1
                    break
            if check == 0:
                data["student"+str(no_of_students+1)] = {}
                data["student"+str(no_of_students+1)]["name"] = student_name
                data["student"+str(no_of_students+1)]["email"] = student_email
                data["student"+str(no_of_students+1)]["no_of_books"] = 0
                data["student"+str(no_of_students+1)]["books_taken"] = []
                with open("students_data.json","w") as j:
                    json.dump(data,j,indent = 2)
                    j.close()
                f.close()

                print(f"Added New Student : \"{student_name}\".")


books = Library()
