from sys import argv
script, newline = argv
print ('your file is' , newline)
txt = open (newline)
print (txt.read())
print ('enter new line')
febin = input()
print ("I'm going to write these to the file.")
txt = open (newline, 'a')
txt.write(febin)