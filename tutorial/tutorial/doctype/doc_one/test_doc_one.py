# Copyright (c) 2025, suman and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDocOne(FrappeTestCase):
	def test_full_name_correcty_set(self):
		test_doc = frappe.new_doc("Doc One")
		test_doc.name1 = "Test Doc One"
		test_doc.last_name = "Test Doc One Title"
		test_doc.phone = "+918587854125"
		test_doc.save()

		self.assertEqual(test_doc.name1,"Test Doc One")