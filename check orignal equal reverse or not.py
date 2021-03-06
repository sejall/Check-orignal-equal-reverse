# Python Program - Check Original Equals Reverse or Not

print("Enter 'x' for exit.");
num = input("Enter any number: ");
if num == 'x':
    exit();
try:
    number = int(num);
except ValueError:
    print("Please, enter a number...");
else:
    orig = number;
    rev = 0;
    while number > 0:
    	rev = (rev*10) + number%10;
    	number //= 10;
    if orig == rev:
    	print("Original number is equal to its reverse.");
    else:
    	print("Original number is not equal to its reverse.");
