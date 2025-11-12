import matplotlib.pyplot as plt

runs = ["Run-1", "Run-2", "Run-3", "Run-4", "Run-5"]
traditional_energy = [100, 98, 95, 93, 90]
proposed_energy = [85, 78, 73, 70, 68]

plt.figure(figsize=(8, 5))
plt.plot(runs, traditional_energy, marker='o', color='red', linewidth=2, label="Traditional Model")
plt.plot(runs, proposed_energy, marker='o', color='green', linewidth=2, label="Proposed EADS Model")

plt.title("Figure 4.2: Energy Consumption Trend Across Simulation Runs")
plt.xlabel("Simulation Runs")
plt.ylabel("Energy Consumption (Joules)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

