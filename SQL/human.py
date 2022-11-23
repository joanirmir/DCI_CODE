# static methods, classmethods and instance methods
import psycopg2


# functions(to connect to the database)
def get_connection():
    conn = psycopg2.connect(
        database="november",
        user = "postgres",
        host = "5432",
        password = "postgres")
    cur = conn.cursor()
    return (conn, cur) # Tuple

def write_to_db(conn):
    conn.commit()


class Human:
    # first name, last name
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    
    # walking(), eating(), greeting(), save()

    """
    fausto = Human('fausto', 'doe')
    fausto.save()
    """
    def save(self):
        conn, cur = get_connection()
        name = f"{self.first_name} {self.last_name}"
        cur.execute(f"INSERT INTO users(name) VALUES('{name})")
        write_to_db(conn)

    # ORM -> Object Relations Mappers
    # Classes ->  tables (methods represent SQL actions)

    @staticmethod
    def delete(id):
        print("Deleting human with id", id)
    # Human.delete(1)

    @classmethod
    def get(cls, id):
        print("Getting a human")
        conn, cur = get_connection()
        cur.execute(f"SELECT name FROM users WHERE id={id}")
        h = cur.fetchone()
        name = h[0]
        f_name, l_name = name.split(" ")
        print(f_name, l_name)
        human_instance = cls(f_name, l_name)
        return human_instance

if __name__== '__main__':
    # Human.delete(1)
    x = Human.get(1)
    print(x)
    h = Human('X', 'Y')
    h.save()

    Human.delete(1) # Static method
    h.delete(1) # Instance method
   
