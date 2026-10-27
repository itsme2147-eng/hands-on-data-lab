# Environment Setup Guide

Tested with Python 3.12. Any Python 3.10+ works.

## 1. Install Python
- Windows/macOS: download from https://www.python.org/downloads/ (tick "Add Python to PATH" on Windows).
- Ubuntu/Debian: `sudo apt install python3 python3-venv python3-pip`
- Check: `python --version`

## 2. Create an isolated virtual environment
```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
```
(Alternative with conda: `conda env create -f environment.yml && conda activate ds-lab`)

## 3. Install libraries
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
Installs NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, SciPy and Jupyter.

## 4. Verify
```bash
python src/check_environment.py
```
Every library should print `OK` with its version.

## 5. Launch Jupyter
```bash
jupyter notebook notebooks/Hands_On_Data_Lab.ipynb
```

## Troubleshooting
| Problem | Fix |
|---|---|
| `python` not found | Use `python3`, or re-install with PATH ticked |
| `ModuleNotFoundError` | Activate the venv, then `pip install -r requirements.txt` |
| Kernel not listed in Jupyter | `python -m ipykernel install --user --name ds-lab` |
| Plots not showing | Run `%matplotlib inline` in the first cell |
