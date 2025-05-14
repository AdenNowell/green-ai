# Green AI Energy Savings – Proof‑of‑Savings Token

**One‑sentence pitch**  
A TensorFlow‑based model forecasts baseline vs. optimized energy use in compute clusters, and a Solidity smart contract mints one `kWhSave` token for every kilowatt‑hour your AI controller actually saves.

---

## 1. Motivation
As AI workloads surge, data‑center energy demand risks outpacing grid growth. By quantifying each kilowatt‑hour saved **on‑chain**, operators gain a verifiable carbon‑savings ledger they can trade or retire.

## 2. Architecture
```
┌───────────┐     telemetry      ┌────────────┐     ΔkWh     ┌───────────────────┐
│ Prometheus│ ───────────────▶  │  Predictor  │ ───────────▶ │  kWhSave ERC‑20   │
└───────────┘                   │ (TensorFlow)│             │ smart contract    │
     ▲                          └────────────┘             └───────────────────┘
     │ Grafana dashboards                                 Polygon test‑net
```

- **Predictor**: LSTM model in TensorFlow/Keras (`src/model.py`)  
- **Energy delta** = _baseline – actual_ (computed in `src/inference.py`)  
- **Smart contract**: `EnergySavingsToken.sol` (ERC‑20 with `mint(address,uint256)`)

## 3. Repo Layout
```
|-- contracts/
|   `-- EnergySavingsToken.sol
|-- notebooks/
|   `-- energy_baseline.ipynb   # starter notebook
|-- src/
|   |-- data_loader.py
|   |-- model.py
|   |-- train.py
|   `-- inference.py
|-- .gitignore
|-- requirements.txt
|-- LICENSE (MIT)
|-- README.md
```

## 4. Quickstart
```bash
# 1) Clone & install
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 2) Train a toy model on synthetic data
python src/train.py --epochs 3

# 3) Run inference to compute ΔkWh and mint token (test‑net)
python src/inference.py --actual_watts_csv data/actual.csv --baseline_watts_csv data/baseline.csv
```

## 5. Roadmap
- [ ] Collect real cluster telemetry
- [ ] Hyperparameter tune LSTM vs. TCN
- [ ] Integrate Web3 gateway for automatic mint on prediction
- [ ] Add Streamlit dashboard

## 6. License
MIT
