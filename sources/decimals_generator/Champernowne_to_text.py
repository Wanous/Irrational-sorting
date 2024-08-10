def suite_Champernowne(n):
    C10 = ''
    for decimale in range(1,n):
        C10 +=str(decimale)
    return C10

content = suite_Champernowne(250000) # number where to stop

#creation of the file
with open('Champernowne.txt', 'w') as file:
        file.write(content)

print("Done whith the creation of the file 'Champernowne.txt'.")