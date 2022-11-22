from flask import Flask, jsonify, request
import psycopg2

from psycopg2.extras import DictCursor


connection = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",  # database
    database="flask_intro",
)

cur = connection.cursor()
cursor_obj = connection.cursor(cursor_factory=DictCursor)

# instantiating a class (Flask)
app = Flask(__name__)

# List (empty)
REMINDERS = []

# Decorator
@app.route("/")
# Function
def index():
    # Fetch all the reminders from the database
    cur.execute("SELECT * FROM reminders")

    # store in a variable
    reminder_data = cur.fetchall()
    reminder_data = [
        {"title": item[0], "description": item[1]} for item in reminder_data
    ]  # list comprehension
    print(reminder_data)
    """
    # TODO: Exercise for the day (Submit on Tuesday):
    # Without using `pyscop2.extras.DictCursor`, make changes to the output 
    # to return the following - a list of dictionaries
    # Instead of {
    "reminders": [
        [
            "Mirjam is awesome",
            "She is learning to code"
        ],
        [
            "Eat",
            "Food is healthy"
        ],
        [
            "Exercise",
            "Get your heart moving"
        ]
        ]
    }
    
    Return the following:

    "reminders": [
            {
                "title": "Mirjam is awesome",
                "description": "She is learning to code"
            },
            {
                "title": "Eat",
                "description": "Food is healthy"
            },
            {
                "title": "Exercise",
                "description": "Get your heart moving"
            }
          ]
        }
    """

    # JSON ->
    return jsonify({"reminders": reminder_data})
    # return jsonify("hello am a string")
    # return jsonify([{"name": "Shaban"}, {"name": "Fausto"}, (1,2,3)])


# we want to store "reminders"
#
# GET
# POST
# DELETE
# PATCH
# PUT
# how do we save the reminders?

# Decorator -- URL path call add-reminder
@app.route("/hinzufuegen-reminder", methods=["POST"])
def add_reminder():
    try:
        title = request.json["title"]
    except KeyError:
        title = None

    # handle the exception (error handling)
    try:
        description = request.json["description"]
    except KeyError:
        description = None
    # Null
    print(f"INSERT INTO reminders (title, description) VALUES({title}, {description});")
    cur.execute(
        f"INSERT INTO reminders (title, description) VALUES('{title}', '{description}');"
    )
    connection.commit()
    print(title, description)
    # change the return value from empty list to have REMINDERS instead
    return jsonify({"reminders": REMINDERS})


@app.route("/reminders/<int:id>")
def reminder(id):
    print(id)

    cur.execute(f"SELECT * FROM reminders WHERE id = {id};")
    reminder_data = cur.fetchone()
    try:
        reminder_dict = {
            "id": id,
            "title": reminder_data[0],
            "description": reminder_data[1],
        }
        return jsonify(reminder_dict)
    except:
        return jsonify({"message": "sorry, something bad did happened"})
    # print(reminder_data)
    # return jsonify({})

# DELETE
@app.route("/reminders/<int:id>", methods=['DELETE'])
def delete_reminder(id):
    # TODO: Write a query that deletes a reminder
    cur.execute(f"DELETE FROM reminders WHERE id = {id};")
    # dangerous? changes data?
    # commit the changes to make the changes to the database persistent
    connection.commit()
    return jsonify({"messsage": "Successfully deleted!"})

@app.route("/reminders/<int:id>/update", methods=['PUT'])
def update_reminder(id):
    print(request.json)
    cur.execute(f"""
        UPDATE reminders
        SET title='{request.json.get('title')}, 
        description'{request.json.get('description')}'
        WHERE id={id}
    """)
    connection.commit()
    return jsonify({})


# Core HTTP verbs a developer must know
# - GET
# - POST
# - DELETE
# - PUT (Update)
# - PATCH

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5050)  # port for flask
