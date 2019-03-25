'''
play with strings
'''
import string
print ('enter a string')
a = str(input())
print ('ented one more string')
one_more_string = str(input())
print ('entered strings length is ' , len(a) , len(one_more_string))
#print (a[2:6])
#print ('The length of the string entered is' ,len(a+one_more_string))
newstring = a + one_more_string
print ('new string is' , newstring)
split_line=(newstring.split('m'))
print (split_line)
print (split_line[1])
#while split_line != 'n':
 #print ('febin')
 #break
 











