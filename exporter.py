import xmlrpc.client
import csv
import openpyxl
from config import ODOO_URL, ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, EXPORT_PATH

def connect_to_odoo():
    """Establish connection to Odoo instance."""
    common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
    uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
    models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
    
    if not uid:
        print("❌ Connection failed. Check your config.py credentials.")
        return None, None
    
    print(f"✅ Connected to Odoo successfully. User ID: {uid}")
    return uid, models

def fetch_sales_orders(uid, models):
    """Fetch confirmed sales orders from Odoo."""
    orders = models.execute_kw(
        ODOO_DB, uid, ODOO_PASSWORD,
        'sale.order', 'search_read',
        [[['state', '=', 'sale']]],
        {'fields': ['name', 'partner_id', 'amount_total', 
                    'date_order', 'state']}
    )
    print(f"📦 Fetched {len(orders)} sales orders.")
    return orders

def export_to_csv(orders):
    """Export orders to CSV file."""
    if not orders:
        print("⚠️ No data to export.")
        return

    with open(EXPORT_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Header
        writer.writerow(['Order Name', 'Customer', 
                         'Total Amount', 'Date', 'Status'])
        # Rows
        for order in orders:
            writer.writerow([
                order['name'],
                order['partner_id'][1] if order['partner_id'] else 'N/A',
                order['amount_total'],
                order['date_order'],
                order['state']
            ])

    print(f"✅ Exported successfully to: {EXPORT_PATH}")

def main():
    print("🚀 Odoo Report Exporter Starting...")
    uid, models = connect_to_odoo()
    if uid:
        orders = fetch_sales_orders(uid, models)
        export_to_csv(orders)
    print("✅ Done.")

if __name__ == "__main__":
    main()