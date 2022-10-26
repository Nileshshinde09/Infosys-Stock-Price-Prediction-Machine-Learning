from flask import Flask,render_template,request
import joblib
import numpy as np
app = Flask(__name__)
model = joblib.load("model_infosys.joblib")
@app.route('/',methods = ['GET', 'POST'])
def index_page():
    open = request.form.get("open")
    high = request.form.get("high")
    low = request.form.get("low")
    volume = request.form.get("volume")
    input_data =[open,high,low,volume]
    data = np.array(input_data)
    predict = model.predict([data])
    return render_template("index.html",data = predict[0])
        


if __name__=="__main__":
    app.run(debug=True)
