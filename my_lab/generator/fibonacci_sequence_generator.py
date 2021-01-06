def fibonacci_gen():
    trailing, lead = 0, 1
    while True:
        yield lead
        trailing, lead = lead, trailing + lead

fib = fibonacci_gen()
fib_list = []
for _ in range(10):
    fib_list.append(fib.__next__())

print(fib_list)
# ==> [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    
    
    
