# Copyright (c) 2013, ARD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):

	return get_columns(), get_data(filters)

def get_columns():

	return[
		"Item Name:Link/Item:150",
		"Asset Category:Link/Asset Category:150",
		"description:Data:150",
		"Last Purchase Rate:Int:150",
		"Receipt Assets:Int:150",
		"Used Assets Count:Int:150",
	]

def get_data(filters):
	condition = " 1=1 "
	if(filters.get('asset_category')):condition +=f" AND item.asset_category='{filters.get('asset_category')}'	"
	if(filters.get('item_name')):condition +=f" AND item.item_name='{filters.get('item_name')}'	"
	if(filters.get('is_created_asset')):condition += " AND (SELECT COUNT(name) FROM `tabAsset` WHERE item_code = pr_item.item_code AND status != 'Draft') > 0 "
	data = frappe.db.sql(f"""SELECT pr_item.item_name, item.asset_category,  item.description, item.last_purchase_rate, COUNT(pr_item.item_name) as 'Assets Count' , (SELECT COUNT(name) FROM `tabAsset` WHERE item_code = pr_item.item_code AND status != 'Draft') as 'Used Asset Count' FROM `tabPurchase Receipt Item` as pr_item  JOIN `tabItem` as item ON pr_item.item_code = item.name WHERE item.is_fixed_asset = 1 AND {condition} GROUP BY pr_item.item_name ;""")

	print(f"\n\n\n{filters}\n\n\n")
	return data
