list1=["Harry","Sohana","sam","Rahul"]
names=""
for name in list1:
    names=name.lower()
    if(names.startswith("s")):
        print(f"hello {name}")