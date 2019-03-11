from time import time
from inspect import signature, getargspec, getmembers, isfunction
from types import ModuleType
import sys, warnings
import api.ack_py.ackermann as ackers # import clack, ack, gen_ack, tup_ack
#from api.cy_ack import ack as cy_ack

all_funcs = {member[0]: member[1] for member in inspect.getmembers(ackers, inspect.isfunction)}

def return_func(func):
    to_return = None
    for key in all_funcs.keys():
        if func.lower() == key:
            to_return = all_funcs[key]
    if to_return != None:
        return to_return
    else:
        print("Function not found")
        return {"Error": "Function not found"}



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
            print("This is a module and time_func can't handle it")
            raise NotImplementedError
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
    try:
        int(val)
        if val >= 2000:
            warnings.warn("Setting recursion limit to high values can cause stack overflows", Warning) 
            sys.setrecursionlimit(val)
        elif val == 1000:
            warnings.warn("You are setting a recursion limit to a value that is probably default or low in most systems", Warning)
            sys.setrecursionlimit(val)
        elif val < 1000:
            warnings.warn("You are lowering your recursion limit returning...", Warning)
            return
        else:
            raise ValueError
    except Exception as e:
        if e.__class__ == ValueError:
            print("The value must be an integer EX: m=2 & n=3 ")
            return { "Error": "The value must be an integer EX: m=2 & n=3" }
        else:
            print("Error")
            print(e)