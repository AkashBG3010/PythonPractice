num1 = 100;
print(id(num1));
print(type(num1));

num2 = 15.25;
print(id(num2));
print(type(num2));

num3 = 100;
print(id(num3));
num3 = 150;
print(id(num3));

#string-----------------------
constant = "Python";
print(constant);
print(id(constant));
print(type(constant));
constant = "Java";
print(constant);
print(id(constant));
print(type(constant));

doubleString = "'Python' is a sample string"
print(doubleString);

#list---------------------------
list = [1,2,3,90,100,1000,"Python", "Django"]
print(list);
print(id(list));
list.append(10000);
print(list);
print(id(list));

#tuple------------------------
tuple = (10,20,30);
print(tuple);

#dictonary---------------------
dictonary = {"name":"Abc", "email":"abc@gmail.com", "contact":"1234567890"};
print(dictonary);

#set-------------------------
set = {1, 2, 3, 4, 5}
print(set);

#boolean---------------------
boolean : [True, False]

#complex datatypes---------------
comp : 4 + 3j;

#help-------------------
help(str)