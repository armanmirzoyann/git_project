phone = input("Phone : ")
num = {
    "1" : "ONE",
    "2" : "TWO",
    "3" : "THREE",
    "4" : "FOUR"
}
output = ""
for i in phone :
    output += num.get(i,"!") + "  "
print(output)
    