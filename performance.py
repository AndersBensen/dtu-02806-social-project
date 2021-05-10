import time 
import pandas as pd 

start = time.time()
df = pd.read_csv("data/Motor_Vehicle_Collisions_-_Crashes.csv",low_memory=False)
df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'], format="%m/%d/%Y")
df['CRASH TIME'] = pd.to_datetime(df['CRASH TIME'], format="%H:%M")
end = time.time()
print(end-start)