a = {"apple":10,"grape":20,"orange":30}
if not "apple" in a :
    a.update({'apple': -1,})
if not "pineapple" in a:
    a.update({"pineapple" : -1})
print(a)