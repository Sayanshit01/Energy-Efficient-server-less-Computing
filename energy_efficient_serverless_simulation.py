import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import os

# =============================
# 1️⃣ SIMULATION CONFIGURATION
# =============================
num_tasks = 200
cloud_energy_cost = 2.5   # Joules per ms
edge_energy_cost = 1.2
cloud_latency_factor = 1.5
edge_latency_factor = 0.7

np.random.seed(42)

# Random workload generation
tasks = pd.DataFrame({
    'Task_ID': range(1, num_tasks + 1),
    'CPU_Required': np.random.randint(10, 100, num_tasks),
    'Execution_Time': np.random.randint(50, 500, num_tasks),
    'Priority': np.random.randint(1, 4, num_tasks)
})

# =============================
# 2️⃣ TRADITIONAL SCHEDULING
# =============================
rr_energy, rr_latency, rr_cpu_util, rr_throughput = [], [], [], []

for _, row in tasks.iterrows():
    node_type = random.choice(["cloud", "edge"])
    energy = row["Execution_Time"] * (cloud_energy_cost if node_type == "cloud" else edge_energy_cost)
    latency = row["Execution_Time"] * (cloud_latency_factor if node_type == "cloud" else edge_latency_factor)
    cpu_util = random.uniform(55, 75) if node_type == "cloud" else random.uniform(50, 70)
    throughput = 1000 / latency
    rr_energy.append(energy)
    rr_latency.append(latency)
    rr_cpu_util.append(cpu_util)
    rr_throughput.append(throughput)

# =============================
# 3️⃣ PROPOSED EADS MODEL
# =============================
eads_energy, eads_latency, eads_cpu_util, eads_throughput = [], [], [], []

for _, row in tasks.iterrows():
    if row["Priority"] == 1 or row["Execution_Time"] < 250:
        node_type = "edge"
    else:
        node_type = "cloud"

    energy = row["Execution_Time"] * (cloud_energy_cost if node_type == "cloud" else edge_energy_cost)
    latency = row["Execution_Time"] * (cloud_latency_factor if node_type == "cloud" else edge_latency_factor)
    cpu_util = random.uniform(75, 90) if node_type == "cloud" else random.uniform(70, 85)
    throughput = 1000 / latency
    eads_energy.append(energy)
    eads_latency.append(latency)
    eads_cpu_util.append(cpu_util)
    eads_throughput.append(throughput)

# =============================
# 4️⃣ RESULT AGGREGATION
# =============================
results = pd.DataFrame({
    "Metric": ["Energy (J)", "Latency (ms)", "CPU Utilization (%)", "Throughput (req/sec)"],
    "Traditional": [
        np.mean(rr_energy),
        np.mean(rr_latency),
        np.mean(rr_cpu_util),
        np.mean(rr_throughput)
    ],
    "EADS": [
        np.mean(eads_energy),
        np.mean(eads_latency),
        np.mean(eads_cpu_util),
        np.mean(eads_throughput)
    ]
})

print("===== Simulation Results =====")
print(results.to_string(index=False))

# Save CSV
output_csv = "simulation_results.csv"
results.to_csv(output_csv, index=False)
print(f"\n✅ Results saved as: {output_csv}")

# =============================
# 5️⃣ VISUALIZATION
# =============================
metrics = results["Metric"]
traditional = results["Traditional"]
proposed = results["EADS"]

x = np.arange(len(metrics))
width = 0.35

plt.figure(figsize=(10, 6))
bars1 = plt.bar(x - width/2, traditional, width, label='Traditional', color='#d9534f')
bars2 = plt.bar(x + width/2, proposed, width, label='Proposed (EADS)', color='#5cb85c')

plt.ylabel('Average Values')
plt.title('Performance Comparison: Traditional vs Proposed (EADS)')
plt.xticks(x, metrics, rotation=15)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Annotate bars
for bar in bars1 + bars2:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.02*yval, f'{yval:.2f}', ha='center', va='bottom', fontsize=8)

# Save graph
graph_path = "performance_comparison.png"
plt.tight_layout()
plt.savefig(graph_path)
print(f"📊 Graph saved as: {graph_path}")
plt.show()
