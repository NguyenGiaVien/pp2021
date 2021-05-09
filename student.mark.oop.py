#!/usr/bin/env python
# coding: utf-8

# In[12]:


students = []
courses = []
mark = []
       class students:
        
        def __init__(creative, name, id, DOB):
            creative.name = std_name
            creative.id = std_id
            creative.DOB = std_dob
        def student_name(creative):
            return creative.name
        
        def student_id(creative):
            return creative.id
        
        def student_dob(creative):
            return creative.DOB
        
        def __str__(creative):
            return f" The name of this student is: {creative.name}, The id of this student is :{creative.id}, the dob of this student is :{creative.DOB}"
       
    

        def Student_Info():
    
   
        
        creative.name = input(" Please enter the name of this student :")
        student_id = input("  Please enter the id of this student :")
        student_dob = input(" Please enter the dob of this student :")
        
        
      class courses:
       def __init__(creative, name, id):
            creative.name = crs_name
            creative.id = crs_id
            
       def course_name(creative):
            return creative.name
        
       def course_id(creative):
            return creative.id
        
        
           
       def course_Info():

        
        course_name = input(" Please enter the name of this course :")
        course_id = input(" Please enter the id of this course :")
        
       def __str__(creative):
           return f" The name of this course is: {creative.name}, The id of this course is: {creative.id}"
        
      class Mark:
       def __init__(creative, student, course, mark="")
           creative.student = student
           creative.course = course
           creative.mark = mark
       
       def st_info(creative):
            return creative.student
        
       def crs_info(creative):
            return creative.course
        
       def get_ mark(creative):
            return creative.mark
     
       def __str__(creative):
            return f" Student's name: {creative.student}, with the course: {creative.course},has the score: {creative.mark}"
       
       def input_mark(creative):
           creative.mark = input(f"Please enter the mark of student : {creative.student.student_name()}"
                                 f"in course {creative.course.course_name()}: "))
        
    number_students = int(input("Please enter the number of students : "))
    for i in range(number_students)
    print ("  Please enter the information about this student" + str(i+1) + ":")
        student_name = input(" Student " + str(i+1) + "name is :")
        student_id = input("  Student " + str(i+1) + "id is :")
        student_dob = input(" Student " + str(i+1) + "dob is :")
        students.append({"Student Name" : student_name , "Student ID" : student_id, "Student DOB" : student_dob})
        print()
        
         
     number_courses = int(input("Please enter the number of courses :"))
     for i in range (number_courses):
        print (" Please enter the detail of this course " + str(i+1) + ":")
        course_name = input(" + Course" + str(i+1) + "name is :")
        course_id = input(" + Course" + str(i+1) + "id is :")
        courses.append({"Course Name" : course_name, "Course ID" : course_id})
        print()
        
        
    
        
        
def show_studentInfo():
    print(students)
    print()
    
    show_studentInfo()
    print("please select the ID of a student :")
    student_id = input()
 
def show_courseInfo():
    print(courses)
    print()
     
     
    show_courseInfo()
    print("please select the ID of a course :")
    course_id = input()
 


def mark_Student():
    print()
    mark_each = input("Please enter the mark :")
    mark.append({"Student ID": student_id,"Course ID ": course_id, "Mark": mark_each})
    print()

def action():
    
    while True:
     print("Press '1' : Please input the information for this student ")
     print("Press '2' :  Please input the information for this course ")
     print("Press '3 : Show the information for this student  ")
     print("Press '4' : Show the information for this course ")
     print("Press '5' : Mark ")
     print("Press '0' : To exit ")
    Option = input("please choose your option :")
    if (Option == '1'):
       Student_info()
    elif (Option == '2'):
         course_Info()
    elif (Option == '3'):
         show_studentInfo() 
    elif (Option == '4'):
         show_courseInfo()
    elif (Option == '5'):
         mark_Student()
    elif (Option == '0'):
         print("mission fail,we'll get em next time")
    else:
    break


# In[ ]:




