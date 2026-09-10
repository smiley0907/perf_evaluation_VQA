# Cell 1: Environment and Library Setup

import sys
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import qiskit
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

print("=" * 70)
print("VARIATIONAL QUANTUM ALGORITHM EXPERIMENT")
print("=" * 70)

print("Python Version :", sys.version)
print("Qiskit Version:", qiskit.__version__)
print("NumPy Version  :", np.__version__)
print("Pandas Version :", pd.__version__)

print("\nEnvironment initialized successfully.")
