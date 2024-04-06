from pwn import xor

HEX = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

HEX = bytes.fromhex(HEX)

# key = str.encode('crypto{FLAG}')
# following that we got an idea about key
key = str.encode('myXORkey')

# for xor operation: encoded form is better
xored = xor(HEX, key)
print(xored)