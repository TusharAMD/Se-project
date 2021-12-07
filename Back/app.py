from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
import pymongo
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/basicdetails",methods=["POST","GET","OPTIONS"])
@cross_origin()
def basicdetails():
    if request.method=="POST":
        client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.wonbr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
        db = client['Diet']
        collection = db["BasicDetails"]
        result = request.json["formdata"]
        x = collection.find_one({"email":result["email"]})
        if x:
            print(x,"<<<<X<<<<")
            myquery = { "email":result["email"] }
            newvalues = { "$set": result} 
            collection.update_one(myquery, newvalues)
        else:
            collection.insert_one(result)
            
    
        print(request.json)
    return jsonify({"response":"200"})

@app.route("/dailydetails",methods=["POST","GET","OPTIONS"])
@cross_origin()
def dailydetails():
    if request.method=="POST":
        client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.wonbr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
        db = client['Diet']
        collection = db["DailyIntake"]
        result = request.json["formValues"]
        
        
        nutritionOfItems = {
            "Ladyfinger": {
                "Calories": 33,
                "Fat": 0.2,
                "Cholesterol": 0,
                "Sodium": 7,
                "Potassium ": 299,
                "Fiber": 3.2,
                "Sugar": 1.5,
                "Protein": 1.9,
            },
            "Tomato": {
                "Calories": 18,
                "Fat": 0.2,
                "Cholesterol": 0,
                "Sodium": 5,
                "Potassium ": 237,
                "Fiber": 1.2,
                "Sugar": 2.6,
                "Protein": 0.9,
            },
            "Onion": {
                "Calories": 40,
                "Fat": 0.1,
                "Cholesterol": 0,
                "Sodium": 4,
                "Potassium ": 146,
                "Fiber": 1.7,
                "Sugar": 4.2,
                "Protein": 1.1,
            },
            "Potato": {
                "Calories": 77,
                "Fat": 0.1,
                "Cholesterol": 0,
                "Sodium": 6,
                "Potassium ": 421,
                "Fiber": 2.2,
                "Sugar": 0.8,
                "Protein": 2,
            },
            "Turnip": {
                "Calories": 77,
                "Fat": 0.1,
                "Cholesterol": 0,
                "Sodium": 6,
                "Potassium ": 421,
                "Fiber": 2.2,
                "Sugar": 0.8,
                "Protein": 2,
            },
            "Turmeric": {
                "Calories": 354,
                "Fat": 3.1,
                "Cholesterol": 0,
                "Sodium": 38,
                "Potassium ": 2525,
                "Fiber": 21,
                "Sugar": 3.2,
                "Protein": 8,
            },
            "Sweet Potato": {
                "Calories": 86,
                "Fat": 0.1,
                "Cholesterol": 0,
                "Sodium": 55,
                "Potassium ": 337,
                "Fiber": 3,
                "Sugar": 4.2,
                "Protein": 1.6,
            },
            "Spring Onion": {
                "Calories": 32,
                "Fat": 0.2,
                "Cholesterol": 0,
                "Sodium": 16,
                "Potassium ": 276,
                "Fiber": 2.6,
                "Sugar": 2.4,
                "Protein": 1.8,
            },
            "Spinach": {
                "Calories": 23,
                "Fat": 0.4,
                "Cholesterol": 0,
                "Sodium": 79,
                "Potassium ": 558,
                "Fiber": 2.2,
                "Sugar": 0.42,
                "Protein": 2.86,
            },
            "Pumpkin": {
                "Calories": 26,
                "Fat": 0.1,
                "Cholesterol": 0,
                "Sodium": 1,
                "Potassium ": 340,
                "Fiber": 0.5,
                "Sugar": 2.8,
                "Protein": 1,
            },
            "Garlic": {
                "Calories": 149,
                "Fat": 0.5,
                "Cholesterol": 0,
                "Sodium": 17,
                "Potassium ": 401,
                "Fiber": 2.1,
                "Sugar": 1,
                "Protein": 6.4,
            },
            "Ginger": {
                "Calories": 80,
                "Fat": 0.8,
                "Cholesterol": 0,
                "Sodium": 13,
                "Potassium ": 415,
                "Fiber": 2,
                "Sugar": 1.7,
                "Protein": 1.8,
            },
            "Fenugreek": {
                "Calories": 323,
                "Fat": 6,
                "Cholesterol": 0,
                "Sodium": 67,
                "Potassium ": 770,
                "Fiber": 25,
                "Sugar": 2.7,
                "Protein": 23,
            },
            "Green Chilli": {
                "Calories": 40,
                "Fat": 0.4,
                "Cholesterol": 0,
                "Sodium": 9,
                "Potassium ": 232,
                "Fiber": 1.5,
                "Sugar": 5,
                "Protein": 1.9,
            },
            "Green Beans": {
                "Calories": 32,
                "Fat": 0.1,
                "Cholesterol": 0,
                "Sodium": 6,
                "Potassium ": 209,
                "Fiber": 3.4,
                "Sugar": 3.3,
                "Protein": 1.8,
            },
            "Radish": {
                "Calories": 16,
                "Fat": 0.1,
                "Cholesterol": 0,
                "Sodium": 39,
                "Potassium ": 233,
                "Fiber": 1.6,
                "Sugar": 1.9,
                "Protein": 0.7,
            },
            "Jackfruit": {
                "Calories": 157,
                "Fat": 2,
                "Cholesterol": 0,
                "Sodium": 96,
                "Potassium ": 303,
                "Fiber": 3,
                "Sugar": 31,
                "Protein": 3,
            },
            "Mushroom": {
                "Calories": 22,
                "Fat": 0.3,
                "Cholesterol": 0,
                "Sodium": 5,
                "Potassium ": 318,
                "Fiber": 1,
                "Sugar": 2,
                "Protein": 3.1,
            },
            "Maize": {
                "Calories": 88,
                "Fat": 1.4,
                "Cholesterol": 0,
                "Sodium": 15,
                "Potassium ": 221,
                "Fiber": 2,
                "Sugar": 6.4,
                "Protein": 3.3,
            },
            "Peas": {
                "Calories": 84,
                "Fat": 0.2,
                "Cholesterol": 0,
                "Sodium": 3,
                "Potassium ": 271,
                "Fiber": 5.5,
                "Sugar": 5.9,
                "Protein": 5.4,
            },
            "Cauliflower": {
                "Calories": 23,
                "Fat": 0.5,
                "Cholesterol": 0,
                "Sodium": 15,
                "Potassium ": 142,
                "Fiber": 2.3,
                "Sugar": 2.1,
                "Protein": 1.8,
            },
            "Cabbage": {
                "Calories": 23,
                "Fat": 0.1,
                "Cholesterol": 0,
                "Sodium": 8,
                "Potassium ": 196,
                "Fiber": 1.9,
                "Sugar": 2.8,
                "Protein": 1.3,
            },
            "Carrot": {
                "Calories": 35,
                "Fat": 0.2,
                "Cholesterol": 0,
                "Sodium": 58,
                "Potassium ": 235,
                "Fiber": 3,
                "Sugar": 3.5,
                "Protein": 0.8,
            },
            "Capsicum": {
                "Calories": 40,
                "Fat": 0.2,
                "Cholesterol": 0,
                "Sodium": 7,
                "Potassium ": 340,
                "Fiber": 1.5,
                "Sugar": 5.1,
                "Protein": 2,
            },
            "Brinjal": {
                "Calories": 35,
                "Fat": 0.2,
                "Cholesterol": 0,
                "Sodium": 1,
                "Potassium ": 123,
                "Fiber": 2.5,
                "Sugar": 3.2,
                "Protein": 0.8,
            },
            "Bitter Gourd": {
                "Calories": 16,
                "Fat": 0.2,
                "Cholesterol": 0,
                "Sodium": 6,
                "Potassium ": 275,
                "Fiber": 2.6,
                "Sugar": 1.1,
                "Protein": 0.9,
            },
            "Beetroot": {
                "Calories": 44,
                "Fat": 0.2,
                "Cholesterol": 0,
                "Sodium": 78,
                "Potassium ": 306,
                "Fiber": 2,
                "Sugar": 8,
                "Protein": 1.7,
            },
            "Broccoli": {
                "Calories": 31,
                "Fat": 0.3,
                "Cholesterol": 0,
                "Sodium": 41,
                "Potassium ": 239,
                "Fiber": 3.3,
                "Sugar": 1.4,
                "Protein": 2.4,
            },
            "Colocasia Root": {
                "Calories": 97,
                "Fat": 0,
                "Cholesterol": 0,
                "Sodium": 11,
                "Potassium ": 484,
                "Fiber": 1,
                "Sugar": 1.3,
                "Protein": 3,
            },
            "Rice": {
                "Calories": 130,
                "Fat": 0.3,
                "Cholesterol": 0,
                "Sodium": 1,
                "Potassium ": 35,
                "Fiber": 0.4,
                "Sugar": 0.1,
                "Protein": 2.7,
            },
            "Wheat": {
                "Calories": 364,
                "Fat": 1,
                "Cholesterol": 0,
                "Sodium": 2,
                "Potassium ": 107,
                "Fiber": 2.7,
                "Sugar": 0.3,
                "Protein": 10,
            },
            "Maida": {
                "Calories": 364,
                "Fat": 0.98,
                "Cholesterol": 0,
                "Sodium": 2,
                "Potassium ": 107,
                "Fiber": 2.7,
                "Sugar": 0.27,
                "Protein": 10.3,
            },
            "Barley": {
                "Calories": 354,
                "Fat": 2.3,
                "Cholesterol": 0,
                "Sodium": 12,
                "Potassium ": 452,
                "Fiber": 17,
                "Sugar": 0.8,
                "Protein": 12,
            },
            "Sago": {
                "Calories": 332,
                "Fat": 1,
                "Cholesterol": 0,
                "Sodium": 27,
                "Potassium ": 484,
                "Fiber": 1,
                "Sugar": 1.3,
                "Protein": 1,
            },
            "Sorghum": {
                "Calories": 316,
                "Fat": 0,
                "Cholesterol": 0,
                "Sodium": 6,
                "Potassium ": 60,
                "Fiber": 6,
                "Sugar": 1.5,
                "Protein": 10,
            },
            "Semolina": {
                "Calories": 360,
                "Fat": 1,
                "Cholesterol": 0,
                "Sodium": 1,
                "Potassium ": 186,
                "Fiber": 3.9,
                "Sugar": 0.4,
                "Protein": 12.8,
            },
            "Oat": {
                "Calories": 140,
                "Fat": 2.5,
                "Cholesterol": 0,
                "Sodium": 0,
                "Potassium ": 236,
                "Fiber": 4,
                "Sugar": 0,
                "Protein": 5,
            },
            "Chickpeas": {
                "Calories": 364,
                "Fat": 6,
                "Cholesterol": 0,
                "Sodium": 24,
                "Potassium ": 875,
                "Fiber": 17,
                "Sugar": 11,
                "Protein": 19,
            },
            "Lentil": {
                "Calories": 116,
                "Fat": 0.4,
                "Cholesterol": 0,
                "Sodium": 2,
                "Potassium ": 369,
                "Fiber": 8,
                "Sugar": 1.8,
                "Protein": 9,
            },
            "Black gram": {
                "Calories": 341,
                "Fat": 0,
                "Cholesterol": 0,
                "Sodium": 7,
                "Potassium ": 983,
                "Fiber": 7.4,
                "Sugar": 0,
                "Protein": 25,
            },
            "Millet": {
                "Calories": 378,
                "Fat": 4.2,
                "Cholesterol": 0,
                "Sodium": 5,
                "Potassium ": 390,
                "Fiber": 8,
                "Sugar": 1.3,
                "Protein": 11,
            },
            "Pinto Beans": {
                "Calories": 347,
                "Fat": 1.2,
                "Cholesterol": 0,
                "Sodium": 12,
                "Potassium ": 1393,
                "Fiber": 16,
                "Sugar": 2.1,
                "Protein": 21,
            },
            "Sugar": {
                "Calories": 389,
                "Fat": 0,
                "Cholesterol": 0,
                "Sodium": 2,
                "Potassium ": 2,
                "Fiber": 0,
                "Sugar": 98,
                "Protein": 0,
            },
            "Soya Beans": {
                "Calories": 25,
                "Fat": 1,
                "Cholesterol": 0,
                "Sodium": 560,
                "Potassium ": 0,
                "Fiber": 0,
                "Sugar": 3,
                "Protein": 53,
            },
            "Goat Meat": {
                "Calories": 143,
                "Fat": 3,
                "Cholesterol": 75,
                "Sodium": 86,
                "Potassium ": 405,
                "Fiber": 0,
                "Sugar": 0,
                "Protein": 27,
            },
            "Chicken": {
                "Calories": 239,
                "Fat": 14,
                "Cholesterol": 88,
                "Sodium": 82,
                "Potassium ": 223,
                "Fiber": 0,
                "Sugar": 0,
                "Protein": 27,
            },
            "Fishes": {
                "Calories": 206,
                "Fat": 12,
                "Cholesterol": 63,
                "Sodium": 61,
                "Potassium ": 384,
                "Fiber": 0,
                "Sugar": 0,
                "Protein": 22,
            },
            "Eggs": {
                "Calories": 155,
                "Fat": 11,
                "Cholesterol": 373,
                "Sodium": 124,
                "Potassium ": 126,
                "Fiber": 0,
                "Sugar": 1.1,
                "Protein": 13,
            },
            "Pork": {
                "Calories": 242,
                "Fat": 14,
                "Cholesterol": 80,
                "Sodium": 62,
                "Potassium ": 423,
                "Fiber": 0,
                "Sugar": 0,
                "Protein": 27,
            },
            "Cow Milk": {
                "Calories": 42,
                "Fat": 1,
                "Cholesterol": 5,
                "Sodium": 44,
                "Potassium ": 150,
                "Fiber": 0,
                "Sugar": 5,
                "Protein": 3.4,
            },
            "Buffalo Milk": {
                "Calories": 236,
                "Fat": 16.8,
                "Cholesterol": 46.4,
                "Sodium": 126.9,
                "Potassium ": 434,
                "Fiber": 0,
                "Sugar": 4.3,
                "Protein": 9.2,
            },
            "Cheese": {
                "Calories": 105,
                "Fat": 33,
                "Cholesterol": 105,
                "Sodium": 621,
                "Potassium ": 98,
                "Fiber": 0,
                "Sugar": 0.5,
                "Protein": 25,
            },
            "Ghee": {
                "Calories": 42,
                "Fat": 5,
                "Cholesterol": 0,
                "Sodium": 11,
                "Potassium ": 24,
                "Fiber": 1,
                "Sugar": 0.1,
                "Protein": 0.9,
            },
        }
        
        curr_data = {"Calories":0,"Fat":0,"Cholesterol":0,"Sodium":0,"Potassium ":0,"Fiber":0,"Sugar":0,"Protein":0}
        
        for ele in result:
            #print(ele["name"])
            x = ele["name"].strip()
            #print(nutritionOfItems[x])
            curr_item_calorie= nutritionOfItems.get(x)
            for x in curr_item_calorie:
                curr_data[x]=curr_data[x]+(curr_item_calorie[x]*0.01*int(ele["weight"]))
        print(curr_data)
        email = request.json["user"]["email"]
        date = request.json["d"].split("T")[0]
        #date = "2021-10-15"
        print(email,date)
        
        #print(result)
        curr_data["date"]=date
        curr_data["email"]=email
        
        
        x = collection.find_one({"email":email,"date":date})
        if x:
            print(x,"<<<<X<<<<")
            myquery = { "email":email }
            newvalues = { "$set": curr_data} 
            collection.update_one(myquery, newvalues)
        else:
            collection.insert_one(curr_data)
        
        
    
    #print(request.json)
    return jsonify({"response":"200"})

@app.route("/stats",methods=["POST","GET","OPTIONS"])
@cross_origin()
def stats():
    if request.method=="GET":
        client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.wonbr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
        db = client['Diet']
        collection = db["DailyIntake"]
        x=collection.find()
        result = []
        for ele in x:
            result.append(ele)
            del ele["_id"]
            print(ele)
        print(result)
        tosend={}
        tosend["result"] = result        
    return tosend

if __name__ == "__main__":
    app.run()