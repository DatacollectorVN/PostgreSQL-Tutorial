import argparse
import psycopg2
from config import config

def update_one_row(vendor_id, vendor_name):
    """Update vendorname base on the vendor id"""
    sql = """UPDATE vendors 
             SET vendor_name = %s
             WHERE vendor_id = %s"""
    conn = None
    update_rows = 0
    try:
        # read database configuration
        params = config()

        # connect to PostgreSQL database
        conn = psycopg2.connect(**params)

        # create a new cursor
        cur = conn.cursor()

        # Execute the UPDATE statement
        cur.execute(sql, (vendor_name, vendor_id))

        # get the number of updated rows
        update_rows = cur.rowcount

        # commit the changes to the database
        conn.commit()

        # close communication with PostgreSQL database
        cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
    
    return update_rows


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--vendorid", dest = "vendor_id", type = int,
                        default = None)
    parser.add_argument("--vendorname", dest = "vendor_name", type = str,
                        default = None)
    args = parser.parse_args()
    vendor_id = args.vendor_id
    vendor_name = args.vendor_name
    update_rows = update_one_row(vendor_id, vendor_name)
    print(f"Number of update rows = {update_rows}")
        