import psycopg2
from config import config


def add_part(part_name, vendor_name):

    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()

        # call a stored procedure
        cur.execute('CALL add_new_part(%s,%s)', (part_name, vendor_name))

        # commit the transaction
        conn.commit()

        # close the cursor
        cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    add_part('OLED', 'LG')