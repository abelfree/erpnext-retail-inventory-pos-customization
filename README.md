# ERPNext Retail Inventory + POS Customization

Portfolio project for retailer-focused ERPNext improvements.

## Features
- POS barcode-first item scanning helper (client script)
- Auto reorder job for low-stock items
- Supplier prioritization based on lead time
- Thermal receipt print format template

## Installation
```bash
bench get-app retail_ops <repo-url>
bench --site yoursite install-app retail_ops
```

## Scheduled Task
Run `retail_ops.services.reorder.run_auto_reorder` hourly via scheduler.
