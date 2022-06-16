from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
<<<<<<< HEAD
    return "Hi!! Saurabh. Flask inside Docker is up and running for final testing working"

=======
    return "Hi!! Saurabh. Flask inside Docker is up and running for final test11!!"
>>>>>>> 3a8f032fed1b3009aabc439706924307b9322614

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)