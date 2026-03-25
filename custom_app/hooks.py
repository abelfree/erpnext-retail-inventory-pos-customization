app_name = "retail_ops"
app_title = "Retail Ops"
app_publisher = "Portfolio"
app_description = "Inventory and POS extensions"
app_email = "dev@example.com"
app_license = "MIT"

scheduler_events = {
    "hourly": [
        "retail_ops.services.reorder.run_auto_reorder"
    ]
}

doctypes_js = {
    "POS Invoice": "public/js/pos_invoice.js"
}
