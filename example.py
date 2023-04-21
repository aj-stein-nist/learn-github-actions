#!/usr/bin/env
import hashlib
import sys

if __name__ == '__main__':
    if not len(sys.argv) == 3:
        print('bad')

    secret, expected_hash = sys.argv[1], sys.argv[2]
    sha256 = hashlib.sha256()
    sha256.update(secret.encode('utf-8'))
    actual_hash = sha256.hexdigest()

    if actual_hash == expected_hash: print('good')
    else: print('bad')
