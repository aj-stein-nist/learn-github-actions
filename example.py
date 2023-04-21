#!/usr/bin/env
import hashlib
import sys

if __name__ == '__main__':
    if not len(sys.argv) == 3:
        print('bad')

    secret, expected_hash = sys.argv[1], sys.argv[2]
    h = hashlib.sha256()
    h.update(secret.encode('utf-8'))
    actual_hash = h.hexdigest()

    if actual_hash == expected_hash: print('good')
    else: print('bad')
