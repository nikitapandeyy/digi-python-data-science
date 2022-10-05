l=[10,20,30,40,50,60,70,80]
print(l[3:-2])
fruits=[]
fruits.append("apple")
fruits.append("cherry")
fruits.append(3)
fruits.append("677")
print(fruits)
fruits.insert(5,"gavava")
print(fruits)
metal=["tytf","56","Tytf"]
print(l.extend(metal))
print(l)
k=["apple","gavava","orange","apple"]
dry_fruits=["almonds","Walnut"]
k.extend(dry_fruits)
k.append(l)
metal.sort()
k.remove("apple")
k.pop(1)

print(metal)
print(k)

