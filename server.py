from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)
# Needs file.html format

@app.route("/works")
def my_works():
    return render_template("works.html")

@app.route("/works/work")
def my_work():
    return render_template("work.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('thankyou')
        except:
            return 'did not save to database'
    else:
        return "something went wrong, please try again."

