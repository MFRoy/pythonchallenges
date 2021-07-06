print("Welcome to average grade calculater ")
maths = int(input(" Please imput your Maths mark : "))
physics = int(input(" Please imput your Physics mark : "))
chemistry = int(input(" Please imput your Chemistry mark : "))
def grade_calc(maths,physics,chemistry):
    average =((maths+physics+chemistry)/3)

    grade= "Fail"

    if average < 40:
        grade = "Fail"
    elif average >= 40 and average <60:
        grade = "C"
    elif average >=60 and average <80:
        grade = "B"
    else:
        grade = "A"
    return(grade,average)

print ("your grade and percentage is", " ",grade_calc(maths,physics,chemistry),"%")
