class BankAccount:
    def __init__(self, balance):
        self.balance = balance          # public by convention (no prefix)
        self._pin = "1234"              # single underscore: "internal use", NOT enforced
        self.__secret_key = "xyz789"    # double underscore: NAME-MANGLED, not truly private

account = BankAccount(100)

print(account.balance)     # fine, it's public
print(account._pin)        # ALSO fine -- Python does nothing to stop this, it's just a hint

# this looks like it should fail...
try:
    print(account.__secret_key)
except AttributeError as e:
    print("AttributeError:", e)

# ...but the attribute still exists, just under a mangled name:
print(account.__dict__)          # shows the REAL stored attribute names
print(account._BankAccount__secret_key)   # and you CAN still reach it this way
