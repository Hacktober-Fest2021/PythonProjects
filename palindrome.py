n = int(input("Number: "))
if (n == int(str(n)[::-1])):
	print("Palindrome")
else:
	print("Not a palindrome")