"""Train model on synthetic data."""
import argparse, numpy as np
from data_loader import generate_synthetic
from model import build_model
import tensorflow as tf

parser = argparse.ArgumentParser()
parser.add_argument('--epochs', type=int, default=5)
args = parser.parse_args()

df = generate_synthetic()
seq_len = 24
X, y = [], []
for i in range(len(df)-seq_len):
    X.append(df['baseline'].values[i:i+seq_len])
    y.append(df['baseline'].values[i+seq_len])
X = np.array(X)[..., None]
y = np.array(y)

model = build_model(seq_len)
model.fit(X, y, epochs=args.epochs, batch_size=32)
model.save('saved_model')
print('Model trained and saved.')
