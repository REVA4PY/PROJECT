# TO IDENTIFY WHETHER THE NUMBER IS PRIME OR NOT
num = int(input("Enter the num:"))
if all (num % i != 0 for i in range (2, num)):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# TO IDENTIFY WHETHER THE NUMBER IS EVEN OR ODD
num = int(input("Enter the num:"))
for num in range (1,num+1):
   if num % 2== 0:
       print(num, "is a even number")
   else:
      num % 2 !=0
      print(num, "is a odd number")


# TO IDENTIFY WHETHER THE NUMBER IS EVEN OR NOT IN LIST
list = [12, 45, 58, 64, 69]
for num in list:
   if num % 2 == 0:
      print(num, end=" ")





