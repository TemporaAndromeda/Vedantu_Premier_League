import numpy as np
import datetime
import pandas as pd

pd.set_option('mode.chained_assignment', None)
df1 = pd.read_csv("psc_hybrid_data_requirements_user_session_ay_2022_2022-08-17T08_46_52.218295Z.csv",
                  usecols=["userid", "sessionid", "fullname", "Student Name", "email", "session_time",
                           "groupname", "attendedtis", "stickiness",
                           "quiz_asked", "quiz_attempt",
                           "quiz_correct", "subject",
                           "enrollment_status", "email", "batchid", "session_title"])

batch_alphabet = str(input("Enter the batch alphabet: "))
df_exclude = df1.loc[df1["groupname"].str.startswith(f"Sankalp JEE-Hinglish-{batch_alphabet}(22-23)")]
df_exclude.drop(columns=["sessionid", "fullname", "Student Name", "email", "session_time",
                         "groupname", "attendedtis", "stickiness",
                         "quiz_asked", "quiz_attempt",
                         "quiz_correct", "subject",
                         "enrollment_status", "email", "batchid", "session_title"], inplace=True)
df_exclude.drop_duplicates(subset=["userid"], inplace=True)
df = df_exclude.merge(df1, on=["userid"], how="inner")
df["session_time"] = pd.to_datetime(df["session_time"], format="%Y-%m-%d")
df["session_date"] = df["session_time"].dt.date
df.drop(columns=["session_time"], inplace=True)
df.fillna(0, inplace=True)
date_start = input("Enter the first filter date in the format yyyy-mm-dd: ")
year, month, day = map(int, date_start.split('-'))
date1_in = datetime.date(year, month, day)
date_end = input("Enter the last filter date in the format yyyy-mm-dd: ")
year, month, day = map(int, date_end.split('-'))
date2_in = datetime.date(year, month, day)

frame1 = df.loc[(df["session_date"] >= date1_in) & (df["session_date"] <= date2_in)]
frame1 = frame1[frame1["session_title"] != "Tatva Discussion"]
frame1 = frame1[frame1["session_title"] != "Parent Teacher Session"]

cancel = int(input("Do you have any Cancelled sessions, if yes, enter how many, if no enter 0: "))
cancel_list = []
if cancel != 0:
    for i in range(cancel):
        cancel_id = input("Enter ID: ")
        cancel_list.append(cancel_id)

frame1 = frame1[~frame1.sessionid.isin(cancel_list)]

frame1.drop(columns=["session_title"], inplace=True)
frame2 = frame1.sort_values(by="userid")
frame2.index.name = "index 1"
frame2.rename(columns={"fullname": "MT Name", "attendedtis": "Attendance",
                       "enrollment_status": "Enrollment Status", "email":
                           "E-mail", "subject": "Subject"}, inplace=True)
frame2["Attendance"] = np.where((frame2.Attendance == "Present"), 1, 0)

frame2.drop_duplicates(subset=["sessionid", "userid"], inplace=True, keep='first')
frame3 = frame2.groupby(["userid", "groupname", "Student Name", "E-mail",
                         "Subject", "batchid"]).sum()

frame5 = frame2.groupby(["userid", "groupname", "Student Name", "E-mail",
                         "Subject", "batchid"])["Attendance"].count()
new = frame3.join(frame5, how='left', rsuffix=' Total')
frame4 = new.sort_values(["Student Name", "Attendance"], ascending=[True,
                                                                    False])
frame4.reset_index(inplace=True)
frame4.drop_duplicates(subset=["userid", "Subject"], keep='first',
                       inplace=True)
Active_group = frame4.rename(columns={"userid": "userID", "E-mail": "User Email",
                                      "groupname": "Active Group",
                                      "Attendance Total": "Total Sessions"})
Active_group["Average Stickiness Percentage"] = Active_group["stickiness"] / Active_group["Total Sessions"]
Active_group = Active_group[Active_group["Subject"] != "Maths,Chemistry,Physics"]

df2 = pd.read_csv("wavebook_id_for_session_id___date_range_filter____coe_2022-08-17T08_48_22.187204Z.csv",
                  usecols=["sessionid", "wavebookid"])
wavebook_list = pd.DataFrame(df2)
date2 = frame2.merge(wavebook_list, on=["sessionid"])
date2.rename(columns={"wavebookid": "Wavebook ID"}, inplace=True)

df_wavelist = date2.merge(frame4, on=["userid", "groupname", "Subject", "batchid", "E-mail"])
df_wavelist = df_wavelist[df_wavelist["Subject"] != "Maths,Chemistry,Physics"]
df_wavelist.drop(columns=["Student Name_y", "Attendance_y", "stickiness_y", "quiz_asked_y",
                          "quiz_attempt_y", "quiz_correct_y", "Attendance Total"], inplace=True)
