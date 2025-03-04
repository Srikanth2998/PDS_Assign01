import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

RAW_FILE = 'raw_data.csv'
CLEAN_FILE = 'clean_data.csv'
PLOT_FOLDER = 'plots'
SUMMARY_FILE = 'summary.txt'

os.makedirs(PLOT_FOLDER, exist_ok=True)

df = pd.read_csv(RAW_FILE)
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
df = df.dropna()

df.to_csv(CLEAN_FILE, index=False)

sns.histplot(df['math_score'])
plt.title('Math Score Distribution')
plt.savefig(f'{PLOT_FOLDER}/math_score_distribution.png')
plt.close()

sns.barplot(x='parental_level_of_education', y='math_score', data=df)
plt.title('Math Score by Parental Education')
plt.xticks(rotation=45)
plt.savefig(f'{PLOT_FOLDER}/math_score_by_education.png')
plt.close()

sns.barplot(x='lunch', y='math_score', data=df)
plt.title('Math Score by Lunch Type')
plt.savefig(f'{PLOT_FOLDER}/math_score_by_lunch.png')
plt.close()

sns.barplot(x='test_preparation_course', y='math_score', data=df)
plt.title('Math Score by Test Preparation')
plt.savefig(f'{PLOT_FOLDER}/math_score_by_test_prep.png')
plt.close()

sns.barplot(x='gender', y='math_score', data=df)
plt.title('Math Score by Gender')
plt.savefig(f'{PLOT_FOLDER}/math_score_by_gender.png')
plt.close()

with open(SUMMARY_FILE, 'w') as f:
    f.write("Summary - Student Performance Data\n\n")
    f.write(f"Total Rows: {len(df)}\n\n")
    f.write(f"Average Math Score: {df['math_score'].mean():.2f}\n\n")
    f.write("Plots are saved in plots folder.\n")