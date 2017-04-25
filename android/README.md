# **Android101**

Decompiling the apk with jd-gui  
In Main2Activity
```
String Validate(String paramString)
  {
    StringBuilder localStringBuilder = new StringBuilder(paramString);
    for (int i = 0; i < localStringBuilder.length(); i++) {
      for (int j = i; j < -1 + localStringBuilder.length(); j++)
      {
        char c = localStringBuilder.charAt(j);
        localStringBuilder.setCharAt(j, localStringBuilder.charAt(j + 1));
        localStringBuilder.setCharAt(j + 1, c);
      }
    }
    if (localStringBuilder.toString().equals(String.valueOf(new char[] { 108, 103, 99, 110, 121, 117, 114, 86, 114, 51, 52, 100, 48, 68, 102, 123, 95, 95, 51, 95, 82, 125, 52, 51, 110, 97, 53, 48, 49 }))) {
      Toast.makeText(getApplicationContext(), String.valueOf(new char[] { 67, 111, 114, 114, 101, 99, 116 }), 1).show();
    }
    return "" + localStringBuilder.toString();
  }
```
It simply swaps the input flag then compare it to some order and outputs correct if they match.

```
# crack.py
rev = [108, 103, 99, 110, 121, 117, 114, 86, 114, 51, 52, 100, 48, 68, 102, 123, 95, 95, 51, 95, 82, 125, 52, 51, 110, 97, 53, 48, 49]

i = len(rev)
while i >= 0:
	j = len(rev) - 1
	while j > i:
		rev[j], rev[j-1] = rev[j-1], rev[j]
		j -= 1
	i -= 1
print ''.join(chr(s) for s in rev)
```
The flag is flag{c4n_y0u_r3V3r53_4ndR01D}
