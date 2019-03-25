'''
Learn listsw in python - list is a collection like Arrays in other languages
'''
import math
print ('enter student name')
student_name = str(input())
marks = [10,20,90,90]
print ('Febin scored' ,marks[0], 'in maths out of 100')
print ('Febin scored' , marks[1], 'in science out of 100')
print ('Febin scored' , marks[2], 'in language out of 100')
print ('Febin scored' , marks[3], 'in chemistry out of 100')
Total_marks = (marks[0] + marks[1] + marks[2] + marks[3])
#Total_marks = math.fsum(marks[0,1,2,3])
print (Total_marks)
Percentage = (Total_marks/400*100)
print ('Total Percentage of' , student_name , 'is' , Percentage)
if (Percentage>=90):
 print (student_name , 'has scored distiontion' )
elif (Percentage >=50 and Percentage<90):
 print (student_name , 'has scored 1st class') 
else:
 print(student_name , 'has to rewrite the exam')
 




