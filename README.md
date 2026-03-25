# ERPNext Retail Inventory + POS Customization

[![ERPNext](https://img.shields.io/badge/ERPNext-v15-blue)](https://erpnext.com/)
[![POS](https://img.shields.io/badge/Module-POS-orange)](https://docs.erpnext.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Retail-focused ERPNext customization for inventory control, POS speed, and reorder automation.

## Author
Abel Takele

## What This Project Demonstrates
- POS client scripting for barcode-first operations
- Server-side stock intelligence and reorder automation
- Supplier optimization logic by lead time
- Custom thermal print format for receipts

## Key Features
- Quick-scan barcode action on `POS Invoice`
- Item lookup via barcode API
- Hourly job that auto-creates purchase orders when stock is below reorder level
- Thermal receipt Jinja template for retail counters

## Architecture
- `custom_app/hooks.py`: scheduler and client script mappings
- `custom_app/retail_ops/public/js/pos_invoice.js`: POS UX customization
- `custom_app/retail_ops/services/pos.py`: barcode lookup API
- `custom_app/retail_ops/services/reorder.py`: reorder engine
- `custom_app/retail_ops/print_formats/thermal_receipt.jinja`: receipt format

## Quick Start
```bash
bench get-app retail_ops https://github.com/abelfree/erpnext-retail-inventory-pos-customization
bench --site yoursite install-app retail_ops
```

## Demo Flow
1. Open `POS Invoice` and use `Scan Barcode` action.
2. Confirm matching item is added to invoice lines.
3. Configure reorder levels and simulate low stock in `Bin`.
4. Run scheduler and verify generated `Purchase Order` records.

## Recruiter Notes
This repository showcases ERPNext retail customization, front-end scripting in Frappe Desk, and inventory automation logic.
