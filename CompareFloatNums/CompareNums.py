
class NumStruct():
    def __init__(self, str1, str2):
        self.num1 = NumStruct.parse(str1)
        self.num2 = NumStruct.parse(str2)
        self.result = ""

    # Take in 2 floating point numbers in form of string and convert
    # compare them and return if first number is bigger, smaller or equal
    def compareNums(self) -> float:
        if self.num1 > self.num2:
            self.result =  "Bigger"
        if self.num1 < self.num2:
            self.result = "Smaller"
        if self.num1 == self.num2:
            self.result = "Same"
        return self.result

    def parse(string):
        return float(string) 

#Driver code
output = [] #Initialize o/p list
case = 0
# Read input line by line and print o/p at a time in the end
# Start reading a i/p line
print("Enter Input Line By Line:")
while True:
    line = input()
    if line:
        str1, str2 = line.split()
        obj = NumStruct(str1, str2)
        result = obj.compareNums()
        output.append(result)
    else:
        break    

# For each input line print the output
print("Output ")
for result in output:
    case += 1
    print("Case ",case,":",result)
