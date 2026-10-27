"""Verify that Python and the essential data-science libraries are installed."""
import importlib
import sys

REQUIRED = ["numpy", "pandas", "matplotlib", "seaborn", "sklearn", "scipy", "jupyter_core"]


def main() -> int:
    print(f"Python {sys.version.split()[0]}  ({sys.executable})")
    failed = []
    for name in REQUIRED:
        try:
            mod = importlib.import_module(name)
            print(f"{name:<14} OK   {getattr(mod, '__version__', '')}")
        except ImportError:
            print(f"{name:<14} MISSING  -> pip install -r requirements.txt")
            failed.append(name)
    # smoke test: a tiny end-to-end computation
    import numpy as np, pandas as pd
    assert pd.DataFrame({"x": np.arange(5)})["x"].sum() == 10
    print("Smoke test passed" if not failed else f"{len(failed)} package(s) missing")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
