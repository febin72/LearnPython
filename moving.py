from sys import argv
from os.path import exists
import pandas
script , source_file , dest_file = argv
print ('copying to %s from %s' %(dest_file,source_file))
open_file = open(source_file)
orig_file = open_file.read()
#print (orig_file)
final_file = open (dest_file , 'w')
final_file.write(orig_file)



