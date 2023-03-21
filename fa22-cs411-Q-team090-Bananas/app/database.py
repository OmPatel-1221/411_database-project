from app import db

def insert_new_account(text) -> int:
    print(text)
    conn = db.connect()
    query = 'Insert Into UserProfile (name, UserName, Password) VALUES (%s, %s, %s);'
    conn.execute(query, (text[0], text[1], text[2]))
    conn.close()
    return task_id

def remove_task_by_username(text) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From UserProfile where UserName = %s;'
    conn.execute(query, text[1])
    conn.close()


def fetch_cars(text):
    conn = db.connect()
    query = 'Select manufacturer_name, model_name, year_produced, color, CarId \
    from CarModels where manufacturer_name LIKE %s or model_name LIKE %s or year_produced = %s or color LIKE %s limit 5;'
    query_results = conn.execute(query, text[0], text[1], text[2], text[3])
    query_results = [x for x in query_results]
    conn.close()
    todo_list = []
    for i in range(5):
        todo_list.append({"id": query_results[i][4], "manufacturer": query_results[i][0], "model": query_results[i][1] , "year": str(query_results[i][2]), "color": query_results[i][3]})
    return todo_list

def fetch_reviews(text):  
    conn = db.connect()
    query = 'select reviewID, content, upvotes, UserName, star from Reviews where CarID = %s limit 5;'
    
    query_results = conn.execute(query, text[0])
    query_results = [x for x in query_results]
    print(query_results)
    conn.close()
    todo_list = []  
    for i in range(len(query_results)):
        todo_list.append({"id": query_results[i][0], "contents": str(query_results[i][1]), "upvotes": str(query_results[i][2]) , "username": str(query_results[i][3]), "stars": str(query_results[i][4])})
    return todo_list

def upvote_review(text):
    print("entered db")
    print(int(text[0]))     
    conn = db.connect()
    query = 'update Reviews set upvotes = upvotes+1 where reviewID = %s'
    query2 = 'update Reviews set dummy = dummy * 1;'
    query_results = conn.execute(query, text[0])
    print("query done")
    query = 'select reviewID, content, upvotes, UserName, star from Reviews where reviewID = %s limit 5;'
    conn.execute(query2)
    query_results = conn.execute(query, text[0])
    query_results = [x for x in query_results]
    conn.close()
    todo_list = []
    print(query_results)
    for i in range(len(query_results)):
        todo_list.append({"id": query_results[i][0], "contents": "Review: " + str(query_results[i][1]), "upvotes": str(query_results[i][2]) , "username": str(query_results[i][3]), "stars": str(query_results[i][4])})
    print("connor")
    return todo_list

def downvote_review(text):
    print("entered db")
    print(int(text[0]))     
    conn = db.connect()
    query = 'update Reviews set upvotes = upvotes-1 where reviewID = %s'
    query2 = 'update Reviews set dummy = dummy * 1;'
    query_results = conn.execute(query, text[0])
    print("query done")
    query = 'select reviewID, content, upvotes, UserName, star from Reviews where reviewID = %s limit 5;'
  
    query_results = conn.execute(query, text[0])
    query_results = [x for x in query_results]

    conn.execute(query2)
    conn.close()
    todo_list = []
    print(query_results)
    for i in range(len(query_results)):
        todo_list.append({"id": query_results[i][0], "contents": "Review: " + str(query_results[i][1]), "upvotes": str(query_results[i][2]) , "username":  str(query_results[i][3]), "stars": str(query_results[i][4])})
    print("connor")
    return todo_list


def fetch_cars1(text):
    conn = db.connect()
    query = 'Select manufacturer_name, model_name, year_produced, color, CarID, avg(upvotes) as avgUpvotes\
            from CarModels join Reviews using (CarID)\
            where manufacturer_name LIKE %s or model_name LIKE %s or year_produced = %s or color LIKE %s\
            group by CarID\
            having avg(upvotes) > 20\
            order by avgUpvotes desc limit 5;'
    query_results = conn.execute(query, text[0], text[1], text[2], text[3])
    query_results = [x for x in query_results]
    conn.close()
    todo_list = []
    for i in range(len(query_results)):
        todo_list.append({"id": query_results[i][4], "manufacturer": query_results[i][0], "model": query_results[i][1] , "year": str(query_results[i][2]), "color": query_results[i][3]})
    return todo_list

def fetch_cars2 (text):
    conn = db.connect()
    print("here1")
    query =     "Select manufacturer_name, model_name, year_produced, color, CarID\
                from CarModels natural join Reviews\
                where upvotes > 25 and (manufacturer_name LIKE %s or model_name LIKE %s or year_produced = %s or color LIKE %s)\
                union\
                Select manufacturer_name, model_name, year_produced, color, CarID\
                from CarModels natural join Reviews\
                where content like 'g' and (manufacturer_name LIKE %s or model_name LIKE %s or year_produced = %s or color LIKE %s)\
                order by CarID limit 5;"
    query_results = conn.execute(query, text[0], text[1], text[2], text[3], text[0], text[1], text[2], text[3])
    print("here2")
    query_results = [x for x in query_results]
    conn.close()
    todo_list = []
    for i in range(5):
        todo_list.append({"id": query_results[i][4], "manufacturer": query_results[i][0], "model": query_results[i][1] , "year": str(query_results[i][2]), "color": query_results[i][3]})

    return todo_list

def fetch_graph():
    conn = db.connect()
    print("graphfetch")
    # query = 'call cars.custom_ratings();'
    # query_results = conn.execute(query)
    #query = 'select model_name, avg(upvotes) from Reviews natural join CarModels group by model_name order by avg(upvotes) desc limit 10'
    query = 'SELECT model_name, avg(totalRating) as avg1\
    FROM cars.CustReviewTable natural join cars.CarModels group by model_name order by avg1 desc limit 10'
    query_results = conn.execute(query)
    query_results = [x for x in query_results]
    print("GRAPH RESULTS: ", query_results)
    conn.close()
    model_data = []
    for i in range(len(query_results)):
       model_data.append((query_results[i][0], query_results[i][1]))
    print(model_data)
    return model_data

def fetch_ratings():
    print("Starting stored Procedure")    
    conn = db.connect()
    query = 'call cars.custom_ratings();'
    query_results = conn.execute(query)
    print("finished procedure")
    query = "SELECT CarID, manufacturer_name, model_name, odomRating, engineRating, ageRating, popularityRating, totalRating \
    FROM cars.CustReviewTable natural join cars.CarModels order by totalRating desc limit 5"
    query_results = conn.execute(query)
    query_results = [x for x in query_results]
    print(query_results)
    
    todo_list = []
    #print(query_results)
    for i in range(len(query_results)):
        todo_list.append({"id": query_results[i][0], "manufacturer": str(query_results[i][1]), "model": str(query_results[i][2]) , "Odom": str(query_results[i][3]), "Engine": str(query_results[i][4]), "Age": str(query_results[i][5]), "Popularity": str(query_results[i][6]), "Total": str(query_results[i][7])})
    
    query2 = "select * from cars.CustReviewTable"
    query_results1 = conn.execute(query2)
    query_results1 = [x for x in query_results1]
    print("HERE", query_results1)
    conn.close()
    return todo_list
