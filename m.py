#!/usr/bin/env python3
# Encrypted with 35-layer AES-GCM. Do not modify.
import base64, sys, getpass
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend

__PAYLOAD__ = "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"
__LAYERS__ = 35
__ITERS__ = 100000

def _derive(password, i):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32,
                     salt=(password + str(i)).encode(),
                     iterations=__ITERS__, backend=default_backend())
    return kdf.derive((password + str(i)).encode())

def _decrypt(payload, password):
    data = base64.b64decode(payload.encode())
    for i in reversed(range(__LAYERS__)):
        key = _derive(password, i)
        nonce, ct = data[:12], data[12:]
        data = AESGCM(key).decrypt(nonce, ct, None)
    return data.decode()

if __name__ == "__main__":
    pwd = getpass.getpass("\U0001f510 Password: ")
    try:
        src = _decrypt(__PAYLOAD__, pwd)
    except Exception:
        print("\u274c Wrong password or corrupted file.")
        sys.exit(1)
    exec(compile(src, "<decrypted>", "exec"), {"__name__": "__main__"})
