import psycopg2
from config import config

def update_many_rows(vendor_list):
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
        cur.executemany(sql, vendor_list)

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
    vendor_list = [("AKM Inc", 2), ("Foster Co. Ltd", 5)]
    update_rows = update_many_rows(vendor_list)
    print(f"Number of update rows = {update_rows}")

        