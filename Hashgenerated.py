import hashlib

input = input('ENTER ANY PASSWORD:')

#md5
h = hashlib.md5()
h.update(input.encode())
print('md5:',h.hexdigest())

#sha256
h = hashlib.sha256()
h.update(input.encode())
print('sha256:',h.hexdigest())

#sha224
h = hashlib.sha224()
h.update(input.encode())
print('sha224:',h.hexdigest())

#sha384
h = hashlib.sha384()
h.update(input.encode())
print('sha384:',h.hexdigest())

#sha512
h = hashlib.sha512()
h.update(input.encode())
print('sha512:',h.hexdigest())

#sha1
h = hashlib.sha1()
h.update(input.encode())
print('sha1:',h.hexdigest())
