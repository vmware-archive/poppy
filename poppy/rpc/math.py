async def fib(hub, num=10):
    num = int(num)
    if num < 2:
        return num
    prev = 0
    curr = 1
    i = 1
    while i < num:
        prev, curr = curr, prev + curr
        i += 1
    return curr


async def triple(hub, num=10):
    num = int(num)
    return num * 3
