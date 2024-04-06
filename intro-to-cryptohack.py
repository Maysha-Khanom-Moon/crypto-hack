from pwn import xor

key = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
key = bytes.fromhex(key)


for i in range(len(key)):
    flag = xor(i, key)
    print(flag)
    
# from all of these flags find the crypto flag


# xor: num ^ string, num ^ bytes, bytes ^ bytes
# we can't do xor directly from hex