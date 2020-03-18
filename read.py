'''

------------------- READ FILES ---------

'''
# split lines removes "\n"
# at the end of every line 
with open("a_solar.txt", 'rb') as f:
    f_contents  = f.read().splitlines()
    print(f_contents)

# example access an element 
# decode utf-8 is important 
# this is why : b"###"
    
f_contents[0].decode("utf-8")