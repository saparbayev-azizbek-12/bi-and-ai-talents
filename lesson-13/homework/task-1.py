import sqlite3

def create_db():
    sql = """
        DROP TABLE IF EXISTS Students;
        CREATE TABLE Students(Name TEXT, Species TEXT, Age INTEGER);
        INSERT INTO Students VALUES
        ('Benjamin Sisko', 'Human', 40), 
        ('Jadzia Dax', 'Trill', 300), 
        ('Kira Nerys', 'Bajoran', 29);
    """
    with sqlite3.connect("roster.db") as c:
        cursor = c.cursor()
        cursor.executescript(sql)
        query = "SELECT * FROM Students"
        data = cursor.execute(query)
    data_ = data.fetchall()
    for n in data_:
        print(n)
    return True

def update_db():
    with sqlite3.connect("roster.db") as c:
        cursor = c.cursor()
        query = "UPDATE Students SET Name='Ezri Dax' WHERE Name='Jadzia Dax'"
        cursor.execute(query)
    print("Updated Jadzia Dax to Ezri Dax.")
    return True

def select_db():
    with sqlite3.connect("roster.db") as c:
        cursor = c.cursor()
        query = "SELECT Name, Age FROM Students WHERE Species='Bajoran'"
        data = cursor.execute(query)
    data_ = data.fetchall()
    for n in data_:
        print(n)
    return True

def delete_db():
    with sqlite3.connect("roster.db") as c:
        cursor = c.cursor()
        query = "DELETE FROM Students WHERE Age > 100"
        cursor.execute(query)
    print("Removed all characters aged over 100 years.")
    return True

def bonus_task():
    with sqlite3.connect("roster.db") as c:
        cursor = c.cursor()
        cursor.execute("ALTER TABLE Students ADD COLUMN Rank TEXT")
        updates = [
            ("Benjamin Sisko", "Captain"),
            ("Ezri Dax", "Lieutenant"),
            ("Kira Nerys", "Major")
        ]
        for name, rank in updates:
            cursor.execute("UPDATE Students SET Rank=? WHERE Name=?", (rank, name))
    print("Added and updated Rank column.")
    return True

def advanced_query():
    with sqlite3.connect("roster.db") as c:
        cursor = c.cursor()
        query = "SELECT * FROM Students ORDER BY Age DESC"
        data = cursor.execute(query)
    data_ = data.fetchall()
    for n in data_:
        print(n)
    return True

def main():
    print("Creating Database and Table:")
    create_db()
    
    print("\nUpdating Data:")
    update_db()
    
    print("\nSelecting Bajoran Characters:")
    select_db()
    
    print("\nDeleting Old Characters:")
    delete_db()
    
    print("\nAdding Rank Column and Updating Data:")
    bonus_task()
    
    print("\nAdvanced Query - Sorting by Age:")
    advanced_query()

if __name__ == "__main__":
    main()
