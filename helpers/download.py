import gzip
import json
import requests
from datetime import datetime, timedelta

def download_files(url, exchange):
    file_content = []  # Initialize file_content as an empty list
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Files of deutsche boerse have json format
            if exchange in ['DEUR']:
                file_content = gzip.decompress(response.content)
                file_content = json.loads(file_content)

    except Exception as e:
        print(f"Error downloading {url}: {e}")
    
    return file_content
        
def insert_data_to_db(db_conn, exchange, file_content):
    
    cursor = db_conn.cursor()


    def convert_timestamp(timestamp_str):
        if timestamp_str is None:
            return None
        timestamp_str = timestamp_str[:-4] + "Z"  # Truncate the fractional part to 6 digits
        try:
            dt = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            dt = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")
        iso_timestamp = dt.isoformat(timespec='seconds')  # Convert to ISO 8601 format string
        return iso_timestamp

    # Insert data into the appropriate table
    if exchange in ['DEUR']:
            for record in file_content:
                data = (
                    record.get('messageId'),
                    record.get('sourceName'),
                    record.get('symbol'),
                    record.get('contractDate'),
                    record.get('optionCategory'),
                    record.get('generationNumber'),
                    record.get('originalStrikePrice'),
                    record.get('contractType'),
                    record.get('settlementMethod'),
                    record.get('exerciseStyle'),
                    convert_timestamp(record.get('mdQuotationTime'))
                )
                cursor.execute(f'INSERT INTO {exchange}_opt (messageId, sourceName, symbol, contractDate, optionCategory, generationNumber, originalStrikePrice, contractType, settlementMethod, exerciseStyle, mdQuotationTime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', data)





    db_conn.commit()
    
    return f"Data inserted into the {exchange}_opt table."