import psycopg2
import datetime

# Define your database connection parameters
conn = psycopg2.connect(
        dbname="Teste Aprovador",
        user="XX",
        password="XX",
        host="localhost",
        port="5432"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

dataHoraInicio = datetime.datetime.now()

cur.execute("SELECT id FROM logs WHERE timestamp <= NOW() - INTERVAL '72 hours'")
idLogs = cur.fetchall()

loglist = [i[0] for i in idLogs]


logsEncontrados = len(loglist)

cur.execute("DELETE * from logs WHERE timestamp <= NOW() - INTERVAL '72 hours'")


    
cur.execute("SELECT id FROM logs WHERE timestamp <= NOW() - INTERVAL '72 hours'")
idLogs = cur.fetchall()
loglist = [i[0] for i in idLogs]

conn.commit()

cur.close()
conn.close()


