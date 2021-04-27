def cin() :
    string = input().strip()
    while string == "" :
         string = input().strip()
    return string

def read_input() :
    n,k = cin().split()
    n = int(n)
    k = int(k)
    bags = list()
    bags_unsplitted = cin()
    biggest_bag = 0
    for x in bags_unsplitted.split():
        x = int(x)
        bags.append(x)
        if biggest_bag < x :
            biggest_bag = x
    return n,k,bags,biggest_bag

def find_gcd_max(n,k,bags,biggest_bag) :
    gcd_max = 1
    add_to_bags = [0]*n
    for gcd in range(2,biggest_bag+k+1) :
        for idx,bag in enumerate(bags) :
            remainder = bag%gcd
            x = 0
            if remainder != 0 : 
                x = gcd - remainder
            add_to_bags[idx] = x
        if sum(add_to_bags) <= k :
            gcd_max = gcd
    return gcd_max

def main() :
    n,k,bags,biggest_bag = read_input()
    gcd_max = find_gcd_max(n,k,bags,biggest_bag)
    print(gcd_max) 

main()