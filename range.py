#!/usr/bin/env python3
p = print
r = range(10)
print(list(r))

i = 45
if i == 45:
    print('i is 45')

i = 35
if i == 45:
    print('1 is 45')
elif i == 35:
    print('i is 35')

cat = 'spot'
if 's' in cat:
    print("Found an 's in a cat")

for i in range(10):
    x = i * 2
    print(x)


for i in range(6):
    if i == 3:
        continue
    print(i)

count = 0
while count < 3:
    print(f"The count is {count}")
    count += 1

count = 0
while True:
    print(f"The count is {count}")
    if count > 5:
        break
    count += 1

thinkers = ['Plato', 'PlayDo', 'Gumby']
while True:
    try:
        thinker = thinkers.pop()
        print(thinker)
    except IndexError as e:
        print("We tried to pop too many thinkers")
        print(e)
        break

# object


class FancyCar():
    wheels = 4

    def driveFast(self):
        print("Driving so fase")


p(type(FancyCar))

my_car = FancyCar()
p(type(my_car))

p(my_car.wheels)
my_car.driveFast()

p(2 in [1, 2, 3])
p('a' not in 'cat')
p(10 in range(12))
p(10 not in range(2, 4))

my_sequence = 'Bill Cheatham'
p(my_sequence[0])
p(my_sequence[1])
p(my_sequence[2])

p(my_sequence.index('C'))
p(my_sequence.index('a'))
p(my_sequence.index('a', 9, 12))
p(my_sequence[11])
p(my_sequence[1:10:2])

pies = ['cherry', 'apple']
desserts = ['cookies', 'paste']

desserts.extend(pies)
p(desserts)
p(pies)

squares = []
for i in range(10):
    squared = i*i
    squares.append(squared)

p(squares)
p([i*i for i in range(10)])
p([i*i for i in range(10) if i % 2 == 0])

my_list = list()
p(str(my_list))

multi_line = """This is a
multi-line string,
which includes linebreaks.
"""

print(multi_line)

name = "Bill MonRoe"
p(name.swapcase())
