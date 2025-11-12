import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Define simulation parameters
num_tasks = 100
cloud_nodes = 3
edge_nodes = 3

# Generate random workload data
np.random.seed(42)
tasks = pd.DataFrame({
    'Task_ID': range(1, num_tasks+1),
    'CPU_Required': np.random.randint(10, 100, num_tasks),
    'Execution_Time': np.random.randint(50, 500, num_tasks),
    'Priority': np.random.randint(1, 4, num_tasks),  # 1=high, 3=low
})

# Define node characteristics
cloud_energy_cost = 2.5   # J per ms
edge_energy_cost = 1.2    # J per ms
cloud_latency = 1.5
edge_latency = 0.7

# Traditional Round Robin Scheduling
rr_energy = []
rr_latency = []

for _, row in tasks.iterrows():
    node_type = random.choice(["cloud", "edge"])
    energy = row["Execution_Time"] * (cloud_energy_cost if node_type == "cloud" else edge_energy_cost)
    latency = row["Execution_Time"] * (cloud_latency if node_type == "cloud" else edge_latency)
    rr_energy.append(energy)
    rr_latency.append(latency)

# Proposed Energy-Aware Dynamic Scheduler (EADS)
eads_energy = []
eads_latency = []

for _, row in tasks.iterrows():
    # If high priority or short job -> send to edge
    if row["Priority"] == 1 or row["Execution_Time"] < 250:
        node_type = "edge"
    else:
        node_type = "cloud"

    # Reduce energy if executed at edge
    energy = row["Execution_Time"] * (cloud_energy_cost if node_type == "cloud" else edge_energy_cost)
    latency = row["Execution_Time"] * (cloud_latency if node_type == "cloud" else edge_latency)
    eads_energy.append(energy)
    eads_latency.append(latency)

# Compute results
rr_avg_energy = np.mean(rr_energy)
eads_avg_energy = np.mean(eads_energy)
rr_avg_latency = np.mean(rr_latency)
eads_avg_latency = np.mean(eads_latency)

print("===== Simulation Results =====")
print(f"Average Energy Consumption (Traditional): {rr_avg_energy:.2f} J")
print(f"Average Energy Consumption (EADS): {eads_avg_energy:.2f} J")
print(f"Average Latency (Traditional): {rr_avg_latency:.2f} ms")
print(f"Average Latency (EADS): {eads_avg_latency:.2f} ms")

# Visualization
labels = ['Energy Consumption (J)', 'Latency (ms)']
traditional = [rr_avg_energy, rr_avg_latency]
proposed = [eads_avg_energy, eads_avg_latency]

x = np.arange(len(labels))
width = 0.35

plt.figure(figsize=(8, 5))
plt.bar(x - width/2, traditional, width, label='Traditional', color='#d9534f')
plt.bar(x + width/2, proposed, width, label='Proposed (EADS)', color='#5cb85c')
plt.xticks(x, labels)
plt.ylabel('Average Values')
plt.title('Performance Comparison')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
