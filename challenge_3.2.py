class student:
  def __init__(self,name,rollno,cgba):
    self.name=name
    self.rollno=rollno
    self.cgba=cgba

  def sort_students(student_list):

    sorted_student=sorted(student_list,key=lambda student:student.cgba,reverse=True)
    return sorted_student


students=[student("Arivelan","1000",9.2),
         student("vignesh","1001",7.2),
         student("Mathan","1002",8.9),
         student("Durai","1003",7.5)]

sorted_students=student.sort_students(students)
for student in sorted_students:
  print("Name:{},Roll Number:{},CGBA:{}".format(student.name,student.rollno,student.cgba))

 