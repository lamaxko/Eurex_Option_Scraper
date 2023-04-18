import sqlite3

def con_setup():
        con = sqlite3.connect('PFOF.db')
        cur = con.cursor()
        return con, cur

def db_setup_opt(exchanges):
    con, cur = con_setup()

    # create a table for each exchange to store option data
    for exchange in exchanges: 
        cur.execute(f'''CREATE TABLE IF NOT EXISTS {exchange}_opt
                (row_number INTEGER PRIMARY KEY AUTOINCREMENT,
                messageId TEXT, 
                sourceName TEXT, 
                symbol TEXT, 
                contractDate TEXT, 
                optionCategory TEXT,
                generationNumber INTEGER,
                originalStrikePrice REAL,
                contractType TEXT,
                settlementMethod TEXT,
                exerciseStyle TEXT,
                mdQuotationTime TEXT)''')

    con.commit()
    return con
