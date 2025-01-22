# Example 1: Manually calculating Mean Square Error
import numpy as np

# Actual and predicted values
actual = [3, -0.5, 2, 7]
predicted = [2.5, 0.0, 2, 8]

# Manual calculation of MSE
errors = [(a - p) ** 2 for a, p in zip(actual, predicted)]
mse_manual = sum(errors) / len(errors)
print("Mean Square Error (Manual Calculation):", mse_manual)

