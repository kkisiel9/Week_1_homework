import sys
#importing an external module which gives us details about the environment in which python is running
argc = len(sys.argv)
#variable created and assigned, len function to count the number of sys.argv

if argc > 1:
    print('Too many args')
#
else:
    where = 'World'
    print("Hello", where)
# otherwise, the above will be printed, with string concatenation adding the where variable to "hello"

print('Goodbye from ' + sys.argv[0])

print(sys.argv)
      #checking what's stored in the function


