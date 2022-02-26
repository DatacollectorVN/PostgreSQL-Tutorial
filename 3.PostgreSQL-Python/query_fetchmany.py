import psycopg2
from config import config
import sys

def iter_row(cursor, size=10):
    time_query = 1
    while True:
        rows = cursor.fetchmany(size)
        print(f"{time_query} time query {len(rows)} data")
        if not rows:
            break
        for row in rows:
            yield row
        time_query += 1

def get_part_vendors():
    """ query part and vendor data from multiple tables"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("""
            SELECT part_name, vendor_name
            FROM parts
            INNER JOIN vendor_parts ON vendor_parts.part_id = parts.part_id
            INNER JOIN vendors ON vendors.vendor_id = vendor_parts.vendor_id
            ORDER BY part_name;
        """)
        for row in iter_row(cur, 10):
            print(row)
        
        cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    get_part_vendors()