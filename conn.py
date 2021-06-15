import pyodbc
server = '' 
database = '' 
username = '' 
password = ''
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM table1;")
row = cursor.fetchone() 
while row: 
    #print row[0]
    print(str(row[4]))
    row = cursor.fetchone()
