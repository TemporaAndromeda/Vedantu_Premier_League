import pandas as pd

df1 = pd.read_csv("../../../../Excel_Vedantu/Result_2022-05-02_to_2022-05-17.csv", usecols=["Student Name", "Active Group", "V-Coins",
                                                                    "Maximum V-Coins", "V-Coin Percentage",
                                                                    "Attendance",
                                                                    "userID", "Stickiness V-Coins",
                                                                    "Quiz V-Coins", "Assignment V-Coins",
                                                                    "Test V-Coins",
                                                                    "Average Stickiness Percentage", "Total Quiz Asked"
                                                                    , "Total Quiz Attempted"])
df1 = df1[df1["Attendance"] !=0]
df1["quiz attempt rate"] = (df1["Total Quiz Attempted"] / df1["Total Quiz Asked"])*100
df1.drop(columns=["Total Quiz Asked", "Total Quiz Attempted"], inplace=True)
df1_grouped = df1.groupby(["Student Name", "Active Group", "userID"]).mean()
df1_stick = df1["Average Stickiness Percentage"].mean()
df1_quiz = df1["quiz attempt rate"].mean()
df1_assignment = (df1["Assignment V-Coins"].mean())/2.5
df1_test = (df1["Test V-Coins"].mean())/2.5

V_list_B = {"Student Count":df1_grouped["V-Coin Percentage"].count(), "Max V-Coins":df1_grouped["Maximum V-Coins"].mean(),
            "V-Coin":df1_grouped["V-Coins"].mean(),"Percentage": df1_grouped["V-Coin Percentage"].mean(),
            "Stickiness":df1_stick, "Quiz": df1_quiz, "Assignment": df1_assignment, "Test": df1_test}
df2 = pd.read_csv("Result_2022-04-11_to_2022-04-29.csv", usecols=["Student Name", "Active Group", "V-Coins",
                                                                  "Maximum V-Coins", "V-Coin Percentage", "Attendance",
                                                                  "userID", "Stickiness V-Coins",
                                                                  "Quiz V-Coins", "Assignment V-Coins", "Test V-Coins",
                                                                  "Average Stickiness Percentage", "Total Quiz Asked"
                                                                     , "Total Quiz Attempted"])
df2 = df2[df2["Attendance"] !=0]
df2["quiz attempt rate"] = (df2["Total Quiz Attempted"] / df2["Total Quiz Asked"])*100
df2.drop(columns=["Total Quiz Asked", "Total Quiz Attempted"], inplace=True)
df2_grouped = df2.groupby(["Student Name", "Active Group", "userID"]).mean()
df2_stick = df2["Average Stickiness Percentage"].mean()
df2_quiz = df2["quiz attempt rate"].mean()
df2_assignment = (df2["Assignment V-Coins"].mean())/2.50
df2_test = (df2["Test V-Coins"].mean())/2.50
V_list_C = {"Student Count":df2_grouped["V-Coin Percentage"].count(), "Max V-Coins":df2_grouped["Maximum V-Coins"].mean(),
            "V-Coin":df2_grouped["V-Coins"].mean(),"Percentage": df2_grouped["V-Coin Percentage"].mean(),
            "Stickiness":df2_stick, "Quiz": df2_quiz, "Assignment": df2_assignment, "Test": df2_test}


df3 = pd.read_csv("Result_2022-04-11_to_2022-04-29-A.csv", usecols=["Student Name", "Active Group", "V-Coins",
                                                                    "Maximum V-Coins", "V-Coin Percentage",
                                                                    "Attendance",
                                                                    "userID", "Stickiness V-Coins",
                                                                    "Quiz V-Coins", "Assignment V-Coins",
                                                                    "Test V-Coins",
                                                                    "Average Stickiness Percentage", "Total Quiz Asked"
                                                                     , "Total Quiz Attempted"])
df3 = df3[df3["Attendance"] !=0]
df3["quiz attempt rate"] = (df3["Total Quiz Attempted"] / df3["Total Quiz Asked"])*100
df3.drop(columns=["Total Quiz Asked", "Total Quiz Attempted"], inplace=True)
df3_grouped = df3.groupby(["Student Name", "Active Group", "userID"]).mean()
df3_stick = df3["Average Stickiness Percentage"].mean()
df3_quiz = df3["quiz attempt rate"].mean()
df3_assignment = (df3["Assignment V-Coins"].mean())/2.5
df3_test = (df3["Test V-Coins"].mean())/2.5
V_list_A = {"Student Count":df3_grouped["V-Coin Percentage"].count(), "Max V-Coins":df3_grouped["Maximum V-Coins"].mean(),
            "V-Coin":df3_grouped["V-Coins"].mean(),"Percentage": df3_grouped["V-Coin Percentage"].mean(),
            "Stickiness":df3_stick, "Quiz": df3_quiz, "Assignment": df3_assignment, "Test": df3_test}

