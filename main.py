num = 40 #Enter mean
numl = [55, 51, 12, 20, 50, 25, 54, 20, 51, 47, 37, 58] #Enter list of values
x = 0

def get_mean(listx):
	total = sum(listx)
	mean = total / len(listx)
	return mean

def distance_between(num1, num2):
	if num1 > num2:
		return num1 - num2
	else:
		return num2 - num1

def main():
	global x
	while x < len(numl):
		ans = distance_between(num, numl[x])
		numl[x] = ans
		x = x + 1
		
	print(get_mean(numl))

if __name__ == "__main__":
	main()		 
