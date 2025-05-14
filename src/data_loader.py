"""Simple synthetic data generator / loader."""
import numpy as np
import pandas as pd

def generate_synthetic(series_len: int = 1000):
    """Generate baseline and actual watt series."""
    time = np.arange(series_len)
    baseline = 200 + 10*np.sin(2*np.pi*time/144)  # toy daily cycle
    actual = baseline - np.random.uniform(5, 25, size=series_len)
    return pd.DataFrame({'time': time, 'baseline': baseline, 'actual': actual})
