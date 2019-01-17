import pandas as pd
players = {
    "Key Passes" : [10, 9, 15, 13, 23],
    "shots" : [7, 9, 8, 12, 6],
    "goals" : [2, 1, 1, 8, 3],
    "ball wins" : [33, 22, 5, 11, 17]
}
df = pd.DataFrame(players)
df.index = ["Lucas Torreira", "Matteo Guendouzi", "Mesit Ozil", "Aaron Ramsey", "Granit Xhaka"]
print(df)
