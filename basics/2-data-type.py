# String
mystring = "Hello World"
print(mystring[0])    #print H
print(mystring[-1])   #print d  --> Reverse(0 -> -Infinity).
print(mystring[2:])   #até o fim
print(mystring[:2])   #começo até o index 1, não inclui o 2 
print(mystring[2:5])
print(mystring[::])
print(mystring[::2])  #pulando de dois em dois
print(mystring[::-1]) #inverte

#Properties and Methods
name = "Sam"
last_letters = name[1:]

print('P' + last_letters)
print(mystring + " it is beautiful outside!")

name = 'P' + last_letters

letter = 'z'
print(letter * 10)

