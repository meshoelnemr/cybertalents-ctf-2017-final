## **Is it really here**

Spending like two hours with the main function trying to figure out what it does and if it contained the flag. A hint was it might be in file sections. which was a good place to inspect as the description was:
> Our scanners flagged this file suspicious. can you know why.

```bash
$ readelf --sections Is+it+really+here
...
[27] .rwdata           PROGBITS         0000000000000000  0000106b
	 0000000000001e4e  0000000000000000           0     0     1
...
```
This section should have WA flags regarding its name.

```bash
$ objdump -s -j .rwdata Is+it+really+here | awk '{print $2$3$4$5}'| tail +5 | tr -d '\n' > obfuscated
```
We dump the section content in a file to work on it.  
It looks like some kind of shellcode as it ends with 0x90s, but it had no meaning.  
Trying to subtract 0x90 from all bytes but it didn't make sense.  
Finally tried to xor 0x90 with all bytes, it produced assembly instructions that containd the flag.

```bash
$ python deobfuscate.py
LC0:
	.string	"%s"
.LC1:

main:
.LFB0:
	.cfi_startproc
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	.cfi_def_cfa_register 5
	mov	DWORD PTR [esp+20], 0
	lea	eax, [esp+26]
	mov	DWORD PTR [esp+4], eax
	mov	DWORD PTR [esp], OFFSET FLAT:.LC0
	call	__isoc99_scanf
	movzx	edx, BYTE PTR [esp+54]
	movzx	eax, BYTE PTR [esp+53]
	cmp	dl, al
	je	.L2
	mov	eax, 0
	jmp	.L34
.L2:
	movzx	eax, BYTE PTR [esp+54]
	movzx	edx, al
	movzx	eax, BYTE PTR [esp+26]
	movzx	eax, al
	add	eax, edx
	cmp	eax, 135
	jg	.L4
	movzx	eax, BYTE PTR [esp+53]
	movzx	edx, al
	movzx	eax, BYTE PTR [esp+26]
	movzx	eax, al
	add	eax, edx
	cmp	eax, 134
	jg	.L5
.L4:
	mov	eax, 0
	jmp	.L34
.L5:
	movzx	edx, BYTE PTR [esp+48]
	movzx	eax, BYTE PTR [esp+51]
	xor	eax, edx
	cmp	al, 32
	je	.L6
	mov	eax, 0
	jmp	.L34
.L6:
	movzx	edx, BYTE PTR [esp+48]
	movzx	eax, BYTE PTR [esp+51]
	cmp	dl, al
	jbe	.L7
	mov	eax, 0
	jmp	.L34
.L7:
	movzx	eax, BYTE PTR [esp+51]
	movzx	edx, al
	movzx	eax, BYTE PTR [esp+50]
	movzx	eax, al
	add	eax, edx
	cmp	eax, 210
	je	.L8
	mov	eax, 0
	jmp	.L34
.L8:
	movzx	edx, BYTE PTR [esp+38]
	movzx	eax, BYTE PTR [esp+52]
	cmp	dl, al
	je	.L9
	mov	eax, 0
	jmp	.L34
.L9:
	movzx	eax, BYTE PTR [esp+26]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 102
	je	.L10
	mov	eax, 0
	jmp	.L34
.L10:
	movzx	eax, BYTE PTR [esp+27]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 210
	je	.L11
	mov	eax, 1
	jmp	.L34
.L11:
	movzx	eax, BYTE PTR [esp+28]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 307
	je	.L12
	mov	eax, 2
	jmp	.L34
.L12:
	movzx	eax, BYTE PTR [esp+29]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 410
	je	.L13
	mov	eax, 3
	jmp	.L34
.L13:
	movzx	eax, BYTE PTR [esp+30]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 533
	je	.L14
	mov	eax, 4
	jmp	.L34
.L14:
	movzx	eax, BYTE PTR [esp+31]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 637
	je	.L15
	mov	eax, 5
	jmp	.L34
.L15:
	movzx	eax, BYTE PTR [esp+32]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 685
	je	.L16
	mov	eax, 6
	jmp	.L34
.L16:
	movzx	eax, BYTE PTR [esp+33]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 804
	je	.L17
	mov	eax, 7
	jmp	.L34
.L17:
	movzx	eax, BYTE PTR [esp+34]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 899
	je	.L18
	mov	eax, 8
	jmp	.L34
.L18:
	movzx	eax, BYTE PTR [esp+35]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 967
	je	.L19
	mov	eax, 9
	jmp	.L34
.L19:
	movzx	eax, BYTE PTR [esp+36]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 1072
	je	.L20
	mov	eax, 10
	jmp	.L34
.L20:
	movzx	eax, BYTE PTR [esp+37]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 1172
	je	.L21
	mov	eax, 11
	jmp	.L34
.L21:
	movzx	eax, BYTE PTR [esp+38]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 1267
	je	.L22
	mov	eax, 12
	jmp	.L34
.L22:
	movzx	eax, BYTE PTR [esp+39]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 1388
	je	.L23
	mov	eax, 13
	jmp	.L34
.L23:
	movzx	eax, BYTE PTR [esp+40]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 1436
	je	.L24
	mov	eax, 14
	jmp	.L34
.L24:
	movzx	eax, BYTE PTR [esp+41]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 1553
	je	.L25
	mov	eax, 15
	jmp	.L34
.L25:
	movzx	eax, BYTE PTR [esp+42]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 1648
	je	.L26
	mov	eax, 16
	jmp	.L34
.L26:
	movzx	eax, BYTE PTR [esp+43]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 1758
	je	.L27
	mov	eax, 17
	jmp	.L34
.L27:
	movzx	eax, BYTE PTR [esp+44]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 1806
	je	.L28
	mov	eax, 18
	jmp	.L34
.L28:
	movzx	eax, BYTE PTR [esp+45]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 1922
	je	.L29
	mov	eax, 19
	jmp	.L34
.L29:
	movzx	eax, BYTE PTR [esp+46]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 2027
	je	.L30
	mov	eax, 20
	jmp	.L34
.L30:
	movzx	eax, BYTE PTR [esp+47]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 2126
	je	.L31
	mov	eax, 21
	jmp	.L34
.L31:
	movzx	eax, BYTE PTR [esp+48]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 2195
	je	.L32
	mov	eax, 22
	jmp	.L34
.L32:
	movzx	eax, BYTE PTR [esp+49]
	movzx	eax, al
	add	DWORD PTR [esp+20], eax
	cmp	DWORD PTR [esp+20], 2290
	je	.L33
	mov	eax, 23
	jmp	.L34
.L33:
	mov	DWORD PTR [esp], OFFSET FLAT:.LC1
	call	printf
	mov	eax, 0
.L34:
	mov	ecx, DWORD PTR [esp+76]
	xor	ecx, DWORD PTR gs:20
	je	.L35
	call	__stack_chk_fail
.L35:
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE0:
```

Working with function.s  
```bash
$ python get_flag.py
flag{h0w_Did_y0u_n0ticE_
```

The rest part of the flag from the top of the function is pretty simple.  
flag{h0w_Did_y0u_n0ticE_me!!}
