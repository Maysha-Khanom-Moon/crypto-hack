## General

#### encoding
- ascii:
    - 7-bit encoding standard. 
    - chr(): integer into character
    - ord(): character into integer
    - use .join() for make a whole string or array

- hex:
    - ciphertext commonly has bytes which is not portable ascii characters.
    - bytes.fromhex(): hex decode into bytes
    - .hex(): bytes encode into hex

- base64:
    - import base64
    - common encoding scheme
    - hex string decode into bytes
    - then encode into base64
    - base64.b64encode()

- bytes and big integers:
    - RSA works on numbers
    - form Crypto.Util.number import bytes_to_long
        - bytes into number
    - form Crypto.Util.number import long_to_bytes
        - number into bytes