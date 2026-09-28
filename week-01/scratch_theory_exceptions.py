print("=== 1. every for loop ends with an exception ===")
it = iter([10, 20])
print(next(it))
print(next(it))
try:
    next(it)
except StopIteration:
    print("StopIteration raised: this is how a for loop knows the list is done")

print("\n=== 2. the exception hierarchy (except matches by isinstance) ===")
for cls in ZeroDivisionError.__mro__:
    print(" ", cls.__name__)

print("\n=== 3. why `else` exists: keep the try body narrow ===")
def broad(a, b):
    try:
        result = a / b
        print("result is", reslt)   # typo: NameError, but caught below by mistake?
    except Exception:
        print("  broad try: caught something, assuming it was a division problem")

def narrow(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("  narrow try: division by zero")
    else:
        print("result is", reslt)   # same typo: now it is NOT swallowed

print("broad version hides the typo:")
broad(4, 2)
print("narrow version exposes it:")
try:
    narrow(4, 2)
except NameError as e:
    print("  NameError surfaced:", e)

print("\n=== 4. finally always runs ===")
def demo_finally():
    try:
        return "returned from try"
    finally:
        print("  finally ran even though we returned")
print(demo_finally())
