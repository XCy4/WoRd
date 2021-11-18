st = 'АаЯ яЕеЁё'

a = ord('а')
alf = list(''.join([chr(i) for i in range(a,a+6)] + [chr(a+33)] + [chr(i) for i in range(a+6,a+33)]))
ind = range(1,len(alf))
arr = dict(zip(alf,ind))

result = ''
for s in list(st.lower()):
	res = ''
	if s not in alf:
		res = ' '
	elif s == 'а':
		res = 'я'
	else:
		res = alf[arr[s]-2]
	
	result = result + res

print(st)
print(result)
