from functools import wraps

def ensureNoKwargs(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        if kwargs:
            raise ValueError("NNOOOOOOO kwaaaargs allooooowed")
        return fn(*args,**kwargs)
    return wrapper

@ensureNoKwargs
def sayHi(name):
    print(f"Hi {name}")

sayHi("Bob") #will work

sayHi(name="Bobby") #wont work cause cause no kwargs allowed
            