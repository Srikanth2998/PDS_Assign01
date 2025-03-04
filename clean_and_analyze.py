import pandas as pd
import matplotlib.pyplot as plt
import os

RAW_FILE = 'data_raw.csv'
CLEAN_FILE = 'data_clean.csv'
PLOT_FOLDER = 'analysis_output'
SUMMARY_FILE = 'summary.txt'

os.makedirs(PLOT_FOLDER, exist_ok=True)

df = pd.read_csv(RAW_FILE)
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
df = df.dropna()

df.to_csv(CLEAN_FILE, index=False)

df.boxplot(column='grip_strength', by='frailty', grid=False)
plt.title('Grip Strength by Frailty')
plt.suptitle('')
plt.savefig(f'{PLOT_FOLDER}/grip_vs_frailty.png')
plt.close()

plt.scatter(df['age'], df['grip_strength'])
plt.title('Grip Strength vs Age')
plt.xlabel('Age')
plt.ylabel('Grip Strength')
plt.savefig(f'{PLOT_FOLDER}/grip_vs_age.png')
plt.close()

with open(SUMMARY_FILE, 'w') as f:
    f.write("Summary - Frailty Data\n\n")
    f.write(f"Total Rows: {len(df)}\n\n")
    f.write("Average Grip Strength by Frailty:\n")
    f.write(df.groupby('frailty')['grip_strength'].mean().to_string())
    f.write("\n\nPlots are saved in analysis_output folder.\n")