df_wavelist.rename(columns={"Student Name_x": "Student Name", "Attendance_x": "Attendance",
                            "stickiness_x": "stickiness", "quiz_asked_x": "quiz_asked",
                            "quiz_attempt_x": "quiz_attempt", "quiz_correct_x": "quiz_correct"}, inplace=True)

Assignment_list = pd.read_csv("Wavebook Assignment Mapping  - JEE LT.csv")
assignment_df = pd.DataFrame(Assignment_list)

df_wavelist["Assignment ID"] = df_wavelist["Wavebook ID"].map(
    dict(zip(assignment_df["Wavebook id"], assignment_df["Assignment Id"])))

Assignment_attempt = pd.read_csv("assignment_attempt_data__filter___batchid_or_date___coe_2022-08-17T08_51_34.876081Z.csv",
                                 usecols=["studentid", "testid", "batchid", "contenttitle", "attemptstate",
                                          "attempted"], low_memory=False)
Assignment_attempt_df = pd.DataFrame(Assignment_attempt)

Assignment_attempt_df.rename(columns={"studentid": "userid", "testid": "Assignment ID", "contenttitle": "Content Title",
                                      "attemptstate": "Evaluation Status", "attempted": "Questions Attempted"},
                             inplace=True)
df_wavelist2 = df_wavelist.merge(Assignment_attempt_df, on=["userid", "Assignment ID", "batchid"], how="inner")

df_wavelist2.loc[df_wavelist2["Content Title"].isnull(), "Content Title"] = "N/A"
df_wavelist2.loc[df_wavelist2["Evaluation Status"].isnull(), "Evaluation Status"] = "EVALUATION PENDING"
df_wavelist2.loc[df_wavelist2["Questions Attempted"].isnull(), "Questions Attempted"] = 0.0
df_wavelist2.rename(columns={"userid": "userID", "E-mail": "User Email",
                             "groupname": "Active Group"}, inplace=True)
df_wavelist2.drop(
    columns=["sessionid", "MT Name", "Attendance", "stickiness", "quiz_asked", "quiz_attempt", "quiz_correct",
             "Enrollment Status",
             "session_date", "Wavebook ID", "Assignment ID"], inplace=True)
df_wavelist2.drop_duplicates(subset=["userID", "Content Title"], keep="first", inplace=True)
df_assignment_csv = df_wavelist2.drop(columns="batchid")

total_assignment_count = df_wavelist2[df_wavelist2["Evaluation Status"] == "EVALUATE_COMPLETE"]
total_assignment_count.drop(columns=["Questions Attempted", "Content Title"], inplace=True)

total_assignments_Solved = total_assignment_count.groupby(['userID', "User Email", "Student Name",
                                                           "Subject", 'Active Group', "batchid"])[
    "Evaluation Status"].count()

total_assignments_Solved.drop(columns=["batchid", "User Email", "Active Group", ], inplace=True)

df_assignment_csv.to_csv(f"Assignment_{batch_alphabet}_{date1_in}_to_{date2_in}.csv")

df_assignment_csv2 = df_wavelist2[df_wavelist2["Content Title"] != "N/A"]
df_assignment_vcoin = df_wavelist2.drop(columns=["Content Title",
                                                 "Evaluation Status"])
Assignment_attempt = df_assignment_vcoin["Questions Attempted"].tolist()
Assignment_coins = []
for i in Assignment_attempt:
    if i == 0:
        Assignment_coins.append(0)
    else:
        Assignment_coins.append(10)

df_assignment_vcoin["Assignment V coins"] = Assignment_coins

df_assignment_vcoin2 = df_assignment_vcoin.groupby(['userID', "User Email", "Student Name",
                                                    "Subject", 'Active Group', "batchid"]).sum()
df_assignment_vcoin3 = df_assignment_csv.groupby(['userID', "User Email", "Student Name",
                                                  "Subject", 'Active Group'])["Content Title"].count()
new2 = df_assignment_vcoin2.join(df_assignment_vcoin3, how='left')
new2.reset_index(inplace=True)

frame4.rename(columns={"userid": "userID", "E-mail": "User Email",
                       "groupname": "Active Group",
                       "Attendance Total": "Total Sessions"}, inplace=True)
final = frame4.merge(new2, on=['userID', "User Email",
                               "Student Name", "Subject", 'Active Group'],
                     how="outer")

final.rename(columns={"stickiness": "Total Stickiness",
                      "quiz_asked": "Total Quiz Asked", "quiz_attempt":
                          "Total Quiz Attempted",
                      "quiz_correct": "Total Quiz Corrected",
                      "Content Title": "Total Assignments Shared"},
             inplace=True)
final.fillna(0, inplace=True)
final.drop(columns=["batchid_x"], inplace=True)

test = pd.read_csv("assignments___test_attempts_ay_2022_23_2022-08-17T08_48_34.837927Z.csv",
                   usecols=["userid", "groupname", "batchid", "tests_shared", "tests_attempted"])

