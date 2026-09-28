
# ---------- a tiny version of unittest, built from scratch ----------

class MiniTestCase:
    def setUp(self):
        pass                                   # subclasses may override this

    def assertEqual(self, actual, expected):
        if actual != expected:                 # this is ALL assertEqual does:
            raise AssertionError(f"{actual!r} != {expected!r}")   # raise an exception


def mini_main(test_class):
    passed = failed = errors = 0
    for name in dir(test_class):               # 1. list every name inside the class
        if name.startswith("test"):            # 2. keep the ones that start with "test"
            test = test_class()                # 3. make a brand-new object for this test
            test.setUp()                       # 4. run the setup code
            try:
                getattr(test, name)()          # 5. call the test method
                print(f"{name} ... ok")
                passed += 1
            except AssertionError as e:        # 6a. a failed comparison
                print(f"{name} ... FAIL: {e}")
                failed += 1
            except Exception as e:             # 6b. the code itself crashed
                print(f"{name} ... ERROR: {type(e).__name__}: {e}")
                errors += 1
    print(f"\nRan {passed + failed + errors} tests: "
          f"{passed} ok, {failed} failed, {errors} errors")


# ---------- using it exactly like you would use unittest ----------

def get_formatted_name(first, last):
    return f"{first} {last}".title()

class TestNames(MiniTestCase):
    def test_janis(self):
        self.assertEqual(get_formatted_name("janis", "joplin"), "Janis Joplin")

    def test_bob(self):
        self.assertEqual(get_formatted_name("bob", "dylan"), "Bob Dylann")   # wrong on purpose

    def test_crash(self):
        get_formatted_name("only one argument")                              # the code crashes

    def helper_not_a_test(self):
        print("this never runs: the name doesn't start with 'test'")

mini_main(TestNames)
