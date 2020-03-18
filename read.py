'''
------------------- READ FILES ---------

output files:
    
        width       : integer
        height      : integer
        temp_map    : list with dimensions  --> height * width 
        f_contents  : i-index is the i-th line of our file ( starts from 0 )
'''
# split lines removes "\n"
# at the end of every line 
with open("a_solar.txt", 'rb') as f:
    f_contents  = f.read().splitlines()
    print(f_contents)

# example access an element 
# decode utf-8 is important 
# this is why : b"###"
    
dimensions  = ( f_contents[0].decode("utf-8") ).split()

# index in Python starts from zero 
# our data is in a list

width      = int ( dimensions[0] ) ;
height     = int ( dimensions[1] ) ;

our_map = f_contents[1:(height+1)]