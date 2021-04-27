import psycopg2

con = psycopg2.connect(
    host="localhost", 
    port = 5432, 
    database = "Bengkel Motor",
    user = "postgres",
    password = "postgre123")

cur = con.cursor()


print("       Program Demo CRUD PostgreSQL Database ")
print("       Rafif Rafikhansa (19/447315/SV/17009)            ")
print("========================================================\n")
def main():
    print("Menu operasi database:")
    print("1. Create database & tabel")
    print("2. Insert data")
    print("3. Select/search data")
    print("4. Update data")
    print("5. Delete data")
    menu=input("Silahkan pilih operasi ( 1/2/3/4/5 ) ? ")
    print("Operasi : " + menu)

    if menu=='1' :
        print("Create database dan tabel")
        # create a database named bengkel
        con = psycopg2.connect(
        host="localhost", 
        user = "postgres",
        database = "Bengkel Motor",
        port = 5432,
        password = "postgre123")
        cur = con.cursor()
        # create a table named user
        cur = con.cursor()
        cur.execute("CREATE TABLE percobaan (nama VARCHAR(60) NOT NULL, umur NUMERIC NOT NULL)")
        con.commit()
    elif menu=='2' :
        print("Insert data")
        #insert
        con = psycopg2.connect(
        host="localhost", 
        user = "postgres",
        database = "Bengkel Motor",
        port = 5432,
        password = "postgre123")
        cur = con.cursor()
        cur.execute('''INSERT INTO managemenuser (id, username, password, status) VALUES('9', 'David B', 'bekam', 'Berlangganan');''')  
        con.commit()
    elif menu=='3' :
        print("Select/search data")
        con = psycopg2.connect(
    host="localhost", 
        user = "postgres",
        database = "Bengkel Motor",
        port = 5432,
        password = "postgre123")
        cur = con.cursor()
        cur.execute("""SELECT * FROM managemenuser""")
        query_res = cur.fetchall()
        print(query_res)

    elif menu=='4' :
        print("Update data")
        con = psycopg2.connect(
        host="localhost", 
        user = "postgres",
        database = "Bengkel Motor",
        port = 5432,
        password = "postgre123")
        cur = con.cursor()
        sql1 = "UPDATE managemenuser SET password = '0000000' WHERE id = 4"
        cur.execute(sql1)
        con.commit() 
        print(sql1)

    elif menu=='5' :
        print("Delete data")
        con = psycopg2.connect(
        host="localhost", 
        user = "postgres",
        database = "Bengkel Motor",
        port = 5432,
        password = "postgre123")
        cur = con.cursor()
        sql2 = "DELETE FROM managemenuser WHERE id = 9"
        cur.execute(sql2)
        con.commit()
        print(sql2)

    again=input("\nInput Operasi Kembali (y/n) ? ")
    if again.lower() == "y" :
        main ()
    else :
        print("Operasi Selesai")
    cur.close()
    con.close()

main()