import frappe


def execute ():
    fullnames = frappe.db.get_all("Doc One",pluck="name")
    for dc in fullnames:
        fullname = frappe.get_doc("Doc One", dc)
        fullname.set_fullname()
        fullname.save()

    frappe.db.commit()
