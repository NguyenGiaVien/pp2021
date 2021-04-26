#!/usr/bin/env python
# coding: utf-8

# In[17]:


def get_number_students():
    number_student = int(input("Enter the number of students: "))
    return number_students

     
    


# # def student_information():
#     student_id = input('please enter the student id: ')
#     student_name = input("please enter the student name: ")
#     student_dob = input("please enter the student dob: ")
#     
#     the_basic_info = {'id': student_id, 'name': student_name, 'dob': student_dob}
#     print (id, name, dob)
# student_information()
#     

# In[3]:


student=[]
def add_student():
    name = input("enter name: ")
    id = input("enter id: ")
    dob = input("enter dob: ")
    s = {'id':id,'name': name, 'dob':dob}
    student.append(s)
add_student()
print(student)
    


# In[14]:


course=[]
def course_information():
    Courses = int(input("please enter the number of course: "))
    courseID = input("please enter the course id :")
    courseName = input("please enter the course name :")
    c = {'Courses':Courses,'courseID':courseID,'courseName':courseName}
    course.append(c)
course_information()
print(course) 

  


# In[14]:





# In[18]:


def mark_of_eachCourse():
    
    print("The mark for this course is : ",mark)
courseID = input("please enter the course id : ")
courseName = input("please enter the course name : ")
studentName = input("please enter the student name : ")
mark = input("please enter the course mark : ")
mark_of_eachCourse()

 

    
    
    


# In[ ]:




