# Eurex_Option_Scraper

This Python script scrapes pre-trade options data for Eurex and saves the data into an SQLite database.

## Usage

1. Clone this repository.
2. Install the required packages:
    ```
    pip install requests
    ```
3. Update the following variables in `scrape.py` to your needs:
    ```python
    exchanges = ['DEUR']
    date = '2023.04.18'
    begin_time = '120000'
    stop_time = '130000'
    ```
4. Run the `scrape.py` script:
    ```
    python scrape.py
    ```
 
The script sets up an SQLite database, downloads data for the specified exchanges, date, and time range, and inserts it into the appropriate tables.

The general data from Deutsche Börese is to find under the following link:
https://www.mds.deutsche-boerse.com/mds-en/real-time-data/Delayed-data 
