# Copyright (c) 2025, suman and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DocOne(Document):
	def before_save(self):
		self.set_name()
		

	def set_name(self):
		self.full_name = f"{self.name1} {self.last_name}"
		
		
