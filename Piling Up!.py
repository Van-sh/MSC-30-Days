T = int(input())
for _ in range(T):
    N = int(input())
    blocks = list(map(int, input().split()))
    vertical_stack = []
    
    if blocks[0] > blocks[-1]:
        vertical_stack.append(blocks.pop(0))
    else:
        vertical_stack.append(blocks.pop(-1))
    
    while blocks != []:
        if blocks[0] >= blocks[-1] and blocks[0] <= vertical_stack[-1]:
            vertical_stack.append(blocks.pop(0))
        elif blocks[0] < blocks[-1] and blocks[-1] <= vertical_stack[-1]:
            vertical_stack.append(blocks.pop(-1))
        else:
            print('No')
            break
        
    else:
        print('Yes')
