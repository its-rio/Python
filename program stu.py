#wap to display the grade of the student as per following conditions if the age >90 and age<=90 grade M
#age is >=60 age<=89 then First
#age>=50 and age<=59 then second
#age>=35 and age<=40 then third
#age<35 then fail  need to read input from user and impliment with class

class StudentResult:
    def _init_(self):
        self.__roll=0
        self.__name=""
        self.__marks=[]
        self.__total=0
        self.__per=0
        self.__grade=""
        self.__result=""
 h
    def studentData(self):
        self.__roll=int(input("Enter student roll: "))
        self.__name=input("Enter student name: ")
        print("Enter marks of five subjects: ")
        for i in range(5):
            self.__marks.append(int(input("Subject "+str(i+1)+": ")))
			
    def calTotalMarks(self):
        for x in self.__marks:
            self.__total+=x
			
    def calPercentage(self):
        self.__per=self.__total/5
		
    def calGrade(self):
        if self.__per>=85:
            self.__grade="A+"
        elif self.__per>=75:
            self.__grade="A"
        elif self.__per>=65:
            self.__grade="B"
        elif self.__per>=55:
            self.__grade="C"
        elif self.__per>=50:
            self.__grade="D"
        else:
            self.__grade="F"
			
    def getResult(self):
        count=0
        for x in self.__marks:
            if x>=50:
                count+=1
        if count==5:
            self.__result="PASS"
        elif count>=3:
            self.__result="COMP."
        else:
            self.__result="FAIL"
			
    def showStudent(self):
        self.studentData()
        self.calTotalMarks()
        self.calPercentage()
        self.calGrade()
        self.getResult()
        print(self.__roll,"\t\t",self.__name,"\t\t",self.__total,"\t\t",self.__per,"\t\t",self.__grade,"\t\t",self.__result)


def main():
    # object is created for StudentResult
    s=StudentResult()
    s.showStudent()

if _name=="__main_":
    main()
