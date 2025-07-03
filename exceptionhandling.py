try :
    a = int(input())
    b = int(input())
    c = a/b
except ZeroDivisionError:
    print("number cannot be divided by zero")
except TypeError:
    print("invalid error")
except Exception as e:
    print(f"unexcepted error {e}")
else:
    print(f"result {c}")
finally:
    print("cleanup")
#what is custom exception in python and how you can create it?
