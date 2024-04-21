li = [1,2,3,4,5,6,7,8,9]
n_list = [x * 3 for x in li if x >= 1]

print("3단", n_list[:])


s = "oneLine"[:3]
print(s)

v = "oneLine"
print(v)

v.lower()
print(v.lower())

v.upper()
print(v.upper())

v.swapcase()
print(v.swapcase())

v.lstrip()
print(v.lstrip())

v.rstrip()
print(v.rstrip)

v.count("n")
print(v.count("n"))

v.find("e")
print(v.find("e"))

v.index("n")
print(v.index("n"))

v.index("e")
print(v.index("e"))

v.startswith("i")
print(v.startswith("i"))

print("=" * 5 , "문제4-2" , "=" * 5)

w1="Korea"
w2="Baseball"
w3="Orag"
w4="Victory"

w1[4]+w2[7]+w3[0]+w4[0]

p = w2[7]+w3[0]+w4[0]+w1[3]

print(p.capitalize())

print("=" * 5 , "문제4-3" , "=" * 5)
b = w2[0]+w1[3]
o = w3[0]+w3[1]+w3[3]
print(b,w1.lower()+"."+o.lower())
