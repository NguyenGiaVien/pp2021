#!/usr/bin/env python
# coding: utf-8

# In[63]:


students = []
courses = []
mark = []

def get_studentInfo():
    number_students = int(input("Please enter the number of students : "))
    for i in range (number_students):
        print ("  Please enter the information about this student" + str(i+1) + ":")
        student_name = input(" Student " + str(i+1) + "name is :")
        student_id = input("  Student " + str(i+1) + "id is :")
        student_dob = input(" Student " + str(i+1) + "dob is :")
        students.append({"Student Name" : student_name , "Student ID" : student_id, "Student DOB" : student_dob})
        print()
        

def course_Info():
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
    if Option == 1:
       get_studentInfo()
    elif Option == 2:
         course_Info()
    elif Option == 3:
         show_studentInfo() 
    elif Option == 4:
         show_courseInfo()
    elif Option == 5:
         mark_Student()
    elif Option == 6:
         print("mission fail,we'll get em next time")
    else:
    break
     
 
        
        
        
        
    
   
    
    
    


    


# In[ ]:





# In[ ]:




