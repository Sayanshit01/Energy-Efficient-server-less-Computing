import matplotlib.pyplot as plt
import numpy as np

# Data for charts
metrics = ["Energy Consumption", "Average Latency", "Cold Start Frequency", "CPU Utilization", "Throughput"]
traditional = [100, 420, 25, 75, 145]
proposed = [68, 280, 9, 85, 195]

x = np.arange(len(metrics))
width = 0.35

# Bar chart
plt.figure(figsize=(10, 6))
bars1 = plt.bar(x - width/2, traditional, width, label='Traditional Model', color='#d9534f')
bars2 = plt.bar(x + width/2, proposed, width, label='Proposed EADS Model', color='#5cb85c')

# Labels, title, and legend
plt.ylabel('Performance Metrics (Scaled Values)')
plt.title('Figure 4.1: Performance Comparison – Traditional vs Proposed EADS Model')
plt.xticks(x, metrics, rotation=20)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Annotate bars
for bar in bars1 + bars2:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 3, f'{yval}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()

