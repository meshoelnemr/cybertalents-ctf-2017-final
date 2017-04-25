with open('obfuscated', 'r') as fp:
	data = fp.read()

	result = []
	for i in range(2, len(data), 2):
		byte = int(data[i:i+2], 16)
		result.append(chr(byte ^ 0x90))

	print ''.join(result)
