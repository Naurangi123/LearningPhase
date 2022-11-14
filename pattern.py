"""Square Pattern
*****
*****
*****
*****
*****
"""


for i in range(6):
    for j in range(5):
        print("*",end="")
    print()
    


print("=="*10)

"""
*
**
***
****
*****
******
"""


for i in range(6):
    for j in range(i+1):
        print("*",end="")
    print()

print("=="*10)
"""
*****
****
***
**
*
"""
for i in range(6):
    for j in range(6,i,-1):
        print("*",end="")
    print()

print("=="*10)
"""
*
**
***
****
*****
******
*****
****
***
**
*
"""
for i in range(6):
    for j in range(i+1):
        print("",end="*")
    print()
print("*"*7)
for i in range(6):
    for j in range(6,i,-1):
        print("*",end="")
    print()

print("=="*10)
"""
    *
   **
  ***
 ****
*****
"""
for i in range(6):
    for j in range(i):
        print(end="*")
    print()

print("=="*10)

k=0
for i in range(6):
    for j in range():
        k+=1
        print(j,end="")
    print()

print("=="*10)
