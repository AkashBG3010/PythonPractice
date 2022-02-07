num1 = 100
num2 = 200
print("Value of num1 is {} and Value of num2 is {}".format(num1,num2))


num1 = 100
num2 = 200
print("Value of num1 is {val1} and Value of num2 is {val2}".format(val1=num1,val2=num2))


s = "python sample string"
print(s) 
print(id(s))
s= s.capitalize()
print(s)
print(id(s))

print(s.upper())
print(s.lower())
print(s.title())  

print(s.isupper()) 
print(s.islower())
print(s.istitle()) 

s = "HTML,CSS,PYTHON,JAVA,Django"
l = s.split(",")
print(l)

s1 = (" ").join(l)
print(s1)


s2 = "abcd"
s3 = "1234"
s4 = "Python Sapmle string abcd"
table = str.maketrans(s2,s3)
result = s4.translate(table)
print(result)


s5 = "HTML,CSS,PYTHON"
print("PYTHON" in s5)
print(s5.index("PYTHON"))
print(s5.find("python"))
print(s5.rfind("PYTHON"))

s = "   This is Sample String   "
s1 = s.strip(" ")
print(s1)
s2 = s.rstrip(" ")
print(s2)
s3 = s.lstrip(" ")
print(s3)


s = "python"
s1 = s.rjust(20,"+")
print(s1)
s2 = s.ljust(20,"+")
print(s2)


s = "html,css,python,html"
s1 = s.replace("html", "HTML5")
print(s1)


help(str)
print(dir(str))