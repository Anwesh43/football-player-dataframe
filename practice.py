import pandas as pd
players = {
    "Key Passes" : [10, 9, 15, 13, 23],
    "shots" : [7, 9, 8, 12, 6],
    "goals" : [2, 1, 1, 8, 3],
    "ball wins" : [33, 22, 5, 11, 17]
}
df = pd.DataFrame(players)
df.index = ["Lucas Torreira", "Matteo Guendouzi", "Mesut Ozil", "Aaron Ramsey", "Granit Xhaka"]
print(df)

## printing columns of df
print("all columns")
print(df.columns)

print("--------")
print("________")

kp_of_all = df.loc[:,["Key Passes"]]
print("key passes of all players")
print(kp_of_all)

print("--------")
print("________")

bw_of_all = df.loc[:, ["ball wins"]]
print("ball wins of all players")
print(bw_of_all)

print("--------")
print("________")

lt_stats = df.loc[["Lucas Torreira"]]
print("stats for Lucas Torreira")
print(lt_stats)

print("--------")
print("________")
mo_stats = df.loc[["Mesut Ozil"]]
print("Mesut Ozil stats")
print(mo_stats)
