print("Welcome to average grade calculater ")
maths = int(input(" Please imput your Maths mark : "))
physics = int(input(" Please imput your Physics mark : "))
chemistry = int(input(" Please imput your Chemistry mark : "))
average =((maths+physics+chemistry)/3)
print ("your percentage is", " ",average,"%")

grade= "Fail"

if average < 40:
    grade = "Fail"
elif average >= 40 and average <60:
    grade = "C"
elif average >=60 and average <80:
    grade = "B"
else:
    grade = "A"

print("your final grade is",grade)