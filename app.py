from flask import Flask, render_template, request, redirect, session, url_for, flash
from pymongo import MongoClient
from waitress import serve


app = Flask(__name__, static_url_path='/static')


# app.config["MONGO_URI"] = "mongodb+srv://wrieddude:Pranav369@cluster0.xu62g1z.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient("mongodb+srv://Pranav:Pranav_369@blooddonatio.h8fbs15.mongodb.net/?retryWrites=true&w=majority&appName=bloodDonatio")
db = client.get_database('B&D_Donation')

records = db.donors

app.secret_key = 'Donation_website'


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/get_involved")
def getinvolved():
    return render_template("get_involved.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")

@app.route("/add_donors" ,methods=["POST"])
def add_donors():
    name = request.form.get('name')
    email = request.form.get('email')
    blood_grp = request.form.get('blood_type')
    organ = request.form.get('organ')
    number = request.form.get('phone')
    address = request.form.get('address')

    new_donor = {
        "full_name" : name,
        "email" : email,
        "blood_grp" : blood_grp,
        "organ" : organ,
        "number" : number,
        "address" : address
    }

    if new_donor:
        records.insert_one(new_donor)
        return redirect('/')
    else:
        return redirect('/add_donors',info="Got Error")

@app.route("/donors", methods=["GET"])
def donors():
    donors = records.find({})
    return  render_template("donors.html", donors=donors)

@app.route('/search', methods=['GET'])
def search():
    blood_grp = request.form.get('search_param')
    query = {"blood_grp": blood_grp}
    search_results = records.find(query)
    return render_template('donors.html', search_results=search_results)


if __name__ == "__main__":

    app.run(host='0.0.0.0')
