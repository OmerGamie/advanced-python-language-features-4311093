# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

# TODO: define some starting values
b = bytes([0x41, 0x42, 0x43, 0x44])
print(b)

s = "This is a string"
print(s)

# Try combining them.
# print(s+b)

# TODO: Bytes and strings need to be properly encoded and decoded before we can work on them together
s2 = b.decode("utf-8")
print(s+s2)

# TODO: Encode the string as UTF-32
b3 = s.encode("utf-32")
print(b3)
