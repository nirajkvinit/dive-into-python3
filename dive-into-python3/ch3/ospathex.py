#path = ~/code/python3-study/dive-into-python3/ch3/ospathex.py
import os
print(os.path.join(os.path.expanduser('~'), 'code', 'python3-study', 'dive-into-python3', 'ch3', 'ospathex.py'))
print(os.path.join(os.path.expanduser('~'), 'code', 'python3-study', 'dive-into-python3', 'example', 'humansize.py'))

pathname = os.path.join(os.path.expanduser('~'), 'code/python3-study/dive-into-python3/example', 'humansize.py')
#print(pathname)

'''
Following is an example of a multi-variable assignment.
Here os.path.split(pathname) is returning a tuple of two variables
(containing directory and file name) if the path of a file name
is given to the function. Each variable receives the value of
the corresponding element of the returned tuple.
'''
(dirname, filename) = os.path.split(pathname)
print(dirname, ', ', filename)
(shortname, extension) = os.path.splitext(filename)
print(shortname, ', ', extension)

'''
os.path also contains the os.path.splitext() function, which splits a filename and returns a tuple
containing the filename and the file extension. You use the same technique to assign each of them to
separate variables.
'''