df4 = pd.read_csv("Result_2022-04-11_to_2022-04-29-B-English.csv", usecols=["Student Name", "Active Group", "V-Coins",
                                                                    "Maximum V-Coins", "V-Coin Percentage",
                                                                    "Attendance",
                                                                    "userID", "Stickiness V-Coins",
                                                                    "Quiz V-Coins", "Assignment V-Coins",
                                                                    "Test V-Coins",
                                                                    "Average Stickiness Percentage", "Total Quiz Asked"
                                                                     , "Total Quiz Attempted"])
df4 = df4[df4["Attendance"] !=0]
df4["quiz attempt rate"] = (df4["Total Quiz Attempted"] / df4["Total Quiz Asked"])*100
df4.drop(columns=["Total Quiz Asked", "Total Quiz Attempted"], inplace=True)
df4_grouped = df4.groupby(["Student Name", "Active Group", "userID"]).mean()
df4_stick = df4["Average Stickiness Percentage"].mean()
df4_quiz = df4["quiz attempt rate"].mean()
df4_assignment = (df4["Assignment V-Coins"].mean())/2.5
df4_test = (df4["Test V-Coins"].mean())/2.5
V_list_B_Eng = {"Student Count":df4_grouped["V-Coin Percentage"].count(), "Max V-Coins":df4_grouped["Maximum V-Coins"].mean(),
            "V-Coin":df4_grouped["V-Coins"].mean(),"Percentage": df4_grouped["V-Coin Percentage"].mean(),
            "Stickiness":df4_stick, "Quiz": df4_quiz, "Assignment": df4_assignment, "Test": df4_test}


df5 = pd.read_csv("Result_2022-04-11_to_2022-04-29-C-Eng.csv", usecols=["Student Name", "Active Group", "V-Coins",
                                                                    "Maximum V-Coins", "V-Coin Percentage",
                                                                    "Attendance",
                                                                    "userID", "Stickiness V-Coins",
                                                                    "Quiz V-Coins", "Assignment V-Coins",
                                                                    "Test V-Coins",
                                                                    "Average Stickiness Percentage", "Total Quiz Asked"
                                                                     , "Total Quiz Attempted"])
df5 = df5[df5["Attendance"] !=0]
df5["quiz attempt rate"] = (df5["Total Quiz Attempted"] / df5["Total Quiz Asked"])*100
df5.drop(columns=["Total Quiz Asked", "Total Quiz Attempted"], inplace=True)
df5_grouped = df5.groupby(["Student Name", "Active Group", "userID"]).mean()
df5_stick = df5["Average Stickiness Percentage"].mean()
df5_quiz = df5["quiz attempt rate"].mean()
df5_assignment = (df5["Assignment V-Coins"].mean())/2.5
df5_test = (df5["Test V-Coins"].mean())/2.5
V_list_C_Eng = {"Student Count":df5_grouped["V-Coin Percentage"].count(), "Max V-Coins":df5_grouped["Maximum V-Coins"].mean(),
            "V-Coin":df5_grouped["V-Coins"].mean(),"Percentage": df5_grouped["V-Coin Percentage"].mean(),
            "Stickiness":df5_stick, "Quiz": df5_quiz, "Assignment": df5_assignment, "Test": df5_test}

df6 = pd.read_csv("Result_2022-04-11_to_2022-04-29-D-Eng.csv", usecols=["Student Name", "Active Group", "V-Coins",
                                                                    "Maximum V-Coins", "V-Coin Percentage",
                                                                    "Attendance",
                                                                    "userID", "Stickiness V-Coins",
                                                                    "Quiz V-Coins", "Assignment V-Coins",
                                                                    "Test V-Coins",
                                                                    "Average Stickiness Percentage", "Total Quiz Asked"
                                                                     , "Total Quiz Attempted"])
df6 = df6[df6["Attendance"] !=0]
df6["quiz attempt rate"] = (df6["Total Quiz Attempted"] / df6["Total Quiz Asked"])*100
df6.drop(columns=["Total Quiz Asked", "Total Quiz Attempted"], inplace=True)
df6_grouped = df6.groupby(["Student Name", "Active Group", "userID"]).mean()
df6_stick = df6["Average Stickiness Percentage"].mean()
df6_quiz = df6["quiz attempt rate"].mean()
df6_assignment = (df6["Assignment V-Coins"].mean())/2.5
df6_test = (df6["Test V-Coins"].mean())/2.5
V_list_D_Eng = {"Student Count":df6_grouped["V-Coin Percentage"].count(), "Max V-Coins":df6_grouped["Maximum V-Coins"].mean(),
            "V-Coin":df6_grouped["V-Coins"].mean(),"Percentage": df6_grouped["V-Coin Percentage"].mean(),
            "Stickiness":df6_stick, "Quiz": df6_quiz, "Assignment": df6_assignment, "Test": df6_test}

