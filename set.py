set2={"apple","mango","kiwi"}
set1={10,20,30,40}

set2.add("orange")
print(set2)

set1.update(set2)
print(set1)
    
list1=[60,70]
set1.update(list1)
print(set1)




set2.clear()
print(set2)

del set2


set1.remove(20)
print(set1)

set1.discard(40)
print(set1)
