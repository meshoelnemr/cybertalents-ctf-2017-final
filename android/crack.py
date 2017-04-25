rev = [108, 103, 99, 110, 121, 117, 114, 86, 114, 51, 52, 100, 48, 68, 102, 123, 95, 95, 51, 95, 82, 125, 52, 51, 110, 97, 53, 48, 49]

i = len(rev)
while i >= 0:
	j = len(rev) - 1
	while j > i:
		rev[j], rev[j-1] = rev[j-1], rev[j]
		j -= 1
	i -= 1
print ''.join(chr(s) for s in rev)
