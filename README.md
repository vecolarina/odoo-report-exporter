# Odoo Report Exporter 🚀

A lightweight Python tool that connects to any Odoo instance via XML-RPC
and exports Sales Orders into a clean CSV file.

Built by a working Odoo ERP Developer — this solves a real problem
faced daily in production environments.

---

## Features
- Connects to any Odoo 16/17/18/19 instance via XML-RPC
- Fetches confirmed Sales Orders automatically
- Exports to clean CSV format ready for Excel or further processing
- Simple configuration — just update config.py with your credentials

---

## Requirements
- Python 3.8+
- Access to an Odoo instance (v16, v17, v18, or v19)

---

## Installation

1. Clone the repository:
   git clone https://github.com/vecolarina/odoo-report-exporter.git
   cd odoo-report-exporter

2. Install dependencies:
   pip install -r requirements.txt

3. Configure your Odoo connection in config.py:
   ODOO_URL = "http://your-odoo-instance.com"
   ODOO_DB = "your_database"
   ODOO_USERNAME = "your@email.com"
   ODOO_PASSWORD = "your_password"

4. Run:
   python exporter.py

---

## Output
A CSV file will be generated inside the sample_output/ folder containing:
- Order Name
- Customer
- Total Amount
- Date
- Status

---

## Tech Stack
- Python 3
- Odoo XML-RPC API
- openpyxl
- CSV (built-in)

---

Built by Von Adrian Colarina
Python Developer | Odoo ERP Specialist
github.com/vecolarina