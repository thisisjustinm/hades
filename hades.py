"""
Hades is a complex hashing algorithm written in Python.
Hades makes use of the following algorithms to generate a **128-bit hex digest**.


*   Ares (Simple Hashing algorithm)
*   Zeus (Simple Encoding Agoritm)
"""

from textwrap import wrap

"""
zeus
"""
def nume(s):
  m=''
  for i in s:
    m=m+str(hex(int(ord(i)))[2:])
  m=int('0x'+m,16)
  return m

def fill(s,n):
  m=[]
  a=wrap(str(s),10)
  for i in a:
    m.append(str(i).zfill(n))
    # q="".join(str(x) for x in m)
  return m

def bina(s):
  t=[];q=''
  for i in fill(nume(s),8):
    t.append(bin(int(i)))
    q="".join(str(x[2:]) for x in t)
  return q

def ordi(s):
  m=[];q=''
  for i in s:
    m.append((int(i)))
    q="".join(str(x) for x in m)
  return q

def mixi(s):
  s=ordi(fill(bina(s),7))+ordi(fill(bina(s[::-1]),7))
  return s

def zeus(s):
  m=[];n=[];o=[]
  s='0b'+mixi(s)
  s=int(s,2)
  m=wrap(str(s),3)
  for i in m:
    n.append(int(i)%122)
  for i in n:
    if i<65:
      o.append(120-i)
    else:
      o.append(i)
  # return o
  q="".join(str(chr(x)) for x in o)
  return q

"""
mod-ares
"""
s=0
m=''
b=''
t=''

def rev(a):
	return a[::-1]

def rot47(s):
	x=[]
	for i in range(len(s)):
		j=ord(s[i])
		if j>=33 and j<=126:
			x.append(chr(32+((j+14)%94)))
		else:
			x.append(s[i])
	return  ''.join(x)

def func_a(a):
	m=[i for i in str(a)]
	a=[]
	for j in m:
		a.append(ord(j))
	lk=''
	lk = "".join(str(x) for x in a)
	s=len(bin(int(lk)))
	if(s < 256):
		jk = str(bin(int(lk)))[2:]+'0'*(258-s)
	else:
		jk=str(bin(int(lk)))[2:258]

	kl = wrap(jk,64)

	g=int(kl[0])>>17
	b=int(rev(kl[0]))<<15
	c=(g+b)>>31
	d=int(rev(str(abs(g-b+c))))
	return hex(abs(g+b-c+d))[2:35]

def func_b(a):
	m=[i for i in str(a)]
	a=[]
	for j in m:
		a.append(ord(j))
	lk=''
	lk = "".join(str(x) for x in a)
	s=len(bin(int(lk)))
	if(s < 256):
		jk = str(bin(int(lk)))[2:]+'0'*(258-s)
	else:
		jk=str(bin(int(lk)))[2:258]

	kl = wrap(jk,64)

	g=int(kl[0])<<32
	b=int(rev(kl[0]))<<2
	c=(g+b)>>15
	d=int(rev(str(abs(g+b+c))))
	return hex(abs(g+b+c+d))[2:34]

def func_c(a):
	m=[i for i in str(a)]
	a=[]
	for j in m:
		a.append(ord(j))
	lk=''
	lk = "".join(str(x) for x in a)
	s=len(bin(int(lk)))
	if(s < 256):
		jk = str(bin(int(lk)))[2:]+'0'*(258-s)
	else:
		jk=str(bin(int(lk)))[2:258]

	kl = wrap(jk,64)

	g=int(kl[1])>>12
	b=int(rev(kl[1]))<<12
	c=(g-b)>>2
	d=int(rev(str(abs(g+b-c))))
	return hex(abs(g-b+c+d))[2:31]

def func_d(a):
	m=[i for i in str(a)]
	a=[]
	for j in m:
		a.append(ord(j))
	lk=''
	lk = "".join(str(x) for x in a)
	s=len(bin(int(lk)))
	if(s < 256):
		jk = str(bin(int(lk)))[2:]+'0'*(258-s)
	else:
		jk=str(bin(int(lk)))[2:258]

	kl = wrap(jk,64)

	g=int(kl[0])>>25
	b=int(rev(kl[1]))<<5
	c=(g-b)>>31
	d=int(rev(str(abs(g+b+c))))
	return hex(abs(g+b+c+(d>>21)))[2:35]


def ares(a):
	s=0
	for i in [i for i in a]:
		s=s+ord(i)+len(zeus(a))+len(func_d(i))
	for i in range(s%len(zeus(a))):
		k=func_a(func_b(a))+func_c(func_d(i))
		a=func_a(k+rot47(str(s)))
	return a

def hades(inpt):
	addn=func_d(func_b(inpt))
	revr=func_a(zeus(func_c(inpt)))
	return ares(rev(ares(rev(ares(inpt+func_a(revr)+addn+revr)))))[1:33]
