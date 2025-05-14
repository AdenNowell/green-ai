"""Compute ΔkWh and (placeholder) mint token."""
import argparse, pandas as pd, numpy as np
from web3 import Web3

def compute_delta(baseline_csv, actual_csv):
    base = pd.read_csv(baseline_csv)['watts'].sum()
    act = pd.read_csv(actual_csv)['watts'].sum()
    delta_kwh = (base - act) / 1000.0
    return max(delta_kwh, 0)

def mint_token(delta_kwh):
    print(f'[MOCK] Mint {delta_kwh:.2f} kWhSave tokens to caller address.')

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--baseline_watts_csv', required=True)
    p.add_argument('--actual_watts_csv', required=True)
    args = p.parse_args()

    delta = compute_delta(args.baseline_watts_csv, args.actual_watts_csv)
    mint_token(delta)
