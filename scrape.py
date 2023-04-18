from helpers import db_setup_opt, generate_url_list, download_files, insert_data_to_db

def main():
    
    # Initialize variables
    exchanges = ['DEUR']
    date = '2023.04.18'
    begin_time = '120000'
    stop_time = '130000'
    
    # Set up databases
    db_conn = db_setup_opt(exchanges)
        
    # Interate through exhanges and scrape data
    for exchange in exchanges:
        url_list = generate_url_list(exchange, date, begin_time, stop_time)
        for url in url_list:
            print(url)
            file_content = download_files(url, exchange)
            response = insert_data_to_db(db_conn, exchange, file_content)
            print(response)

if __name__ == '__main__':
    main()
    