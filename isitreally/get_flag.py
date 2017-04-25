import re

with open('function.s', 'r') as fp:
	data = fp.read()

	n = re.findall(r'\[esp\+20\], (\d+)', data)

	prev = 0
	flag = []
	for c in n[1:]:
		val = int(c)
		flag.append(chr(val - prev))
		prev = val

	print ''.join(flag)
