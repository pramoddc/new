import psycopg2
 
# Update connection string information
host = "bigd.postgres.database.azure.com"
dbname = "postgres"
user = "bigd@bigd"
password = "Hawks123"
sslmode = "require"
 
# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")
 
cursor = conn.cursor()


f = open('C:/Users/Dell/Documents/SRH_Course/BigData Programming-1/project/SolutionArchitects.csv', 'r')
cursor.copy_from(f, 'geo', sep=',')
f.close()
conn.close()
print((conn))


