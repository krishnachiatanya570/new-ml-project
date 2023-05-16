import numpy as np
import pandas as pd
from flask import Flask,request,jsonify,render_template,request
import pickle

app = Flask(__name__)
model =pickle.load(open('qwerty.pkl','rb'))
sal=pd.read_csv("cleaned salary.csv")


@app.route('/',methods=['GET','POST'])
def index():
    gender=sorted(sal.Gender.unique())
    education_level=sorted(sal['Education Level'].unique())
    job_type=sorted(sal['Job Title'].unique())
    gender.insert(0,'Select Gender')
    education_level.insert(0,'Select Education')
    job_type.insert(0,'Job Type')
    
    return render_template('index.html',genders=gender, education_levels=education_level, job_types=job_type)

@app.route("/predict",methods=['POST'])

def predict():
    age=request.form.get('age')
    gender=request.form.get('gender')
    education_level=request.form.get('edu')
    job=request.form.get('job')
    exp=request.form.get('Experience')
    prediction=model.predict(pd.DataFrame([[age,gender,education_level,job,exp]],columns=['Age','Gender','Education Level','Job Title','Years of Experience']))

    print(age)
    # int_features = [float(x) for x in request.form.values()]
    
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)


    output= round(prediction[0],2)

    return render_template('index.html', prediction_text='Employee Salary should be  {}'.format(output))
if __name__ == "__main__":
    app.run(debug=True)



    
    
    

    
    