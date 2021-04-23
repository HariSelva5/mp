# import pandas as pd
# import csv
# users = pd.read_csv('loginhp.csv')
# user = pd.DataFrame(users)
# u="Nivetha"
# index = users.index
# condition = users["Name"] == u
# idx = index[condition]
# idx_list = idx.tolist()
# #print(idx_list)
# users.at[idx_list, "Password"] ="hello"
# print(users)



import pandas as pd
p=pd.read_csv("1.csv")
p.to_csv("2.csv")
# df3=pd.DataFrame(p)

# if "a" in p['Name'].unique():
#     df3.drop(df3[df3['Name']=="a"].index, inplace = True)
#     df3.to_csv("csvprac.csv",index=False )


# u="Nivetha"
# print(user.loc[user['Name'] == u, 'Name'])







# index = user.index
# condition = user["Name"] == "Nivetha"
# idx = index[condition]
# idx_list = idx.tolist()

# #print(idx_list)
# user['Password'][idx_list]='Nive@hut'
# #print(user['Password'][idx_list])
# user.to_csv('loginhp.csv', mode='w', header=True, index=False)
# users = pd.read_csv('loginhp.csv')
# users.drop(users[users['Name']=="Nivetha"].index,axis=0,inplace = True)
#print(users)
#user = pd.DataFrame(users)

# #print(user.loc[user['Name'] == "Nivetha", 'Password'])
# index = user.index
# condition = user["Name"] == "Nivetha"
# idx = index[condition]
# idx_list = idx.tolist()

# #print(idx_list)
# #user['Password'][idx_list].update('Nive@hut')
# user.at[idx_list, 'Password'] = "Nive@hut"
# #print(user['Password'][idx_list])
# user.to_csv('loginhp.csv', mode='a', header=True, index=False)