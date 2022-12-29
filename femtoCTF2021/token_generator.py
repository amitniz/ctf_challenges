import sys
import requests
import json
import struct

# This script performs
# Known plaintext Attack on AES128-CBC Token.

URL = "https://spring-feather-9233.fly.dev"
PASSWORD = "planet!!!11"
USERNAME = "Zero Cool"


def padding(input: bytes, b_size: int) -> bytes:
    '''
    pkcs#7 padding
    '''
    padding_size = b_size - len(input) % b_size
    padding = struct.pack(">B", padding_size) * padding_size
    return input + padding

def xor(a: bytes, b: bytes) -> bytes: 
    '''
    xor two equal sized bytestrings
    '''

    return b''.join([struct.pack(">B",a[i] ^ b[i]) for i in range(len(b))])


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("usage: token_generator.py {new_plaintext}")
        exit(1)
    new_pt = sys.argv[1]  # the plaintext to be replaced

    res = requests.post(f'{URL}/login', json={"password": PASSWORD})
    if res.status_code != 200:
        print("Something went wrong.")
        exit(1)

    json_res = json.loads(res.text)
    token = json_res['token']
    print(f"[*] got token: {token}")
    iv = token[:32]  # the IV that was used for the encryption
    ct = token[32:]  # the ct which is k

    padded_pt = padding(USERNAME.encode(), 16) #fix the size of the plaintext
    bytes_iv = bytes.fromhex(iv)
    #phase 1 - xor the original plaintext with the IV
    xored_pt_iv = xor(padded_pt, bytes_iv)
    #phase 2 - xor the xored original plaintext with the new plaintext 
    padded_new_pt = padding(new_pt.encode(),16)
    new_iv = xor(padded_new_pt,xored_pt_iv).hex()

    print(f"[*] new iv: {new_iv}")
    print(f"[*] new token: {new_iv+ct}")
