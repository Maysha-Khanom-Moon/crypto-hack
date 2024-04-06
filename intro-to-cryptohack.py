from pwn import xor

ans = xor("label", 13).decode()

print("crypto{"+ans+"}")