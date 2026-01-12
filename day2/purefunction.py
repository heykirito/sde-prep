## Always return the return outside of a function, not printing it
## Keep logic pure and I/O at the edges
## side effect is when a function changes or depends on something outside itself. 
## For DB, files. networking and logs


def add(a,b):
    return a+b ##pure function

## some side effect examples 

total = 0

def addd(x):
    global total 
    total += x     # modifies outside state
    return total


## Good practice example

def calculate(price, tax):
    return price + price*tax

def save_to_db(value):
    print("Saved:", value)

total = calculate(100, 0.10)
save_to_db(total)
