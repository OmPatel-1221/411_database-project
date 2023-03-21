from flask import render_template, request, jsonify
from app import app
from app import database as db_helper

todo_list = [
    {"id": '1', "manufacturer": "Honda", "model": "civic" , "year": "2005", "color": "blue"},
    {"id": '2', "manufacturer": "Honda", "model": "oddessey" , "year": "2005", "color": "blue"},\
]

review_list = [{"id": "Test", "contents": "Nice car", "upvotes": "5", "username": "joe", "stars": "0"}]

ratings = []

model_data = [
        ("Subaru", 80),
        ("Subaru", 80),
        ("Subaru", 80),
        ("Subaru", 80),
        ("Subaru", 80),
        ("Subaru", 80),
        ("Subaru", 80),
        ("Subaru", 80),
        ("Subaru", 80),
        ("Subaru", 80),
    ]
done = 0
@app.route("/")
def homepage():
    global model_data
    global done
    if not done:
        model_data = db_helper.fetch_graph()
        done = 1
    labels = [row[0] for row in model_data]
    values = [float(row[1]) for row in model_data]

    return render_template("index.html", items=todo_list, reviews=review_list, labels=labels, values=values, rating= ratings)

@app.route("/create", methods=['POST'])
def create():
    data = request.get_json()
    print("data works")
    db_helper.insert_new_account(data['description'])
    result = {'success': True, 'response': 'Done'}
    print("result works")
    return jsonify(result)

@app.route("/delete", methods=['POST'])
def delete():
    data = request.get_json()
    db_helper.remove_task_by_username(data['description'])
    result = {'success': True, 'response': 'done'}
    return jsonify(result)

@app.route("/search", methods=['POST'])
def search():
    data = request.get_json()
    global todo_list
    todo_list = db_helper.fetch_cars(data['description'])
    homepage()
    result = {'success': True, 'response': 'done'}
    return jsonify(result)

@app.route("/fetch_reviews", methods=['POST'])
def fetch_revs():
    data = request.get_json()
    global review_list
    temp = data['description']
    review_list = db_helper.fetch_reviews(temp)
    homepage()
    result = {'success': True, 'response': 'done'}
    return jsonify(result)

@app.route("/upvote", methods=['POST'])
def upvote_rev():
    print("here1")
    data = request.get_json()
    global review_list
    temp = data['description']
    print(temp)
    print("here2")
    review_list = db_helper.upvote_review(temp)
    print("this is review list", review_list)
    
    homepage()
    result = {'success': True, 'response': 'done'}
    return jsonify(result)


@app.route("/downvote", methods=['POST'])
def downvote_rev():
    data = request.get_json()
    global review_list
    temp = data['description']
    print(temp)
    review_list = db_helper.downvote_review(temp)
    print("this is review list", review_list)
    homepage()
    result = {'success': True, 'response': 'done'}
    return jsonify(result)

@app.route("/query1", methods=['POST'])
def querynuts():
    data = request.get_json()
    global todo_list
    todo_list = db_helper.fetch_cars1(data['description'])
    homepage()
    result = {'success': True, 'response': 'done'}
    return jsonify(result)

@app.route("/query2", methods=['POST'])
def querydeez():
    data = request.get_json()
    global todo_list
    todo_list = db_helper.fetch_cars2(data['description'])
    homepage()
    result = {'success': True, 'response': 'done'}
    return jsonify(result)

@app.route("/ratings", methods=['POST'])
def get_ratings():
    data = request.get_json()
    print("data works")
    global ratings
    ratings = db_helper.fetch_ratings()
    homepage()
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


