import matplotlib.pyplot as plt
import numpy as np

models = [
    "Baseline",
    "Optimized",
    "Ensemble Averaging",
    "Ensemble Bagging"
]

rmse = [
    0.7487715098504877,
    0.75140560577774,
    0.8016135577287999,
    0.7528708446849643
]

mae = [
    0.6320879453542282,
    0.6338136159157267,
    0.5862740615922577,
    0.6309838448738566
]

x = np.arange(len(models))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

rmse_bars = ax.bar(
    x - width / 2,
    rmse,
    width,
    label="RMSE",
    color="#1B365D"
)

mae_bars = ax.bar(
    x + width / 2,
    mae,
    width,
    label="MAE",
    color="#2D6A4F"
)

ax.set_title("Model Performance Comparison")
ax.set_xlabel("Model Configuration")
ax.set_ylabel("Error")

ax.set_xticks(x)
ax.set_xticklabels(models)

ax.legend()

ax.bar_label(
    rmse_bars,
    fmt="%.3f",
    padding=3
)

ax.bar_label(
    mae_bars,
    fmt="%.3f",
    padding=3
)

plt.xticks(rotation=10)
plt.tight_layout()

plt.savefig(
    "model-performance-comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()