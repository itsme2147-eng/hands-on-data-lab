# Hands-On Data Lab Implementation

Task 2 of the AI/ML Research Specialist virtual internship (Yuva Intern, Thiruvananthapuram).
A reproducible data-analysis lab using Python, NumPy, Pandas, Matplotlib, Seaborn and Scikit-learn
on a synthetic retail dataset (customers, products, orders) with deliberately messy data.

## Objective -> where covered
| # | Objective | Location |
|---|-----------|----------|
| 1 | Set up the environment | `SETUP.md`, `requirements.txt`, `environment.yml`, `src/check_environment.py`, notebook Part 1 |
| 2 | Pandas and NumPy | notebook Parts 2A and 2B |
| 3 | Data cleaning | notebook Part 3 (detect -> fix -> validate with assertions) |
| 4 | Visualisation (8 chart types) | notebook Part 4, images in `outputs/figures/` |
| 5 | Basic data analysis | notebook Part 5 (statistics, correlations, t-test, chi-square, sklearn smoke test) |
| 6 | Documented exercises | notebook Part 6, `docs/Hands_On_Data_Lab_Report.docx` |

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/check_environment.py                        # verify installation
python src/generate_data.py                            # creates data/customers|products|orders.csv (seed=7)
jupyter notebook notebooks/Hands_On_Data_Lab.ipynb     # Run All
```

## Project layout
```
data/        raw CSVs + retail_clean_merged.csv
notebooks/   Hands_On_Data_Lab.ipynb (executed, with outputs)
src/         generate_data.py, check_environment.py
outputs/     figures/, key_metrics.json, environment_check.txt
docs/        Hands_On_Data_Lab_Report.docx
```

## Headline results (delivered orders, synthetic data)
- INR 10.65 crore revenue at a 25.1% margin from 4,362 orders
- Electronics = 52% of revenue; Oct-Dec months earn 80% more than Jan-Sep
- Discounted orders: 21.1% margin vs 31.5% at full price (p < 0.001)
- Order value is right-skewed (mean 24,409 vs median 5,550); age and payment method show no effect

Data is synthetic; results illustrate technique, not real business facts.
