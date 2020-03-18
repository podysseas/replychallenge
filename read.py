'''

------------------- READ FILES ---------


'''

# split lines removes "\n"
# at the end of every line 
with open("a_solar.txt", 'rb') as f:
    f_contents  = f.read().splitlines()
    print(f_contents)


