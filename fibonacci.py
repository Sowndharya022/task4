fibonacci=lambda n:reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2),[1,1])
from functools import reduce
result=fibonacci(50)
print(result)