__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""


def fib(n):
    """
    Calculates the Fibonacci number iteratively

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(10)
    55
    >>> fib(15)
    610
    >>>

    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
