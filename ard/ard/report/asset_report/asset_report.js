// Copyright (c) 2016, ARD and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Asset report"] = {
	"filters": [
		{
			fieldname:"company",
			label: __("Company"),
			fieldtype: "Link",
			options: "Company",
			default: frappe.defaults.get_user_default("Company")
		},
		{
			fieldname:"asset_category",
			label: __("Asset Category"),
			fieldtype: "Link",
			options: "Asset Category",
		},
		{
			fieldname:"item_name",
			label: __("Item Name"),
			fieldtype: "Link",
			options: "Item",
			get_query: () => {
				return {
					filters: [
						['Item', 'is_fixed_asset', '=', 1],
					]
				}
			}
		},
		{
			fieldname:"is_created_asset",
			label: __("Is Created Asset"),
			fieldtype: "Check"
		},
	]
};
