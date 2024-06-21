
from src.models.operation import Operation



operation1 =  Operation[int](2,3)
operation2 =  Operation[str]('2','3')
operation3 =  Operation[bool](True,True)
operation4 =  Operation[bool]([],'job')


print(operation1.plus())
print(operation2.plus())
print("Return BOOL : ",operation3.plus())
print(operation4.plus())


