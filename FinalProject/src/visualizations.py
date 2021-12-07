# Programmer: Raul Martinez Luna Date: 12/7/21

#Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#csv --> DataFrame
df = pd.read_csv("../Data/googleplaystore.csv")

#Cleans Installs by eliminating everything in the string except numbers
df["Installs"] = df['Installs'].str.replace(r'\D','')

#["Installs"] String --> Float
df["Installs"] = pd.to_numeric(df["Installs"])

#Gives a list of index' of all "Varies with device" strings in ["Size"]
index = 0
remIndexList = []
for string in df["Size"]:
    if string == "Varies with device":
        remIndexList.append(index)
    index+=1

#Drops list of rows with "Varies with device" strings in the Data Frame
df.drop(df.index[remIndexList], inplace=True)

#Resets index'
df.reset_index(drop=True, inplace=True)

#Makes two copies of Data Frame
dfCopy1 = df.copy(deep=True)
dfCopy2 = df.copy(deep=True)

#Gives a list of index' of all numbers with decimals strings in ["Size"]
index = 0
remIndexList.clear()
for string in dfCopy1["Size"]:
    if "." in string:
        remIndexList.append(index)
    index+=1

#Drops list of rows with decimals in the first copy of the Data Frame
dfCopy1.drop(dfCopy1.index[remIndexList], inplace=True)

#CLeans up strings in ["Size"]
dfCopy1["Size"] = dfCopy1["Size"].str.replace('k','000')
dfCopy1["Size"] = dfCopy1["Size"].str.replace('M','000000')

#Makes a list of all index' in the first copy of Data Frame
nonDecNums = list(dfCopy1.index.values)

#Drops all non-decimal strings from the second copy of the Data Frame by using newly made list
dfCopy2.drop(dfCopy2.index[nonDecNums], inplace=True)

#Cleans second copy of Data Frame and cleans up string
for i in range(10):
    repStringM = '.'+str(i)+'M'
    repStringK = '.'+str(i)+'k'
    stringToM = str(i)+'00000'
    stringToK = str(i)+'00'
    dfCopy2["Size"] = dfCopy2["Size"].str.replace(repStringM, stringToM)
    dfCopy2["Size"] = dfCopy2["Size"].str.replace(repStringK, stringToK)

#Swaps rows from the first and second copy into the original Data Frame
df.loc[dfCopy1.index, :] = dfCopy1[:]
df.loc[dfCopy2.index, :] = dfCopy2[:]

#Converts ["Size"]; String --> Float
df["Size"] = pd.to_numeric(df["Size"], errors='coerce')

#-------------------------------------------------------------------------------------------------

#Visualizations

#Size & Rating
ax = sns.regplot(data=df, x="Size", y="Rating", scatter=False)
plt.title("Correlation between Size and Rating")
plt.show()

#Correlation
x1 = df["Size"]
y1 = df["Rating"]
print(y1.corr(x1))

#Size & Installs
ax = sns.regplot(data=df, x="Size", y="Installs", scatter=False)
plt.title("Correlation between Size and Installs")
plt.show()

#Correlation
x2 = df["Size"]
y2 = df["Installs"]
print(y2.corr(x2))

#Installs & Rating
ax = sns.regplot(data=df, x="Installs", y="Rating", scatter=False)
plt.title("Correlation between Installs and Rating")
plt.show()

#Correlation
x3 = df["Installs"]
y3 = df["Rating"]
print(y3.corr(x3))


