class TracedResource:
    def __enter__(self):
        print("ACQUIRE: resource opened")
        return self   # this becomes the value bound by `as`

    def __exit__(self, exc_type, exc_value, traceback):
        print("RELEASE: resource closed (runs no matter what)")
        return False  # False = don't suppress the exception, let it propagate

print("--- normal case ---")
with TracedResource() as r:
    print("doing work inside the with block")

print("\n--- exception case ---")
try:
    with TracedResource() as r:
        print("about to raise...")
        raise ValueError("something went wrong mid-block")
except ValueError as e:
    print(f"caught it after the with block: {e}")
