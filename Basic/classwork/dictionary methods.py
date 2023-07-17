bio={'name':'srimathikalpana','age':17,'native':"salem"}
print(bio)

#clear method
bio={'name':'srimathikalpana','age':17,'native':"salem"}
bio.clear()
print(bio)

#copy method
bio={'name':'srimathikalpana','age':17,'native':"salem"}
a=bio.copy()
print(a)

#get method
a=bio.get('native')
print(a)
#items
a=bio.items()
print(a)

#key method
a=bio.keys()
print(a)

#different types of adding a key and value
#set default
a=bio.setdefault("frnds",'nevetha')
print(a)

#update
bio.update({'car':"ameo"})
print(bio)

bio['std']='12th'
print(a)
print(bio)

#values
a=bio.values()
print(a)
