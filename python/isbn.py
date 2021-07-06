isbn = input("enter isbn")
nodash = "".join(isbn.split("-"))
index = 0
total = 0

for number in nodash:
    if index%2 == 0:
        total += int(number)
        index += 1
    else:
        total += int(number) *3
        index += 1

check_digit = 10 - total % 10
print(isbn + "-" + str(check_digit))

#978-0-306-40615
#978-0-306-40615-7= goal