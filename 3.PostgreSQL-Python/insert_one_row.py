import argparse
import psycopg2
from config import config

def inser_vendor(vendor_name):
    """ Insert a new vendor into the vendors table """
    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id"""
    conn = None
    vendor_id = None
    try: 
        # STEP1: Connect to PostgreSQL database
        
        # read database configuration
        params = config()
        
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)

        # STEP2: Create the new cursor
        
        # create new cursor
        cur = conn.cursor()

        # STEP3: Execute INSERT statement
        cur.execute(sql, (vendor_name,))

        # get generated id back
        vendor_id = cur.fetchone()[0]

        # STEP4: Commit
        conn.commit()

        # STEP5: Close communication
        cur.close

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
    
    return vendor_id

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--vendorname", dest = "vendorname", type = str,
                        default = None, help = "vendor name to add into suppliers database in PostgreSQL")
    args = parser.parse_args()
    vendor_name = args.vendorname
    inser_vendor(vendor_name)