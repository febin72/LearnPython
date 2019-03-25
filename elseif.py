'''
how to use else if
'''
print ('enter how many backups')
Number_backups = int(input())
print ('enter success backups')
success_backups = int(input())
if (Number_backups == success_backups):
  print ('backups percentage is %100')
elif (success_backups/Number_backups*100>=50):
  print ('backup status is green')
else:
 print ('backup status is red')