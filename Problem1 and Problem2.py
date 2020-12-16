import pandas as pd
import statistics as st
import matplotlib.pyplot as plt
import numpy as np

#Problem 1 : Creating a histogram of the total number of steps taken each day and getting the mean and median of steps of each day.

#data to be referenced for the next few operations
data = pd.read_csv("activity.csv", sep = ",")

#Converts the dataframe into a dictionary
Prob1_dict = {}
for date in data.date:
    if date not in Prob1_dict:
        Prob1_dict[date] = []
        for steps in data.steps[data.date == date]:
            Prob1_dict[date].append(steps)

#Creates a new dictionary with the mean of the steps per day
Prob1_mean = []
for keys in Prob1_dict:
    if np.isnan(np.nanmean(Prob1_dict[keys])):
        Prob1_mean += 0 * [keys]
    else:
        Prob1_mean += int(np.floor(np.nanmean(Prob1_dict[keys]))) * [keys]

#Creates a new dictionary with the mean and the median of the steps per day to then be reported in the console
Prob1_data = {}
for date in Prob1_dict:
    Prob1_data[date] = f"mean = {np.nanmean(Prob1_dict[date])}, median = {np.nanmedian(sorted(Prob1_dict[date]))}"

#Prints the report of the mean and median into the console
print("Problem 1 =======================================================================================================")
for key,values in Prob1_data.items():
    print(key)
    print(values.replace(", ", "\n"))

#Creates the historgram for the average amount of steps taken each day
AverageStepsPerDay, ax = plt.subplots()
ax.hist(Prob1_mean)
ax.set_xlabel("Day")
ax.set_ylabel("Steps")
ax.set_title("Average steps taken per day")

#Problem 2 : Creating a histogram of the average steps per interval and getting the largest amount of steps recorded in an interval 

#Creates a new dictionary with the key being the hours of the day and the values being the steps taken each day
Prob2_dict = {}
for hour in data.interval:
    if hour not in Prob2_dict:
        Prob2_dict[hour] = []
        for steps in data.steps[data.interval == hour]:
            Prob2_dict[hour].append(steps)

#Creates a new dictionary with the value of the average steps taken each hour
Prob2_mean = []
for keys in Prob2_dict:
    if np.isnan(np.nanmean(Prob2_dict[keys])):
        Prob2_mean += 0 * [keys]
    else:
        Prob2_mean += int(np.floor(np.nanmean(Prob2_dict[keys]))) * [keys]

#Calculates which is the hour with the larges average steps 
maxStepsInInterval = 0
for keys in Prob2_dict:
    if (np.nansum(Prob2_dict[keys])) > maxStepsInInterval:
        maxStepsInInterval = np.nansum(Prob2_dict[keys])
        Hours = keys

#Reports the largest average and creates the histogram fo the average steps taken per interval
print("\nProblem 2 =======================================================================================================")
print(f"The max steps in an interval across all day is {maxStepsInInterval} at hour {Hours}.")
AverageStepsPerInterval, ax = plt.subplots()
ax.hist(Prob2_mean)
ax.set_xlabel("Hour")
ax.set_ylabel("Steps")
ax.set_title("Average steps taken per interval")
plt.show()