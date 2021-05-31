#compare numpy vs python list
#speed difference between numpy and python lists

import time
size_of_vec = 10000

def pure_python_version():
    t1 = time.time()
    x = range(size_of_vec)
    y = range(size_of_vec)
    z = [x[i] + y [i] for i in range(len(x))]
    return time.time() - t1

def numpy_version():
    t1 = time.time()
    x = np.arange(size_of_vec)
    y = np.arange(size_of_vec)
    z = x + y
    return time.time() - t1

t1 = pure_python_version()
t2 = numpy_version()
#7.62 times faster than numpy.
