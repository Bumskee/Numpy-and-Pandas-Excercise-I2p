import pandas as pd
import statistics as st
import matplotlib.pyplot as plt
import numpy as np
import datetime

#data to be referenced for the next few operations
data = pd.read_csv("activity.csv", sep = ",")

#counts the total of the missing values (Nan) from the data frame
Missing = sum(pd.isnull(data["steps"]))
print(f"The amount of missing values in this data frame is {Missing}.")

#creating the original dictionary that still contains the Nan values
Prob3_dict = {}
for date in data.date:
    if date not in Prob3_dict:
        Prob3_dict[date] = []
        for steps in data.steps[data.date == date]:
            Prob3_dict[date].append(steps)

#Prepare another dictionary that will then be replaced with the new data (after inputting the nan values)
Prob3_replaced = Prob3_dict

#Check the first 7 keys from the dictionary. If the value of those keys are a nan value it will then compare itself with the same next day(s)
#Value of nan will be replaced by the average of the sum of its value, its next value, and a value before it.
#Exception for the first and the last value since both doesn't have a value before it and after it respectively.
for keys in range(len(list(Prob3_replaced.keys())[:7])):
    for items in range(len(Prob3_replaced[list(Prob3_replaced)[keys]])):
        if pd.isnull(Prob3_replaced[list(Prob3_replaced)[keys]][items]):
            if items == 0:
                check = 1
                while pd.isnull(Prob3_replaced[list(Prob3_replaced)[keys]][items]) and check < 5:
                    Prob3_replaced[list(Prob3_replaced)[keys]][items] = np.floor((Prob3_replaced[list(Prob3_replaced)[keys + (check * 7)]][items] + Prob3_replaced[list(Prob3_replaced)[keys + (check * 7)]][items + 1] + Prob3_replaced[list(Prob3_replaced)[keys + (check * 7)]][items + 2]) / 3)
                    check += 1
            else : 
                if items == 287:
                    check = 1
                    while pd.isnull(Prob3_replaced[list(Prob3_replaced)[keys]][items]) and check < 5:
                        Prob3_replaced[list(Prob3_replaced)[keys]][items] = np.floor((Prob3_replaced[list(Prob3_replaced)[keys + (check * 7)]][items] + Prob3_replaced[list(Prob3_replaced)[keys + (check * 7)]][items - 1] + Prob3_replaced[list(Prob3_replaced)[keys + (check * 7)]][items - 2]) / 3)
                        check += 1
                else:
                    check = 1
                    while pd.isnull(Prob3_replaced[list(Prob3_replaced)[keys]][items]) and check < 5:
                        Prob3_replaced[list(Prob3_replaced)[keys]][items] = np.floor((Prob3_replaced[list(Prob3_replaced)[keys + (check * 7)]][items] + Prob3_replaced[list(Prob3_replaced)[keys + (check * 7)]][items - 1] + Prob3_replaced[list(Prob3_replaced)[keys + (check * 7)]][items + 1]) / 3)
                        check += 1   

#Check the rest of the value of the dictionary. If the value of those keys are a nan value it will then compare itself with same day before it.
#Value of nan will be replaced by the average of the sum of its value, its next value, and a value before it.
#Exception for the last value since it doesn't have any value after it.
for keys in range(len(list(Prob3_replaced.keys())))[7::]:
    for items in range(len(Prob3_replaced[list(Prob3_replaced)[keys]])):
        if pd.isnull(Prob3_replaced[list(Prob3_replaced)[keys]][items]):
            if items == 287:
                Prob3_replaced[list(Prob3_replaced)[keys]][items] = np.floor((Prob3_replaced[list(Prob3_replaced)[keys - 7]][items] + Prob3_replaced[list(Prob3_replaced)[keys - 7]][items - 1] + Prob3_replaced[list(Prob3_replaced)[keys - 7]][items - 2]) / 3)
            else:
                Prob3_replaced[list(Prob3_replaced)[keys]][items] = np.floor((Prob3_replaced[list(Prob3_replaced)[keys - 7]][items] + Prob3_replaced[list(Prob3_replaced)[keys - 7]][items - 1] + Prob3_replaced[list(Prob3_replaced)[keys - 7]][items + 1]) / 3)

#The Prob3_replaced now is the initial dictionary but with all the nan values replaced.

#array that is going to be used for making the histogram
Prob3_mean = []
for keys in Prob3_replaced:
    Prob3_mean += int(np.floor((np.mean(Prob3_replaced[keys])))) * [keys]

#dictionary for the mean and median report
Prob3_data = {}
for date in Prob3_replaced:
    Prob3_data[date] = f"mean = {np.nanmean(Prob3_replaced[date])}, median = {np.nanmedian(sorted(Prob3_replaced[date]))}"

#Reporting the mean and median of steps from each date
for key,values in Prob3_data.items():
    print(key)
    print(values.replace(", ", "\n"))

#Creating the histogram of the average steps taken each day with the new nan values filled
AverageStepsPerDayNew, ax = plt.subplots()
ax.hist(Prob3_mean)
ax.set_xlabel("Day")
ax.set_ylabel("Steps")
ax.set_title("Average steps taken per day (nan values filled in)") 

#Creates empty dictionaries that will be filled with the filtered data from Prob3_replaced
Prob4_weekdays = {}
Prob4_weekends = {}

#Filtering which are weekends and which are weekdays
for keys in Prob3_replaced:
    if datetime.datetime.strptime(keys, "%Y-%m-%d").weekday() < 5:
        Prob4_weekdays[keys] = np.floor(np.mean(Prob3_replaced[keys]))
    else:
        Prob4_weekends[keys] = np.floor(np.mean(Prob3_replaced[keys]))

#Plotting for weekends
AverageStepsWeekEnd, ax2 = plt.subplots()
ax2.bar(list(Prob4_weekends.keys()), Prob4_weekends.values())
ax2.set_xlabel("Day")
ax2.set_ylabel("Steps")
ax2.set_title("Average steps taken per day (weekends)")

#Plotting for Weekdays
AverageStepsWeekDay, ax3 = plt.subplots()
ax3.bar(list(Prob4_weekdays.keys()), Prob4_weekdays.values())
ax3.set_xlabel("Day")
ax3.set_ylabel("Steps")
ax3.set_title("Average steps taken per day (weekday)")
plt.show()