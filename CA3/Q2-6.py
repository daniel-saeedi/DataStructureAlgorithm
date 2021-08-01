class Node:
    def __init__(self, data):
        self.data = data
        # dictionary from child_data to child_node
        self.children = dict()
        self.word_end_here = False

    @staticmethod
    def print_graph(cur_node, cur_word = ''):
        if cur_node.word_end_here:
            print(cur_word)
        for data, child in cur_node.children.items():
            Node.print_graph(child, cur_word + data)


def build_graph(strings):
    root = Node(None)
    for str_ in strings:
        parent = root
        for char in str_:
            if char in parent.children.keys():
                cur_node = parent.children[char]
            else:    
                cur_node = Node(char)
                parent.children[char] = cur_node
            parent = cur_node
        cur_node.word_end_here = True
    return root


def is_similar_recursive(cur_node, query, index, skipped_node=False):
    if index == len(query):
        if skipped_node and cur_node.word_end_here:
            return True
        return False
    char = query[index]
    if char in cur_node.children.keys():
        if is_similar(cur_node.children[char], query, index+1, skipped_node):
            return True
    if skipped_node is False:
        for child in cur_node.children.values():
            if char != child.data:  # skipping the already traversed child
                if is_similar(child, query, index+1, skipped_node=True):
                    return True
    return False


def is_similar(cur_node, query, index, skipped_node=False):
    stack = [(cur_node, index, skipped_node)]  # root
    while len(stack):
        cur_node, index, skipped_node = stack.pop()
        if index == len(query):
            if skipped_node and cur_node.word_end_here:
                return True
            continue
        char = query[index]
        if char in cur_node.children.keys():
            stack.append((cur_node.children[char], index+1, skipped_node))
        if skipped_node is False:
            for child in cur_node.children.values():
                if char != child.data:  # skipping the already traversed child
                    stack.append((child, index+1, True))
    return False


def similarity_checker(strings, queries):
    root = build_graph(strings)
    resutls = []
    # Node.print_graph(root)
    for query in queries:
        if is_similar(root, query, 0):
            resutls.append('YES')
        else: 
            resutls.append('NO')
    return resutls


def run(inputs):
    n, q = map(int, inputs[0].strip().split())
    strings, queries = [], []
    for i in range(1, n+1):
        strings.append(inputs[i])
    for i in range(n+1, len(inputs)):
        queries.append(inputs[i])
    
    return similarity_checker(strings, queries)

def run2() :
    n, q = input().split()
    n = int(n)
    q = int(q)
    strings = []
    for i in range(0, n):
        strings.append(input())

    root = build_graph(strings)

    for i in range(0, q):
        if is_similar(root, input(), 0):
            print('YES')
        else: 
            print('NO')

def main():
    # inputs = [input()]
    # n, q = map(int, inputs[0].strip().split())
    # for _ in range(n+q):
    #     inputs.append(input())
    # print('\n'.join(run(inputs)))
    run2()

main()
# inputs = [
#     "5 6",
#     "ab",
#     "cacab",
#     "cbabc",
#     "acc",
#     "cacab",
#
#     "abc",
#     "aa",
#     "acbca",
#     "cb",
#     "a", # NO
#     "",
#     "cac",
#     "ccc",
#     "aacab",
#     "cbaac",
#     "cbaba",
#     "aaa",
#
#     "ab",
#     "cacab",
#     "cbabc",
#     "acc",
#     "cacab",
#
#     "cacabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
#
# ]
# print('\n'.join(run(inputs)))
# assert run(inputs) == ['YES', 'YES', 'NO', 'YES', 'NO', 'NO',
#                        'NO', 'YES', 'YES', 'YES', 'YES', 'NO',
#                        'NO', 'NO', 'NO', 'NO', 'NO', 'NO']
