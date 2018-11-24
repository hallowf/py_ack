from multiprocessing import Process, Queue

#queue = Queue()


def ack(m, n):
    ans = 0
    if (m == 0):
        ans = n+1
    elif (n == 0):
        ans = ack(m-1,1)
    else:
        ans = ack(m-1, ack(m,n-1))
    print("Ackerman of [{},{}] is {}".format(m,n,ans))
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
        ans = tup_ack((m-1, n))
    else:
        #Faster ??
        #b = (m, n-1)
        #a = (m-1, tup_ack(b))
        ans = tup_ack((m-1, tup_ack((m, n-1))))
    print("Ackerman of [{},{}] is {}".format(m,n,ans))
    return ans

def que_ack(q, a)
    ans = 0
    m,n = a
    if(m == 0):
        ans = n+1
    elif (n == 0):
        fq = Queue()
        Process(target=que_ack, args=(fq, (m-1,n)))
        ans = fq.get()
    else:
        fq = Queue()
        sq = Queue()
        tq = Queue()
        Process(target=que_ack, args=(fq, (m, n-1)))
        Process(taget=que_ack, args=(sq, (m-1, fq.get())))

def mp_ack(a):
    ans = 0
    m,n = a
    if (m == 0):
        ans = n + 1
    elif (n == 0):
        fq = 
        ans =
    else:

########### Deprecated =============>
"""
## Can't do this to put multiple items in the queue it seems to be only possible
if all items are already obtained
q = multiprocessing.Queue()
"""
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


