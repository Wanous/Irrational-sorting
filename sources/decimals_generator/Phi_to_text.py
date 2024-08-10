from mpmath import mp

mp.dps = 1000010                   #number of decimals
phi = (1 + mp.sqrt(5)) / 2
phi_str = str(phi)                 #float to str
phi_decimals = phi_str[2:1000002]  # get the 1 000 000 decimals

#creation of the file
with open('phi_decimals.txt', 'w') as f:
    f.write(phi_decimals)

print("Done whith the creation of the file 'phi_decimals.txt'.")

