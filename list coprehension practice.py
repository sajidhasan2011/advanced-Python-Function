num = int(input("Enter a number :"))

list = []

for i in range(0,num + 1):
  list.append(i)
print(list)

oddnum =[x for x in list if x % 2 != 0]
print("Odd numbers are :",oddnum)

fruits = ["apple","banana","cherry","kiwi","mango"]

upperCasedfruit = []

for i in range(0,len(fruits)):
  upperCasedfruit.append(fruits[i].capitalize())


print(f"The Updated list is {upperCasedfruit}")