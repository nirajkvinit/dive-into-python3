import sys, os, time
#load sibline directory into memory for importing a python file
sys.path.append(os.path.abspath('../example'))
import humansize

# get path of current direcoty by getting the path of current executing file
current_dir = os.path.dirname(os.path.abspath(__file__))
# get parent directory of current directory and join that
# with the name of sibling directory (example directory) to get its path
example_directory = os.path.join( os.path.dirname( current_dir ), 'example' )
#print(os.path.join(os.path.expanduser('~'), 'code', 'python3-study', 'dive-into-python3', 'example', 'humansize.py'))

#get path of a file from the sibling directory
humansize_file = os.path.join(example_directory, 'humansize.py')

'''
Following is an example of a multi-variable assignment.
Here os.path.split(pathname) is returning a tuple of two variables
(containing directory and file name) if the path of a file name
is given to the function. Each variable receives the value of
the corresponding element of the returned tuple.
'''
(dirname, filename) = os.path.split(humansize_file)
print(dirname, ', ', filename)
(shortname, extension) = os.path.splitext(filename)
print(shortname, ', ', extension)

'''
os.path also contains the os.path.splitext() function, which splits a filename and returns a tuple
containing the filename and the file extension. You use the same technique to assign each of them to
separate variables.
'''
print('-------Printing Metadata--------')

metadata = os.stat(humansize_file)
print(metadata.st_mtime)
print(time.localtime(metadata.st_mtime))
print(metadata.st_size)
print(humansize.approximate_size(metadata.st_size))
print(humansize.approximate_size(os.stat(__file__).st_size)) # current file size
