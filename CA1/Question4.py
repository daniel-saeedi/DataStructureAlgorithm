def sum_calculator(numbers,x) :
    sum_ = 0
    for idx,bit in enumerate(x) : 
        number = numbers[idx]
        if bit == 1: 
            sum_ += number
    return sum_

def main():
    n = int(input())
    numbers = list()
    for x in input().split():
        x = int(x)
        numbers.append(x)
    max = input()
    i = 0
    sum_zero = 0
    zero_list = list()
    numbers = numbers[::-1]
    j = 0
    x_max = [0] * n
    for element in max[::-1]:
        element = int(element)
        if numbers[j] > 0 and element == 0 :
            i += 1
            sum_zero += numbers[j]
            zero_list.append(j)
        elif numbers[j] > 0 and element == 1 :
            if(sum_zero > numbers[j]) :
                for test in zero_list :
                    x_max[test] = 1
                zero_list = list()
                zero_list.append(j)
                i = 1
                sum_zero = numbers[j]
            else : 
                x_max[j] = 1
        elif numbers[j] <= 0 and element == 1:
            if(i > 0) :
                sum_zero = 0
                for test in zero_list :
                    x_max[test] = 1
                zero_list = list()
                i = 0
            x_max[j] = 0
        j += 1
    
    # Printing the results
    t = len(x_max) - 1
    while t >= 0 :
        print(x_max[t], end='')
        t -= 1
    print("\n" + str(sum_calculator(numbers,x_max)))
main()