import random
o = open('out.txt', 'w')
s = '''
        Put List here
        it must be like
        *surname* *name*, *number of room or город*
        
        '''
sa = s.split('\n')
sb = []
n = random.randint(0, len(sa))
sb.append(sa[n])
sa.pop(n)
for i in range(0, 79):
    surname, name, room = str(sb[i]).split(' ')
    n2 = random.randint(0, len(sa) - 1)
    s1 = sa[n2]
    surname2, name2, room2 = str(s1).split(' ')
    if room != 'город':
        if room == room2:
            while room == room2:
                n2 = random.randint(0, len(sa) - 1)
                s1 = sa[n2]
                surname2, name2, room2 = str(s1).split()
    sa.pop(n2)
    sb.append(s1)
for i in range(0, 79):
    o.write(sb[i] + ' --> ' + sb[i+1] + '\n')
o.write(sb[79] + ' --> ' + sb[0])
o.close()
