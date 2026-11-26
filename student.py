class  StudentDatabase :
    student_list = []

    @classmethod
    def add_student(self , student) :
        self.student_list.append(student)

    @classmethod
    def find_student(c , id) :
        for student in c.student_list :
            if student.get_id() == int(id) :
                return student
        return None

class Student :
    def __init__(self ,id , name ,  department):
        self.__id = id
        self.__name = name
        self.__department = department
        self.__enrolled = False

        StudentDatabase.add_student(self)

    def enroll_student(self) :
        if not self.__enrolled :
            self.__enrolled = True
            print("Student is enrolled!!")
        else :
            print("student is already enrolled")


    def drop_student(self) :
        if self.__enrolled :
            self.__enrolled = False
            print("Student dropped out")
        else :
            print("Student is not enrolle")

    def view_student_info(self) :
        print("Student name : " , self.__name)
        print("Student id : " , self.__id)
        print("Department : " , self.__department)
        if self.__enrolled :
            print("Enrollment status : Enrolled")
        else :
            print("Enrollment status : Not enrolled")

    def get_id(self) :
        return self.__id
    
s1 = Student(101, "Rahim", "CSE")
s2 = Student(102, "Karim", "EEE")
s3 = Student(103, "Nila", "ECE")

while True :
    print("1.View all students")
    print("2.Enroll student")
    print("3.Drop student")
    print("4.Exit")

    choice = input("Enter choice : ")
    if choice == "1" :
        for student in StudentDatabase.student_list:
            student.view_student_info()

    elif choice == "2" :
        id = int(input("enter id :"))
        student = StudentDatabase.find_student(id)
        if student :
            student.enroll_student()
        else :
            print("Enter correct id")

    elif choice == "3" :
        id = int(input("Enter id : "))
        student = StudentDatabase.find_student(id)
        if student :
            student.drop_student()
        else :
            print("Enter correct id")

    elif choice == "4" :
        break

    else :
        print("Invalid choice")

