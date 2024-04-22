import mysql.connector
from mysql.connector import Error

def create_connection():
    """ Create a database connection to the MySQL database """
    try:
        conn = mysql.connector.connect(
            host='localhost',  # or your host, e.g., '127.0.0.1'
            database='Library',
            user='root',
            password='Foxtrot8'
        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return None
# -20 pts, missing the table creation functions.

# -10 pts, the attributes that are managed by addBook(), searchBook(), and updateBook(), are not as required according to the database screenshots.
def addBook():
    """ Function to add a book to the Bookrecord table """
    try:
        conn = create_connection()
        if conn is not None:
            cursor = conn.cursor()
            bno = input("Enter Book Number (Bno): ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            isbn = input("Enter ISBN: ")
            publication_year = input("Enter Publication Year: ") 
            
            query = """INSERT INTO Bookrecord (Bno, Title, Author, ISBN, PublicationYear)
                       VALUES (%s, %s, %s, %s, %s);"""
            values = (bno, title, author, isbn, publication_year)
            
            cursor.execute(query, values)
            conn.commit()
            print("Book added successfully.")
        else:
            print("Failed to insert data into MySQL table")
    except Error as e:
        print(f"Failed to insert book into table: {e}")
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

def deleteBook():
    """ Function to delete a book from the Bookrecord table """
    try:
        conn = create_connection()
        if conn is not None:
            cursor = conn.cursor()
            bno = input("Enter Book Number (Bno) to delete: ")
            query = "DELETE FROM Bookrecord WHERE Bno = %s;"
            cursor.execute(query, (bno,))
            conn.commit()
            print(f"Book {bno} deleted successfully.")
        else:
            print("Failed to delete data from MySQL table")
    except Error as e:
        print(f"Failed to delete book: {e}")
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

def searchBook():
    """ Function to search for a book from the Bookrecord table """
    try:
        conn = create_connection()
        if conn is not None:
            cursor = conn.cursor()
            bno = input("Enter Book Number (Bno) to search: ")
            query = "SELECT * FROM Bookrecord WHERE Bno = %s;"
            cursor.execute(query, (bno,))
            records = cursor.fetchall()
            if records:
                for record in records:
                    print("Book Number:", record[0])
                    print("Title:", record[1])
                    print("Author:", record[2])
                    print("ISBN:", record[3])
                    print("Publication Year:", record[4])
            else:
                print("No book found with this number.")
        else:
            print("Failed to retrieve data from MySQL table")
    except Error as e:
        print(f"Failed to search for book: {e}")
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

def updateBook():
    """ Function to update a book in the Bookrecord table """
    try:
        conn = create_connection()
        if conn is not None:
            cursor = conn.cursor()
            bno = input("Enter Book Number (Bno) to update: ")
            title = input("Enter new Title: ")
            author = input("Enter new Author: ")
            isbn = input("Enter new ISBN: ")
            publication_year = input("Enter new Publication Year: ")
            
            query = """UPDATE Bookrecord 
                       SET Title = %s, Author = %s, ISBN = %s, PublicationYear = %s
                       WHERE Bno = %s;"""
            values = (title, author, isbn, publication_year, bno)
            
            cursor.execute(query, values)
            conn.commit()
            print("Book updated successfully.")
        else:
            print("Failed to update data in MySQL table")
    except Error as e:
        print(f"Failed to update book: {e}")
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()
