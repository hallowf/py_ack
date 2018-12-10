from time import time
from inspect import signature
import sys

def time_func(func, args, checklist = False):
    """
    Takes a function, it's args in a tuple, and a checklist
    """
    m,n = args
    # The name of the function passed as param
    func_name = func.__name__
    # Returns parameters of function sig.parameters
    sig = signature(func)
    if len(sig.parameters) == 1:
        st_t = time()
        ans = func(args)
        end_t = time()
        speed = str(format(end_t - st_t, '.6f'))
        ans = str("{} took {} s.\nAckerman of [{}, {}] is: {}\n").format(func_name, speed, m, n, ans)
        if checklist:
            checklist.append({func_name: speed + " s."})
        return ans
    else:
        st_t = time()
        ans = func(m,n)
        end_t = time()
        speed = str(format(end_t - st_t, '.6f'))
        ans = str("{} took {} s.\nAckerman of [{}, {}] is: {}\n").format(func_name, speed, m, n, ans)
        if checklist:
            checklist.append({func_name: speed + " s."})
        return ans


def get_max_rec():
    return sys.getrecursionlimit()

def set_max_rec(val):
    current_val = sys.getrecursionlimit()
    if val >= 2000:
        print("Warning setting recursion limit to high values can cause stack overflows")
    if val == 1000:
        print()

    sys.setrecursionlimit(val)

print(get_max_rec())