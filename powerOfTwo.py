# Finding if a number is a power of 2 or not using bitwise operator.
# When a number which is a power of 2 is only one bit set and when we sutract 1 out of that all unset bits become set and set becomes unset. 
# In this case if we do and operation over number ( which is a power of 2 ) and number -1 , result is zero. 


x = int(input())

def power(x):
    return (x and (not(x&(x-1))))

if power(x):
  print("{} is a power of 2".format(x))
else:
  print("{} is not a power of 2".format(x))

