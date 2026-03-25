from __future__ import annotations

import frappe


@frappe.whitelist()
def find_item_by_barcode(barcode: str):
    item = frappe.db.get_value(
        "Item Barcode",
        {"barcode": barcode},
        ["parent as item_code"],
        as_dict=True,
    )
    return item
