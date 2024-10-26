# 8-16. Imports

# Using a program I wrote that has one function in it.
# Store that function in a separate file.
'''printing_functions.py'''

# Import the function into my main program file, and call the function.
import printing_functions
from printing_functions import print_function
from printing_functions import print_function as pf
import printing_functions as pfs
from printing_functions import *