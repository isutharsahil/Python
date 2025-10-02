#Implement a Student class with information such as rollno, name, class. The information must be entered by the user.
#Create a program to implement library management system using classes and objects

class Student:
    def __init__(self, rollno, name, clas):
        self.rollno = rollno
        self.name = name
        self.clas = clas
        self.issuedbook = None

    def display_info(self):
        print(f"Roll.No: {self.rollno}\nName: {self.name}\nClass: {self.clas}\n Issued Book: {self.issuedbook} ")

class Library:
    def __init__(self):
        self.booksavailable = ["Python Basics", "DBMS", "Networking", "Cryptography", "Devops"]
        self.students = {}

    def add_students(self, rollno, name, clas):
        if rollno not in self.students:
            self.students[rollno] = Student(rollno, name, clas)
        else:
            print("there is already an entry from same rollno")

    def display_books(self):
        if (len(self.booksavailable)) == 0:
            print("No books available at this moment")
        else:
            print("Available Books.")
            for book in self.booksavailable:
                print("-",book)

    def issue_book(self, rollno, book):
        if rollno not in self.students:
            print("student is not regestered yet.")
            return
        student = self.students[rollno]
        if student.issuedbook:
            print(f"this student {student.name} already have an issued book {student.issuedbook}")
            return
        if book in self.booksavailable:
            self.booksavailable.remove(book)
            student.issuedbook = book
            print(f"{book} is issued to {student.name}")
        else:
            print("book not available")

    def return_book(self, rollno, book):
        if rollno not in self.students:
            print("student is not regestered yet.")
            return
        student = self.students[rollno]
        if student.issuedbook:
            self.booksavailable.append(student.issuedbook)
            print(f"book: {student.issuedbook} sucessfully returned by {student.name}")
            student.issuedbook = None
        else:
            print("student has no book to return")
        
    def display_student(self):
        print("Students")
        for students in self.students.values():
            students.display_info()

#--------------------------------main program--------------------------------------------

if __name__ == "__main__":
        library = Library()

        while True:
            print("\n=========== Library Menu ===========")
            print("1. Add Student")
            print("2. Display Books")
            print("3. Issue Book")
            print("4. Return Book")
            print("5. Display Students")
            print("6. Exit")
        
            choise = int(input("\nEnter Here: "))

            if choise == 1:
                rollno = input("roll no: ")
                name = input("name: ")
                clas = input("class: ")
                library.add_students(rollno, name, clas)
            elif choise == 2:
                library.display_books()
            elif choise == 3:
                rollno = input("roll no: ")
                book = input("book name: ")
                library.issue_book(rollno, book)
            elif choise == 4:
                rollno = input("roll no: ")
                book = input("book name: ")
                library.return_book(rollno, book)
            elif choise == 5:
                library.display_student()
            elif choise == 6:
                print("Exiting Library System. Goodbye")
                break
            else:
                print("Invalid choice, Execute again.")
