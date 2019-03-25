from sys import argv
script , file_name = argv
print ('script and file names are' , script, '&' , file_name ,  'respectively')
txt=open(file_name)
print ('File contains' , txt.read())
print ('Enter to update the file' , file_name)
txt1= str(input())
NEWLINE = open(file_name , 'w')
NEWLINE.write(txt1)



#febin = str(input())
#print ("I'm going to write these to the file.")
#txt = open (newline, 'w')
#txt.write(febin)
#txt.close
#print (txt.read())








