class calc2(calc1):
	def factorial(n):
		if n==0:
			return 1
		else:
			return n*factorial(n-1)
n=int(input("Enter a number: "))
print("The factorial of the entered number is:",math.factorial(n))