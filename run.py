from flask import Flask, render_template, url_for, redirect, request
import numpy as np
import pickle
from forms import CheckForm


app = Flask(__name__)
app.config['SECRET_KEY']='GTHACKERS'

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('GT home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    # int_features = [1, 3, 565235956.44242, 13959898.5346, 5464.5434, 21545.54534354, 564.4323434]
    form = CheckForm()
    
    if form.is_submitted():
        result = request.form.values()
       
        a = list(result)
        a.remove('Submit')
        a.remove(form.D_name.data)
        a.remove(form.P_name.data)
       
        
        a=[int(x) for x in a]
        
        
        
        final_features = [np.array(a)]
       
        
        prediction=model.predict(final_features)
        return render_template('answer.html',prediction=prediction)
        
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)

    return render_template('formsection.html', form=form)
    


if __name__ == '__main__':
    app.run(debug=True)
