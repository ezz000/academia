# Copyright (c) 2024, SanU and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ProposedTimes(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		date: DF.Date | None
		from_time: DF.Time | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		to_time: DF.Time | None
	# end: auto-generated types
	pass
