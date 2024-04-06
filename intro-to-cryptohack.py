# hex ^ hex to string:
# 1. hex to bytes
# 2. bytes(a ^ b for a, b in zip(byte1, byte2))
# 3. then decode it

key_1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key_1 = bytes.fromhex(key_1)

key_2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
key_2_3 = bytes.fromhex(key_2_3)

all = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
all = bytes.fromhex(all)


# to byte ^ byte have to use bytes()
flag = bytes(a ^ b ^ c for a, b, c in zip(key_1, key_2_3, all))


print(flag.decode())




"""
a ^ b = c
b ^ c = a
c ^ a = b
"""