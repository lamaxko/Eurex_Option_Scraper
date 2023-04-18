from helpers import db_setup_opt

def print_sample_rows(db_conn, exchange, num_rows):
    cursor = db_conn.cursor()
    
    # Fetch first num_rows from the exchange_opt table
    cursor.execute(f'SELECT * FROM {exchange}_opt LIMIT {num_rows}')
    rows = cursor.fetchall()

    # Print the rows
    print(f"Sample rows from {exchange}_opt table:")
    for row in rows:
        print(row)


def main():

    db_conn = db_setup_opt(['DEUR'])
    print_sample_rows(db_conn, 'DEUR', 10)

if __name__ == '__main__':
    main()