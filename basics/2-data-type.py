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

something = 'Hi, everything is okay with u?'
print(something.upper())
print(something.lower())
print(something.split())
print(something.split('i'))

print('Hi {} everything is {}?'.format('Erick', 'okay'))
print('Hi {1} everything is {1}?'.format('Erick', 'okay'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

age = 3
name = 'Sam'
print(f'{name} is {age} years old')

# lists 
lists = ['H', 1, "Hello"]
print(dir(lists))
lists.append(3)
help(lists.remove())
lists.remove(3)

# tuples
tuples = ('Hello', 3, 4.5)
print(tuples[-1])


# dictionaries
dictionaries = { "Name": "John", "Surname": "Smith" }
