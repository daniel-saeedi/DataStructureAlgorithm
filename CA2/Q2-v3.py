class Link:
    def __init__( self, start, end ):
        self.start = start
        self.end = end


def count_subarrys(arr,l) :
    count = {}
    links = [None] * l

    for i in sorted(range(0,l),key = lambda i: int(arr[i])):
        link_previous = links[i - 1] if i > 0 else None
        link_next = links[i + 1] if i < (l - 1) else None

        start = link_previous.start if link_previous else i
        end = link_next.end if link_next else i

        links[i] = Link( start, end )

        if link_previous:
            links[link_previous.start].end = end

        if link_next:
            links[link_next.end].start = start
        number = int(arr[i])
        if not number in count.keys() : 
            count[number] = (1 + i - start) * (1 + end - i)
        else :
            count[number] += (1 + i - start) * (1 + end - i)
    
    return count
    

def cin() :
    string = input().strip()
    while string == "" :
        string = input().strip()
    return string

def main() :
    n,q = input().split()
    n = int(n)
    q = int(q)
    numbers = input().split()
    req = []
    while q > 0 :
        q -= 1
        req.append(int(input()))
    # count = count_subarrys(numbers,n)
    # for i in req :
    #     if not i in count.keys() : 
    #         print(0)
    #     else :
    #         print(count[i])

main()