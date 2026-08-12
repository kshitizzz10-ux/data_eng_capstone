# Data Engineering Capstone A: Extraction Engine

## Overview
This project is a scalable data extraction pipeline. Currently in development, the engine is built to securely connect to external APIs, extract raw data, and process it for downstream analytics.

## Day 1 Architecture
* **Language:** Python
* **Dependency Management:** `venv` and `requirements.txt`
* **Security:** Local `.env` file for API credentials (ignored by Git)
* **Structure:** Modularized source (`/src`), testing (`/tests`), and configuration directories.