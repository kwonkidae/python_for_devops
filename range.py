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
