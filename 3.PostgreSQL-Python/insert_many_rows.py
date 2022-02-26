import psycopg2
from config import config

def insert_vendor_list(vendor_list):
    """ Insert multiple vendors into the vendors table """

    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    conn = None 

    try: 
        # STEP1: Connect to PostgreSQL database

        # read database configureation
        params = config()
        
        # connect to PostgreSQL database
        conn = psycopg2.connect(**params)

        # STEP2: Create the new cursor
        
        # create new cursor
        cur = conn.cursor()

        # STEP3: Execute INSERT statement
        
        # execute the INSERTE statement, use excutemany method
        cur.executemany(sql, vendor_list)

        # STEP4: Commit
        conn.commit()

        # STEP5: Close communication
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    vendor_list = [
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ]
    insert_vendor_list(vendor_list)