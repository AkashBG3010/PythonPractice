# #HASH MAP--------->>
# #Dictionaries---------------------->
#
my_dict = {'Andy' : '01', 'Rocky' : '02'}
# print(my_dict)
# print(type(my_dict))
#
#
# new_dict = dict()
# print(new_dict)
# print(type(my_dict))
#
# new_dict = dict(Ricky='001', Ava='002')
# print(new_dict)
#
# # #Nested Dictionaries---------------------->
#
emp_details = {'Employee':{'Dave':{'ID':'001','Salary':'2000','Designation':'Team Lead'},
                           'Ava':{'ID':'002','Salary':'1000','Designation':'Associate'}}}
# print(emp_details)

# #HASH TABLES--------->>
# #Dictionaries---------------------->

# print(my_dict['Andy'])
# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
#
# print(my_dict.get('Rocky'))
#
# for x in my_dict:
#     print(x)
#
# for x in my_dict.values():
#     print(x)
#
# for x in my_dict.keys():
#     print(x)
#
# for x,y in my_dict.items():
#     print(x,y)

# #Updating items from dictionary--->

my_dict['Andy'] = '04'
my_dict['Joe'] = '03'
print(my_dict)

# #Delete items from dictionary--->

my_dict.pop('Joe')
print(my_dict)

# my_dict.popitem()
# print(my_dict)

del my_dict['Rocky']
print(my_dict)


# #Dictonary to Data Frame----------->
# import pandas as pd
#
# data_frame = pd.DataFrame(emp_details['Employee'])
# print(data_frame)