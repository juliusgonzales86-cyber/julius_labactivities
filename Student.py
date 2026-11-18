class Student:
    def __init__(self, name, studentId, grade):
        self.__name = name
        self.__studentId = studentId
        self.__grade = grade

    def getName(self):
        return self.__name

    def getStudentId(self):
        return self.__studentId

    def getGrade(self):
        return self.__grade

    def setName(self, name):
        self.__name = name

    def setStudentId(self, studentId):
        self.__studentId = studentId

    def setGrade(self, grade):
        self.__grade = grade

    def displayInfo(self):
        print("Name:", self.__name,"|","Student ID:", self.__studentId,"|","Grade:", self.__grade)

student1 = Student("Julius", "251-0785-1", 91)
student2 = Student("Garcia ", "251-0785-2", 87)

student1.displayInfo()
student2.displayInfo()
