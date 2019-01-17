import pandas as pd
players = {
    "keyp" : [10, 9, 15, 13, 23],
    "shots" : [7, 9, 8, 12, 6],
    "goals" : [2, 1, 1, 8, 3],
    "bws" : [33, 22, 5, 11, 17]
}
df = pd.DataFrame(players)
df.index = ["Lucas Torreira", "Matteo Guendouzi", "Mesut Ozil", "Aaron Ramsey", "Granit Xhaka"]
print(df)

## printing columns of df
print("all columns")
print(df.columns)

print("--------")
print("________")

kp_of_all = df.loc[:,["keyp"]]
print("key passes of all players")
print(kp_of_all)

print("--------")
print("________")

bw_of_all = df.loc[:, ["bws"]]
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


ball_winners = df[df["bws"] > 20]
print("ball winners are")
print(ball_winners)

goal_scorers = df[df["goals"] >= 3]
print("top gaol scorers are ")
print(goal_scorers)

shooters = df[df["shots"] >= 8]
print("shooters are")
print(shooters)
