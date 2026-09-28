import json

original = {
    "name": "Ada",
    "scores": (90, 85),          # a tuple
    1: "int key",                # a non-string key
    "active": True,
    "nickname": None,
    "ratio": 0.5,
}

text = json.dumps(original)      # dumps = dump to a string (no file needed)
print("JSON text:", text)

restored = json.loads(text)
print("restored :", restored)
print()
print("tuple became:", type(restored["scores"]).__name__)
print("int key 1 present after round trip?", 1 in restored)
print("string key '1' present after round trip?", "1" in restored)
print("equal to original?", restored == original)

print("\n--- types JSON cannot represent ---")
for value in ({1, 2, 3}, 3 + 4j, open):
    try:
        json.dumps(value)
    except TypeError as e:
        print("TypeError:", e)

print("\n--- a truncated file (e.g. crash mid-write) ---")
try:
    json.loads(text[:-8])
except json.JSONDecodeError as e:
    print("JSONDecodeError:", e)
print("is JSONDecodeError a ValueError?", issubclass(json.JSONDecodeError, ValueError))
