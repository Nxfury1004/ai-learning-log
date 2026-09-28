import unittest

def get_formatted_name(first, last):
    return f"{first} {last}".title()

print("=== 1. no framework: plain assert statements ===")
def run_plain():
    assert get_formatted_name("janis", "joplin") == "Janis Joplin"
    print("  check 1 passed")
    assert get_formatted_name("bob", "dylan") == "Bob Dylann"      # deliberately wrong
    print("  check 2 passed")
    assert get_formatted_name("ada", "lovelace") == "Ada Lovelace"
    print("  check 3 passed")

try:
    run_plain()
except AssertionError:
    print("  AssertionError, and no detail about what the values were")
    print("  check 3 never ran, so we know nothing about it")

print("\n=== 2. same three checks as unittest test methods ===")
class TestNames(unittest.TestCase):
    def test_janis(self):
        self.assertEqual(get_formatted_name("janis", "joplin"), "Janis Joplin")

    def test_bob(self):
        self.assertEqual(get_formatted_name("bob", "dylan"), "Bob Dylann")   # deliberately wrong

    def test_ada(self):
        self.assertEqual(get_formatted_name("ada", "lovelace"), "Ada Lovelace")

unittest.main(argv=["ignored"], exit=False, verbosity=2)
