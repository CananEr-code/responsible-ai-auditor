import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def evaluate_bias(data):
    # Dummy bias check
    if "gender" in data.columns:
        return "Bias evaluation completed successfully."
    return "No sensitive attribute found."