df7 = pd.read_csv("Result_2022-04-11_to_2022-04-29-E-Eng.csv", usecols=["Student Name", "Active Group", "V-Coins",
                                                                    "Maximum V-Coins", "V-Coin Percentage",
                                                                    "Attendance",
                                                                    "userID", "Stickiness V-Coins",
                                                                    "Quiz V-Coins", "Assignment V-Coins",
                                                                    "Test V-Coins",
                                                                    "Average Stickiness Percentage", "Total Quiz Asked"
                                                                     , "Total Quiz Attempted"])
df7 = df7[df7["Attendance"] !=0]
df7["quiz attempt rate"] = (df7["Total Quiz Attempted"] / df7["Total Quiz Asked"])*100
df7.drop(columns=["Total Quiz Asked", "Total Quiz Attempted"], inplace=True)
df7_grouped = df7.groupby(["Student Name", "Active Group", "userID"]).mean()
df7_stick = df7["Average Stickiness Percentage"].mean()
df7_quiz = df7["quiz attempt rate"].mean()
df7_assignment = (df7["Assignment V-Coins"].mean())/2.5
df7_test = (df7["Test V-Coins"].mean())/2.5
V_list_E_Eng = {"Student Count":df7_grouped["V-Coin Percentage"].count(), "Max V-Coins":df7_grouped["Maximum V-Coins"].mean(),
            "V-Coin":df7_grouped["V-Coins"].mean(),"Percentage": df7_grouped["V-Coin Percentage"].mean(),
            "Stickiness":df7_stick, "Quiz": df7_quiz, "Assignment": df7_assignment, "Test": df7_test}

df8 = pd.read_csv("Result_2022-04-11_to_2022-04-29-A-Hin.csv", usecols=["Student Name", "Active Group", "V-Coins",
                                                                    "Maximum V-Coins", "V-Coin Percentage",
                                                                    "Attendance",
                                                                    "userID", "Stickiness V-Coins",
                                                                    "Quiz V-Coins", "Assignment V-Coins",
                                                                    "Test V-Coins",
                                                                    "Average Stickiness Percentage", "Total Quiz Asked"
                                                                     , "Total Quiz Attempted"])
df8 = df8[df8["Attendance"] !=0]
df8["quiz attempt rate"] = (df8["Total Quiz Attempted"] / df8["Total Quiz Asked"])*100
df8.drop(columns=["Total Quiz Asked", "Total Quiz Attempted"], inplace=True)
df8_grouped = df8.groupby(["Student Name", "Active Group", "userID"]).mean()
df8_stick = df8["Average Stickiness Percentage"].mean()
df8_quiz = df8["quiz attempt rate"].mean()
df8_assignment = (df8["Assignment V-Coins"].mean())/2.5
df8_test = (df8["Test V-Coins"].mean())/2.5
V_list_A_Hin = {"Student Count":df8_grouped["V-Coin Percentage"].count(), "Max V-Coins":df8_grouped["Maximum V-Coins"].mean(),
            "V-Coin":df8_grouped["V-Coins"].mean(),"Percentage": df8_grouped["V-Coin Percentage"].mean(),
            "Stickiness":df8_stick, "Quiz": df8_quiz, "Assignment": df8_assignment, "Test": df8_test}

dict1 = pd.DataFrame(list(V_list_B.items()), columns =["Data count","B-Hinglish"] )
dict2 = pd.DataFrame(list(V_list_A.items()), columns =["Data count","A-English"] )
dict3 = pd.DataFrame(list(V_list_C.items()), columns =["Data count","C-Hinglish"] )
dict4 = pd.DataFrame(list(V_list_B_Eng.items()), columns =["Data count","B-English"] )
dict5 = pd.DataFrame(list(V_list_C_Eng.items()), columns =["Data count","C-English"] )
dict6 = pd.DataFrame(list(V_list_D_Eng.items()), columns =["Data count","D-English"] )
dict7 = pd.DataFrame(list(V_list_E_Eng.items()), columns =["Data count","E-English"] )
dict8 = pd.DataFrame(list(V_list_A_Hin.items()), columns =["Data count","A-Hinglish"] )


merge1 = dict1.merge(dict2, on=["Data count"])
final = merge1.merge(dict3, on =["Data count"])
final2 = final.merge(dict4, on= ["Data count"])
final3 = final2.merge(dict5, on = ["Data count"])
final4 = final3.merge(dict6, on= ["Data count"])
final5 = final4.merge(dict7, on=["Data count"])
final6 = final5.merge(dict8, on=["Data count"])
print(final6.round(2))
dict1.to_csv("Dataset-VPL.csv")