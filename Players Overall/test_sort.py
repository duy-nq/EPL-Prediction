import pandas as pd
#15 means 14-15
# Đọc dữ liệu từ file CSV
file_path = "players_overall_1516_2223.csv"
df = pd.read_csv(file_path)

# Sắp xếp theo cột "1516"
df_sorted = df.sort_values(by="1516")
df_sorted.to_csv("du_lieu_sap_xep.csv", index=False)
