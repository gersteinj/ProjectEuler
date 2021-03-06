'''
Each new term in the Fibonacci sequence is generated by adding the previous two 
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
'''
total = 2

def fibs(a, b, limit):
    global total
    results = [a, b]
    new_fib = a + b
    while new_fib <= limit:
        results.append(new_fib)
        a, b = b, new_fib
        if new_fib % 2 == 0:
            total += new_fib
    return results

print(fibs(1, 2, 4000000))
print(total)
