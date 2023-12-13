# stack = data structure, insertion + deletion at the top
N = 10
stack = [0] * N
size = 0


def push(x):
    global size
    stack[size] = x
    size += 1


def pop():
    global size
    size -= 1
    return stack[size]


# queue = data structure, insertion at the back + deletion at the top
# eg: circular buffer
queue = [0] * N
head, tail = 0, 0


def push_q(x):
    global tail
    tail = (tail + 1) % N
    queue[tail] = x


def pop_q():
    global head
    head = (head + 1) % N
    return queue[head]


def size_q():
    return (tail - head + N) % N


def empty():
    return head == tail


# queue in a store, 0=new client, 1=serving
# [1,0,1,1] -> -2 -> there should have been 2 clients (2x0) before the array
# [0,1,0,0] -> 2 -> there should have been 0 clients before the array
def grocery_store(A):
    n = len(A)
    size = 0
    for i in range(n):
        # new client
        if A[i] == 0:
            size += 1
        # leaving client
        else:
            size -= 1

    if size > 0:
        return 0
    else:
        return -size
