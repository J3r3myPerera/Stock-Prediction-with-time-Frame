#Create flask app
app = Flask(__name__)

#Load the pickle model
model = pickle.load(open("Model for General Motors.pkl","rb"))

@app.route("/")
def Home():
    return render_template("")

@app.route("/predict", method =["POST"])
def predict():
