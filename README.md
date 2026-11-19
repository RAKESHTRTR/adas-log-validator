# ADAS Log Validator

An automated vehicle-signal and log validation framework built to verify ADAS/automotive telemetry traces (timing, signal bounds, state transitions, and fault flags) using **Modern C++17**, **Python (`pytest`)**, **Docker**, and **GitHub Actions CI**.

## Why This Exists
Modern ADAS/AV validation requires deterministic, reproducible checks that run identically on an engineer's environment and in nightly CI pipelines. This repository demonstrates:
- **Signal & Trace Invariant Checks:** Validating timestamps, out-of-range values, and state-machine transitions on recorded vehicle logs.
- **Automated Test Orchestration:** Parameterized `pytest` suites that generate structured pass/fail KPI reports.
- **Zero-Install Reproducibility:** Runs cleanly in **GitHub Codespaces** and Docker containers with no local machine setup.

## Run in GitHub Codespaces (Zero Local Install)
1. Click **Code** → **Codespaces** → **Create codespace on main**.
2. Once the browser terminal loads, verify the toolchain and install test dependencies:
   ```bash
   g++ --version
   python3 --version
   pip install pytest

g++ -std=c++17 src/hello_adas.cpp -o hello_adas && ./hello_adas

pytest -v

adas-log-validator/
├── src/                # C++17 log/signal processing utilities
├── validators/         # Python signal-trace & KPI validation modules
├── tests/              # Parameterized pytest suites
├── sample_data/        # Synthetic vehicle/CAN trace CSVs
├── Dockerfile          # Reproducible validation container
└── .github/workflows/  # Automated CI regression gate
