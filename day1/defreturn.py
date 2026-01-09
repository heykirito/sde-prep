def sum(firstnum=34,secondnum=35):
    return firstnum+secondnum

print(sum())
print(sum(12,13))

## using *args and * kwargs

def demo(*args, **kwargs):
    """
    returning args and kwargs
    should be first thing in the function(docstring)
    """
    return *args, *kwargs
print(demo(1,3,4,5, name="Kirito", age=22, doing="nothing"))
print(demo.__doc__)

## typehints

def add (a: int, b:int ) -> str:
    return a+b

print(add(4,5))
num = add(4,5)
print(type(num), "returning int instead of str as it does not change the outcome just to catch errors")
