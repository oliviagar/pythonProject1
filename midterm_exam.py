#Question 1
a = 16
a = a // 2
print(a**2)
a = a + 11
print(a+1)
a = a - 3

#Question 2
print(2+3*6/2)

#Question 3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

#Question 4
def palindrome (word):
    if word == word[::-1]:
        return True
    else:
        return False
print(palindrome("7489617719749244646336564429479177169847"))

#Question 6
mut_list = [1, 2, 3, 4, 5]
mut_list[3] = 19
mut_list.append(6)
mut_list.remove(1)
print("Mut List:", mut_list)

immut_string = "exam"
second_string = immut_string + "time"
print("First String:", immut_string)
print("Second String:", second_string)

#Question 7
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        random_numbers[i] = None
    else:
        random_numbers[i] = "XX"
random_numbers = [num for num in random_numbers if num is not None]
random_numbers

#Question 8
s= "https://news.yahoo.com/confused-michigan-primary-convention-not-122822846.html"
start = 0
while True:
    start = s.find("http://", start)
    if start == -1:
        break
    end = s.find (" ", start)
    if end == -1:
        print (s[start:])
        break
    print (s[start: end])
    start = end




