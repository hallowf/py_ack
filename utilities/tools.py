from time import time
from inspect import signature, getargspec
from types import ModuleType
import sys

def time_func(func, args, checklist = False):
    """
    Takes a function, it's args in a tuple, and a checklist
    """
    m,n = args
    
    # Check if the parameter is a module not function
    if isinstance(func, ModuleType):
        # List attributes
        for name in dir(func):
            # Filter __*__
            if not name.startswith("__") or not name.endswith("__"):
                func = getattr(func, name)
                func_name = name
                sig = dir(func)
                print(sig)
                # Broken: cannot inspect C implementation due to lack of metadata
                # TODO: Find a way to check if args is tuple or not
                """
                sig = signature(func)
                if len(sig.parameters) == 1:
                    st_t = time()
                    ans = func(args)
                    end_t = time()
                    speed = str(format(end_t - st_t, '.6f'))
                """

        return
    else:
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
        print("Warning: setting recursion limit to high values can cause stack overflows")
    if val == 1000:
        print("Warning: you are setting a recursion limit to a value that is probably default in most systems")
    if val < 1000:
        print("Error: you are lowering your recursion limit returning...")

    sys.setrecursionlimit(val)

print(get_max_rec())