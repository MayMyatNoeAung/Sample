List - []


word = 'Programming'


  p  r  o  g  r  a  m  m  i  n  g
  0  1  2  3  4  5  6  7  8  9  10
-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1









word[0]
word[-2]
word[2:5]
word[:5]
word[3:]
word[:7] + word[3:]
word[5:-3]

len(word)

# Len = Length

square = 'Square'
len(square)
len(word) + len(square)

cube = [10, 20, 30, 45, 50]
cube
cube[3] = 40
cube
cube[5] = 60 #error out of range
cube.append(60)
cube.append(4+10+20+36)
cube
cube.reverse()
cube
cube.sort()
cube
cube.remove()
cube
cube.pop()
cube

cube1 = [10, 20, 30, 45, 50]
cube2 = [1, 2, 3, 4, 5]
cube1.extend(cube2)

del cube1[3]
del cube1[1:3]
del cube1[:]

programA = ['A','B','C','D','E']
programB = ['a','b','c','d','e']
ProgramC = programA + programB
ProgramC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
ProgramD = [1, 2, 3, 4, 5]
ProgramC = ProgramC + ProgramD
ProgramC[9:] = []
ProgramC[5:9] = ProgramD
ProgramC

len(ProgramC)

a = [10, 20, 30, 40, 50]
b = [60, 70, 80, 90, 100]
c = [100, 110, 120, 130, 140, 150]
x = [a, b, c]

x[0:2][1]
x[1:2][0]

x[0][]
x[][3]
x[1][2]
x[1:2][1:2]
x[][]
