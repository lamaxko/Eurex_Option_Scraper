# Eurex_Option_Scraper

This Python script scrapes pre-trade options data for Eurex and saves the data into an SQLite database. Keep in mind that only the data for the last 48h or last two trading days is available.

## Usage

1. Clone this repository.
2. Install the required packages:
    ```
    pip install requests
    ```
3. Update the following variables in `scrape.py` to your needs, for now only option data from EUREX is available (see link below):
    ```python
    exchanges = ['DEUR']
    date = '2023.04.18'
    begin_time = '120000'
    stop_time = '130000'
    ```
4. Run the `scrape.py` script:
    ```
    python3 scrape.py
    ```
 
The script sets up an SQLite database, downloads data for the specified exchanges and inserts it into the appropriate table.


The general data from Deutsche Börese is to find under the following link:

https://www.mds.deutsche-boerse.com/mds-en/real-time-data/Delayed-data 
