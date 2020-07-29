say = "Hello World!"
print(say)

profile = {'name' : 'kumaaaa1', 'year' : '26' , 'country' : 'Japan'}
print("hey! My name is " + profile['name'] + "." , end = "")
print(" and I'm " + profile['year'] + 'years old.' , end ="")
print("I'm from " + profile['country'] + ".")

favorite_number = [3 , 55 , 13, 777, 1964]
print("My favorite numbers is.." + str(favorite_number) , end="")
favorite_number.sort()
print("and If I rearrange them," + str(favorite_number) , end="")
favorite_number.reverse()
print("The largst number among them," + str(favorite_number[0]))

if 5 > 2:
	print("5 is indeed grater than 2")
else:
	print("5 is not grater than 2")

name = "Ol"
if name == "Ola":
	print("hey Ola!")
elif name == "Sonja":
	print("hey Sonja!")
else:
	print("hey anonymous!")

speed = 100

if speed <= 20:
	print("too late.")
elif speed <= 40:
	print("so so.")
elif speed <= 60:
	print("good speed.")
elif speed <= 80:
	print("little early.")
else:
	print("too early..!!")


# オリジナル関数を作る

def hello():

	myName = "kumaaaa1"
	print("Nice to meet you!")
	print("My name is " + myName)


hello()

def hello(name):
	if name == "kumaaaa1":
		print("Hi kumaaaa1.")
	elif name == "Sonja":
		print("Hi Sonja.")
	else:
		print("Hi anonymous!")

hello("Unknwon")

def hello(name):
	print("Hi " + name + "!")

hello("Yourname")

girls = ["hanako" , "yuki" , "miya", "saori"]

for name in girls:
	hello(name)
	print("Next girl")

for i in range(2, 5):
	print(i)