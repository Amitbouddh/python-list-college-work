import sqlite3
import pandas as pd

def fetch_data_from_database():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Drop old table and recreate with marks + age columns
    cursor.execute("DROP TABLE IF EXISTS books")
    cursor.execute('''
        CREATE TABLE books
        (id INTEGER PRIMARY KEY, title TEXT, price TEXT, marks INTEGER, age INTEGER)
    ''')

    # Insert sample data with marks and age
    cursor.execute("INSERT INTO books (title, price, marks, age) VALUES (?, ?, ?, ?)", ('Alice', '$10', 85, 23))
    cursor.execute("INSERT INTO books (title, price, marks, age) VALUES (?, ?, ?, ?)", ('Bob', '$15', 90, 30))
    cursor.execute("INSERT INTO books (title, price, marks, age) VALUES (?, ?, ?, ?)", ('Charlie', '$20', 75, 27))
    cursor.execute("INSERT INTO books (title, price, marks, age) VALUES (?, ?, ?, ?)", ('Alice', '$12', 95, 23))  # duplicate name

    conn.commit()

    # Fetch all rows
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    # Create DataFrame
    df = pd.DataFrame(rows, columns=['id', 'title', 'price', 'marks', 'age'])
    print("Original DataFrame:\n", df)

    # Group by name and calculate mean of marks
    mean_marks = df.groupby('title')['marks'].mean().reset_index()
    print("\nMean marks per name:\n", mean_marks)

    # Sort DataFrame by age
    sorted_df = df.sort_values(by='age')
    print("\nDataFrame sorted by age:\n", sorted_df)

    conn.close()

fetch_data_from_database()
