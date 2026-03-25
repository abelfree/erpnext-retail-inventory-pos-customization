frappe.ui.form.on("POS Invoice", {
  refresh(frm) {
    frm.page.set_primary_action("Scan Barcode", () => {
      frappe.prompt(
        [{ fieldname: "barcode", label: "Barcode", fieldtype: "Data", reqd: 1 }],
        (values) => add_item_by_barcode(frm, values.barcode),
        "Quick Scan"
      );
    });
  }
});

function add_item_by_barcode(frm, barcode) {
  frappe.call({
    method: "retail_ops.services.pos.find_item_by_barcode",
    args: { barcode },
    callback(r) {
      if (!r.message) {
        frappe.msgprint("No item found for barcode: " + barcode);
        return;
      }
      const row = frm.add_child("items", {
        item_code: r.message.item_code,
        qty: 1
      });
      frm.refresh_field("items");
      frm.script_manager.trigger("item_code", row.doctype, row.name);
    }
  });
}