test.rename(columns={"userid": "userID", "groupname": "Active Group", "tests_shared": "Tests Shared",
                     "tests_attempted": "Tests Attempted"}, inplace=True)

testdata = frame4.merge(test, on=["userID", "Active Group", "batchid"], how="outer")
testdata.reset_index(inplace=True)
testdata.sort_values(by=["userID"], inplace=True)
testdata.drop(columns=["index", "batchid"], inplace=True)
testdata.fillna(0.0, inplace=True)
testdata = testdata[testdata.Subject != 0.0]
testdata = testdata[testdata.Subject != "Maths,Chemistry,Physics"]

testdata.drop(columns=["Attendance", "stickiness", "quiz_asked", "quiz_attempt",
                       "quiz_correct", "Total Sessions"], inplace=True)

final2 = final.merge(testdata, on=["userID", "Active Group", "Student Name", "User Email", "Subject"], how="outer")
final2.sort_values(by=["userID"], inplace=True)

final2["Average Stickiness Percentage"] = (final2["Total Stickiness"] / final2["Total Sessions"]) * 100
final2["Max Test Coins"] = final2["Tests Shared"].apply(lambda x: 0 if float(x) == 0.0 else 250)
final2["Max Assignment Coins"] = final2["Total Assignments Shared"].apply(lambda x: 0 if float(x) == 0.0 else 250)
final2["Max Quiz Coins"] = final2["Total Quiz Asked"].apply(lambda x: 0 if float(x) == 0.0 else 250)
final2["Max stickiness Coins"] = final2["Total Sessions"].apply(lambda x: 0 if float(x) == 0.0 else 250)
final2["Maximum V-Coins"] = final2["Max Test Coins"] + final2["Max Assignment Coins"] + final2["Max Quiz Coins"] + \
                            final2["Max stickiness Coins"]
final2["Test Attempt Percentage"] = final2["Tests Attempted"] / final2["Tests Shared"]
final2["Test Attempt Percentage"].fillna(0, inplace=True)

final2["Assignment Coins"] = final2["Assignment V coins"] / (10 * final2["Total Assignments Shared"])
final2["Quiz Accuracy"] = final2["Total Quiz Corrected"] / final2["Total Quiz Attempted"]
final2.fillna(0, inplace=True)

final2["Stickiness V-Coins"] = 2.5 * final2["Average Stickiness Percentage"]
final2["Quiz V-Coins"] = 125 * final2["Total Quiz Attempted"] / final2[
    "Total Quiz Asked"] + 125 * final2["Total Quiz Corrected"] / final2[
                             "Total Quiz Attempted"]
final2["Assignment V-Coins"] = 250 * final2["Assignment Coins"]
final2["Test V-Coins"] = 250 * final2["Test Attempt Percentage"]
final2["Quiz V-Coins"].fillna(0, inplace=True)
final2["V-Coins"] = final2["Stickiness V-Coins"] + final2["Quiz V-Coins"] + final2["Assignment V-Coins"] + final2[
    "Test V-Coins"]
final2["V-Coin Percentage"] = (final2["V-Coins"] / final2["Maximum V-Coins"]) * 100

v_coin_percentage = final2["V-Coin Percentage"].tolist()
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
final2["Ranking"] = ranking_list
final3 = final2.round({"V-Coins": 0})

df_final = final3.sort_values(["Student Name"], ascending=True)
df_final = df_final.merge(total_assignments_Solved, on=["userID", "Student Name", "Subject"], how="outer")
df_final.fillna(0, inplace=True)

userlist1 = df_assignment_csv["userID"].tolist()
userlist2 = df_final["userID"].tolist()
user_missing = []
for i in userlist2:
    if i not in userlist1:
        user_missing.append(i)
remove_dup = lambda numbers: list(set(numbers))
user_missing2 = remove_dup(user_missing)
missing_df = pd.DataFrame(user_missing2)
missing_df.to_csv("missing_userids.csv")

df_final = df_final.reindex(columns=["Student Name", "Active Group",
                                     "Subject", "Ranking", "V-Coins", "Maximum V-Coins",
                                     "V-Coin Percentage", "Attendance", "Total Sessions", "Total Assignments Shared",
                                     "Average Stickiness Percentage",
                                     "Total Quiz Asked", "Total Quiz Attempted",
                                     "Total Quiz Corrected", "Tests Shared", "Tests Attempted", "Stickiness V-Coins",
                                     "Quiz V-Coins", "Assignment V-Coins", "Test V-Coins", "userID",
                                     "Evaluation Status", "User Email"])
df_final = df_final.sort_values(["Student Name"])
df_final = df_final[df_final["Subject"] != "Maths,Chemistry,Physics"]
df_final.to_csv(f"Result_{batch_alphabet}_{date1_in}_to_{date2_in}.csv", index=False)
print("Thank You")