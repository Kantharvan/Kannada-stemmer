import collections
import math

def stem(strs):
	if len(strs)<=3:
		return strs
	point=[]
	P=[]
	wr.write("P values:\n")
	for q in range(len(strs)-1,2,-1):
		pre=strs[:q]
		suf=strs[q:]
		# print(pre,suf)
		wr.write(pre)
		wr.write("  ")
		wr.write(suf)
		wr.write("\t")
		x=len(pre)*math.log(prefix[pre])
		y=len(suf)*math.log(suffix[suf])
		P.append(x+y)
		wr.write(str(x+y))
		wr.write("\n")
	# print(P)
	# print(P.index(max(P)))
	wr.write("max P:")
	wr.write("  ")
	wr.write(str(max(P)))
	wr.write("\n")
	l=P.index(max(P))
	# print(l)
	return strs[:-(l+1)]

file=open("input/data.txt","r")
wr=open("output/OUTPUT.txt","w")
a=file.readlines()
s=[]
for x in range(len(a)):
	for y in range(1,len(a[x][:-1])):
		s.append(a[x][y:-1])
# print(s)
x = int(input("Enter the index of the word range(1,60986): "))
if(x>0 and x<60986):
	word=a[x-1][:-1]
else:
	print("Wrong input, Exiting\n")
	exit(0)
suffix=collections.Counter(s)
# print(suffix)
freqs=suffix.most_common(10)
wr.write("10 most frequent suffix\n")
for e in range(len(freqs)):
	wr.write(freqs[e][0])
	wr.write("\t")
	wr.write(str(freqs[e][1]))
	wr.write("\n")
# print(freqs)
p=[]
for x in range(0,len(a)):
	for y in range(1,len(a[x][:-1])):
		p.append(a[x][:-(y+1)])
# print(p)
prefix=collections.Counter(p)
# print(prefix)
freqp=prefix.most_common(10)
wr.write("10 most frequent prefix\n")
for e in range(len(freqp)):
	wr.write(freqp[e][0])
	wr.write("\t")
	wr.write(str(freqp[e][1]))
	wr.write("\n")
wr.write("\n")
# print(freqp)
wr.write("Word: ")
wr.write(word)
wr.write("\n")
ans=stem(word)
wr.write("Stem: ")
wr.write(ans)
wr.write("\n")
wr.close()
print("Word : ",word)
print("Stem : ",ans)
print("Detailed output has been printed to \"OUTPUT.txt\"")
file.close()