# perf_evaluation_VQA
PERFORMANCE EVALUATION OF VARIATIONAL QUANTUM ALGORITHMS ACROSS DIFFERENT CIRCUIT DEPTHS

# Performance Evaluation of VQA Across Circuit Depths

This repository contains the experimental implementation for evaluating
Variational Quantum Algorithms (VQA) across different quantum circuit
depths using simple parameterized quantum circuits.

The experiment compares a fixed-parameter baseline (Without VQA) with
iterative variational optimization (With VQA). The objective is to study
energy optimization, convergence behavior, and computational cost as
circuit depth increases.

## Experimental Setup

- Quantum framework: Qiskit
- Quantum simulator: Qiskit Aer
- Optimizer: COBYLA
- Qubits: 2
- Circuit depths: 3, 6, 9, 12, 15
- Random seed: 42
- Maximum optimization iterations: 200
