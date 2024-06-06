from pathlib import Path
import csv 
import matplotlib.pyplot as plt
from datetime import datetime
path = Path("weather_data\\sitka_weather_07-2021_simple.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
dates,highs = [],[]
# Extract high temps

for row in reader:
    current_date = datetime.strptime(row[2],"%Y-%m-%d")
    high = int(row[5])
    dates.append(current_date)
    highs.append(high)

plt.style.use("Solarize_Light2")
fig,ax = plt.subplots()
ax.plot(dates,highs,color = "red")
ax.set_title("Temps in july 2021",fontsize = 24)
ax.set_xlabel("",fontsize  = 12)
ax.set_ylabel("Temps in (C) celsius for JUlY 2021",fontsize = 14)
ax.tick_params(labelsize =14)
# for index,temp in enumerate(highs):
#     print(f"{index}: {temp}oC")
fig.autofmt_xdate()
plt.show()