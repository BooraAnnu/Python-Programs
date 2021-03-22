
num= int(input("Enter a number : "))
for i in range(1,11):
    print(num*i)
    
    file= open("myTable.txt",'a')
    file.write(str(num*i))
    file.close()