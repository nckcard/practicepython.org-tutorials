num_values = int(input("How many Fibonacci numbers do you want? "))

def generateFibonacci(input_num):
    output = []

    for i in range(1,input_num):
        #print(i)
        #print(output)
        if i<3:
            output.append(1)
        else:
            output.append(output[i-3] + output[i-2])

    return output

output_values = generateFibonacci(num_values)
print(output_values)
