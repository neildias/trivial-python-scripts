import time
def server(x,y, op):
    if op == "add":
        return x + y
    elif op == "sub":
        return x - y
    elif op == "mul":
        return x * y
    elif op == "div":
        return x / y
    elif op == "exp":
        return x ** y
    else:
        print("Operation undefined...")

def proxy(x,y,op):
    if op == 'add':
        return x + y
    elif op == 'sub':
        return x - y
    else:
        print("Redirecting to the main server...")
        time.sleep(5)
        return server(x,y,op)


if __name__ == "__main__":
    for operation in ('add','sub','mul','div','exp'):

        print()
        print(f"The {operation} operation on 5 and 10 {proxy(5,10,op=operation)}")
        print()
