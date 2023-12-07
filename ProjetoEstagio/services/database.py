import pyodbc

SERVER = 'LAPTOP-ELD15QMT'
DATABASE = 'CRUD_Estagio'
USERNAME = 'sa'
PASSWORD = 'senha'
cnxn = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes')
cursor = cnxn.cursor()