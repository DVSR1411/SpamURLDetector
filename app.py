from flask import Flask, request, render_template
import warnings
warnings.filterwarnings('ignore')
from feature import FeatureExtraction
from keras import models
import numpy as np
app = Flask(__name__)
model = models.load_model('nnmodel.keras')
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form["url"]
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1,30)
        prediction = model.predict(x)
        print(prediction)
        res = "Not spam" if prediction[0] == 1 else "Spam"
        return render_template('index.html', result=res)
    return render_template('index.html', result=None)
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
