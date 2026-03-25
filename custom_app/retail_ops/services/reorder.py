from __future__ import annotations

import frappe


def run_auto_reorder():
    low_items = frappe.db.sql(
        """
        SELECT item_code, warehouse, actual_qty, reorder_level
        FROM `tabBin`
        WHERE actual_qty < reorder_level
          AND reorder_level > 0
        """,
        as_dict=True,
    )

    for row in low_items:
        supplier = _best_supplier(row.item_code)
        if not supplier:
            continue

        qty_to_order = max(int(row.reorder_level - row.actual_qty), 1)
        po = frappe.get_doc(
            {
                "doctype": "Purchase Order",
                "supplier": supplier,
                "schedule_date": frappe.utils.add_days(frappe.utils.today(), 2),
                "items": [
                    {
                        "item_code": row.item_code,
                        "qty": qty_to_order,
                        "warehouse": row.warehouse,
                    }
                ],
            }
        )
        po.insert(ignore_permissions=True)

    frappe.db.commit()


def _best_supplier(item_code: str):
    supplier_rows = frappe.db.sql(
        """
        SELECT supplier, lead_time_days
        FROM `tabItem Supplier`
        WHERE parent = %(item_code)s
        ORDER BY lead_time_days ASC
        LIMIT 1
        """,
        {"item_code": item_code},
        as_dict=True,
    )
    return supplier_rows[0].supplier if supplier_rows else None
