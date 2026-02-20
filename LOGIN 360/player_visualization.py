import pandas as pd
import matplotlib.pyplot as plt

# 🧠 Example Data — replace this with your real data
data = {
    'Player': ['Shohei Ohtani', 'Aaron Judge', 'Mike Trout', 'Mookie Betts'],
    'Batting Average': [0.304, 0.287, 0.290, 0.311],
    'Home Runs': [44, 62, 40, 39],
    'RBIs': [95, 131, 83, 107],
    'OPS': [1.066, 1.111, 0.999, 0.987]  # On-base + Slugging %
}

df = pd.DataFrame(data)

# 🎨 1️⃣ Bar chart comparing Home Runs
plt.figure(figsize=(10, 6))
plt.bar(df['Player'], df['Home Runs'], color='skyblue', edgecolor='black')
plt.title('Home Run Comparison', fontsize=16, fontweight='bold')
plt.xlabel('Player', fontsize=12)
plt.ylabel('Home Runs', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# 🎨 2️⃣ Batting Average Comparison
plt.figure(figsize=(10, 6))
plt.bar(df['Player'], df['Batting Average'], color='lightgreen', edgecolor='black')
plt.title('Batting Average Comparison', fontsize=16, fontweight='bold')
plt.xlabel('Player', fontsize=12)
plt.ylabel('Batting Average', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# 🎨 3️⃣ Multi-metric Line Chart
metrics = ['Batting Average', 'Home Runs', 'RBIs', 'OPS']
plt.figure(figsize=(10, 6))

for metric in metrics:
    plt.plot(df['Player'], df[metric], marker='o', label=metric)

plt.title('Overall Player Performance Comparison', fontsize=16, fontweight='bold')
plt.xlabel('Player', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
