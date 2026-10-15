# ames-codex-handson

## Analysis question

Which Ames neighborhoods sell for more or less than their living area would predict?

**Codex session date:** October 15, 2026

## Final filtered results

I fit a simple linear regression predicting sale price from above-ground living area. Following the dataset documentation, I excluded the five houses with more than 4,000 square feet of living area from the regression. I kept neighborhoods with fewer than 10 sales in the regression, but left them out of the neighborhood table and chart so their small samples would not dominate the rankings. Among the remaining neighborhoods, StoneBr had the highest average residual ($90,907.59 above the model prediction) and SWISU had the lowest (-$61,901.78). The filtered model's slope was 116.225271 dollars per square foot, with an R² of 0.517627.

## Files in `analysis/`

- `.gitignore` — excludes the local Python environment and bytecode cache.
- `neighborhood_value.py` — fits the regression and creates the neighborhood summary and chart.
- `neighborhood_residuals.csv` — sales count, average sale price, and average residual by neighborhood.
- `neighborhood_residuals.png` — chart of average neighborhood residuals.
