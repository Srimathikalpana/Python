try:
   a=int(input('enter the value'))
except ValueError as e:
   print('value error:',e)
   raise KeyError('that is value')
else:
   print('value is:',a)
finally:                           #always run whether the output is correct or an error
   print('hello the words')