from functools import lru_cache
############## FUNCTIONS
def ack(m, n):
    ans = 0
    if (m == 0):
        ans = n+1
    elif (n == 0):
        ans = ack(m-1,1)
    else:
        ans = ack(m-1, ack(m,n-1))
    return ans

def gen_ack(m,n):
    ans = 0
    if (m == 0):
        ans = n+1
    elif (n == 0):
        ans = gen_ack(m-1,1)
    else:
        ans = gen_ack(m-1, ack(m,n-1))
    yield ans

@lru_cache(maxsize = 1000)
def memoized_ack(m,n):
    ans = 0
    if (m == 0):
        ans = n+1
    elif (n == 0):
        ans = memoized_ack(m-1,1)
    else:
        ans = memoized_ack(m-1, memoized_ack(m,n-1))
    return ans

### **********
"""
Is there a difference between
Second one seems to take less time

    ans = tup_ack((m-1, tup_ack((m, n-1))))

    And

    b = (m, n-1)
    a = (m-1, tup_ack(b))
    ans = tup_ack(a)
"""

def tup_ack(a):
    ans = 0
    m, n = a
    if (m == 0):
        ans = n+1
    elif (n == 0):
        #a = (m-1, n)
        ans = tup_ack((m-1, 1))
    else:
        #Faster ??
        #b = (m, n-1)
        #a = (m-1, tup_ack(b))
        ans = tup_ack((m-1, tup_ack((m, n-1))))
    print("Ackerman of [{},{}] is {}".format(m,n,ans))
    return ans



######################################### CLASSES

class MemoizedAck:

    def __init__(self):
        self.n = {}
        self.m = {}

    @lru_cache(maxsize = 500)
    def ack(self,m,n):
        ans = 0
        if (m == 0):
            ans = n+1
        elif (n == 0):
            ans = self.ack(m-1,1)
        else:
            ans = self.ack(m-1, self.ack(m, n-1))
        return ans

## Maybe use a class for ackerman function

class Clack:

    def ack(self,m,n):
        ans = 0
        if (m == 0):
            ans = n+1
        elif (n == 0):
            ans = self.ack(m-1,1)
        else:
            ans = self.ack(m-1, self.ack(m, n-1))
        return ans


## See this ==========> a few months later..... wtf is this halloween
"""
def foo(bar, baz):
  print 'hello {0}'.format(bar)
  return 'foo' + baz

from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)

async_result = pool.apply_async(foo, ('world', 'foo')) # tuple of args for foo

# do some other stuff in the main process

return_val = async_result.get()  # get the return value from your function.
"""

########### Deprecated Or not working =============>
"""
## Can't do this to put multiple items in the queue it seems to be only possible
if all items are already obtained
q = multiprocessing.Queue()
"""

"""
queue = Queue()

## Unfinished
def mt_ack(m,n):
    ans = 0
    if (m == 0):
        fin_ans = n + 1
    elif (n == 0):
        fp = ThreadPool(processes=1)
        ans = fp.apply_async(mt_ack, (m-1, 1))
        fin_ans = ans.get()
    else:
        fp = ThreadPool(processes=1)
        sp = ThreadPool(processes=1)
        f_ans = fp.apply_async(mt_ack, (m, n-1))
        f_res = f_ans.get()
        s_ans = sp.apply_async(mt_ack, (m-1, f_res))
        fin_ans = s_ans.get()
    print(fin_ans)
    return fin_ans

def old_mp_ack():
    #ans = 0
    #m, n = a
    q = Queue()
    p = Process(target=do_range, args=(q,5))
    p.start()
    for item in q.get():
        print(item)
    p.join()

def do_range(q, numb):
    for i in range(numb):
        q.put([i])

## Unfinished
def que_ack(q, a):
    print(NotImplementedError)
    ans = 0
    m,n = a
    if(m == 0):
        print("First")
        ans = n+1
    elif (n == 0):
        print("Second")
        fq = Queue()
        fp = Process(target=que_ack, args=(fq, (m-1,n)))
        fp.start()
        ans = fq.get()
        fp.join()
    else:
        print("Third")
        fq = Queue()
        sq = Queue()
        fp = Process(target=que_ack, args=(fq, (m-1, que_ack(sq, (m, n-1)))))
        fp.start()
        #sp = Process(target=que_ack, args=(sq, (m-1, fq.get())))
        ans = fq.get()
        fp.join()
        #sp.start()
        #ans = sq.get()
        #sp.join()
    print(ans)
    return ans

    print(ans)
    return (ans, NotImplementedError)

"""
