import pandas as pd

def compute_autocorrelations(series, lag):
    """
    Compute the autocorrelation of a numeric series at the specified lag.

    Parameters:
    series (pd.Series): The input numeric series.
    lag (int): The lag at which to compute the autocorrelation.

    Returns:
    float: The autocorrelation value at the specified lag.
    """
    if not isinstance(series, pd.Series):
        raise ValueError("Input series must be a Pandas Series.")
    if not isinstance(lag, int):
        raise ValueError("Lag must be an integer.")
    
    return series.autocorr(lag)

# Example usage
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    series = pd.Series(data)
    lag = 2
    autocorrelation = compute_autocorrelations(series, lag)
    print(f"Autocorrelation at lag {lag}: {autocorrelation}")
