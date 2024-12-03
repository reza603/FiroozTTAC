
import pyodbc

conn = pyodbc.connect(
'DRIVER={ODBC Driver 17 for SQL Server};'
'SERVER=127.0.0.1\\SQLEXPRESS;'
'DATABASE=amf_db;'
'UID=sa;'
'PWD=amf@sql'
)

print("Connection successful!")