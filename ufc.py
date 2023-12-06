#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("data.csv")


# In[3]:


df.describe()


# In[5]:


df["year"]=pd.DatetimeIndex(df["date"]).year
df["total_STR_landed"] = df["R_avg_SIG_STR_landed"]+df["B_avg_SIG_STR_landed"]
df["total_avg_LEG_landed"] = df["R_avg_LEG_landed"]+df["B_avg_LEG_landed"]


# In[6]:


data = [[],[],[]]
for i in range(len(df["year"])-1):
    if(df["year"].values[i] != df["year"].values[i+1]):
        data[0].append(df["year"][i])
# add the last element
data[0].append(df["year"].values[-1])
for i in range(len(data[0])):
    data[1].append(df.loc[df["year"] == int(data[0][i])]["total_avg_LEG_landed"].sum())
for i in range(len(data[0])):
    data[2].append(df.loc[df["year"] == int(data[0][i])]["total_STR_landed"].sum())
analytics_df = pd.DataFrame(data).transpose()
analytics_df.columns = ["years","total_avg_LEG_landed","total_avg_STR_landed"]
analytics_df.plot(x="years",y=["total_avg_STR_landed","total_avg_LEG_landed"])


# In[7]:


df[["R_avg_SIG_STR_landed","B_avg_SIG_STR_landed"]].describe()


# In[8]:


analytics_df.loc[(analytics_df["total_avg_STR_landed"] == analytics_df["total_avg_STR_landed"].max()) & (analytics_df["total_avg_LEG_landed"] == analytics_df["total_avg_LEG_landed"].max())]


# In[9]:


analytics_df.sort_values(by=["years","total_avg_LEG_landed","total_avg_STR_landed"]).plot("years","total_avg_STR_landed",xlabel="Year",ylabel="Total average significant strikes landed",figsize=[10,4],kind="bar",title="Total Significant Strikes in UFC from 1994-2021")


# In[10]:


df[["total_STR_landed","total_avg_LEG_landed"]].value_counts()


# In[11]:


color = ["red"] * (df.shape[0]+1) + ["blue"] * (df.shape[0]+1)
plot_color = df["Winner"].apply(lambda x: "red" if x == "Red" else "blue" if x == "Blue" else "yellow")


# In[12]:


df.plot(x="R_avg_TOTAL_STR_landed",y="B_avg_TOTAL_STR_landed",c=plot_color,kind="scatter",xlabel="Total Strike landed by Red",ylabel="Total Strike landed by Blue",figsize=[10,5])
plt.xlim(0)
plt.ylim(0)
legend_labels = {"Red": "Red", "Blue": "Blue", "Draw": "Yellow"}
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=legend_labels[label], markersize=10) for label in legend_labels]
plt.title("Fight Result in UFC with Strikes as a Base value")
plt.legend(handles=handles, labels=legend_labels, title="Winner")
plt.text(x=226.2864997558594,y=101.222421973876953,s="Holloway vs Poirier",fontdict=dict(color="black",size=7))
# Show the plot
plt.show()


# In[13]:


df.loc[(df["B_fighter"] == "Max Holloway") | (df["R_fighter"] == "Max Holloway")][["R_avg_TOTAL_STR_landed","B_avg_TOTAL_STR_landed"]]


# In[14]:


df["R_avg_LEG_landed"].max()


# In[15]:


df.loc[(df["R_avg_LEG_landed"]==62.3515625)|(df["B_avg_LEG_landed"]==51.635986328125)]


# In[16]:


analytics_df.sort_values(by=["years","total_avg_LEG_landed","total_avg_STR_landed"]).plot("years","total_avg_LEG_landed",xlabel="Year",ylabel="Total Average Calf Kick Landed",figsize=[10,4],kind="bar",title="Calf Kick Usage in UFC from 1994-2021")


# In[16]:


max(data[2])


# In[17]:


df.loc[(df["R_fighter"]=="Jon Jones") | (df["B_fighter"]=="Jon Jones")].sort_values(by=["year","total_avg_LEG_landed"]).plot("year","total_avg_LEG_landed",xlabel="Year",ylabel="Total Average Calf Kick Landed (Jon Jones Fight)",figsize=[10,4],kind="bar",title="Calf Kick Usage in UFC base on Jon Jones fight from 2008-2021")


# In[ ]:




