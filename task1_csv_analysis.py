import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the CSV file
df = pd.read_csv("StudentsPerformance.csv")

# Step 2: Display the first few rows
print("\n📊 First 5 rows of the dataset:")
print(df.head())

# Step 3: Summary statistics
print("\n📈 Dataset Statistics:")
print(df.describe())

# Step 4: Calculate averages
avg_math = df['math score'].mean()
avg_reading = df['reading score'].mean()
avg_writing = df['writing score'].mean()

print("\n✅ AVERAGE SCORES:")
print(f"Math: {avg_math:.2f}")
print(f"Reading: {avg_reading:.2f}")
print(f"Writing: {avg_writing:.2f}")

# Step 5: Bar chart - Average scores comparison
plt.figure(figsize=(6,4))
plt.bar(['Math', 'Reading', 'Writing'], [avg_math, avg_reading, avg_writing], color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Average Scores of Students')
plt.ylabel('Score')
plt.tight_layout()
plt.show()

# Step 6: Scatter plot - Math vs Reading
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x='math score', y='reading score', hue='gender')
plt.title('Math Score vs Reading Score (by Gender)')
plt.tight_layout()
plt.show()

# Step 7: Heatmap - Correlation between scores
plt.figure(figsize=(6,4))
score_corr = df[['math score', 'reading score', 'writing score']].corr()
sns.heatmap(score_corr, annot=True, cmap='coolwarm')
plt.title('Correlation Between Scores')
plt.tight_layout()
plt.show()
print("CSV Analysis Complete!")

