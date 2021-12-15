'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
'''
string = "python"
length = len(string)
for row in range(length):
    for col in range(row+1):
        print(string[row], end=" ")
    print()
    
o/p:
p 
y y 
t t t 
h h h h 
o o o o o 
n n n n n n
'''
'''
string = "python"
length = len(string)
for row in range(length):
    for col in range(row+1):
        print(string[col], end=" ")
    print()
    
o/p:
p 
p y 
p y t 
p y t h 
p y t h o 
p y t h o n 
'''
'''
string = "python"
length = len(string)
for row in range(length):
    for col in range(length-row-1):
        print(" ", end=" ")
    for col in range(row+1):
        print(string[row], end=" ")
    print()
    
o/p:
          p 
        y y 
      t t t 
    h h h h 
  o o o o o 
n n n n n n 
'''
'''
string = "python"
length = len(string)
for row in range(length):
    for col in range(length-row-1):
        print(" ", end=" ")
    for col in range(row+1):
        print(string[col], end=" ")
    print()
    
o/p:
          p 
        p y 
      p y t 
    p y t h 
  p y t h o 
p y t h o n 

'''
'''
string = "python"
length = len(string)
for row in range(length):
    for col in range(length-row-1):
        print(" ", end="")
    for col in range(row+1):
        print(string[row], end=" ")
    print()
    
o/p:
     p 
    y y 
   t t t 
  h h h h 
 o o o o o 
n n n n n n 
'''
'''
string = "python"
length = len(string)
for row in range(length):
    for col in range(length-row-1):
        print(" ", end="")
    for col in range(row+1):
        print(string[col], end=" ")
    print()

o/p:
     p 
    p y 
   p y t 
  p y t h 
 p y t h o 
p y t h o n
'''

'''
string = "python"
length = len(string)
for row in range(length):
    for col in range(row+1):
        print(string[length-row-1], end=" ")
    print()
    
o/p:
n 
o o 
h h h 
t t t t 
y y y y y 
p p p p p p 
'''

'''
string = "python"
length = len(string)
for row in range(length):
    for col in range(length-row):
        print(string[col], end=" ")
    print()
    
o/p:
p y t h o n 
p y t h o 
p y t h 
p y t 
p y 
p
'''

'''
string = "python"
length = len(string)
for row in range(length):
    for col in range(length-row):
        print(string[row], end=" ")
    print()
    
o/p:
p p p p p p 
y y y y y 
t t t t 
h h h 
o o 
n    
'''
'''
string = "python"
length = len(string)
for row in range(length):
    for col in range(row):
        print(" ", end=" ")
    for col in range(length-row):
        print(string[col], end=" ")
    print()
    
o/p:
p y t h o n 
  p y t h o 
    p y t h 
      p y t 
        p y 
          p
'''

'''
string = "python"
length = len(string)
for row in range(length):
    for col in range(row):
        print(" ", end=" ")
    for col in range(length-row):
        print(string[row], end=" ")
    print()

o/p:
p p p p p p 
  y y y y y 
    t t t t 
      h h h 
        o o 
          n 
'''
'''
string = "python"
length = len(string)
for row in range(length):
    for col in range(row):
        print(" ", end="")
    for col in range(length-row):
        print(string[col], end=" ")
    print()
    
o/p:
p y t h o n 
 p y t h o 
  p y t h 
   p y t 
    p y 
     p 
'''
'''
string = "python"
length = len(string)
for row in range(length):
    for col in range(row):
        print(" ", end="")
    for col in range(length-row):
        print(string[row], end=" ")
    print()
    
o/p:
p p p p p p 
 y y y y y 
  t t t t 
   h h h 
    o o 
     n 
'''
'''
string = "python"
length = len(string)
for row in range(length,-1,-1):
    for col in range(row):
        print(" ", end=" ")
    for col in range(length-row):
        print(string[row], end=" ")
    print()
    
o/p:
          n 
        o o 
      h h h 
    t t t t 
  y y y y y 
p p p p p p 
'''

'''
string = "python"
length = len(string)
for row in range(length,-1,-1):
    for col in range(row):
        print(" ", end=" ")
    for col in range(length-row):
        print(string[length-col-1], end=" ")
    print()
    
o/p:
          n 
        n o 
      n o h 
    n o h t 
  n o h t y 
n o h t y p
'''
'''
string = "python"
length = len(string)
for row in range(length-1,-1,-1):
    for col in range(length-row-1):
        print(" ", end=" ")
    for col in range(row+1):
        print(string[row], end=" ")
    print()
    
o/p:
n n n n n n 
  o o o o o 
    h h h h 
      t t t 
        y y 
          p 
'''
'''
string = "python"
length = len(string)
for row in range(length-1,-1,-1):
    for col in range(length-row-1):
        print(" ", end=" ")
    for col in range(row,-1,-1):
        print(string[col], end=" ")
    print()
    
o/p: 
n o h t y p 
  o h t y p 
    h t y p 
      t y p 
        y p 
          p
'''