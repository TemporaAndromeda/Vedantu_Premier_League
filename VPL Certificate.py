import pandas as pd
pd.set_option('mode.chained_assignment', None)
week1 = pd.read_csv("Result_C_2022-07-17_to_2022-07-27.csv", usecols=["Student Name", "Subject", "Ranking",
                                                                    "V-Coin Percentage", "User Email", "userID"])

week2 = week1.drop(columns=["Subject", "Ranking"])

week1_cert = week2.groupby(["userID", "User Email", "Student Name"]).mean()

v_coin_percentage = week1_cert["V-Coin Percentage"].tolist()
ranking_list = []
for i in range(len(v_coin_percentage)):
    if v_coin_percentage[i] >= 95:
        ranking_list.append("APEX PREDATORS")
    elif 95 > v_coin_percentage[i] >= 85:
        ranking_list.append("PLATINUM")
    elif 85 > v_coin_percentage[i] >= 70:
        ranking_list.append("GOLD")
    elif 70 > v_coin_percentage[i] >= 50:
        ranking_list.append("SILVER")
    else:
        ranking_list.append("BRONZE")
week1_cert["Ranking"] = ranking_list

math = week1[week1["Subject"] == "Maths"]
math.rename(columns={"V-Coin Percentage": "V-Coin Percentage math", "Subject": "Sub Math", "Ranking": "Rank Math"},
            inplace=True)

phy = week1[week1["Subject"] == "Physics"]
phy.rename(columns={"V-Coin Percentage": "V-Coin Percentage phy", "Subject": "Sub phy", "Ranking": "Rank Physics"},
           inplace=True)

chem = week1[week1["Subject"] == "Chemistry"]
chem.rename(columns={"V-Coin Percentage": "V-Coin Percentage chem", "Subject": "Sub chem", "Ranking": "Rank chem"},
            inplace=True)

merge1 = week1_cert.merge(math, on=["userID", "User Email", "Student Name"])
merge2 = merge1.merge(phy, on=["userID", "User Email", "Student Name"])
merge3 = merge2.merge(chem, on=["userID", "User Email", "Student Name"])
merge3.to_csv("crunch.csv")
