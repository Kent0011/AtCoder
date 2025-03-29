pn=[2];A=10000000
for L in range(3,A):
	chk=True
	for L2 in pn:
		if L%L2 == 0:chk=False
	if chk:pn.append(L)
print(pn)