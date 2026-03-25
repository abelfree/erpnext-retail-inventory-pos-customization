app_name = "retail_ops"
app_title = "Retail Ops"
app_publisher = "Abel Takele"
app_description = "Inventory and POS extensions"
app_email = "abel.takele@example.com"
app_license = "MIT"

scheduler_events = {
    "hourly": [
        "retail_ops.services.reorder.run_auto_reorder"
    ]
}

doctypes_js = {
    "POS Invoice": "public/js/pos_invoice.js"
}
