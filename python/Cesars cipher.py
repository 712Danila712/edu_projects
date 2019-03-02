
'''for i in range(255):
    print('{} {}'.format(i, chr(i)))
quit(0)

i = 0
while i != 255:
    
    print(chr(i))
    i += 1
'''
s = input()
n = int(input())
alphaB = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphaL = alphaB.lower()
nums = "0123456789"
res = ''

for ch in s:
    """print("{} - {}".format(ch, alphaB[(ord(ch) - 65 + n)%len(alphaB)]))"""
    if ch.isupper():
        res += alphaB[(ord(ch) - 65 + n) % len(alphaB)]
    elif ch.islower():
        res += alphaL[(ord(ch) - 97 + n) % len(alphaL)]
    elif ch.isdigit():
        res += nums[(ord(ch) - 48 + n) % len(nums)]
    else:
        res += ch
print(res)
