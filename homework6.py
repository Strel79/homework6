my_dict = {'Anatoliy' : 1979 , 'Victorija' : 1978 , 'Alexander' : 2002 , 'Andrey' : 2008 ,
           'Zenja' : 2011 , 'Ivan' : 2015 , 'Maria' : 2019}
print("Dict:", my_dict)
print("Existing value:" , my_dict ['Zenja'])
print("Non existing value:" , my_dict.get("Erik"))
my_dict.update({'Ljuda' : 1959 , 'Tatjana' : 1956})
a = my_dict.pop("Alexander")
print("Deleted value:" , a)
print("Updated dict.:" , my_dict)

my_set = {1,2,3,4,1,1,1,2,3,'vasja','petja',False,True,1,2,3,4,1,1,1,2,3,'vasja','petja',False}
print("Defind set:", my_set)
my_set.remove(False)
my_set.add((8,9,11))
print("Modified set:", my_set)