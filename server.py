from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def landing():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got the POST!\n")
    print(f"{request.form} was submitted")
    print(f"\n***Name: {request.form['name']}\n***Email: {request.form['email']}\n")
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)