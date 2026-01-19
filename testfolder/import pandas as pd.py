import pandas as pd

df = pd.read_csv("students.csv")
#print(len(df["StudentID"]))
#print(df.describe())

#print(len(df.loc[df["Attendance"] < 80]))
#print(len(df.loc[df["Grade"] == "A"]))
#print(len(df.loc[df["Grade"] == "B"]))
#print(len(df.loc[df["Grade"] == "C"]))
#print(len(df.loc[df["Grade"] == "D"]))
#print(len(df.loc[df["Grade"] == "E"]))
#print(len(df.loc[df["Grade"] == "F"]))

at_risk = pd.DataFrame(df.loc[df["Attendance"] < 80])

print(at_risk)

