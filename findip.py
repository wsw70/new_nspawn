import os
import re

ips = []
regex = re.compile(r"\s*?address\s+?\d+\.\d+\.\d+\.(?P<x>\d+)")
dirs = [d for d in next(os.walk('.'))[1] if d not in ['.git', 'OLD']]
for d in dirs:
    try:
        with open(os.path.join(d, 'etc', 'network', 'interfaces')) as f:
            lines = f.readlines()
            for line in lines:
                if 'address' in line:
                    x = regex.match(line).group('x')
    except FileNotFoundError:
        # no interfaces file
        pass
    else:
        ips.append(int(x))

all_ips = range(1, max(ips)+2)
free_ips = set(all_ips) - set(ips)
print("10.200.0."+str(min(free_ips)))
