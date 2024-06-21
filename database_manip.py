import sqlite3

# ===Create a table called python_programming===
try:
    db = sqlite3.connect('python_programming')

    # Create a cursor object to run queries
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS python_programming (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        grade INTEGER NOT NULL)''')
    
    db.commit()

    # ===Insert new rows into the table===
    students_grades = [
        (55, "Carl Davidson", 61),
        (66, "Dennis Frederickson", 88),
        (77, "Jane Richards", 78),
        (12, "Peyton Sawyer", 45),
        (2, "Lucas Brooke", 99)]

    cursor.executemany(
        '''INSERT INTO python_programming(id, name, grade) VALUES(?,?,?)''',
        students_grades
        )
    
    db.commit()

    # ===Select all records with a grade between 60 and 80===
    cursor.execute('''SELECT * FROM python_programming 
                        WHERE grade BETWEEN ? AND ?''', (60, 80))

    # ===Change Carl Davis’s grade to 65===
    cursor.execute('''UPDATE python_programming SET grade = ? 
                   WHERE name = ?''', (65, 'Carl Davis'))
    db.commit()

    # ===Delete Dennis Fredrickson’s row===
    # First check if the record exists
    cursor.execute('''SELECT * FROM python_programming
                   WHERE id = ?''', (66,))
    
    # Check if the cursor is empty
    if not cursor.fetchall():
        print("No records found. No action taken.")
    else:
        # Execute the DELETE statement to delete records
        cursor.execute('''DELETE FROM python_programming
                       WHERE id = ?''', (66,))
        db.commit()

    # ===Change the grade of all students with an id greater than 55 to
    # a grade of 80===
    cursor.execute('''UPDATE python_programming SET grade = ? 
                   WHERE id > ? ''', (80, 55))
    db.commit()

# Catch the exception
except Exception as error_msg:
    # Roll back any change if something goes wrong
    db.rollback()
    raise error_msg

finally:
    # Close the db connection
    db.close()