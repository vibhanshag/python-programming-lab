a=input("enter the text to append\n")

f=open("sample.txt","r")
print('\nbefore appending',f.read())
f.close()

f=open("sample.txt",'a')
f.write(a)
f.close()

f=open("sample.txt","r")
print('after appending',f.read())
f.close()
