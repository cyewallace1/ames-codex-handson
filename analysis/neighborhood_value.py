"""Regress Ames sale prices on above-ground living area and summarize residuals."""

from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent.parent
ANALYSIS_DIR = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(ANALYSIS_DIR / ".mplconfig"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import numpy as np
import pandas as pd


DATA_PATH = ROOT / "AmesHousing.csv"
OUTPUT_PATH = ANALYSIS_DIR / "neighborhood_residuals.csv"
PLOT_PATH = ANALYSIS_DIR / "neighborhood_residuals.png"


def main() -> None:
    data = pd.read_csv(DATA_PATH)
    # Keep low-count neighborhoods in the overall fit, but exclude the documented
    # large-home outliers from both the regression and neighborhood summaries.
    data = data.loc[data["Gr Liv Area"] <= 4000].copy()
    x = data["Gr Liv Area"].to_numpy(dtype=float)
    y = data["SalePrice"].to_numpy(dtype=float)

    slope, intercept = np.polyfit(x, y, 1)
    predicted = slope * x + intercept
    residuals = y - predicted
    r_squared = 1 - np.sum(residuals**2) / np.sum((y - y.mean()) ** 2)

    data = data.assign(_residual=residuals)
    summary = (
        data.groupby("Neighborhood", as_index=False)
        .agg(
            sales_count=("SalePrice", "size"),
            average_price=("SalePrice", "mean"),
            average_residual=("_residual", "mean"),
        )
        .loc[lambda frame: frame["sales_count"] >= 10]
        .sort_values("average_residual", ascending=False)
    )
    summary.to_csv(OUTPUT_PATH, index=False, float_format="%.2f")

    plot_data = summary.sort_values("average_residual", ascending=False)
    fig_height = max(6, 0.28 * len(plot_data))
    fig, ax = plt.subplots(figsize=(10, fig_height))
    colors = np.where(plot_data["average_residual"] >= 0, "#4472C4", "#D9534F")
    ax.barh(plot_data["Neighborhood"], plot_data["average_residual"], color=colors)
    ax.invert_yaxis()
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlabel("Average sale price residual")
    ax.xaxis.set_major_formatter(StrMethodFormatter("${x:,.0f}"))
    ax.set_ylabel("Neighborhood")
    ax.set_title("Average price residual by neighborhood")
    fig.tight_layout()
    fig.savefig(PLOT_PATH, dpi=150)
    plt.close(fig)

    print(f"Slope: {slope:.6f}")
    print(f"Intercept: {intercept:.6f}")
    print(f"R squared: {r_squared:.6f}")
    print(f"Saved neighborhood summary to {OUTPUT_PATH}")
    print(f"Saved residual plot to {PLOT_PATH}")


if __name__ == "__main__":
    main()
